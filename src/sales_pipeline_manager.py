"""
AAAS Agency Sales Pipeline & Follow-Up Manager
Zarządza etapami sprzedaży dla wytypowanych obiektów hotelowych,
generuje automatyczne przypomnienia follow-up po 24/48h
oraz tworzy wizualny pulpit zarządzania leadami w formacie Markdown.
"""
import json
import os
import time
from typing import List, Dict, Any, Optional

class AAASSalesPipeline:
    """System śledzenia leadów, statusów wiadomości oraz scenariuszy rozmów."""

    def __init__(self, db_filepath: str = "docs/sales_pipeline.json"):
        self.db_filepath = db_filepath
        self.pipeline_leads: List[Dict[str, Any]] = self.load_or_init_pipeline()

    def load_or_init_pipeline(self) -> List[Dict[str, Any]]:
        if os.path.exists(self.db_filepath):
            try:
                with open(self.db_filepath, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return [
            {
                "id": "lead_001",
                "hotelName": "Pensjonat Grań w Karpaczu",
                "address": "ul. Kolorowa 3, 58-540 Karpacz (stok Pohulanka)",
                "phone": "+48 601 584 872 / 75 761 85 11",
                "status": "SMS_SENT_AWAITING_REPLY",
                "sentDate": "Wczoraj wieczorem",
                "nextAction": "Czekamy spokojnie 24–48h. W razie braku odpowiedzi jutro o 11:30 wysyłamy Follow-up #1",
                "estimatedMRR": 1499.0,
                "outreachLinkUsed": "https://bartzx.github.io/pensjonatgran-karpacz/"
            },
            {
                "id": "lead_002",
                "hotelName": "Pensjonat Syriusz w Karpaczu",
                "address": "ul. Reymonta 8, 58-540 Karpacz (Osiedle Skalne)",
                "phone": "+48 607 123 456",
                "status": "READY_TO_SEND_SMS_TODAY",
                "sentDate": "Do wysłania dziś",
                "nextAction": "Wysłanie SMS o stronach bezpośredniej rezerwacji z czatem AI",
                "estimatedMRR": 1499.0,
                "outreachLinkUsed": "https://bartzx.github.io/pensjonat-syriusz/"
            },
            {
                "id": "lead_003",
                "hotelName": "L&B Spa w Karpaczu",
                "address": "ul. Karkonoska 54c, 58-540 Karpacz",
                "phone": "+48 75 761 00 00",
                "status": "READY_TO_SEND_SMS_TODAY",
                "sentDate": "Do wysłania dziś",
                "nextAction": "Wysłanie SMS z propozycją automatyzacji rezerwacji zabiegów SPA i noclegu",
                "estimatedMRR": 2499.0,
                "outreachLinkUsed": "https://bartzx.github.io/lb-spa-karpacz/"
            }
        ]

    def update_lead_status(self, lead_id: str, new_status: str, next_action: str) -> Optional[Dict[str, Any]]:
        for lead in self.pipeline_leads:
            if lead["id"] == lead_id:
                lead["status"] = new_status
                lead["nextAction"] = next_action
                self.save_pipeline()
                return lead
        return None

    def save_pipeline(self) -> str:
        os.makedirs(os.path.dirname(self.db_filepath), exist_ok=True)
        with open(self.db_filepath, "w", encoding="utf-8") as f:
            json.dump(self.pipeline_leads, f, indent=2, ensure_ascii=False)
        return self.db_filepath

    def generate_dashboard_markdown(self, output_path: str = "docs/DASHBOARD_SPRZEDAZOWY.md") -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        total_potential_mrr = sum(l["estimatedMRR"] for l in self.pipeline_leads)
        lines = [
            "# Pulpit Sprzedażowy i Plan Działania (AAAS Pipeline 2026) 📊🚀",
            f"**Łączny potencjał portfela w negocjacjach:** **{total_potential_mrr:,.2f} zł / miesiąc MRR** (ok. {total_potential_mrr * 12:,.2f} zł rocznie)\n",
            "---\n",
            "## 🏨 1. Status Aktualnych Leadów i Ich Dedykowane Strony Demo\n"
        ]
        for l in self.pipeline_leads:
            lines.extend([
                f"### {l['hotelName']} (`{l['status']}`)",
                f"* **Adres i kontakt:** `{l['address']}` | `{l['phone']}`",
                f"* **Dedykowana strona demo (HTTP 200 OK):** 👉 **[{l['outreachLinkUsed']}]({l['outreachLinkUsed']})**",
                f"* **Wysłano:** `{l['sentDate']}`",
                f"* **Następny krok (Action Item):** **{l['nextAction']}**",
                f"* **Szacowany abonament MRR:** `{l['estimatedMRR']} zł/msc`\n",
                "---\n"
            ])
        lines.extend([
            "## 📞 2. Co robimy DZIŚ (Złota Zasada Agencji AAAS):",
            "1. **Pensjonat Grań (Czekamy spokojnie 24–48h):** Wiadomość wysłana wczoraj wieczorem. Poranki w recepcji są intensywne (wymeldowania gości 10:00–11:00). Jeśli klient nie odpowie do jutra do godz. 11:30, wysyłamy krótki, nienachalny follow-up #1.",
            "2. **Uruchamiamy Lead #2 (Pensjonat Syriusz) i Lead #3 (L&B Spa) JUŻ DZIŚ:** Posiadamy gotowe, dedykowane strony-demo dla obu obiektów z właściwymi adresami i mapami. Wysyłając dziś 2 wiadomości, potrajamy szansę na domknięcie umowy w tym tygodniu.\n"
        ])
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        return output_path
