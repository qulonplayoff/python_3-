class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner
        self.hunger = 0
        self.thirst = 0
        self.energy = 100

    def bark(self):
        print(f"{self.name} barks: Woof woof!")

    def eat(self):
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} eats. Hunger level: {self.hunger}")

    def drink(self):
        self.thirst -= 10
        if self.thirst < 0:
            self.thirst = 0
        print(f"{self.name} drinks. Thirst level: {self.thirst}")

    def sleep(self):
        self.energy += 50
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} sleeps. Energy level: {self.energy}")

    def play(self):
        self.energy -= 30
        self.hunger += 10
        self.thirst += 5
        if self.energy < 0:
            self.energy = 0
        if self.hunger > 100:
            self.hunger = 100
        if self.thirst > 100:
            self.thirst = 100
        print(
            f"{self.name} plays. Energy level: {self.energy}, Hunger level: {self.hunger}, Thirst level: {self.thirst}")


class Home:
    def __init__(self, address, family_members):
        self.address = address
        self.family_members = family_members

    def show_address(self):
        print(f"The dog lives at {self.address}")

    def show_family_members(self):
        print(f"The dog's family members are: {', '.join(self.family_members)}")
