from temperature import Temperature
class Calorie:
    """Represents optimal calorie amount a person needs to take today"""

    def __init__(self, weight, height, age, temperature,type=1):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        if type==1:
            result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
            return result
        elif type==2:
            result = 10 * self.weight + 6.5 * self.height + 5 - (self.temperature-32) * 50/9
            return result


if __name__ == "__main__":
    temperature = Temperature(country="india", city="mumbai").get()
    calorie = Calorie(weight=115, height=185.4, age=19, temperature=temperature)
    print(calorie.calculate())
