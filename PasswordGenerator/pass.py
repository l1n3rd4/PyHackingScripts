import random
import re

chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789%$@()&")
things = list("0123456789%$@()&")
vogals = str("aeiou")

def pass_random():
    try:
        word = ''

        with open("BadWare.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            word = random.choice(words)

        pass_len = 10 # int(input("Password length: "))
        password = ""

        print(word)
        word = word.replace(" ", "")
        word = list(word)

        for j in word:
            j = str(j).lower()
            result = re.search(j, vogals)

            if result:
                password += random.choice(things)
            else:
                password += j

        if len(password) <= 12:
            x = len(password)
            for x in range(pass_len):
                password_char = random.choice(chars)
                password += password_char

        print(f"pass_random : {password}")
        file.close()
    except:
        print("Deu ruim")



def pass_phrase():
    try:
        word = ''

        with open("BadWare.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))

            number = 2
            password = ''

            for i in range(number):
                word = random.choice(words)
                password += random.choice(things)
                password += word
                password += random.choice(things)
            
        print(f"pass_phrase : {password}")
        file.close()
    except:
        print("Deu ruim")
#ay9k65vb
pass_phrase()
pass_random()