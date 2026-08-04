n=int(input("Enter the number of library members:"))
list=[]
for b in range(n):
        each=int(input(f"Enter books borrowed by member {b+1}:"))
        list.append(each)

print("Number of books borrowed by each member :",list)
sum=0
for i in list:
    sum=sum+i;


avg=sum/len(list)
print("1.Average of number of books borrowed by each member is:",avg)

lowest=list[0]

highest=list[0]
for b in list:
      if highest>b:
           highest=highest
      else:
           highest=b
print("Highest number of books borrowed by member is",highest)          

lowest=list[0]      
for b in list:
      if lowest<b:
           lowest=lowest
      else:
            lowest=b

print("Lowest number of books borrowed by member is",lowest)

count=0;
for b in list:
      if b==0:
        count=count+1

print("Number of members who have not borrowed any books",count)

max_count = 0
mode = list[0]

for i in range(n):
    count = 0
    for j in range(n):
        if list[i] == list[j]:
            count = count + 1

    if count > max_count:
        max_count = count
        mode = list[i]
print("Most frequently borrowed count (Mode):", mode)

        