# class Human:
#     def __init__(self, name='Human'):
#         self.name = name
#
#
# class Auto:
#     def __init__(self, brand):
#          self.brand = brand
#          self.passengers = []
#
#     def add_passengers(self, *args):
#         print(type(args))
#         for arg in args:
#             self.passengers.append(arg )
#
#     def print_passenger_names(self):
#         if self.passengers != []:
#             print(f"Names of {self.brand} passengers: ")
#             for passengers in self.passengers:
#                 print(passengers.name)
#
#         else:
#             print(f"There are no passenger in {self.brand}")
#
# vlad = Human('Vlad')
# danilo = Human('Danilo')
# oleg = Human('Oleg')
#
# car = Auto('s63')
#
# car.add_passengers(vlad, danilo, oleg )
# car.print_passenger_names()


import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name= name
        self.gladness = 50
        self.money = 100
        self.job = job
        self.home = home
        self.car = car
        self.satiety = 50

    def get_home(self):
        pass

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_car(self):
        self.car = Auto(brands_of_cars)

    def eat(self):
        if self.satiety >= 100:
            self.satietly = 100
            return
        self.satiety += 5
        self.home.food = 100

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satietly -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Delicious!")
            self.money -= 15
            self.satietly += 2

    def chill(self):
        self.gladness -= 5


    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.hp += 100
        self.money -= 100

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name} life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "indexed"
        print(f"{human_indexes:-^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:-^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:-^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.money < -500:
            print("Bankrupt")
            return False

    def live(self):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the House")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I dont have a job, Im going to get a job {self.job.job} with salary {self.job.salary}")
        self

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.hp = brand_list[self.brand]["hp"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.hp >0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.hp -= 1
            return True
        else:
            print("The car can not move")
            return False

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list(self.job)["salary"]
        self.gladness = job_list(self.job)["gladness_less"]





brands_of_cars = {
       " BMW": {"fuel": 100, "hp": 360, "consumption": 6},
        "Mersedes - Benz": {"fuel": 50, "hp": 600, "consumption": 10},
        "Volvo": {"fuel": 70, "hp": 220, "consumption": 8},
        "Audi": {"fuel": 80, "hp": 680, "consumption": 14}}

job_list = {"Java Developer": {"salary": 50, "gladness_less": 10},
            "Python Developer": {"salary": 70, "gladness_less": 3},
            "C++ Developer": {"salary": 45, "gladness_less": 25},
            "C# Developer": {"salary": 60, "gladness_less": 1}}
