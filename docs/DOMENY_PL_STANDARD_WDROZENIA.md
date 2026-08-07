# Standard Wdrożenia Domen Polskich (`.pl`) w Agencji AAAS 🇵🇱🌐
## Jak każda strona hotelowa otrzymuje własną domenę z końcówką `.pl`

W naszej komunikacji handlowej oraz wdrożeniach dla klientów w Polsce zawsze posługujemy się domenami narodowymi z końcówką **`.pl`** (np. **`pensjonatsyriusz.pl`**, **`pensjonatgran.pl`**), a nie surowymi linkami GitHub Pages. Link `bartzx.github.io/Projekt/` służy wyłącznie jako **natychmiastowe środowisko podglądowe (Staging / Live Preview)** dla klienta przed podpięciem jego docelowej domeny.

---

### 1. ⚙️ Jak w 60 sekund podpinamy domenę `.pl` klienta pod nasze repozytorium?

Kiedy hotel (np. Pensjonat Grań) kupuje od nas Pakiet Wdrożeniowy:
1. **Rejestracja lub cesja domeny `.pl`:**
   * Jeśli hotel nie ma domeny, rejestrujemy dla niego **`pensjonatgran.pl`** na polskim hostingu (np. SeoHost, OVH, cyber_Folks – koszt ok. 12–15 zł/rok).
2. **Konfiguracja rekordów DNS w panelu domeny:**
   * Wprowadzamy 4 oficjalne rekordy A wiersza GitHub Pages w strefie DNS domeny `.pl`:
     * `185.199.108.153`
     * `185.199.109.153`
     * `185.199.110.153`
     * `185.199.111.153`
   * Dodajemy rekord CNAME dla poddomeny `www.pensjonatgran.pl` kierujący na `bartzx.github.io`.
3. **Włączenie własnej domeny w GitHub Settings:**
   * W ustawieniach repozytorium (*Settings → Pages → Custom domain*) wpisujemy **`pensjonatgran.pl`**.
   * GitHub automatycznie generuje **darmowy certyfikat bezpieczeństwa SSL (HTTPS)** Let's Encrypt.
4. **Efekt dla klienta:**  
   Strona jest dostępna pod prestiżowym, polskim adresem **`https://pensjonatgran.pl`**, działa z pełną prędkością CDN i ma zieloną kłódkę bezpieczeństwa!

---

### 2. 🎯 Standard w Komunikacji Handlowej
W skryptach SMS i e-mailach wysyłanych do hoteli zawsze zaznaczamy, że w ramach wdrożenia otrzymają (lub unowocześnią) swoją domenę z końcówką **`.pl`**, co buduje zaufanie gości i natychmiast pozycjonuje ich wyżej od konkurencji w polskim Google.
