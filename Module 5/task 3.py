n = int(input("Enter a number to check: "))
for i in range(2,n):
    if(n%i==0):
        break
if i == n -1:
    print("N IS PRIME")
else:
    print("N IS NOT PRIME")
