n=int(input("Enter a number of customer:"))
list=[]
for i in range(n):
    A = int(input("Enter customer Account ID %d: " % (i + 1)))
    list.append(A)
print("List",list)
found=False;
B=int(input("Enter a customer account ID:"))
for i in range(n):
    if list[i]==B:
        print("Linear Search:")
        print("Customer Account ID found at position:",i + 1)
        found = True;
        break;

if not found:
    print("Linear Search:")
    print("Customer Account ID not exists")

list.sort() 
low = 0 
high = n - 1       
found = False;

for i in range(n-1):
    if low <= high:
        mid = (low + high) //2
        if list[mid] == B:
            print("Binary Search:")
            print("Customer Account ID found at position:",mid + 1)
            found = True;
            break
        elif list[mid] < B:
            low = mid + 1
        else:
            high = mid - 1

if not found:
    print("Binary Search:")
    print("Customer Account ID not found.")

print("Sorted Account IDs:",list)