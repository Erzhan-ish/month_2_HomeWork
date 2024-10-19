fruits = ['apple', 'banana', 'pear']
animals = ['cat', 'dog']

for fruit in fruits:
    print(fruit)

for animal in animals:
    print(animal)

# O(F + A)
print('-----------------------------------------------')
for animal in animals:
    for fruit in fruits:
        print(f'{animal} likes {fruit}')
# O(A * F)


j = 8
while (j > 1):
    print(j)
    j = j - 1
    for animal in animals: # 2
        print(animal)
    k = len(animals)
    while (k > 0): # 1
        print(k)
        k = k - 1

#   O((A + A) * J) => O(2A * J) => O(A * J)

for fruit in fruits:
    print(fruit)
    for f in fruits:
        print(f)

# O(F * F) => O(F ** 2)

print('-----------------------------------------------------')
def counter(num):
    print(num)
    if num > 0:
        counter(num - 1)

counter(3)