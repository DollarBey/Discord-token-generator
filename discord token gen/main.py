import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz0123456789"

for i in range(100):
    first = ''.join((random.choice(chars) for i in range (24)))
    second = ''.join((random.choice(chars) for i in range (6)))
    third = ''.join((random.choice(chars) for i in range (27)))
    
    result = first + "." + second + "." + third
    
    output = open("output.txt", "a")
    output.write(result + "\n")