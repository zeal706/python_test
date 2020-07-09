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

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name.title()+ "'s favorite language is "+
        language.title()+".")

#names = {'xiaohong', 'jen', 'xiaoli', 'sarah', 'xiaozhen'}
#for name in names.items():
#    print(name.title()+", Thank you!")

people_0 = {'first_name': 'zhenzhen', 'last_surname':'liu', 'age':'22', 'city':'Henan'}
people_1 = {'first_name': 'hailing', 'last_surname':'li', 'age':'18', 'city':'fujian'}
people_2 = {'first_name': 'haoran', 'last_surname':'chen', 'age':'23', 'city':'luohe'}
peoples = [people_0,people_1,people_2]
for people in peoples:
    print(people)

xiaohua = {'type':'dog', 'host name':'meimei'}
xiaohuang = {'type':'cat', 'host name':'liangliang'}
xiaowei = {'type':'rabit', 'host name':'xiaoruo'}
pets = [xiaohua,xiaohuang,xiaowei]
for pet in pets:
    print(pet)

favorite_places = {
    'xiaoli': ['xiamen', 'qinghai', 'shanxi'],
    'xiaolan': ['henan', 'shenqiu', 'zhoukou'],
    'xiaomei': ['yunnan', 'xizang', 'xinjiang'],
    }
for name, places in favorite_places.items():
    print("\n"+name.title()+"'s favorite places are:")
    for place in places:
        print("\t"+place.title())


#favorite_numbers = {
#   'jen': [1,2],
#   'sarah': [3,4],
#   'edward': [5,6],
#   'phil': [7,8],
#   }
#for name, numbers in favorite_numbers.items():
#    print(name.title()+ "'s favorite number is:")
#   for number in numbers:
#      print("\t"+number.title())

cities = {
    'zhenzhou': {
        'country':'henan',
        'population':' two million',
        'fact':'old',
        },

    'suzhou': {
        'country':'jiangsu',
        'population':' one billion',
        'fact':'beautiful',
        },
    'fuzhou': {
        'country':'fujian',
        'population':' five billion',
        'fact':'nice',
        },
    }
for area, introduce in cities.items():
    print("\n area:"+area)
    ideal_area = introduce['country'] + introduce['population']
    fact = introduce['fact']
    print("\tideal area: " +ideal_area.title())
    print("\tfact:"+fact.title())




message = input("What kind car do you like?")
print("Let me see if I can find you a "+message)

number = input("How many people come here eat?")
number = int(number)
if number > 8:
    print("There is no desk")
else:
    print("There have desk")

prompt = "\nPlease add your favorite ingredients:"
prompt+= "\n(Enter 'quit' when you are finished.)"
while True:
    ingredients = input(prompt)
    if ingredients == 'quit':
        break
    else:
        print("we will add this ingredients "+ingredients.title() +"!")

number = input("\nPlease tell me how old are you?")
number = int(number)
if number < 3:
    print("You are be free")
elif number <= 12:
    print("You need to pay 15$")
else:
    print("You need to pay 15$")

x = 1
while x <= 5:
    print(x)