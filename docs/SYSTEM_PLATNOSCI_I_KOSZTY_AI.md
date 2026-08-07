# Wyjaśnienie Systemu Płatności i Kosztów Sztucznej Inteligencji (AI API) 💳🤖
## Jak zarabiasz, jak rozliczasz klientów i ile naprawdę kosztuje utrzymanie AI?

Przejrzysta ekonomia agencji AAAS opiera się na prostym modelu: **Klient płaci Ci wysoki abonament za wartość biznesową (MRR), a Ty opłacasz mikroskopijny koszt zużycia tokenów AI na swoim serwerze.** Poniżej wyjaśniamy od A do Z, jak to działa w praktyce.

---

### 1. 💳 Jak Klient (Hotel) płaci Tobie (BartzX / AAAS Agency)?

Masz do wyboru 2 najskuteczniejsze systemy rozliczeń dostosowane do polskiego rynku:

#### A. Płatność Jednorazowa za Wdrożenie Strony (np. 4 900 zł – 5 900 zł netto):
* **Bramka Płatności / Faktura:** Wystawiasz klientowi fakturę proforma z 7-dniowym terminem płatności (przelew tradycyjny) LUB wysyłasz mu link do szybkiej płatności w **Stripe / Przelewy24 (BLIK, Karta, Przelew online)**.
* **Warunki:** Prace startują po opłaceniu wdrożenia.

#### B. Płatność Abonamentowa za Obsługę AI 24/7 (MRR – np. 1 499 zł netto / miesiąc):
* **Automatyczne Subskrypcje w Stripe Billing lub Przelewy24 Subskrypcje:**  
  Klient podpina swoją kartę płatniczą w Twoim bezpiecznym panelu klienta (jednorazowo przy starcie). System **automatycznie pobiera kwotę 1 499 zł w każdy 1. dzień miesiąca** i samoczynnie wysyła mu fakturę na e-mail.
* **Brak konieczności ściągania długów:** Jeśli płatność się nie powiedzie, system automatycznie wysyła powiadomienie, a po 7 dniach może zawiesić webhooki AI.

---

### 2. 🤖 Jak Ty płacisz za Sztuczną Inteligencję (AI API) i skąd się bierze AI w n8n?

Nasza architektura recepcjonisty 24/7 w **`n8n`** korzysta z oficjalnych interfejsów programistycznych (API) dostawców modeli AI (np. **OpenAI GPT-4o-mini**, **DeepSeek-V3** lub **Claude 3.5 Haiku**).

#### Jak działa rozliczenie za AI?
* Zakładasz konto dla programistów na platformie np. `platform.openai.com` i podpinasz tam swoją kartę płatniczą LUB doładowujesz saldo np. kwotą 20 USD (ok. 80 zł – system prepaid).
* W n8n wklejasz klucz API (`sk-...`). Model AI rozlicza Cię wyłącznie za **faktycznie przetworzone słowa (tokeny)**.

---

### 3. 📊 Ile naprawdę KOSZTUJE obsługa AI jednego hotelu? (Wyliczenie Tokenów)

Większość osób boi się kosztów sztucznej inteligencji, podczas gdy w rzeczywistości są one **mikroskopijne**:

* **Koszt 1 miliona tokenów w modelu GPT-4o-mini:** ok. 0,15 USD (ok. 0,60 zł).
* **Średnia rozmowa gościa z recepcjonistą AI (6–10 wiadomości):** zużywa ok. 2 000 tokenów.
* **Koszt jednej pełnej rozmowy rezerwacyjnej:** **0,0003 USD = ok. 0,0012 zł (mniej niż 1 grosz!)**

#### Symulacja miesięcznych kosztów dla bardzo obłożonego hotelu (np. Pensjonat Grań):
* **Liczba rozmów AI w miesiącu (selekcja, parking, rezerwacje):** np. 500 zapytań gości.
* **Łączne zużycie tokenów:** 500 * 2 000 = 1 000 000 tokenów.
* **Twój realny miesięczny rachunek od OpenAI za ten hotel:** **0,60 zł – 2,00 zł (mniej niż pół dolara!)**

---

### 4. 💎 Twoja Czysta Marża Finansowa (Zysk Agencji)

| Pozycja w budżecie klienta | Kwota netto / miesiąc |
| :--- | :---: |
| **Przychód od klienta (Abonament MRR za AI 24/7)** | **+1 499,00 zł** |
| Koszt utrzymania API AI (500 zapytań w miesiącu) | -1,50 zł |
| Koszt hostingu strony (GitHub Pages / Cloudflare) | 0,00 zł |
| Koszt infrastruktury n8n / serwera VPS (podzielony na 10 klientów) | -8,00 zł |
| **TWÓJ CZYSTY ZYSK NETTO CO MIESIĄC Z 1 KLIENTA:** | **+1 489,50 zł (Marża: 99,3%!)** |

**Podsumowanie:** Klient z radością płaci Ci 1 499 zł co miesiąc, ponieważ AI oszczędza mu ponad 4 000 zł na prowizjach Booking.com i czasie recepcji. Twój koszt dostarczenia tej technologii nie przekracza 10 złotych miesięcznie!
