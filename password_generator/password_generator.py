import random
characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_+<>./?}{,:;`~"
while True:
    print("".join(random.sample(characters,16)))
    if(input()):
        pass