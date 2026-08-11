n = int(input("Enter number of salaries: "))

salaries = []

for i in range(n):
    salary = int(input("Enter salary %d: " % (i + 1)))
    salaries.append(salary)
print("Employee salaries:",salaries)

#Bubble sort
for i in range (0,n-1):
    for j in range (0,n-i-1):
        if (salaries[j]>salaries[j+1]):
            temp=salaries[j]
            salaries[j]=salaries[j+1]
            salaries[j+1]=temp
print("Employee salaries after bubble sort:",salaries);

#Selection sort
for i in range (0,n-1):
    SI=i
    for j in range (i+1,n):
        if (salaries[j]<salaries[SI]):
             SI=j
    temp=salaries[i]                                                                        
    salaries[i]=salaries[SI]
    salaries[SI]=temp
print("Employee salaries after selection sort:",salaries)




