def myintro(**data):
    print("\nData type of argument: ",type(data))

    for key , value in data.items():
        print("{} is {}".format(key,value))


myintro(Firstname="Mohan",Lastname="Sharma",Age=22,phno=99887766)
myintro(Firstname="sally",Lastname="john",email="test@test.com",country="AUS",Age=22,phno=2233445566)
