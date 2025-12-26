#open("pk.txt","x")
file=open("pk.txt","w")
for i in range(1,3):
    
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    year=int(input("Enter your year:"))
    dept=input("Enter dept:")
    file.write(name+ " "+"\t"+" " "\t"+str(age)+"\n"+dept+"\n"+str(year))
   
file.close()