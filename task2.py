#open("sp.txt","x")
file=open("sp.txt","w")
username=input("Enter the username:")
age=int(input("Enter your age:"))
email=input("Enter your email:")
password=int(input("Enter password:"))
option=int(input("enter your option:"))
if (option==1):
    print("username")
elif (option==2):
    print(age)
elif(option==3):
    print(email,password)
else:
    print("invalid")    


file.write("\n"+username+"\n"+str(age)+"\n"+str(email)+"\n"+str(password))
file.close()
