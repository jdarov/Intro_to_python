import random

def predict_weather():
    sunshine = random.choice([True, False])                   #the problem is here
                                                                   #this returns a string, which is ALWAYS truthy
    if sunshine:                                                   #will always run since sunshine is always truthy
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()