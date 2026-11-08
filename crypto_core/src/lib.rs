use aes_gcm::{Aes256Gcm, Key, aead::{Aead, KeyInit}};
use rand::{RngCore, os::OsRng};

pub struct CryptoEngine {
    key: [u8; 32],
}

impl CryptoEngine {
    pub fn new() -> Self {
        let mut key = [0u8; 32];
        OsRng.fill_bytes(&mut key);
        Self { key }
    }

    pub fn encrypt(&self, data: &[u8]) -> Vec<u8> {
        let cipher = Aes256Gcm::new(Key::<Aes256Gcm>::from_slice(&self.key));
        let mut nonce = [0u8; 12];
        OsRng.fill_bytes(&mut nonce);
        let mut ciphertext = cipher.encrypt(aes_gcm::Nonce::from_slice(&nonce), data).expect("encryption failed");
        let mut result = nonce.to_vec();
        result.append(&mut ciphertext);
        result
    }
}
