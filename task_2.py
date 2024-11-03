def find_common_participants(participants_first_group, participants_second_group, delimeter=','):
    first = participants_first_group.split(delimeter)
    second = participants_second_group.split(delimeter)
    participant = list(set(first) & set(second))
    return sorted(participant)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


participants = find_common_participants(participants_first_group, participants_second_group)
print(participants)