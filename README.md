# AAAS Agency (`bartzX/aaas-agency`) 🚀
## AI Automation Agency as a Service – Kompletna Platforma Operacyjna dla MŚP

Witaj w repozytorium **AAAS Agency** – kompletnej, gotowej do produkcji strukturze biznesowo-technologicznej do automatyzacji procesów marketingowych, rezerwacyjnych i obsługi klienta 24/7 dla hoteli, pensjonatów i firm usługowych w Polsce i w Europie.

---

### 🌟 Nasz Ekosystem i Integracje (100% GitHub Starred Stack 2026)
To repozytorium jest silnikiem integracyjnym dla 15 kluczowych otwartych technologii na Twojej liście gwiazdek (*Starred*):
* **Prospecting & Scraping:** `unclecode/crawl4ai`, `mendableai/firecrawl`, `browser-use/browser-use`
* **Produkcja Stron & UX/UI:** `firecrawl/open-lovable`, `msitarzewski/agency-agents`
* **Deep Research & Audyt:** `dzhng/deep-research`, `Alibaba-NLP/DeepResearch`, `langchain-ai/open_deep_research`, `langchain-ai/local-deep-researcher`
* **CRM & Bezpośrednie Rezerwacje:** `twentyhq/twenty` CRM, `calcom/cal.diy`
* **Automatyzacja 24/7 & Multi-Agent:** `n8n-io/n8n`, `openclaw/openclaw`, `crewAIInc/crewAI`, `langchain-ai/langgraph`
* **Wideo & Media:** `higgsfield-ai/cli`

---

### 📁 Struktura Repozytorium

```text
aaas-agency/
├── agents/                           # 5 Wyspecjalizowanych Agentów AI w formacie YAML
│   ├── lead_prospector.yaml          # Agent wyszukujący hotele bez własnej strony WWW
│   ├── deep_researcher.yaml          # Agent badający prowizje OTA i cenniki konkurencji
│   ├── web_developer.yaml            # Agent klonujący i budujący szybkie strony React/Vite
│   ├── ai_receptionist.yaml          # Wirtualny recepcjonista 24/7 na webhookach n8n
│   └── conversion_optimizer.yaml     # Strateg CRO dbający o konwersję rezerwacji bezpośrednich
├── workflows/                        # Gotowe pliki scenariuszy dla n8n (JSON)
│   ├── 01_hotel_lead_intake_webhook.json      # Obsługa zapytań, kalkulacja cen i zapis do Twenty CRM
│   └── 02_competitor_price_monitor.json       # Tygodniowy monitoring cenników konkurencji w Karpaczu
├── src/                              # Silnik w Pythonie (Loader agentów, walidator workflowów)
│   ├── engine.py
│   └── __init__.py
├── tests/                            # Zestaw testów automatycznych (pytest)
│   └── test_engine.py
├── .github/workflows/ci.yml          # Potok CI/CD walidujący składnię przy każdym commitcie
├── requirements.txt
└── README.md                         # Ten plik
```

---

### 🏨 Case Study #1 – Pensjonat Syriusz w Karpaczu
Naszym pierwszym w pełni wdrożonym projektem w modelu AAAS jest **Pensjonat Syriusz**:
* **Strona na żywo:** [https://bartzx.github.io/Projekt/](https://bartzx.github.io/Projekt/)
* **Wynik:** Strona z czasem ładowania <3s, interaktywnym widgetem rezerwacyjnym w Hero, Lightboxem w galerii i bezprowizyjną rezerwacją dla zwierząt (0 zł).

---

### 💻 Jak uruchomić i testować silnik lokalnie?

```bash
# 1. Instalacja zależności
pip install -r requirements.txt

# 2. Uruchomienie pełnego zestawu testów walidujących agentów i workflowy n8n
pytest -v
```
