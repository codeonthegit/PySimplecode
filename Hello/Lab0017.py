class Person:   #class variables / instance variables
    name = "Manjiri"
    age = None

    def walk(self):       #Function
        a = 10  #Local variable
        print("I am method")
        print("Hi", self.age)

#Object reference = Object
manjiri = Person()  #Object creation
manjiri.walk()
