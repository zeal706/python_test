names = ['zhenzhen', 'xiaochu', 'lijuan']
print(names[0])
names = ['zhenzhen', 'xiaochu', 'lijuan']
print(names[1])
names = ['zhenzhen', 'xiaochu', 'lijuan']
print(names[2])
names = ['zhenzhen', 'xiaochu', 'lijuan']
message = "Long time no see" + names[0].title()+"."
print(message)
names = ['zhenzhen', 'xiaochu', 'lijuan']
message = "Long time no see" + names[1].title()+"."
print(message)
names = ['zhenzhen', 'xiaochu', 'lijuan']
message = "Long time no see" + names[2].title()+"."
print(message)
vehicle = [' Daben bike', 'little car ', 'big car']
message = " I would like to own a " + vehicle[2].title()+"."
print(message)
People = ['xiaohong', 'xiaohua', 'xiaolu']
message = " Can you come to my party, " + People[1].title()+"."
print(message)
People = ['xiaohong', 'xiaohua', 'xiaolu']
message = " Can you come to my party, " + People[1].title()+"."
message = People[0].title()  +  " say:" +" "+ "I can't come here"
print(message)
People = ['xiaohong', 'xiaohua', 'xiaolu']
print(People)
People[0] = 'lihailing'
print(People)
message = "I find another big table"
print(message)
People = ['xiaohong', 'xiaohua', 'xiaolu']
People.insert(0, 'libai')
print(People)
People = ['xiaohong', 'xiaohua', 'xiaolu']
People.insert(2, 'libai')
print(People)
People = ['xiaohong', 'xiaohua', 'xiaolu']
People.append('libai')
print(People)
People = ['xiaohong', 'xiaohua', 'xiaolu']
message = "Welcome to my party," +People[0].title() + "."
print(message)
People = ['xiaohong', 'xiaohua', 'xiaolu']
message = "Welcome to my party," +People[1].title() + "."
print(message)
People = ['xiaohong', 'xiaohua', 'xiaolu']
message = "Welcome to my party," +People[2].title() + "."
print(message)
People = ['xiaohong', 'xiaohua', 'xiaolu']
print(People)
del People[0]
print(People)
People = ['xiaohong', 'xiaohua', 'xiaolu']
message = "Sorry,there is something wrong," +People[1].title() + "."
print(message)
People = ['xiaohong', 'xiaohua', 'xiaolu']
print(People)
People_name = People.pop()
print(People)
message = "Sorry,there is something wrong," +People_name + "."
print(message)
People = ['xiaohong', 'xiaohua']
message = "Please come here on time," +People[1].title() + "."
print(message)
People = ['xiaohong', 'xiaohua']
message = "Please come here on time," +People[0].title() + "."
print(message)
People = ['xiaohong', 'xiaohua']
del People[0]
print(People)
del People[0]
print(People)
address = ['Fuzhou', 'Xinjiang', 'Qinghai']
print(sorted(address))
address = ['Fuzhou', 'Xinjiang', 'Qinghai']
print(address)
address.reverse()
print(address)
address.reverse()
print(address)
address = ['Fuzhou', 'Xinjiang', 'Qinghai']
address.sort(reverse=True)
print(address)
Pizzas = ['bishengke', 'zizhi', 'feng']
for Pizza in Pizzas:
    print("I like " + Pizza.title() + " pizza")
print("I really like pizza!")
animals = ("dog", "cat", "pig")
for animal in animals:
    print(animal)
animals = ("dog", "cat", "pig")
for animal in animals:
    print(animal.title() + "would make a great pet")
print("Any of these animals would make a great pet")
for value in range (1,21):
    print(value)
#numbers = list(range(1,100000))
#f or number in numbers:
 #   print(number)
#numbers = list(range(1,100000))
#print(min(numbers))
#print(max(numbers))
numbers = list(range(1,20))
even_numbers = list(range(1,21,2))
print(even_numbers)
for even_number in numbers:
    print(even_number)
squares = []
for value in range(1,10):
    square = value**3
    squares.append(square)
print(squares)
squares = [value**3 for value in range(1,11)]
print(squares)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are:")
for player in players[:3]:
    print(player.title())
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Three items in the list are:")
for player in players[1:4]:
    print(player.title())
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The last three items in the list are:")
for player in players[-3:]:
    print(player.title())
Pizzas = ['bishengke', 'zizhi', 'feng']
friend_pizza = Pizzas[:]
print(Pizzas)
print(friend_pizza)
Pizzas = ['bishengke', 'zizhi', 'feng']
friend_pizza = Pizzas[:]
Pizzas.append('Yo')
print(Pizzas)
print(friend_pizza)
Pizzas = ['bishengke', 'zizhi', 'feng']
friend_pizza = Pizzas[:]
friend_pizza.append('YY')
print(Pizzas)
print(friend_pizza)
Pizzas = ['bishengke', 'zizhi', 'feng']
friend_pizza = Pizzas[:]
Pizzas.append('Yo')
for pizza in Pizzas:
    print("My favorite pizzas are:")
    print(pizza)
Pizzas = ['bishengke', 'zizhi', 'feng']
friend_pizza = Pizzas[:]
friend_pizza.append('YY')
for pizza in Pizzas:
    print("My friend's favorite pizzas are:")
    print(pizza)
Pizzas = ['bishengke', 'zizhi', 'feng']
for pizza in Pizzas:
    print(pizza)
foods = ("ice", "mantou", "noodle", "dami", "shuiguo")
for food in foods:
    print(food)
foods = ("ice", "mantou", "noodle", "dami", "shuiguo")
print("original foods:")
for food in foods:
    print(food)
foods = ("haochide", "mantou", "noodle", "shucai", "shuiguo")
print( "\n changed foods:")
for food in foods:
    print(food)