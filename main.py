import os
import time
import random
from machine import Pin

led = Pin(25, Pin.OUT)
led.value(1)


def read_tokens_count():
    with open("./tokens.count", "r") as tokens_count:
        tokens = tokens_count.read()
        tokens = int(tokens)
    if tokens < 10:
        with open("./tokens.count", "w") as tokens_count:
            tokens_count.write(str(10))
    return tokens


def increase_tokens(amount):
    actual_tokens_count = read_tokens_count()
    new_tokens_count = actual_tokens_count + amount  
    with open("./tokens.count", "w") as tokens_count:
        tokens_count.write(str(new_tokens_count))


while True:
    confirmation = input("Do you want to bet ? [y/n] > ")
    if confirmation == "y":
        stake = input(f"How many tokens do you want to stake ? (minimum 10 and you have actually {read_tokens_count()}) > ")
        try:
            stake = int(stake)
            if stake < 10:
                print("Stake is under the limit.")
                input("Press ENTER to continue ...")
            elif stake > read_tokens_count():
                print("Operation is impossible you don't have the required number of tokens.")
                input("Press ENTER to continue ...")
            else:
                win_or_lose = random.randint(1, 2)
                
                if win_or_lose == 1:
                    prize = stake * 2
                    increase_tokens(prize)
                    print(f"You win {prize}-tokens you are now to : {read_tokens_count()}-tokens.")
                    input("Press ENTER to continue ...")
                else:
                    stake = -stake
                    increase_tokens(stake)
                    stake = -stake
                    print(f"You lose {stake}-tokens you are now to : {read_tokens_count()}-tokens.")
                    input("Press ENTER to continue ...")
        except ValueError:
            print("please enter a number nothing else.")
            input("Press ENTER to continue ...")
            continue
    elif confirmation == "n":
        print("Ok program will be closed in three seconds :")
        a = [0, 1, 0, 1, 0, 1]
        b = 0
        for i in range(4):
            led.value(a[b])
            time.sleep(0.50)
            b += 1
            led.value(a[b])
            time.sleep(0.50)
            print(i)
        led.value(1)
        break
    else:
        print("please enter 'y' or 'n' nothing else.")
        input("Press ENTER to continue ...")
        continue
    
time.sleep(0.50)
led.value(0)
input("Press ENTER to continue ...")
print("Program exited.")
