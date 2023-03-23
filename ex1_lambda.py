# Hãy viết một chương trính lambda +15 vào một số được nhập từ bàn phím
x = int(input("Please enter your value: "))
total = lambda x: (x + 15)

print(f"The total of x {x} and 15 is ", total(x))


# Hãy nhập vào 2 số x và y (x là đối số của y)=> x*y
x = int(input("Please enter your value x: "))
y = int(input("Please enter your value y: "))

multi = lambda x,y: x * y

print(f"The multi of {x} and {y} is ",multi(x,y))