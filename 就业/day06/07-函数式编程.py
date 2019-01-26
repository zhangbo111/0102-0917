def func(num):
    return num ** 2


result1 = map(func, [1, 2, 3])
print(result1)
result2 = list(result1)
print(result2)

# lst = []
# for i in [1, 2, 3]:
#     result = func(i)
#     lst.append(result)
# print(lst)

def func(num):
    if num % 2 == 1:
        return num


result1 = filter(func, [1, 2, 3, 4, 5, 6])
print(list(result1))


lst1 = [1, 2, 3, 23, 2, 3, 5]
result = list({}.fromkeys(lst1).keys())
print(result)
