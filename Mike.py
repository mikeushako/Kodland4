import random

password = "@j=+-1234567890"

q1 = int(input("Enter number in password: "))

password_ready = ""


for i in range(q1):
    password_ready += random.choice(password)
    
print(password_ready)
