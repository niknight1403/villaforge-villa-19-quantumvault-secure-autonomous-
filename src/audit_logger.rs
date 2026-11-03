use sha2::{Sha256, Digest};
use serde::{Serialize, Deserialize};
use std::time::{SystemTime, UNIX_EPOCH};

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct AuditEntry {
    pub timestamp: u64,
    pub action: String,
    pub actor: String,
    pub prev_hash: String,
    pub hash: String,
}

pub struct AuditLogger {
    pub last_hash: String,
}

impl AuditLogger {
    pub fn new() -> Self {
        Self { last_hash: "0".repeat(64) }
    }

    pub fn log(&mut self, action: &str, actor: &str) -> AuditEntry {
        let timestamp = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs();
        let data = format!("{}{}{}{}", timestamp, action, actor, self.last_hash);
        let mut hasher = Sha256::new();
        hasher.update(data);
        let hash = format!("{:x}", hasher.finalize());

        let entry = AuditEntry {
            timestamp,
            action: action.to_string(),
            actor: actor.to_string(),
            prev_hash: self.last_hash.clone(),
            hash: hash.clone(),
        };

        self.last_hash = hash;
        entry
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_tamper_evidence() {
        let mut logger = AuditLogger::new();
        let entry1 = logger.log("LOGIN", "admin");
        let entry2 = logger.log("DELETE_USER", "admin");
        assert_eq!(entry2.prev_hash, entry1.hash);
    }
}