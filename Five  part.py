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
    print("That is n coot therrect answer.Please try again!")

people = {'first_name': 'zhenzhen', 'last_surname':'liu', 'age':'22', 'city':'Henan'}
print(people)

message = {'xiaohong':'red', 'xiaolv':'yellow', 'xiaohua':'black', 'xiaolan':'blue', 'xiaozi':'white'}
print("xiaohong, if you like "+message['xiaohong'].title()+
"?")
print("xiaolv, if you like "+message['xiaolv'].title()+
"?")
print("xioahua, if you like "+message['xiaohua'].title()+
"?")
print("xiaolan, if you like "+message['xiaolan'].title()+
"?")
print("xiaozi, if you like "+message['xiaozi'].title()+
"?")

user_0 = {
    'choice': 'xuanze', 
    'coding': 'bianma', 
    'error': 'cuowu', 
    'invalid': 'wuxiao',
    }
for key, value in user_0.items():
        print("\nkey:"+key)
        print("value:"+value)

user_0 = {
    'choice': 'xuanze', 
    'coding': 'bianma', 
    'error': 'cuowu', 
    'invalid': 'wuxiao',
    'right': 'dui',
    'pull': 'laqu',
    'file': 'wenjian',
    }
for key, value in user_0.items():
        print("\nkey:"+key)
        print("value:"+value)


country = {
    'nile':'egypt',
    'yamaxun':'feizhou',
    'changjiang':'china',
    }
for river,area in country.items():
    print("The "+river.title()+" runs through "+area.title()+".")
for river in sorted(country.keys()):
    print(river.title())
for area in sorted(country.values()):
    print(area.title())

user_0 = {
    'uaername': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print("\nKey: "+key)
    print("Value:"+value)
