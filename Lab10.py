class SwimmingPool:
    
    chlorine_concentration = 7

    def __init__(self, address=None, water_capacity_in_litres=None, people_capacity=None, depth_in_metres=None,
                 length_in_metres=None, width_in_metres=None):
        self.address = address
        self.water_capacity_in_litres = water_capacity_in_litres
        self.people_capacity = people_capacity
        self.depth_in_metres = depth_in_metres
        self.length_in_metres = length_in_metres
        self.width_in_metres = width_in_metres

    @staticmethod
    def get_chlorine_concentration():
        return SwimmingPool.chlorine_concentration

    def __str__(self):
        return "SwimmingPool adress is " + str(self.address) + "\n" + \
               "Water Capacity in litres is " + str(self.water_capacity_in_litres) + "\n" + \
               "People Capacity is " + str(self.people_capacity) + "\n" + \
               "Depth is " + str(self.depth_in_metres) + "\n" + \
               "Lenght is " + str(self.length_in_metres) + "\n" + \
               "Width is " + str(self.width_in_metres) + "\n"

    def __del__(self):
        return

    @staticmethod
    def main():
        print()
        swimming_pool1 = SwimmingPool("Hata Marana")
        swimming_pool2 = SwimmingPool("Hata Osadu", 10000, 10)
        swimming_pool3 = SwimmingPool("Hata Viti", 1000000, 1, 10, 100, 100)
        print(swimming_pool1.__str__())
        print(swimming_pool2.__str__())
        print(swimming_pool3.__str__())


if __name__ == '__main__':
    SwimmingPool.main()
