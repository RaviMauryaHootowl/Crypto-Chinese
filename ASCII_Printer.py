
print("Start limit:")
n=int(input())          #to input start of the ASCII list

print("End Limit:")
e=input()               #to input end of the ASCII list

print("\n")
print("NUM  ASCII")

while n!=(int(e)+1):        #ASCII printer module
   print(n,' ',chr(n))
   n=n+1
pass