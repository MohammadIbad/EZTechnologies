size=int(input("Enter the Size of the List:"))
print("Enter the Elements to Sort")
List=list(map(int,input().split()))
print("The Given List is:")
print(List)
for i in range(0,size,1):
    for j in range(0,size-i-1,1):
        if(List[j]>List[j+1]):
            temp=List[j]
            List[j]=List[j+1]
            List[j+1]=temp
print("The Sorted List using Bubble Sort is:")
print(List)
