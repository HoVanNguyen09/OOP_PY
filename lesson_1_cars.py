# Viết một chương trình py tạo ra một lớp có tên là cars
# với các thuộc tính bao gồm: company, price, colors

class cars:
    # 1: Cách tự xây dựng ban đầu

    # company = "America"
    # Price = 2441999
    # Colors = ["Red", "Yelow", "White", "Black"]

    # 2: Cách thầy xây dựng
    def __init__(self, company, colors, price ):
        # Định nghĩa các thuộc tính
        self.Company = company
        self.Color = colors
        self.Price = price
# 1: Cách tự xây dựng ban đầu
# print(Cars.company)
# print(Cars.Price)
# print(Cars.Colors)   

# 2: Cách thầy xây dựng
modelY = cars("America","Red", "$55.390")
print(modelY.Company, modelY.Color, modelY.Price)