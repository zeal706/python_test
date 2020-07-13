def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()

def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " +username.title()+"!")
greet_user('jesse')

def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " +username.title()+"!")
greet_user('Liruo')

def display_message():
    """在本章学的是什么"""
    print("In this page, I learned about functions.")
display_message()

def favorite_book(title):
    print("One of my favorite books is "+title+"!")
favorite_book('Alice in Wonderland')

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster', 'harry')

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('harry', 'hamster')

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type='hamster', pet_name='harry')

def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='hamster')

def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster')

def describe_pet(pet_name,animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='hamster',animal_type='hamster')

def make_shirt(shirt_rule,shirt_mode):
    print("\nThe shirt is "+shirt_rule+" and it mode is "+shirt_mode.title()+".")
make_shirt('twenty','Just do it')

def make_shirt(shirt_rule,shirt_mode):
    print("\nThe shirt is "+shirt_rule+" and it mode is "+shirt_mode.title()+".")
make_shirt(shirt_rule='twenty',shirt_mode='Just do it')

def make_shirt(shirt_rule,shirt_mode='I love Python'):
    print("\nI have a "+shirt_rule+" T-shirt,it bearing "+shirt_mode+".")
make_shirt(shirt_rule="big")
make_shirt(shirt_rule="medium")
make_shirt(shirt_rule='at will',shirt_mode='I want to study')

def describe_city(city_name,city_country='China'):
    print(city_name+" is in "+city_country+".")
describe_city('Guangzhou')
describe_city('Fuzhou')
describe_city('Huashengdun')

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')

print(musician)

def get_formatted_name(first_name, last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name, 'last':last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

#def get_formatted_name(first_name, last_name):
#    """返回整洁的姓名"""
#    full_name = first_name+'  '+last_name
#    return full_name.title()
# 这是一个无限循环！
#while True:
#    print("\nPlease tell me your name:")
#    f_name = input("First name: ")
#    l_name = input("Last name: ")
#    formatted_name = get_formatted_name(f_name,l_name)
#    print("\nHello, "+formatted_name+"!")

#def get_formatted_name(first_name, last_name):
#   """返回整洁的姓名"""
#    full_name = first_name+'  '+last_name
#    return full_name.title()
# 这是一个无限循环！
#while True:
#    print("\nPlease tell me your name:")
#   print("(enter 'q' at any time to quit)")
#    f_name = input("First name: ")
#    if f_name == 'q':
#        break
#    l_name = input("Last name: ")
#    if l_name == 'q':
#        break
#    formatted_name = get_formatted_name(f_name,l_name)
#    print("\nHello, "+formatted_name+"!")

def city_country(city_name,city_nation):
    full_name = city_name+' '+city_nation
    return full_name
Free = city_country('Fuzhou', 'China')
print(Free)

def make_album(first_name, last_name):
    """ 返回一个字典，其中包含歌曲的信息"""
    album = {'first':first_name, 'last':last_name}
    return album
musician = make_album('lixiangsanxun','chenhongyu')
print(musician)

def make_album(first_name, last_name, number = ''):
    """ 返回一个字典，其中包含歌曲的信息"""
    album = {'first':first_name, 'last':last_name}
    if number:
        album['number'] = number
    return album
musician = make_album('lixiangsanxun','chenhongyu',number=24)
print(musician)

#def make_album(first_name, last_name):
#    """ 返回一个字典，其中包含歌曲的信息"""
#    album = first_name+ ' '+last_name
#    return album
# 这是一个无限循环！
#while True:
#    print("\nPlease tell me an album of artists an title:")
#    a_name = input("Artists name: ")
#    t_name = input("Title name: ")
#    album = make_album(a_name,t_name)
#    print("\nMy favorite is "+album+"!")

def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, "+name.title()+"!"
        print(msg)
usernames = ['hannan', 'try', 'margot']
greet_users(usernames)  

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: "+current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")

for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant' , 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

    
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant' , 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

def magician(magician_name):
    while magician_name:
        other_name = magician_name.pop()
        print("\nEvery magician name is: "+other_name)
magician_name = ['lihailing', 'xiaohong', 'xiaohua']
magician(magician_name)

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a "+str(size)+ "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', 
                             location='princeton',
                             field='physics')
print(user_profile)

def sandwich_ingredients(*ingredients):
    """打印顾客点的所有配料"""
    print("\nHere are the ingredients for your sandwich: ")
    for ingredient in ingredients:
        print("-"+ingredient)
sandwich_ingredients('butter')
sandwich_ingredients('bread', 'cabbage', 'seasoning')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Li', 'hailing', 
                             age='twenty',
                             gender='girl',
                             interest='read')
print(user_profile)

def car_message(manufacturer, model, **user_info):
    """创建一个字典，其中包含汽车的信息"""
    message = {}
    message['manufacturer_name'] = manufacturer
    message['model_name'] = model
    for key, value in user_info.items():
        message[key]= value
    return message
user_message = car_message('subaru', 'outback',
                           color='blue',
                           tow_package=True)
print(user_message)

import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese' )

from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese' )

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese' )

import sandwich
sandwich.sandwich_ingredients('butter')
sandwich.sandwich_ingredients('bread', 'cabbage', 'seasoning')

from sandwich import sandwich_ingredients
sandwich_ingredients('butter')
sandwich_ingredients('bread', 'cabbage', 'seasoning')

from sandwich import sandwich_ingredients as s
s('butter')
s('bread', 'cabbage', 'seasoning')

import sandwich as w
w.sandwich_ingredients('butter')
w.sandwich_ingredients('bread', 'cabbage', 'seasoning')

from sandwich import *
sandwich_ingredients('butter')
sandwich_ingredients('bread', 'cabbage', 'seasoning')


    

