n1 = []
n12 = input("Enter any number you want to do:")

while n12!="":
    n1.append(int(n12))
    n12 = input("Enter any number you want to do:")

n1.sort(reverse=True)
print("Five greatest number: " ,n1[:5])

