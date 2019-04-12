from random import randint

number = randint(0, 100)
print(number)
if number < 30:
    print("rainy")
elif number < 60:
    print("cloudy")
else:
    print("sunny")