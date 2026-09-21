print("=====function with Position Parameter=======")

def position1(name,age):
    print(name,age)

position1("Akshay",21)
position1(21,"Akshay")

print("=====function with Keyword Parameter=======")

def position2(name,age):
    print(name,age)

position2(name ="Akshay",age=21)
position2(age=31,name="Sagar")

print("=====function with Default Parameter=======")

def position3(name,age=21):
    print(name)
    print(age)

position3("Akshay")
position3("Sagar",25)


