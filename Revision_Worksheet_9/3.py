n = int(raw_input("Enter the number of terms: "))
a = int(raw_input("Enter the value of a: "))
r = int(raw_input("Enter the value of r: "))
s = 0
for i in range(n):
    s = s+ (a * ((r**n) - 1))

print s
