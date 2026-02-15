# vytvoříme nový prázdný slovník
muj_slovnik = {}

# vytvoříme další slovník – kontakty
kontakty = {"mobil": "+420582582582", "email": "matous@matous.cz" }

# do prvního, prázdného slovníku vložíme slovník kontakty
muj_slovnik["kontakt"] = kontakty

# zobrazíme všechny kontakty
print(muj_slovnik["kontakt"])

# zobrazíme mobil
print(muj_slovnik["kontakt"]["mobil"])


# zobrazím email
print(muj_slovnik["kontakt"]["email"])