
class Foo:
    def __str__(self):
        return "bar"

x = Foo()
print(x)

class Boo:
    def __init__(self):
        self.l = [{"Susan": ("Boyle", 50, "alive")}, {"Albert": ("Speer", 106, "dead")}]

x = Boo()
print(x.l)



