"""
Testy dla audytu wydajności i czasu ładowania < 3s (AAAS PageSpeed Test).
"""
import unittest
from src.performance_audit import AAASPerformanceAuditor

class TestAAASPerformance(unittest.TestCase):
    def setUp(self):
        self.auditor = AAASPerformanceAuditor(target_url="https://bartzx.github.io/Projekt/")

    def test_load_time_under_3_seconds(self):
        report = self.auditor.run_speed_test()
        self.assertEqual(report["httpStatusCode"], 200)
        self.assertTrue(report["passedUnder3Seconds"], f"Czas ładowania przekroczył 3s: {report['totalLoadTimeSeconds']}s")
        self.assertLess(report["totalLoadTimeSeconds"], 2.0, "Powinno załadować się poniżej 2,0 s")

if __name__ == "__main__":
    unittest.main()
