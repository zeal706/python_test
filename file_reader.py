with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip)

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ' '
for line in lines:
    pi_string+= line.rstrip()
print(pi_string)
print(len(pi_string))

filename = 'pi_30_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ' '
for line in lines:
    pi_string+= line.rstrip()
print(pi_string)
print(len(pi_string))

filename = 'pi_30_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ' '
for line in lines:
    pi_string+= line.strip()
print(pi_string)
print(len(pi_string))

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ' '
for line in lines:
    pi_string+= line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))