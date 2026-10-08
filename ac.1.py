temperature = int(input("what is today's temperature in:  "))

if temperature < 20:
    outfit="jacket"
    print("it is cold today;;")
    print("wear a", outfit)
else:
    outfit="t-shirt"
    print("it is warm today")
    print("wear a", outfit)


is_raining = input("is it raining today? (yes or no): ")

if is_raining =="yes":
    print("bring an umbrella")


if is_raining =="no":
    print("no umbrella^^")

else:
    print("what")


wind_speed= int(input("enter the wind spead in km/h: "))
if wind_speed > 30:
    needs_windbreaker="yes"
    print("um u need a windbreaker")
    print("wear it over ur", outfit)

else:
    needs_windbreaker="no"
    print("eh no windbreaker for today")