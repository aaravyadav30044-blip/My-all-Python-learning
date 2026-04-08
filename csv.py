import csv


f=open("demo.txt","w")
data = csv.writer(f)
data.writerow(["ID","Name","Salary"])
for i in range(3):
    print("employees_record",(i+1))
    ID=int(input("enter the id: "))
    Name=input("enter the name: ")
    Salary=int(input("enter the salary: "))
    a=[ID,Name,Salary]
    data.writerow(a)
f.close()
