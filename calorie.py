from temperature import Temperature
class Calorie:
    """Represents optimal calorie amount a person needs to take today"""

    def __init__(self, weight, height, age, temperature,type=1):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature
        self.type=type

    def calculate(self):
        if self.type==1:
            result = int(22 * self.weight + 6.5 * self.height + 5 - self.temperature * 10)
            return result
        elif self.type==2:
            result = int(22 * self.weight + 6.5 * self.height + 5 - (self.temperature-32) * 50/9)
            return result


if __name__ == "__main__":
    temperature = Temperature(country="india", city="mumbai").get()
    calorie = Calorie(weight=95, height=185, age=20, temperature=temperature)
    print(calorie.calculate())
