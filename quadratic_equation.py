a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant :"))
print("The quadratic equation is : ",a,"x^2+",b,"x+",c)
d=4*a*c
underroot_term=b*b-d
print(underroot_term)

sqrt=underroot_term**0.5
root1=((-b)+(sqrt))*0.5/a
print(root1)

root2=((-b)-(sqrt))*0.5/a
print(root2)