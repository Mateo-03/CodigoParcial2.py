Lista = []
canti_componentes = int(input("Ingrese la cantidad de componentes de la lista: "))

for i in range(canti_componentes):
    Lista.append(int(input("Ingrese su elemento: ")))

print("Su Lista Es: ",Lista)
Lista.reverse()
print("Su Lista Invertida Es: ",Lista)