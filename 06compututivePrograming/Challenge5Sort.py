
a = [66, 57, 54, 53, 64, 52, 59]

for i in range(len(a)):
    
    for j in range(len(a)):
        if(a[i]<a[j]):
            
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
                       


print("Best timing is ",a[0] , "second")


   
