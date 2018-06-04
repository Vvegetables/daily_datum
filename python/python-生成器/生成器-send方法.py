#demo1
def gener():
    name = 'not input'
    while True:
        name = yield name
        if name == None:
            name = "not input"
        else:
            name = "I'm " + name


it = gener()
print it.next()

# print it.send(None)
print it.send("zhainankl")
print it.next()
print it.next()
# print it.next()




#demo2

def gener():
    name = 'not input'
    while True:
        yield name
        if name == None:
            name = "not input"
        else:
            name = "I'm " + name


it = gener()
print it.next()

# print it.send(None)
print it.send("zhainankl")
print it.next()
print it.next()