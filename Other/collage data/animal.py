class Animal(object):
    def feed(self):
        print("Animal is eating..!")

class Herbivorous(Animal):
    def feed(self):
        print("Herbivorous Animal eating Plants...!")

animal1 = Herbivorous()

animal1.feed()


