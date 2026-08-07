"""
Testy jednostkowe i integracyjne dla silnika agencji AAAS.
"""
import unittest
from src.engine import AAASAgentLoader, AAASWorkflowValidator, AAASOrchestrator

class TestAAASEngine(unittest.TestCase):
    def test_load_all_agents(self):
        loader = AAASAgentLoader(agents_dir="agents")
        agents = loader.load_all_agents()
        self.assertGreaterEqual(len(agents), 5, "Powinno załadować min. 5 agentów")
        names = [a.get("name") for a in agents]
        self.assertIn("Lead Prospector Agent", names)
        self.assertIn("AI Receptionist & Booking Automator Agent", names)

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
        self.assertEqual(report["agents_loaded"], 5)
        self.assertEqual(report["workflows_validated"], 2)

if __name__ == "__main__":
    unittest.main()
