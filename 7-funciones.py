# Yunior Dennis 
#funciones 

print("hola, juan")
print("Bienvenido al sistema")
print("---------------------")

print("hola, Diego")
print("Bienvenido al sistema")
print("---------------------")


print("hola, pepito")
print("Bienvenido al sistema")
print("---------------------")
print("------------------------------------------------------------------------------------")

nombres = ["juan", "diego", "pepito"]
for i in nombres:
    print("hola, ",i)
    print("bienvenido al sistema")
    print("----------------------------")
    def saludar(nombre):
        print("Hola,",nombre)
        print("Bienvenido al sistema")
        print("-------------------")
    saludar("juan")
    saludar("diego")
    saludar("pepito")

#Funciones con retorno return()
def suma(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    return(resultado)

print(suma(2,2))

pass

#Funciones sin entorno
def suma2(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    print(resultado)

suma2(2,2)





    

    


