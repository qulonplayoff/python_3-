# class Student:
#   def __init__(self, height, name):
#         self.name = name
#         self.height = height
#
#   def set_height(self, haight):
#         self.haight = haight
#
#   def get_height(self):
#         print(self.haight)
#
#   def __str__(self):
#         return f"I`m students. My name is {self.name}"
#
# vlad = Student(170, name ="Vlad")
#
# vlad.get_height()
# vlad.set_height(180)
# vlad.get_height()
#
# print(vlad)

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.gladness -= 3
        self.progress += 0.20

    def to_chill(self):
        print("Time to relax")
        self.gladness += 5
        self.progress -= 0.1

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depresion...")
            self.alive = False
        elif self.progress > 5:
            print("Passed exam!!!")
            self.alive = False

    def day_info(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {self.progress}")

    def live(self, day):
        day = "Day" + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        rundom_number = random.randit == (1, 3)
        if rundom_number == 1:
            self.to_study()
        elif rundom_number == 2:
            self.to_chill()
        else:
            self.to_sleep()
        self.day_info()
        self.is_alive()

vlad = Student("Vlad")
for day in range(1, 366):
    if vlad.alive == False:
        break
    vlad.live(day)






