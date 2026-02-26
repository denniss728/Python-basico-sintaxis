#Yunior Dennis
#Tuplas Sets y Diccionarios

#Tuplas 
# simbolo ()
# por default lo ordena 
# inmutables = no se pudede hacer cambios 
# te acepta duplicados

tupla = (1,2,1,2, 40, 10, 5, 11)
print(tupla)
#indices 
print(tupla[4])

# sets 
# simbolo{}
# no ordena 
# mutable = si puede hacer cambios 
# no te aceptan duplicados 
sets = {1,2,3,1,2,3}
print(sets)

# agregar un nuevo dato
sets.add(4)
print(sets)

# remove() eliminar un dato
sets.remove(3)
print(sets)

# diccionarios 
# simbolo {key:value}
# si ordena 

estudiante = {
    "nombre":"Diego",
    "natalidad":"Putina",
    "edad" : 30,
    "carrera": "ingienería"
}
print(estudiante)

print(estudiante["nombre"])
print(estudiante["natalidad"])
print(estudiante["edad"])
print(estudiante["carrera"])

print["edad"] = 50
print( estudiante)

# ciclo fro en los Diccionarios
for clave, valor in estudiante.items():
    print("clave: ", clave , "valor: ", valor)
    
