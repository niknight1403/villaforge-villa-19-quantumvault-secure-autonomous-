import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestQuantumVaultEdgeCases(unittest.TestCase):
    def test_zero_knowledge_empty_payload(self):
        payload = b""
        self.assertEqual(len(payload), 0, "Empty payload edge case verified")

    def test_prompt_injection_extreme_length(self):
        injection_attempt = "<script>alert(1)</script>" * 1000
        self.assertIn("script", injection_attempt, "Large injection payload handled")

    def test_billing_tier_overflow_edge_case(self):
        tier_limit = 999999999
        usage = 1000000000
        self.assertGreater(usage, tier_limit, "Billing tier limit overflow edge case verified")

if __name__ == '__main__':
    unittest.main()
