a = int(input("Enter your age: "))

# If statement no: 1
if(a%2 == 0):
    print("a is even")
# End of If statement no: 1

# If statement no: 2

if(a>=18):
    print("Access granted")
    print("You are eligible to enter")

elif(a<0):
    print("You are entering a negative number which is not a valid age")

else: 
    print("Access denied") 
    print("You are not eligible to enter") 

# End of If statement no: 2

print("--- End of Transmission ---") 