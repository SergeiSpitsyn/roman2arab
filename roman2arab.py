rim = input('Введите римское число: ')
#rim = 'MMCMLXXXVIII'
#rim = 'MMV'
list_rim = list(rim)
print(list_rim)
i = 0
for element in list_rim:
    if element == 'M':
        list_rim[i] = 1000
    elif element == 'D':
        list_rim[i] = 500
    elif element == 'C':
        list_rim[i] = 100
    elif element == 'L':
        list_rim[i] = 50
    elif element == 'X':
        list_rim[i] = 10
    elif element == 'V':
        list_rim[i] = 5
    elif element == 'I':
        list_rim[i] = 1
    i = i + 1
print(list_rim)
itog = 0
i = 0
while i < len(list_rim) - 1:
    if list_rim[i] < list_rim[i + 1]:
        itog = itog + (list_rim[i + 1] - list_rim[i])
        i = i + 1
    elif list_rim[i] > list_rim[i + 1]:
        itog = itog + (list_rim[i])
    elif list_rim[i] == list_rim[i + 1]:
        itog = itog + (list_rim[i])
    i = i + 1
print(i)
itog = itog + list_rim[i]

print(itog)
