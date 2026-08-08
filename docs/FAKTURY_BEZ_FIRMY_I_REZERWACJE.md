# Przewodnik: Faktury bez Firmy i Mechanizm Blokady Zarezerwowanych Terminów 💼🗓️
## Agencja AAAS (`bartzX/aaas-agency`) – Legalne Rozliczenia 2026 i Technologia Rezerwacji

Niniejszy dokument w pełni wyjaśnia kwestie prawno-podatkowe wystawiania faktur bez zarejestrowanej działalności gospodarczej w Polsce w 2026 roku oraz techniczną architekturę zapobiegania podwójnym rezerwacjom (*Overbooking / dubel terminów*) na stronach naszych klientów.

---

### CZĘŚĆ 1: 💼 Jak legalnie wystawić fakturę dla hotelu BEZ ZAKŁADANIA FIRMY?

W Polsce masz do dyspozycji **2 w 100% legalne i bezpieczne rozwiązania**, dzięki którym nie płacisz stałych składek ZUS ani nie musisz rejestrować Jednoosobowej Działalności Gospodarczej (JDG):

#### Rozwiązanie 1: Działalność Nierejestrowana (Dla przychodów do ok. 3 500 zł / miesiąc)
* **Podstawa prawna 2026:** Zgodnie z art. 5 *Prawa przedsiębiorców*, każda osoba fizyczna może prowadzić działalność bez rejestracji w CEIDG i bez ZUS, jeśli jej miesięczny przychód należny nie przekracza **75% kwoty minimalnego wynagrodzenia za pracę**.
* **Limit na rok 2026:** Płaca minimalna w Polsce wynosi ponad 4 666 zł brutto, co daje Ci miesięczny limit przychodu na poziomie **ok. 3 500 zł**.
* **Jak wystawiasz dokument dla hotelu?**
  1. Wystawiasz dokument o nazwie **„Faktura bez VAT”** (lub „Rachunek”).
  2. Dokument zawiera:
     * Twoje imię, nazwisko i adres (jako sprzedawcy),
     * Nazwę, adres i NIP klienta (np. Pensjonat Grań, ul. Kolorowa 3, 58-540 Karpacz, NIP: ...),
     * Numer faktury i datę wystawienia,
     * Nazwę usługi: *„Zarządzanie automatyzacją IT i utrzymanie serwisu internetowego (okres ...)”*,
     * Kwotę do zapłaty (np. **1 499,00 zł**).
  3. **Narzędzia:** Możesz używać darmowych programów online: **Fakturownia.pl**, **iFirma.pl** lub **inFakt.pl** (wybierasz w ustawieniach *„Działalność nierejestrowana / zwolniony z VAT”*).
* **Podatek:** Zarobioną kwotę wpisujesz raz w roku do rocznego PIT-36 w rubryce *„Działalność nierejestrowana”*.

#### Rozwiązanie 2: Inkubatory Przedsiębiorczości / Twój Startup (Dla wdrożeń jednorazowych, np. za 5 900 zł)
* Kiedy sprzedajesz hotelowi **Pakiet Wdrożeniowy (High-Ticket Setup za np. 5 900 zł netto)**, przekraczasz limit miesięczny 3 500 zł.
* **Jak wtedy wystawić fakturę VAT 23% bez własnej firmy?**
  * Zapisujesz się do **Inkubatora Przedsiębiorczości** (np. **Twój Startup - `twojstartup.pl`**, **AIP** lub portal **`Useme.com`**).
  * Inkubator udostępnia Ci swoją osobowość prawną, NIP oraz rachunek bankowy.
  * Klient otrzymuje od Inkubatora oficjalną **Fakturę VAT 23%** (np. na 5 900 zł netto + VAT), wrzuca ją w koszty firmy i odlicza VAT.
  * Ty wypłacasz swoje pieniądze legalnie na podstawie wewnętrznej umowy o dzieło/zlecenie, **nie płacąc żadnego ZUS-u za JDG**!

---

### CZĘŚĆ 2: 🗓️ Jak działa System Rezerwacji na Stronie? (Blokowanie Zajętych Terminów)

Największym obawą właściciela hotelu jest tzw. **Dubel Rezerwacyjny (Overbooking)** – sytuacja, w której gość z Booking.com i gość z naszej strony zarezerwują ten sam pokój w tym samym czasie.

#### Nasze Rozwiązanie: Dwukierunkowa Synchronizacja iCal (.ics) w Czasie Rzeczywistym
Każdy portal noclegowy (Booking.com, Airbnb, Expedia) posiada uniwersalny kalendarz w formacie **iCal (`.ics`)**. Zbudowaliśmy w repozytorium specjalny silnik weryfikacji dostępności (`src/booking_calendar_engine.py`), który działa w 3 krokach:

```text
Booking.com / Airbnb (Kalendarze .ics)
           │
           ▼  (Automatyczna synchronizacja w n8n / iCal Parser)
Silnik AAAS (`booking_calendar_engine.py`) ──► Wyciąga listę dat zajętych (`BUSY DATES`)
           │
           ▼
Wyszukiwarka na stronie (`pensjonatgran.pl` / `FullCalendar`)
  └─► Wyszarza zablokowane daty w kalendarzu (klient NIE MOŻE ich kliknąć!)
```

1. **Odczyt zajętych terminów w locie:**  
   Zanim klient na stronie hotelu otworzy kalendarz, skrypt odczytuje zsynchronizowany plik `.ics` pokoju (np. `room_studio.ics`) z Booking.com.
2. **Automatyczne wyszarzenie w kalendarzu strony:**  
   Wszystkie zarezerwowane już dni (np. *15–18 sierpnia*) są **zablokowane (wyszarzone i nieklikalne)** w widżecie kalendarza (wykorzystujemy bibliotekę `fullcalendar/fullcalendar` z Twoich gwiazdek). Klient **nie ma technicznej możliwości** wyboru zajętego terminu.
3. **Automatyczna propozycja terminu:**  
   Jeżeli gość zapyta o zajętą datę w czacie z wirtualnym recepcjonistą AI, system odpowie:  
   > *„Przepraszamy, pokój Studio w terminie 15–18 sierpnia jest już zarezerwowany. Najbliższy wolny termin dla tego pokoju to **18–21 sierpnia**.”*
4. **Blokada w drugą stronę:**  
   Gdy gość zarezerwuje pokój na naszej stronie, system natychmiast wpisuje datę do naszego `.ics` i informuje Booking.com, który od razu zdejmuje tę datę z portalu.

---

### CZĘŚĆ 3: ⭐ 4 Nowe Narzędzia Dodałe do Twojego GitHub Starred (Research 2026)
W ramach rozszerzenia stosu technologicznego agencji o funkcje kalendarzowe i fakturujące, dodałem do Twoich gwiazdek 4 wiodące repozytoria open-source:

| Narzędzie | Liczba Gwiazdek | Do czego służy w Twojej agencji AAAS? |
| :--- | :---: | :--- |
| **`fullcalendar/fullcalendar`** | **20 600+ ⭐** | Najlepsza biblioteka kalendarzowa JS do wyświetlania wolnych/wyszarzonych terminów na stronach React. |
| **`invoiceninja/invoiceninja`** | **9 900+ ⭐** | Otwartoźródłowy system do fakturowania, ofertowania i śledzenia płatności klientów. |
| **`gotenberg/gotenberg`** | **12 800+ ⭐** | API do generowania pięknych faktur i wycen w formacie PDF w przepływach `n8n`. |
| **`collective/icalendar`** | **1 100+ ⭐** | Standardowy parser kalendarzy `.ics` – weryfikuje dostępność pokoi hotelowych. |
