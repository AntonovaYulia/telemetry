from threading import Thread
from time import sleep

def alphe():
for k in range(5):
sleep (1.5)
print(f'[{k+1}], функция Альфа' )

def brave():
for k in range(5):
sleep(1)
print(f'[{k+1}], функция Браве')

potok = Thread(target=brave)
potok.start()

alphe()
