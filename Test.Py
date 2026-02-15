seznam = ["Petr", "Lorenc", "Lukas", "Jan"]

print([seznam[0]] + ["David"] + seznam[1:])
print(seznam + ["David"] + seznam[1:])
print(seznam)


muj_typ = type("abs")
print(muj_typ)

Jmeno = "Danielka"
Vek = 33
print("Jmenuji se", Jmeno,"a je mi stale ",Vek, "let"  )

Jmeno = "Danielka"
Vek = 33
print("Jmenuji se",Jmeno,"a je mi stale",Vek, "let"  )

# zaokrouhli číslo 0.33333 na 2 desetinná místa
print(round(0.33333, 2))

# z celého čísla (int) udělej desetinné
print(float(2))


# do proměnné ulož dva stringy a vypiš list
promenna = "a", "b"

print(list(promenna))

# v proměnné máš uložený list
# tento list pomocí funkce předělej na tuple

prom_list = list[2,3,4]
print(tuple(prom_list))

