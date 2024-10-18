from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            add = randint(50, 500)
            self.balance += add
            sleep(0.001)
            print(f'Пополнение: {add}. Баланс: {self.balance}')

    def take(self):
        for i in range(100):
            takes = randint(50, 500)
            print(f'Запрос на {takes}')
            if takes <= self.balance:
                self.balance -= takes
                print(f'Снятие: {takes}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
