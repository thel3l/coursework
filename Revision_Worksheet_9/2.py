n=int(raw_input("Enter number of terms: "))
x_val = int(raw_input("Enter the value of x: "))
d=0  #to sum all terms, initial value is 0

while n>0:
     j=n   #we start by taking factorial of the last term
     s=float(1)   #to multiply to find factorial
     while j>0:
               s=s*j   #number gets multiplied to s and stored in s
               j=j-1   #number is decreased until it reaches 0
     n=n-1   #we will keep finding factorial until the very first term, i.e. 1 is reached
     x=1/s   #to find reciprocal of the factorial we just found in     floating point
     xIntermediate = (x_val ** n) * x
     d=d+xIntermediate #adding to final sum

print "The sum is ",d #printing
