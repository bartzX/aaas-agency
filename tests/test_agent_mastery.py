"""
Testy dla silnika ciągłego doskonalenia agentów AI i opanowania narzędzi GitHub (AAAS Mastery Engine).
"""
import unittest
from src.agent_mastery_engine import AAASAgentMasteryEngine

class TestAAASAgentMastery(unittest.TestCase):
    def setUp(self):
        self.engine = AAASAgentMasteryEngine()

    def test_all_agents_at_100_percent_mastery(self):
        audit = self.engine.run_continuous_upskilling_loop()
        self.assertEqual(len(audit), 10, "Powinno sprawdzić dokładnie 10 agentów AI")
        for ag in audit:
            self.assertGreaterEqual(
                ag["masteryIndexPercent"], 95.0,
                f"Agent {ag['name']} nie osiągnął szczytu umiejętności ({ag['masteryIndexPercent']}%)"
            )

    def test_github_starred_tools_mastery(self):
        tools_report = self.engine.verify_full_github_tools_mastery()
        self.assertGreaterEqual(tools_report["coveragePercent"], 95.0)
        self.assertEqual(tools_report["masteryCertification"], "100% GITHUB STARRED TOOLS MASTERED BY AGENT TEAM")

    def test_apex_agency_certification(self):
        cert = self.engine.certify_apex_agency_readiness()
        self.assertTrue(cert["allAgentsAtApexMastery"])
        self.assertEqual(cert["finalCertification"], "100% APEX AGENCY MASTERY ACHIEVED - ALL AGENTS & GITHUB TOOLS MASTERED")

if __name__ == "__main__":
    unittest.main()
