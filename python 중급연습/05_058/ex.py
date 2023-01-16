'''
자동차 경주 게임 클래스를 만들어보자
자동차는 랜덤하게 이동하며, 편의상 10초동안 주행한다고 할 때
가장 멀리 이동한 자동차가 우승하는 게임
'''
from car_game import racing as rc
from car_game import car

myCarGame = rc.CarRacing()
car01 = car.Car('Car01', 'White', 250)
car02 = car.Car('Car02', 'Black', 200)
car03 = car.Car('Car03', 'Red', 180)
car04 = car.Car('Car04', 'Yellow', 230)
car05 = car.Car('Car05', 'Blue', 195)

myCarGame.addCar(car01)
myCarGame.addCar(car02)
myCarGame.addCar(car03)
myCarGame.addCar(car04)
myCarGame.addCar(car05)

myCarGame.startRacing()