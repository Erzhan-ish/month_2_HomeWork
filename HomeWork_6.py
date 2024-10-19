a = [32,3,12,43,98,56,35,15,85,64,38]

def buble_sort(ar):
    iter = len(ar) - 1
    for i in range(iter):
        for j in range(iter - i):
            if ar[j] > ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]

print(a)
buble_sort(a)
print(a)



def  binary_search(list, value):
    n = len(list)
    ResultOk = False
    first = 0
    last = n - 1
    pos = None

    while first < last:
        middle = (first + last) // 2
        if value == list[middle]:
            first = middle
            last = first
            ResultOk = True
            pos = middle
        else:
            if value > list[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if ResultOk == True:
        print('Элемент найден')
        return pos


    else:
        print('Элемент не найден')


index = binary_search([12,34,56,78,89,94,112], 56)
print(f'Искомый элемент в списке имеет индекс {index}!')