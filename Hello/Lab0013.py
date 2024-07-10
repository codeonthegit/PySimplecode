class Dog:
    name = None   #instance variables
    id = None

    def __init__(self, name, id):  #parameterize constructor
        self.name = name
        self.id = id

    def __init__(self):            #Default constructor with no argument
        print("Default No Argumemt")

        # Constructor '__' means private and only available in the class
        # Use to intialize the values of the instance variables (Attributes)

    def sleep(self):
        print("Who is Sleeping -> " + self.name)

//create object
dog1 = Dog("Chow","1")
dog2 = Dog("Mow", "2")

print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')

dog1.sleep()
dog2.sleep()
