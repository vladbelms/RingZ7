def znajdz_dzien_tygodnia(poczatkowy_dzien, dni_do_dodania):
    dni_tygodnia = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
    indeks_poczatkowy = dni_tygodnia.index(poczatkowy_dzien)
    indeks_docelowy = (indeks_poczatkowy + dni_do_dodania) % 7
    return dni_tygodnia[indeks_docelowy]

poczatkowy_dzien = input("Podaj początkowy dzień tygodnia: ")
dni_do_dodania = int(input("Podaj liczbę dni do dodania: "))

wynikowy_dzien = znajdz_dzien_tygodnia(poczatkowy_dzien, dni_do_dodania)
print(f"Za {dni_do_dodania} dni od dnia {poczatkowy_dzien} będzie {wynikowy_dzien}")