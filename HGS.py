from calendar import c
from datetime import datetime


class Vehicle():
    def __init__(self, hgsNo, name, surname, date, balance):
      self.hgsNo = hgsNo
      self.name = name
      self.surname = surname
      self.date= date
      self.balance = balance
    def information(self):
        print("hgsNO:", self.hgsNo)
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Date:", self.date)
        print("Balance:", self.balance, "\n") 
class Auto(Vehicle):
    def __init__(self, hgsNo, name, surname, date, balance):
        super().__init__(hgsNo, name, surname, date, balance)
    def information(self):
        super().information()
class Minibus(Vehicle):
    def __init__(self, hgsNo, name, surname, date, balance):
        super().__init__(hgsNo, name, surname, date, balance)
    def information(self):
        super().information()
class Bus(Vehicle):
    def __init__(self, hgsNo, name, surname, date, balance):
        super().__init__(hgsNo, name, surname, date, balance)
    def information(self):
        super().information()
        
daily_vehicle = []
daily_revenue = 0

class counter():
    def __init__(self):
        self.AutoFee = 100
        self.minibusFee = 200
        self.busFee = 300
        global daily_revenue
    def Payment(self, vehicle):
        if isinstance(vehicle, Auto):
            global daily_revenue
            if vehicle.balance >= self.AutoFee:
                vehicle.balance -= self.AutoFee
                daily_revenue += self.AutoFee
            else:
                print("insufficient balance")
        elif isinstance(vehicle, Minibus):
            if vehicle.balance >= self.minibusFee:
                vehicle.balance -= self.minibusFee
                daily_revenue += self.minibusFee
            else:
                 print("insufficient balance")
        elif isinstance(vehicle, Bus):
            if vehicle.balance >= self.busFee:
                vehicle.balance -= self.busFee
                daily_revenue += self.minibusFee
            else:
                 print("insufficient balance")
        else:
            return 0
class Report():
    def __init__(self):
        print("Today Revenue:", daily_revenue)
        

gise = counter()

v0 = Auto(1,"Kuzey","Durden",datetime.now(), 300)
v1 = Minibus(2,"Tyler","Durden",datetime.now(),765)
v2 = Bus(3,"Marla","Singer",datetime.now(),943)


gise.Payment(v0)
daily_vehicle.append(v0.information())
gise.Payment(v1)
daily_vehicle.append(v1.information())
gise.Payment(v2)
daily_vehicle.append(v2.information())
Report()


