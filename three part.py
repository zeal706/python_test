bicycles = ['trek', 'cannondale,' 'redline', 'specialized']
print(bicycles)
bicycles = ['trek', 'cannondale,' 'redline', 'specialized']
print(bicycles[0])
bicycles = ['trek', 'cannondale,' 'redline', 'specialized']
print(bicycles[0].title())
bicycles = ['trek', 'cannondale',  'redline', 'specialized' ]
print(bicycles[3])
print(bicycles[1])
bicycles = ['trek', 'cannondale',  'redline', 'specialized' ]
print(bicycles[-1])
bicycles = ['trek', 'cannondale',  'redline', 'specialized' ]
message = "My first bicycle was a "+bicycles[0].title()+"."
print(message)
names = ['zhenzhen', 'xiaochu', 'xiaoshuang', 'xiaojuan']
print(names[0])
names = ['zhenzhen', 'xiaochu', 'xiaoshuang', 'xiaojuan']
print(names[3])
names = ['zhenzhen', 'xiaochu', 'xiaoshuang', 'xiaojuan']
print(names[-1])
names = ['zhenzhen', 'xiaochu', 'xiaoshuang', 'xiaojuan']
message = "Long time no see "+names[1].title()+"."
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " +last_owned.title()+".")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " +first_owned.title()+".")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the oringinal list again:")
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
address = ['fuzhou', 'xinjiang', 'qinghai']
print(address)
print(sorted(address))