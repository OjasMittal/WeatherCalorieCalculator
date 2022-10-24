from trycourier import Courier
import os
from dotenv import load_dotenv
load_dotenv()
client = Courier(auth_token=os.getenv("AUTH_TOKEN"))
from calorie import Calorie
def send_email(name,email,weight,height,age,temperature,type,city,country):
                if type==1:
                    CorF="C"
                else:
                    CorF="F"
                city=city.title()
                country=country.title()
                calorie=Calorie(weight=weight,height=height,age=age,temperature=temperature,type=type)
                print(calorie.calculate())
                client.send_message(
                        message={
                          "to": {
                            "email": f"{email}",
                          },
                          "content": {
                            "title": f"Your Calorie intake for today",
                            "body": f"Hi {name}!\n Welcome to {city},{country}!\n"
                                    f"The current temperature is {temperature}°{CorF} \n So your today's Calorie intake should be: {calorie.calculate()} Calories. "
                                    f"\n\nDo not reply back to this email. "
                                    f"\n\nRegards,\nTeam - Weather Calorie Calculator",
                          },
                          "data": {"note": f"\nDo not reply back to this email. \n\n {calorie.calculate()}\nRegards,\nCalorie Calculator",
                          },
                          "routing": {
                                "method": "single",
                                "channels": ["email"],
                            },
                        }
                      )
                return True
if __name__=="__main__":
    print(send_email("Ojas","ojasfarm31@gmail.com",90,172,19,31))
