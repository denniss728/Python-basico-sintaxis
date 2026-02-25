#Yunior Dennis
#Listas
lista = ["Yunior","Dennis",25,True]
print(lista[0])
# Lista de frutas 
frutas = ["mango", "durazno", "plátano", "uva", "manzana"]
print(frutas[3])

frutas[1] = "Granada"
print(frutas)

for i in frutas:
    print(i)

#Matriz
matriz = [
    [1,2,3],
    [4,6,1],
    [0,1,0]
]
print(matriz[2][2])

#Lista de números 
numeros = [1,2,3,4,5,6,7,8,9,0]
print(numeros[8])
print(numeros[:3])
print(numeros[1:5])
print(numeros[::2])
print(numeros[::-1])


#Ciclo for en las listas
for i in numeros:
    print(i * 10)

#Métodos en las listas 
print("-------------------------------------------------------métodos")
frutas = ["mango", "durazno", "plátano", "uva", "manzana"]
#agregar un nuevo dato
frutas.append("ciruela")
print(frutas)

#insert
frutas.insert(2, "pera")
print(frutas)

#remove = borrar un dato
frutas.remove("uva")
print(frutas)

#pop = para obtener o eliminar el último dato
frutas.pop()
print(frutas)

#sort() = ordenar la lista 
frutas.sort()
print(frutas)

# reverse() = revertir 
frutas.reverse()
print(frutas)

#len() = contar 
cantidad = len(frutas)
print(cantidad)

#index() = encontrar el índice 
índice = frutas.index("plátano")
print(índice)







