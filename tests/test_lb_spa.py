"""
Testy dla schematu weryfikacji strony i prawdziwości danych L&B Spa w Karpaczu.
"""
import unittest
from src.lb_spa_verifier import LBSpaWebsiteVerifier

class TestLBSpaVerifier(unittest.TestCase):
    def setUp(self):
        self.verifier = LBSpaWebsiteVerifier()

    def test_operational_success(self):
        op = self.verifier.run_operational_test()
        self.assertTrue(op["operational_success"], f"Strona L&B Spa jest niedostępna: {op}")
        self.assertEqual(op["status_code"], 200)

    def test_data_authenticity(self):
        auth = self.verifier.verify_data_authenticity()
        self.assertTrue(auth["authenticity_passed"], f"Audyt autentyczności nie powiódł się: {auth}")
        self.assertEqual(auth["certification"], "100% VERIFIED AUTHENTIC & OPERATIONAL")

if __name__ == "__main__":
    unittest.main()
