

# Zadanie 2

print (end="\n")

uczelnia = ("Studiuję na WSIiZ")

print (uczelnia)

# Zadanie 3

print (end="\n")

imie = ("Jan")
wiek = ("20")
wzrost = ("178")

print ("Nazywam się", imie, "i mam", wiek, "lat.", end="\n")
print ("Mój wzrost to", wzrost, "cm.")

# Zadanie 4

print (end="\n")

cena = 39.99
Rabat = 0.2

# cena po rabacie = cena * (1-Rabat) = cena * 0.8
cena_po_rabacie = 39.99 * 0.8

print ("Cena po rabacie wynosi")
print (round(cena_po_rabacie, 2))

# Zadanie 5

print (end="\n")

bok_a = float(input("Podaj długość 1-szego boku prostokąta"))
bok_b = float(input("Podaj długość 2-ego boku prostokąta"))

pole = (bok_a * bok_b)
obwod = (2 * bok_a + 2 * bok_b)

print ("Pole wynosi", pole, end=("\n)"))
print ("Obwód wynosi", obwod)

# Zadanie 6

print (end="\n")

droga = float(input("Podaj drogę w km:"))
spalanie = float(input("Podaj spalanie samochodu w litrach na 100 km:"))
cena_paliwa_za_litr = 6.5
print ("cena paliwa za litr = 6.5 zł")

zuzycie_paliwa = droga * (spalanie / 100)
koszt = zuzycie_paliwa * cena_paliwa_za_litr

print ("Samochód spali", zuzycie_paliwa, "litrów paliwa", end=("\n"))
print ("Koszt wyniesie", koszt, "zł")

# Zadanie 6a

print (end="\n")

import random

los = random.randint(1, 20000)
droga = los
print ("Droga wynosi", droga)
spalanie = float(input("Podaj spalanie samochodu w litrach na 100 km:"))
cena_paliwa_za_litr = float(input("Podaj cenę paliwa za litr:"))

zuzycie_paliwa = droga * (spalanie / 100)
koszt = zuzycie_paliwa * cena_paliwa_za_litr

print ("Samochód spali", zuzycie_paliwa, "litrów paliwa", end=("\n"))
print ("Koszt wyniesie", koszt, "zł")

# Zadanie 6b1

print (end="\n")

droga = float(input("Podaj drogę w km:"))
spalanie = float(input("Podaj spalanie samochodu w litrach na 100 km:"))
cena_paliwa_za_litr = 6.5
print ("cena paliwa za litr = 6.5 zł")

zuzycie_paliwa = droga * (spalanie / 100)
koszt = zuzycie_paliwa * cena_paliwa_za_litr

print(f "Samochód spali {zuzycie_paliwa} litrów paliwa")
print (end=("\n"))
print (f "Koszt wyniesie {koszt} zł")