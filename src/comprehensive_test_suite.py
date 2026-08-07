"""
AAAS Agency Comprehensive Test Suite & Readiness Verification Engine (2026)
Wykonuje kompleksowe testy sieciowe, integracyjne, finansowe i automatyzacyjne
potwierdzające 100% gotowości agencji do startu komercyjnego.
"""
import urllib.request
import urllib.error
import json
import os
import glob
from typing import Dict, Any, List
from src.billing_engine import AAASBillingEngine
from src.e2e_pipeline import E2EBookingPipeline
from src.lead_prospector_agent import LeadProspector

class AAASReadinessAudit:
    """Kompleksowy audytor gotowości technologiczno-handlowej agencji AAAS."""

    def __init__(self):
        self.billing = AAASBillingEngine()
        self.pipeline = E2EBookingPipeline()
        self.prospector = LeadProspector()

    def test_live_urls(self) -> List[Dict[str, Any]]:
        """Sprawdza dostępność HTTP 200 na żywych adresach agencji i klienta."""
        urls = [
            "https://bartzx.github.io/pensjonatgran-karpacz/",
            "https://bartzx.github.io/pensjonatgran-demo/",
            "https://bartzx.github.io/hotel-gran/",
            "https://bartzx.github.io/pensjonat-syriusz/",
            "https://bartzx.github.io/Projekt/"
        ]
        results = []
        for url in urls:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "AAAS-Agency-Audit-Bot/1.0"})
                with urllib.request.urlopen(req, timeout=8) as res:
                    results.append({
                        "url": url,
                        "status_code": res.getcode(),
                        "success": res.getcode() == 200
                    })
            except urllib.error.HTTPError as e:
                results.append({
                    "url": url,
                    "status_code": e.code,
                    "success": e.code == 200,
                    "error": str(e)
                })
            except Exception as e:
                results.append({
                    "url": url,
                    "status_code": 0,
                    "success": False,
                    "error": str(e)
                })
        return results

    def verify_n8n_workflows(self) -> List[Dict[str, Any]]:
        """Weryfikuje kompletność 3 scenariuszy n8n i ich składnię JSON."""
        results = []
        workflows = [
            "workflows/01_hotel_lead_intake_webhook.json",
            "workflows/02_competitor_price_monitor.json",
            "workflows/03_pensjonat_gran_ski_receptionist.json"
        ]
        for path in workflows:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    results.append({
                        "file": path,
                        "name": data.get("name"),
                        "nodes_count": len(data.get("nodes", [])),
                        "valid": len(data.get("nodes", [])) >= 3
                    })
            except Exception as e:
                results.append({
                    "file": path,
                    "valid": False,
                    "error": str(e)
                })
        return results

    def verify_outreach_compliance(self) -> Dict[str, bool]:
        """Sprawdza zgodność skryptów handlowych ze standardem ogólnopolskim i domen .pl."""
        outreach_path = "docs/OUTREACH_PENSJONAT_GRAN.md"
        if not os.path.exists(outreach_path):
            return {"exists": False}
        with open(outreach_path, "r", encoding="utf-8") as f:
            content = f.read()
            return {
                "exists": True,
                "has_nationwide_scope": "w całej Polsce" in content,
                "has_pl_domain_standard": "pensjonatgran.pl" in content,
                "has_photo_disclaimer": "zdjęcia w demo są podglądowe" in content,
                "has_phone_number": "601 584 872" in content
            }

    def run_complete_readiness_audit(self) -> Dict[str, Any]:
        """Wykonuje pełny test gotowości i zwraca raport końcowy."""
        url_results = self.test_live_urls()
        workflow_results = self.verify_n8n_workflows()
        compliance = self.verify_outreach_compliance()
        e2e_sim = self.pipeline.run_full_e2e_simulation()
        billing_sim = self.billing.generate_client_invoice_and_margin_report(
            client_name="Pensjonat Grań",
            monthly_mrr_fee_pln=1499.0,
            monthly_inquiries=500
        )

        all_urls_ok = all(u["success"] for u in url_results)
        all_workflows_ok = all(w["valid"] for w in workflow_results)
        outreach_ok = compliance.get("has_nationwide_scope") and compliance.get("has_photo_disclaimer")

        is_ready = all_urls_ok and all_workflows_ok and outreach_ok and e2e_sim["status"] == "100%_TESTED_SUCCESS"

        return {
            "agencyName": "AAAS Agency (AI Automation Agency as a Service)",
            "overallReadiness": "100% READY FOR COMMERCIAL LAUNCH" if is_ready else "NEEDS REVIEW",
            "urlVerification": url_results,
            "workflowsVerification": workflow_results,
            "outreachCompliance": compliance,
            "e2ePipelineStatus": e2e_sim["status"],
            "agencyOperatingMargin": f"{billing_sim['agencyOperatingMarginPercent']}%"
        }
