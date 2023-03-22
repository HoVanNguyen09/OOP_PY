# Viết một ct py, để tạo ra một lớp con có tên bus() kế thừa
# tất cả các hàm trong lớp cha có tên là car() ở câu hỏi số 1.

## from lesson_1 import cars, sử dụng được
from lesson_1_cars import *

# from lesson_1 import cars
# class cars:
#    def __init__(self, Company, Price, Colors):
#       self.company = Company
#       self.price = Price
#       self.colors = Colors

class bus(cars):
   pass

school_bus = bus('School Bus', 'Yellow', '$48.890')
print("School bus company", school_bus.Company)
print("School Bus Color", school_bus.Color)
print("School_Bus_Prices", school_bus.Price)