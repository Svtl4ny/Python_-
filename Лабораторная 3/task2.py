# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, splitter=','):
    list_1 = set(group1.split(splitter))
    list_2 = set(group2.split(splitter))
    same_ = list(list_1.intersection(list_2))
    same_.sort()
    return same_

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))