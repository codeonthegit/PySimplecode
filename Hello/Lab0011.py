class Person:
    name = None
    id = None
    age = None
    phone_number = None

    # Behavior
    def talk(self):  # No Argu , No Return
        print("I can talk")

    def sleep(self, name):  # Arg with No Return
        print("I am a method!!")
        print("Sleep", name)

    def sleep2(self, name):  # Arg with Return
        print("I am a method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):  # No Arg with Return
        return "I am walking"

    # Create Object of the person class
    # objectRef = Object -> ClassName()


surya = Person()
surya.name = "Surya Prakash"
surya.talk()

ritika = Person()
ritika.name = "Ritika Gupta"
ritika.walk()
