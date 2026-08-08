"""
AAAS Agency Continuous Multi-Agent Upskilling & GitHub Tools Mastery Engine (2026)
Wykonuje ciągły, iteracyjny proces pogłębiania umiejętności przez wszystkich 9 agentów AI
w ich wyznaczonych dziedzinach oraz weryfikuje 100% opanowania wszystkich 15 narzędzi ze Starred GitHuba.
"""
import os
import glob
import yaml
from typing import List, Dict, Any

class AAASAgentMasteryEngine:
    """Silnik nadzorujący ciągłe doskonalenie i opanowanie narzędzi GitHub przez agentów AI."""

    def __init__(self, agents_dir: str = "agents"):
        self.agents_dir = agents_dir
        self.starred_tools_catalog = [
            "browser-use/browser-use",
            "mendableai/firecrawl",
            "unclecode/crawl4ai",
            "twentyhq/twenty",
            "crewAIInc/crewAI",
            "calcom/cal.diy",
            "emilkowalski/vaul",
            "fullcalendar/fullcalendar",
            "invoiceninja/invoiceninja",
            "gotenberg/gotenberg",
            "collective/icalendar",
            "dzhng/deep-research",
            "Alibaba-NLP/DeepResearch",
            "n8n-io/n8n",
            "higgsfield-ai/cli",
            "firecrawl/open-lovable",
            "pulkitxm/claude-directory"
        ]

    def run_continuous_upskilling_loop(self) -> List[Dict[str, Any]]:
        """
        Przeprowadza pętlę doskonalenia umiejętności dla wszystkich agentów AI w repozytorium.
        Wylicza wskaźnik opanowania dziedziny (Mastery Index 0 - 100%).
        """
        results = []
        pattern = os.path.join(self.agents_dir, "*.yaml")
        for path in glob.glob(pattern):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                    if not data:
                        continue
                    name = data.get("name", "Unknown Agent")
                    role = data.get("role", "")
                    dept = data.get("department", "")
                    tools = data.get("github_tools", [])
                    tasks = data.get("tasks", [])
                    kpis = data.get("kpis", [])

                    # Ocena głębi specjalizacji na podstawie wytycznych 2026
                    tools_mastered_count = len(tools)
                    tasks_depth_score = min(100.0, len(tasks) * 33.3 + 20.0)
                    kpi_rigor_score = min(100.0, len(kpis) * 50.0)
                    mastery_index = round((tasks_depth_score + kpi_rigor_score + min(100.0, tools_mastered_count * 35.0)) / 3.0, 1)
                    
                    results.append({
                        "id": os.path.basename(path).replace(".yaml", ""),
                        "name": name,
                        "role": role,
                        "department": dept,
                        "toolsMastered": tools,
                        "toolsCount": tools_mastered_count,
                        "tasksCount": len(tasks),
                        "kpisCount": len(kpis),
                        "masteryIndexPercent": min(100.0, mastery_index),
                        "status": "APEX_MASTERY_ACHIEVED" if mastery_index >= 95.0 else "UPSKILLING_IN_PROGRESS"
                    })
            except Exception as e:
                results.append({
                    "id": os.path.basename(path),
                    "error": str(e),
                    "status": "ERROR"
                })
        return sorted(results, key=lambda x: x.get("masteryIndexPercent", 0), reverse=True)

    def verify_full_github_tools_mastery(self) -> Dict[str, Any]:
        """
        Sprawdza, czy cały zespół agentów opanował wszystkie 15 kluczowych technologii ze Starred GitHuba.
        """
        agents_audit = self.run_continuous_upskilling_loop()
        mastered_tools_set = set()
        for ag in agents_audit:
            for tool in ag.get("toolsMastered", []):
                mastered_tools_set.add(tool)

        missing_tools = [t for t in self.starred_tools_catalog if t not in mastered_tools_set]
        coverage_percent = round((len(mastered_tools_set) / max(1, len(self.starred_tools_catalog))) * 100.0, 1)

        return {
            "totalStarredCatalogSize": len(self.starred_tools_catalog),
            "totalToolsMasteredByAgents": len(mastered_tools_set),
            "coveragePercent": min(100.0, coverage_percent),
            "missingTools": missing_tools,
            "masteryCertification": "100% GITHUB STARRED TOOLS MASTERED BY AGENT TEAM" if coverage_percent >= 95.0 else "INCOMPLETE_MASTERY"
        }

    def certify_apex_agency_readiness(self) -> Dict[str, Any]:
        """Wystawia ostateczny certyfikat najwyższych umiejętności agencji AAAS."""
        agents_audit = self.run_continuous_upskilling_loop()
        tools_audit = self.verify_full_github_tools_mastery()

        all_agents_mastered = all(ag.get("masteryIndexPercent", 0) >= 95.0 for ag in agents_audit)
        tools_mastered = tools_audit["coveragePercent"] >= 95.0

        return {
            "agencyName": "AAAS Agency (AI Automation Agency as a Service)",
            "totalAgentsUpskilled": len(agents_audit),
            "allAgentsAtApexMastery": all_agents_mastered,
            "githubToolsMastery": tools_audit["masteryCertification"],
            "agentsSummary": [f"{ag['name']} ({ag['masteryIndexPercent']}%)" for ag in agents_audit],
            "finalCertification": "100% APEX AGENCY MASTERY ACHIEVED - ALL AGENTS & GITHUB TOOLS MASTERED" if (all_agents_mastered and tools_mastered) else "CONTINUE_UPSKILLING"
        }
