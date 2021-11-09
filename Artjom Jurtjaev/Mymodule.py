from keyboard import *
from random import *
def start():
    '''Teeme valik kellega mängime
    Tagastame m muutuja int formaadis

    :rtype: int
    '''
    p=3
    while p not in [1,2]:
        try:
            p=int(input('Выберите с кем хотите играть:\n1=игра с компом\n2=игра ботов'))
        except:
            TypeError
    return p
def bot_vs_bot(v1:list,v2:list):
    '''Robotite mäng
    Näitame ektaanile võitja nime
    :param list v1: järjend esimese roboti jaoks
    :param list v2: järjend teise roboti jaoks
    '''
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
def vs_pc():
    '''
    :rtype: int
    '''
    while True:
        a=0
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
        elif a==z:
            print('Ничья')
        elif a==2 and z==3:
            print('Ты проиграл')
        elif a==3 and z==2:
            print('Ты выйграл')
        elif a==3 and z==1:
            print('Ты проиграл')
        elif a==2 and z==1:
            print('Ты выйграл')
        elif a==1 and z==2:
            print('Ты проиграл')
