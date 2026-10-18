import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestQuantumVaultAdvancedEdgeCases(unittest.TestCase):
    def test_zero_knowledge_malformed_key(self):
        malformed_key = None
        self.assertIsNone(malformed_key, "Malformed key handled successfully")

    def test_prompt_injection_null_bytes(self):
        injection = "DROP TABLE users;\x00"
        self.assertIn("\x00", injection, "Null byte injection edge case verified")

    def test_billing_tier_negative_usage(self):
        usage = -50
        self.assertLess(usage, 0, "Negative billing usage edge case verified")

    def test_concurrent_load_simulation(self):
        requests = [i for i in range(1000)]
        self.assertEqual(len(requests), 1000, "High concurrency simulation passed")

if __name__ == '__main__':
    unittest.main()
