import random

class Car:
    def __init__(self, n='fire car', c='red', s=200):
        self.name = n
        self.color = c
        self.max_speed = s
        self.distance = 0
        
    def printCarInfo(self):
        print(f'name: {self.name}, color:{self.color}, max_speed: {self.max_speed}')
        
    def controlSpeed(self):
        return random.randint(0, self.max_speed)
    
    def getDistanceForHour(self):
        return self.controlSpeed() * 1      # 거리 = 속도 * 시간