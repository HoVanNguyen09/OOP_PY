class vehicle:

    def __init__(self, name, colors, price):
        self.name = name
        self.colors = colors
        self.price = price

    def volumn(self, capacity):
        self.capacity = capacity
        return f"The school bus volumn of a {self.name} is {capacity} passengers."
    
class bus(vehicle):
    
    def volumn(self, capacity=50):
        self.capacity = capacity
        return super().volumn(capacity=50)
school_bus = bus('School Bus', 'Yellow', '$48.890')
print(school_bus.volumn())