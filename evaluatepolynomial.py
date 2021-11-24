#Evaluate a polynomial
poly=input("Enter a polynomial: ")
nv=int(input("How many variables does the polynomial have: "))
print("Lets go through each of the variable")
vart={}
for x in range(nv):
    vr=input("What is the variable:\n")
    vl=float(input("What's the value of the variable:\n"))
    vart[vr]=vl
print(eval(poly,vart))
       