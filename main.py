# Zaskocz swoich rówieśników!
import time
import random
fakty = []
for i in range(4):
    fakt = input("Dodaj fakt o sobie")
    fakty.append(fakt)
time.sleep(2)
print (random.choice(fakty))
