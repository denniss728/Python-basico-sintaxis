# 1. AND (Y)
# 2. OR  (O)
# 3. NOT (NEGACIÓN)
v = True
f = False

print(v and f ) #false 

#-----------------------------------------
nota = 11 
print(nota >=10 and nota <= 10)

#-----------------------------------------
#YUNIOR DENNIS BERNABE ROQUE
edad = 18
print(18 == edad or edad >10 )
#----------------------
nota1 = 5 
nota2 = 15
nota3 = 20
promedio =((nota1+nota2+nota3))/3
print(promedio)

if(promedio >= 17):
    print('EXCELENTE')
elif(promedio >= 14):
    print('BUENO')
elif(promedio >= 11):
    print('REGULAR')
elif(promedio >= 10):
    print('JALADO')
else:
    print('bien hecho')
