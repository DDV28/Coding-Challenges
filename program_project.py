import random

def randomFunction(num):

    print("number:", num)

    if num % 21 == 0:
       print("biz buz")
    elif num % 7 == 0:
       print("buz")
    elif num % 3 == 0:
       print("biz")

for i in range(100):
    num = int(random.random() * 100)
    randomFunction(num)
