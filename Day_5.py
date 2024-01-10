import random

schars=['.',',',"'",'"','!','?',':',';','*','+','_','-',]
numbers=['1','2','3','4','5','6','7','8','9','0']
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','b','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

print ("Welcome to password generator")
l=int(input("How many letters do you want in your password? "))
c=int(input("How many special characters do you want in your password? "))
n=int(input("How many numbers do you want in your password? "))

password=[]
for i in range(0,c):
  password.append(random.choice(schars))
for i in range(0,n):
  password.append(random.choice(numbers))
for i in range(0,l):
  password.append(random.choice(letters))
  
random.shuffle(password)

password1=""
for i in range(0,(c+n+l)):
  password1+=password[i]

print(password1)pas[i]=chr(random.randint(123,126))
print(f"\nYour new password is {pas}")