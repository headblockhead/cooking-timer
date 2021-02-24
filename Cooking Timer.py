import datetime
asked = 0
Printed = 0

class Item:
    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

def sort_by_minutes(item):
    return item.minutes

items = []

print("Please enter the details about your items. ")
more_items = True
while more_items:
    try:
        name = input("What is the name of your item? ")
        hours = int(input("How many hours will it take to cook? "))
        mins = int(input("How many minutes will it take to cook? "))
        items.append(Item(name, (hours * 60) + mins))
        if input("Press 'y' to add another item or press 'n' to calculate results. ") != "y":
            more_items = False
    except :
        print("Please only use numbers!")
        exit()
try:
    print("-------------------------------------------------------------------")
    print("NOTE: Please do not set the time before the current time of the day")
    print("-------------------------------------------------------------------")
    todays_hour = int(input("Please enter the amout of hours in the time that you want it to be ready by. "))
    todays_mins = int(input("Please enter the amout of mins in the time that you want it to be ready by. "))
except:
    print("Please only use numbers!")
    exit()
full_mins = (todays_hour * 60) + todays_mins
thing = (max(items, key=sort_by_minutes))
cooking_time_min = full_mins 
cooking_time = divmod(cooking_time_min,60)


print("\n Put the items in at the following times:")

for item in items:
    cooking_time_min -= item.minutes
    print(item.name)
    cooking_time_min = divmod(cooking_time_min,60)
    print(cooking_time_min)
    cooking_time_min = full_mins
    cooking_time = divmod(cooking_time_min,60)

    # take each item in the list and take it's minuits away from cooking_time_mins and print it out on a separate line.