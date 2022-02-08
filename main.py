kwota_pozyczki_poczatkowa = float(input("Podaj kwotę Twojej pożyczki: "))
print(end="\n")
oprocentowanie = float(input("Podaj oprocentowanie pożyczki (ilość %): "))
print(end="\n")
rata = float(input("Podaj wysokość miesięcznej raty kredytu: "))
print(end="\n")


szablon = "miesiąc {}: Twoja pozostała kwota kredytu to {}zł, to o {}zł mniej niż w poprzednim miesiącu."

inflacja = float(input())
nr_miesiaca = 0
# z Excela: =(1 + ((inflacjaWDanymMiesiącu+3)/1200)) * kwotaPozostałaDoSpłacenia - 200
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

inflacja = float(input())
nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)
