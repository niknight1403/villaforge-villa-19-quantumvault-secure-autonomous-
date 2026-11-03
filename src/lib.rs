use aes_gcm::{Aes256Gcm, Key, KeyInit, aead::{Aead, OsRng, AeadCore}};
use argon2::{Argon2, PasswordHasher, PasswordVerifier, password_hash::{SaltString, rand_core::OsRng as ArgonRng}};
use anyhow::{Result, anyhow};

pub struct CryptoVault;

impl CryptoVault {
    pub fn derive_key(password: &[u8], salt: &str) -> Result<Vec<u8>> {
        let salt = SaltString::from_b64(salt).map_err(|_| anyhow!("Invalid salt"))?;
        let argon2 = Argon2::default();
        let mut output_key = [0u8; 32];
        argon2.hash_password_into(password, salt.as_bytes(), &mut output_key).map_err(|_| anyhow!("Key derivation failed"))?;
        Ok(output_key.to_vec())
    }

    pub fn encrypt(key: &[u8], plaintext: &[u8]) -> Result<Vec<u8>> {
        let cipher = Aes256Gcm::new(Key::<Aes256Gcm>::from_slice(key));
        let nonce = Aes256Gcm::generate_nonce(&mut OsRng);
        let mut ciphertext = cipher.encrypt(&nonce, plaintext).map_err(|_| anyhow!("Encryption failed"))?;
        let mut result = nonce.to_vec();
        result.append(&mut ciphertext);
        Ok(result)
    }

    pub fn decrypt(key: &[u8], ciphertext: &[u8]) -> Result<Vec<u8>> {
        let cipher = Aes256Gcm::new(Key::<Aes256Gcm>::from_slice(key));
        let (nonce, payload) = ciphertext.split_at(12);
        cipher.decrypt(nonce.into(), payload).map_err(|_| anyhow!("Decryption failed"))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_encryption_decryption() {
        let key = vec![0u8; 32];
        let data = b"secret message";
        let encrypted = CryptoVault::encrypt(&key, data).unwrap();
        let decrypted = CryptoVault::decrypt(&key, &encrypted).unwrap();
        assert_eq!(data, &decrypted[..]);
    }
}