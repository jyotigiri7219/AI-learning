# variable

a = 21
b = 54

c = a

a = b
b = c

print("a is equal to :- ", a)
print("b is equal to :- ", b)

# list

list = [10, 20]

list[0], list[1] = list[1], list[0]

print(list)