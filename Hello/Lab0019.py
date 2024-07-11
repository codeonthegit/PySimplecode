class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed")


# This is the end of the class

manjiri = VWOLoginPage("manjiri@gmail.com", "123")
manjiri.login_confirm()

pooja = VWOLoginPage("pooja@gmail.com", "Pass123")
pooja.login_confirm()
