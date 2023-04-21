import random

print ("welcome to love calculator")

x = input("enter your name:")

y=input("eneter your second name:")

print(x,"LOVE",y)

percentage=random.randrange(1,101)
print(percentage, "%")

if percentage < 40:
    print("worst")
    
elif percentage < 70:
    print("better luck next time and try your best")
    
elif percentage == 100:
    print("MARRY THE GIRL DON'T MISS ")
    
    
else:
    print("super")

