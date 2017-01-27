import datetime
class drone:
    num_of_drones = 0
    speed_raise = 0.5
    price_change = 0.2
    def __init__(self, quality, speed, price):
        self.quality = quality
        self.speed = speed
        self.price = price

        drone.num_of_drones += 1

    def full_details(self): #<-regular instance method
        return 'this drone is of {} quality at {} speed'.format(self.quality, self.speed)

    def speed_change(self):
        self.speed = int(self.speed * drone.speed_raise)

    @classmethod
    def new_price(cls, price, drones): #<- class method
        cls.price_change = price
        cls.num_of_drones = drones

    @classmethod
    def adv_drone(cls, new_drone):
        quality, speed, price = new_drone.split('-')
        return cls(quality, speed, price)

    @staticmethod
    def is_workday(day): #<- static method
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True    


syma = drone('low', 90, 80)
dji = drone('high', 60, 1000)
#drone.set_speed_raise(1.06)
# syma.speed_raise = .9

autel = 'average-75-600'
inspire = 'high-150-3000'
phantom = 'high-120-2000'



drone_adv = drone.adv_drone(autel)

my_date = datetime.date(2017, 1, 27)
print drone.is_workday(my_date)
 






    
