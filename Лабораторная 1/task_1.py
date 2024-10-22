numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
num_ = numbers.index(None)
if numbers.index(None):
    numbers[num_] = 0
sum_ = sum(numbers)
kol_ = len(numbers)
none_ = sum_/kol_
numbers[num_] = none_

print("Измененный список:", numbers)
