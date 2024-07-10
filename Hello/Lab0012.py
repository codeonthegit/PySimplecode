class Dog:
    name = None
    id = None

     #Constructor '__' means private and only available in the class
    #Use to intialize the values of the instance variables (Attributes)

    def sleep(self):
        print("Sleeping")


dog1 = Dog()
print(dog1.name)
dog1.name = "Chow"
print(dog1.name)
dog1.sleep()