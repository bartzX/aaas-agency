# Standard Wdrożenia Domen Polskich (`.pl`) w Agencji AAAS 🇵🇱🌐
## 2 Metody Podpinania Własnej Domeny `.pl` (w tym Metoda Vercel Drop z wideo)

W naszej komunikacji handlowej oraz wdrożeniach dla klientów w Polsce zawsze posługujemy się prestiżowymi domenami narodowymi z końcówką **`.pl`** (np. **`pensjonatsyriusz.pl`**, **`pensjonatgran.pl`**). Link stagingowy służy klientowi tylko do weryfikacji przed podpięciem jego docelowego adresu.

---

### ⭐ METODA 1: Vercel Drop (`vercel.com/drop` – Metoda z poradnika wideo)
Ta metoda jest najszybsza, darmowa i pozwala w 30 sekund opublikować gotowy folder `dist` i podpiąć pod niego dowolną domenę `.pl`:

1. **Przeciągnięcie paczki ze stroną (`vercel.com/drop`):**
   * Wchodzisz w przeglądarce na stronę: **[https://vercel.com/drop](https://vercel.com/drop)**
   * Przeciągasz myszką folder `dist` (lub spakowany plik `.zip` ze zbudowaną stroną) i upuszczasz w oknie.
   * Po 5 sekundach Vercel publikuje projekt na żywo i przydziela natychmiastowy link roboczy.
2. **Podpięcie domeny `.pl` w 1 kliknięcie:**
   * W panelu nowo utworzonego projektu klikasz zakładkę **Settings → Domains**.
   * Wpisujesz polską domenę klienta, np. **`pensjonatgran.pl`** (zaczyna się proces weryfikacji).
   * Vercel wyświetli Ci adres IP (rekord A: `76.76.21.21`) lub CNAME (`cname.vercel-dns.com`).
3. **Konfiguracja u polskiego rejestratora (np. SeoHost, OVH, cyber_Folks):**
   * Wklejasz podany rekord w strefie DNS domeny `.pl`.
   * Vercel automatycznie włącza zieloną kłódkę SSL (HTTPS) – strona działa natychmiast pod adresem **`https://pensjonatgran.pl`**!

---

### METODA 2: GitHub Pages (Bezpośrednio z repozytorium)
Alternatywna metoda podpinania domeny bez zewnętrznych platform:
1. W ustawieniach repozytorium (*Settings → Pages → Custom domain*) wpisujesz **`pensjonatgran.pl`**.
2. W panelu DNS domeny `.pl` ustawiasz 4 rekordy A GitHub Pages (`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`).
3. GitHub automatycznie włącza darmowy SSL Let's Encrypt.

---

### 💡 Wskazówka Handlowa
Dzięki obu tym metodom (w szczególności **Vercel Drop**) koszt utrzymania szybkiego hostingu dla agencji wynosi **0 zł**, a klient otrzymuje witrynę ładującą się poniżej 2 sekund na domenie `.pl`!
