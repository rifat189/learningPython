# password generator
import random
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!','@','#','$','%','^','&', '*', '(', ')']

user_total = int(input("How many letters: "))
user_num = int(input("How many numbers: "))
user_sym = int(input("How many symbols: "))

user_alpha = user_total-user_num-user_sym
password = []
for i in range(0, user_alpha):
    password.append(alpha[random.randint(0, 25)])
for i in range(0, user_num):
    password.append(num[random.randint(0, 9)])
for i in range(0, user_sym):
    password.append(sym[random.randint(0, 9)])

random.shuffle(password)

password_string = ''

for i in range(0, len(password)):
    password_string+=password[i]

print(password_string)
