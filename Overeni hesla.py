jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek": "1234"}


if jmeno in uzivatel and uzivatel[jmeno] == heslo:
    zprava = "Ahoj Marek, vítej v aplikaci! Pokračuj..."
else:
    zprava = "Uživatelské jméno nebo heslo nejsou v pořádku!"

print("Výstup:", zprava)