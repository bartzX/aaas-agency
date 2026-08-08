"""
Testy jednostkowe i integracyjne dla silnika agencji AAAS (9 Agentów AI 2026 w tym Fable 5).
"""
import unittest
from src.engine import AAASAgentLoader, AAASWorkflowValidator, AAASOrchestrator

class TestAAASEngine(unittest.TestCase):
    def test_load_all_agents(self):
        loader = AAASAgentLoader(agents_dir="agents")
        agents = loader.load_all_agents()
        self.assertGreaterEqual(len(agents), 9, "Powinno załadować min. 9 agentów AI (w tym Fable 5)")
        names = [a.get("name") for a in agents]
        self.assertIn("Lead Prospector Agent", names)
        self.assertIn("AI Receptionist & Booking Automator Agent", names)
        self.assertIn("Creative Director & Luxury Art Director Agent (CD-AI)", names)
        self.assertIn("PL Conversion Architect & Direct Booking Strategist Agent (PL-CRO-2026)", names)
        self.assertIn("WCAG 2.2 & Core Web Vitals Performance Auditor Agent", names)
        self.assertIn("Claude Fable 5 Motion & Generative UI Architect Agent", names)

    def test_validate_workflows(self):
        validator = AAASWorkflowValidator(workflows_dir="workflows")
        results = validator.validate_workflows()
        self.assertGreaterEqual(len(results), 2, "Powinno zwalidować min. 2 przepływy n8n")
        for res in results:
            self.assertTrue(res.get("valid"), f"Przepływ {res.get('file')} jest nieprawidłowy")

    def test_orchestrator(self):
        orch = AAASOrchestrator()
        report = orch.run_agency_audit()
        self.assertEqual(report["status"], "active")
        self.assertGreaterEqual(report["agents_loaded"], 9)
        self.assertGreaterEqual(report["workflows_validated"], 2)

if __name__ == "__main__":
    unittest.main()
