from random import *
from keyboard import *
print('Игра в камень, ножницы, бумага!')
b=0
c=0
p=''
while p not in [1,2]:
    try:
        p=int(input('Выберите с кем хотите играть:\n1=игра с компом\n2=игра ботов'))
    except:
        TypeError
if p==1:
    while True:
        a=''
        while a not in [1,2,3,4]:
            try:
                a=int(input('Выберите камень=1, бумага=2, ножницы=3, закончить игру=4  ='))
            except:
                TypeError
        if a==4: break
        z=randint(1,3)
        if z==1:
            print('Компьютер выбрал камень')
        elif z==2:
            print('Компьютер выбрал бумага')
        else:
            print('Компьютер выбрал ножницы')
        if a==1 and z==3:
            print('Ты выйграл')
            b+=1
        elif a==z:
            print('Ничья')
        elif a==2 and z==3:
            print('Ты проиграл')
            c+=1
        elif a==3 and z==2:
            print('Ты выйграл')
            b+=1
        elif a==3 and z==1:
            print('Ты проиграл')
            c+=1
        elif a==2 and z==1:
            print('Ты выйграл')
            b+=1
        elif a==1 and z==2:
            print('Ты проиграл')
            c+=1
elif p==2:
    v1=['Камень','Ножницы','Бумага']
    v2=['Камень','Ножницы','Бумага']
    while True:
        print('Играем? esc= выходим, enter= играем')
        if read_key()=='esc':
            break
        elif read_key()=='enter':
            p1=choice(v1)
            print('Первый Бот: ',p1)
            p2=choice(v2)
            print('Второй Бот: ',p2)
            if p1==p2:
                print('Ничья')
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print('Выйграл 1')
            else:
                print('Выйграл 2')
print(f'Счёт за игру:\nОчки первого игрока:{b}\nОчки второго игрока:{c}')