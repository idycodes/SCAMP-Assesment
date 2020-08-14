# Idiongoabasi Udoh
# Fibonacci Series solution

a=int(input("Enter the number of terms: "))
first=0                                         
second=1                                       
if a<=0:
    print("The requested series is", first)
else:
    print(first,second,end=" ")
    for x in range(2,a):
        next=first+second                           
        print(next,end=" ")
        first=second
        second=next
 


