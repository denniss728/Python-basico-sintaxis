#YUNIOR DENNIS BERNABE ROQUE

while False:
    print('Dennis')



#Valida contraseña
contrasenia_correcta = '123456'
intentos = 0

while True:
    contrasenia = input('ingrese porfavor su contraseña:')
    intentos += 1 

    if (contrasenia == contrasenia_correcta):
        print('contraseña correcta👌')

    else:
        print('contraseña incorrecta😒')
        if(intentos >= 3):
            print('trajeta bloqueada😡')
            break