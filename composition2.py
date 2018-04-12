class Scene:

    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()


class Actor:

    name = 'customer'

    def says(self): pass

    def line(self):
        print(str(self.says()))


class Customer(Actor):
    name = 'customer'

    def says(self):
        return self.name + " hello"


class Clerk(Actor):
    name = 'clerk'

    def says(self):
        return self.name + " is speaking"


class Parrot(Actor):
    name = 'parrot'

    def says(self):
        return self.name + " car car"


if __name__ == "__main__":
    x = Scene()
    print(x.customer.line())
    print(x.parrot.line())
    print(x.clerk.line())
