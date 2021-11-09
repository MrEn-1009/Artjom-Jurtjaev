from random import *
from Mymodule import *
from keyboard import *
v1=['Камень','Ножницы','Бумага']
v2=['Камень','Ножницы','Бумага']
print('Игра в камень, ножницы, бумага!')
p=start()
if p==1:
    vs_pc
elif p==2:
    bot_vs_bot(v1,v2)