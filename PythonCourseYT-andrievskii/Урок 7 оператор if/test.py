a = int(input("Vvedite a"))
b = int(input("Vvedite b"))
func = str(input("Vvedite func"))

if func == "+":
    print(a+b)
elif func == "-":
    print(a-b)
elif func == "/":
    if b != 0:
        print(a/b)
    else:
        print("delenie na 0")
elif func == "*":
    print(a*b)
    