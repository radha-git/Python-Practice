name='This is a global name!'

def greet():
    name="sammy"

    def hello():
        print('hello '+name)

    hello()
greet()
print(name)


y=10

def fun():
    global y
    y=1000

print("before function call,y is: ",y)
fun()
print("After function call, y is :",y)