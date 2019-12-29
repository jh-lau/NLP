from threading import Thread, Lock

_lock = Lock()


class Account:

    def __init__(self, money):
        self.money = money
        self._lock = Lock()

    def add(self, money):
        self.money = self.money + money

    def desc(self, money):
        self.money = self.money - money

"""
money = money + n

Thread A                  Thread B
get lock
tmp = money + n           tmp = money + n  
money = tmp               money = tmp
release lock

"""


account = Account(1000)

def change(money):
        # lock = Lock()
        # lock.acquire()
    account.add(money)
    account.desc(money)
        # lock.release()


def run(money):
    global _lock
    for _ in range(1000000):
        with _lock:
            change(money)

"""
def change(money):     
    temp = money     
    with threading.Lock():         
    acct.add(temp)         
    acct.desc(temp) 
"""


if __name__ == '__main__':
    t1 = Thread(target=run, args=(100, ))
    t2 = Thread(target=run, args=(200, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"total money: {account.money}")
