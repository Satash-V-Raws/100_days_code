print ("Welcome to tip calculator")
t1 =float (input ("What was the todal bill amount? $"))
p=int(input("How many people to split the bill?"))
ti=int(input("What percentage tip would you like to give? 10,12 or 15?"))
tip=((1+(ti/100))*t1)/p
print("Each person should pay : $"+str(tip))