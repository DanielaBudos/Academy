vyska = 1.63
vaha = 65
jmeno = "Daniela"
bmi = vaha/vyska**2


kategorie = None

if bmi < 18.5:
    kategorie = "Podvýživa"
elif 18.5 <= bmi <= 24.9:
    kategorie="Zdravá váha"
elif 25 <= bmi <= 29.9:
    kategorie="Mírná nadváha"
elif 30 <= bmi <= 39.9:
    kategorie="Obezita"
else:
    kategorie="Těžká obezita"

print("Jméno: <",jmeno,">,", "kategorie: <", kategorie, ">")