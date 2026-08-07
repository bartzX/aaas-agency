"""
AAAS Agency Engine - Główny moduł wykonawczy dla agencji AI Automation Agency as a Service.
Łączy narzędzia z Twojego GitHub Starred:
- agency-agents
- n8n
- openclaw
- deep-research
- firecrawl & open-lovable
- crawl4ai & browser-use
- twentyhq/twenty CRM & calcom/cal.diy
- crewAI & langgraph
"""
import os
import glob
import json
import yaml
from typing import List, Dict, Any

class AAASAgentLoader:
    """Ładuje definicje agentów z katalogu agents/."""
    def __init__(self, agents_dir: str = "agents"):
        self.agents_dir = agents_dir

    def load_all_agents(self) -> List[Dict[str, Any]]:
        agents = []
        pattern = os.path.join(self.agents_dir, "*.yaml")
        for path in glob.glob(pattern):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if data:
                        agents.append(data)
            except Exception as e:
                print(f"Błąd ładowania agenta z {path}: {e}")
        return agents

class AAASWorkflowValidator:
    """Waliduje pliki przepływów n8n w formacie JSON z katalogu workflows/."""
    def __init__(self, workflows_dir: str = "workflows"):
        self.workflows_dir = workflows_dir

    def validate_workflows(self) -> List[Dict[str, Any]]:
        results = []
        pattern = os.path.join(self.workflows_dir, "*.json")
        for path in glob.glob(pattern):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    name = data.get("name", os.path.basename(path))
                    nodes_count = len(data.get("nodes", []))
                    results.append({
                        "file": os.path.basename(path),
                        "name": name,
                        "nodes_count": nodes_count,
                        "valid": nodes_count > 0
                    })
            except Exception as e:
                results.append({
                    "file": os.path.basename(path),
                    "valid": False,
                    "error": str(e)
                })
        return results

class AAASOrchestrator:
    """Orkiestrator symulujący obsługę nowego leada przez agencję."""
    def __init__(self):
        self.agent_loader = AAASAgentLoader()
        self.workflow_validator = AAASWorkflowValidator()

    def run_agency_audit(self) -> Dict[str, Any]:
        agents = self.agent_loader.load_all_agents()
        workflows = self.workflow_validator.validate_workflows()
        return {
            "agency_name": "AAAS Agency (AI Automation Agency as a Service)",
            "status": "active",
            "agents_loaded": len(agents),
            "workflows_validated": len(workflows),
            "agents_list": [a.get("name") for a in agents],
            "workflows_list": [w.get("name") for w in workflows if w.get("valid")]
        }
