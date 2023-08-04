""" if it looks like a duck, swins like duck, quacks like a duck, then its a duck"""


class Maharashtrian:
    def speak_in_marathi(self):
        print("Kasa kay mandli")


class Gujrati:
    def speak_in_marathi(self):
        print("uttam mandli")


class Punjabi:
    def speak_in_marathi(self):
        print("chala yeto mi")


m = Maharashtrian()
# m.speak_in_marathi()

g = Gujrati()
# g.speak_in_marathi()

p = Punjabi()
# p.speak_in_marathi()


def start_conversation(person):
    person.speak_in_marathi()


start_conversation(m)
start_conversation(g)
start_conversation(p)
