kwota_pozyczki_poczatkowa = float(input("Podaj kwotę Twojej pożyczki: "))
oprocentowanie = float(input("Podaj oprocentowanie pożyczki (ilość %): "))
rata = float(input("Podaj wysokość miesięcznej raty kredytu: "))

inflacja = float(input())

#TODO:  poprawić pobieranie inputów - jak zrobić, że część inputów jest podawana przez użytkownika, a część zaciągana z pliku .txt

# z Excela: =(1 + ((inflacjaWDanymMiesiącu+3)/1200)) * kwotaPozostałaDoSpłacenia - 200
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki

szablon = "miesiąc {}: Twoja pozostała kwota kredytu to {}zł, to o {}zł mniej niż w poprzednim miesiącu."
nr_miesiaca = 0

podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

nr_miesiaca += 1
kwota_pozyczki_poczatkowa = pozostala_kwota_pozyczki
pozostala_kwota_pozyczki = (1 + (inflacja + oprocentowanie) / 1200) * kwota_pozyczki_poczatkowa - 200
roznica = kwota_pozyczki_poczatkowa - pozostala_kwota_pozyczki
podsumowanie_miesiaca = szablon.format(nr_miesiaca + 1, (round(pozostala_kwota_pozyczki, 2)), (round(roznica, 2)))
print(podsumowanie_miesiaca)

# print("Twoja pozostała kwota kredytu to ", round(kwota_pozyczki_koncowa, 2), "zł, ")
# print("to o ", round(roznica, 2), "zł mniej niż w poprzednim miesiącu.")

#TODO: napisać to dla 24 miesięcy

