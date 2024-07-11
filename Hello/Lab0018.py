class Car:
    name = None
    make = None
    modal = None

    def __init__(self,o_name, o_make, o_modal):
        self.name = o_name
        self.make = o_make
        self.modal = o_modal

    def start_engine(self):
        print("Starting a car with name " + self.name)
        print("Starting a car with make " + self.make)
        print("Starting a car with modal " + self.modal)
#This is end of the class

lambo = Car("lambo", "V2", "2024")
lambo.start_engine()

xuv = Car("XUV", "V6", "2023")
xuv.start_engine()