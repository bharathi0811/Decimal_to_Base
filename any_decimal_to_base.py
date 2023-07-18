def binary_converter(n,i):
    if n >=1:
        i==i
        binary_converter(n//i,i)
    print(n%i,end="")
a = int(input("A = "))
b= int(input("B= "))
l = binary_converter(a,b)