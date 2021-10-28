from random import *
print('Игра в камень, ножницы, бумага!')
a=''
b=0
while a.isdigit()!=True:
    a=input('Выберите камень=1, бумага=2, ножницы=3')
try:
    TypeError
z=randint(1,3)
if z==1:
    print('Компьютер выбрал камень')
elif z==2:
    print('Компьютер выбрал бумага')
else:
    print('Компьютер выбрал ножницы')
if a=z:
    print('Ничья')
elif a==1 and z==3:
    print('Ты выйграл')
    b+=1
elif a<z:
    print('Ты проиграл')
    b-=1
elif a>z:
    print('Ты выйграл')

