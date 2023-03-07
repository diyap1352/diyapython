a=int(input("Enter marks of Maths:"))
b=int(input("Enter marks of English:"))
c=int(input("Enter marks of Science:"))
d=int(input("Enter marks of Hindi:"))
e=int(input("Enter marks of SS:"))

add=a+b+c+d+e

print("Total Marks : " ,add)

per=add/300*100

print("Percentage : " ,per)

if per>=45: or per<=60
    print("Grade: C ")
elif per==75: or per<=85
    print("Grade: B ")
else:
    print("Grade: A ")

        
        
