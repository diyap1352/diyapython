d={1:'Circle',2:'Triangle',3:'Rectangle'}
def circle(r):
    return 2*3.14*r
def triangle(n1,n2):
    return 1/2*n1*n2
def rectangle(h1,h2):
    return h1*h2
print("----AREA FINDER---")
for i, j in d.items():
    print(i,j)

choice=int(input("Please Enter Any Number From 1 to 3:"))

if choice==1:
    radius=int(input("Enter Radius:"))
    print("AREA OF CIRCLE IS:",circle(radius))
    print("----THANK YOU----")
elif choice==2:
    base=int(input("Enter Base:"))
    hieght=int(input("Enter Hieght:"))
    print("AREA OF TRIANGLE IS:",triangle(base,hieght))
    print("----THANK YOU----")
elif choice==3:
    hieght=int(input("Enter hieght:"))
    width=int(input("Enter width:"))
    print("AREA OF REACTANGLE IS:",rectangle(hieght,width))
    print("----THANK YOU----")
else:
    print("INPUT NOT VALID")


    
    

    
    

