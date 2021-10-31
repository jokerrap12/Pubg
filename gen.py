import random
def Getpassword(data):
 Max = 11
 password = "010"
 while len(password) !=Max:
  value = random.choice(data)
  password += value
 return password

data = '0123456789'
for i in range(99999999999*99999):
    print(Getpassword(data))
    joker = open("Numbers.txt","a")
    joker.write(Getpassword(data)+"\n")