cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
answer = 17
if answer != 42:
    print("That is not the correct  answer.Please try again!")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title()+", you can post a response if you wish.")
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car =='audi'? I predict False.")
print(car == 'audi')
age = 19
if age >= 18:
    print("You are old enough to vote!")
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote sa soon as you turn 18!")
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
age = 12
if age < 4:
    pice = 0
if age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" +str(price)+".")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" +str(price)+".")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" +str(price)+".")

requested_toppings = ['mushrooms', 'extra cheese',]
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'extra cheese',]
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

alien_color = ['green', 'yellow']
if 'green' in alien_color:
    print("You get five point.")

alien_color = ['green', 'yellow']
if 'red' in alien_color:
    print("You get five point.") 

alien_color = ['green', 'yellow']
if 'red' in alien_color:
    print("You get five point.")
else:
    print("You can't get five point.")

alien_color = ['green', 'yellow']
if 'green' in alien_color:
    print("You get five point.")
else:
    print("You can't get five point.")

alien_color = ['green', 'yellow']
if 'red' in alien_color:
    print("You get five point.")
else:
    print("You can get ten point.")

alien_color = ['green', 'yellow']
if 'green' in alien_color:
    print("You get five point.")
if 'red' in alien_color:
    print("You can't get five point.")

alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You get five point.")
elif 'yellow' in alien_color:
    print("You can get ten point.")
else:
    print("You can get fifth point.")

alien_color = ['green', 'yellow', 'red']
if 'yellow' in alien_color:
    print("You get ten point.")
elif 'green' in alien_color:
    print("You can get ten point.")
else:
    print("You can get fifth point.")

alien_color = ['green', 'yellow', 'red']
if 'red' in alien_color:
    print("You get fiften point.")
elif 'yellow' in alien_color:
    print("You can get ten point.")
else:
    print("You can get fifth point.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+"." )
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
         print("Adding "+requested_topping+"." )
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
         print("Adding "+requested_topping+"." )
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+"." )
    else:
        print("Sorry,we don't have " + requested_topping+".")
print("\nFinished making your pizza!")
age = 1
if age < 2:
    print("He is a baby")
age = 3
if age < 4:
    print("He is a toddler")
age = 12
if age < 13:
    print("He is a child")
age = 18
if age < 20:
    print("You are a teenager")

favorite_fruits = ["banbana", "apple", "grape"]
if 'banbana' in favorite_fruits:
    print("You really like bananas!")
if 'candy' in favorite_fruits:
    print("You really like candy")
if 'apple' in favorite_fruits:
    print("You really like apple")
if 'peach' in favorite_fruits:
    print("You really like peach")
if 'grape' in favorite_fruits:
    print("You really like grape")

names = ['admin', 'Lihailing', 'xiaohong', 'xiaolan', 'xiaohua']
for name in names:
    if name == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print(name + " thank you for logging in again.")

names = ['admin', 'Lihailing', 'xiaohong', 'xiaolan', 'xiaohua']
if names:
    for name in names:
        print("Hello "+name)
    else:
        print("We need to find some users!")

current_users = ['xiaohua', 'xiaohong', 'xiaolv', 'xiaolan', 'xiaohua']
new_users = ['lihailing', 'meigou', 'zhenzhen', 'xiaohua',  'xiaolan']
for new_users in current_users:
    if new_users in current_users:
        print("Hello "+new_users+".")
    else:
        print("Sorry, I can't find you "+new_users+".")
names = ['admin', 'Lihailing', 'xiaohong', 'xiaolan', 'xiaohua']
if names:
    for name in names:
        print("Hello "+name)
    else:
        print("We need to find some users!")