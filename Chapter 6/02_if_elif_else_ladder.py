a = int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("Access granted")
    print("You are eligible to enter")

elif(a<0):
    print("You are entering a negative number which is not a valid age")

elif(a==0):
    print("You are entering zero which is not a valid age")    

else:
    print("Access denied")
    print("You are not eligible to enter")


print("End of Transmission")

