lista=["Kasia ","Basia ","Marek ","Darek "]
lista.append("Józek ")
lista.extend(("Ania ", "Basia "))
lista_sortowana = sorted(lista)
print(lista_sortowana[4])
print(lista_sortowana[:2])
print(lista_sortowana[-2:])
lista_sortowana.remove("Basia ")
print(len(lista_sortowana))
krotka = tuple(lista_sortowana)
print(krotka)