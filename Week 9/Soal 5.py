my_array = [1, 2, 3, 4, 5]
my_array_new = [77, 99, 66, 88]
my_array.extend(my_array_new)
print('1.', my_array)

my_array.sort()
print('2.', my_array)

my_array.reverse()
print('3.', my_array)

print('4.', my_array.index(5))

my_array.remove(99)
print('5.', my_array)

salinan = my_array.copy()
my_array.clear()

print("6.", my_array)
print("7.", salinan)
