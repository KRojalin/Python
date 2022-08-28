def func():
    global x
    x = "Powerful"
    print(x)


func()
print("Python is", x)
x = "Awesome"
print("Python is", x)