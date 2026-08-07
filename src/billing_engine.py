"""
AAAS Agency Billing & AI Cost Calculator Engine
Moduł wyliczający koszty tokenów AI, generujący pakiety płatności Stripe / BLIK
oraz monitorujący czystą marżę operacyjną agencji na klientach abonamentowych (MRR).
"""
from typing import Dict, Any, List

class AAASBillingEngine:
    """Kalkulator finansowy rozliczeń z klientem i kosztów utrzymania API AI."""

    def __init__(self, agency_name: str = "AAAS Agency"):
        self.agency_name = agency_name

    def calculate_ai_token_cost(self, monthly_inquiries: int, avg_tokens_per_inquiry: int = 2000, 
                                cost_per_million_tokens_usd: float = 0.15, usd_to_pln: float = 4.0) -> Dict[str, Any]:
        """
        Wylicza rzeczywisty koszt API AI (np. OpenAI GPT-4o-mini / DeepSeek-V3)
        dla danej liczby rozmów na stronie hotelu w miesiącu.
        """
        total_tokens = monthly_inquiries * avg_tokens_per_inquiry
        cost_usd = (total_tokens / 1_000_000) * cost_per_million_tokens_usd
        cost_pln = cost_usd * usd_to_pln

        return {
            "model": "GPT-4o-mini / DeepSeek-V3 (LLM API)",
            "monthlyInquiries": monthly_inquiries,
            "avgTokensPerInquiry": avg_tokens_per_inquiry,
            "totalTokensUsed": total_tokens,
            "totalCostUSD": round(cost_usd, 4),
            "totalCostPLN": round(cost_pln, 2),
            "costPerInquiryPLN": round(cost_pln / max(1, monthly_inquiries), 4)
        }

    def generate_client_invoice_and_margin_report(self, client_name: str, monthly_mrr_fee_pln: float = 1499.0, 
                                                  monthly_inquiries: int = 500, hosting_cost_pln: float = 0.0,
                                                  vps_share_cost_pln: float = 10.0) -> Dict[str, Any]:
        """
        Generuje raport zysku netto agencji z danego klienta abonamentowego
        wraz z wyliczeniem marży operacyjnej i linku płatności subskrypcyjnej.
        """
        ai_cost = self.calculate_ai_token_cost(monthly_inquiries)
        total_operational_cost = ai_cost["totalCostPLN"] + hosting_cost_pln + vps_share_cost_pln
        net_profit_pln = monthly_mrr_fee_pln - total_operational_cost
        margin_percent = (net_profit_pln / max(0.01, monthly_mrr_fee_pln)) * 100

        return {
            "clientName": client_name,
            "billingType": "AUTOMATIC_MONTHLY_SUBSCRIPTION (MRR)",
            "paymentMethods": ["Stripe Subscriptions (Karta)", "Przelewy24 (BLIK / Przelew cykliczny)"],
            "monthlySubscriptionFeePLN": monthly_mrr_fee_pln,
            "costBreakdownPLN": {
                "aiTokensLLM": ai_cost["totalCostPLN"],
                "githubPagesHosting": hosting_cost_pln,
                "n8nServerShare": vps_share_cost_pln,
                "totalOperationalCost": round(total_operational_cost, 2)
            },
            "agencyNetProfitPLN": round(net_profit_pln, 2),
            "agencyOperatingMarginPercent": round(margin_percent, 1),
            "paymentLinkDemo": f"https://buy.stripe.com/demo_{client_name.lower().replace(' ', '_')}_mrr_1499"
        }
