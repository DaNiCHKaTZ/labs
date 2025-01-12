import os

def read_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines[1:]]

files = {
    'Sp1.txt': 'Кружок информатики',
    'Sp2.txt': 'Кружок математики',
    'Sp3.txt': 'Кружок физики',
    'Sp4.txt': 'Отличники',
    'Sp5.txt': 'Прогульщики',
    'Sp6.txt': 'Спортсмены',
    'Sp7.txt': 'Участники хора',
    'Sp8.txt': 'Члены БРСМ',
    'Sp9.txt': 'Члены профсоюза',
    'Sp10.txt': 'Занимающиеся наукой'
}

students_activities = {}

# Читаем все файлы и заполняем словарь students_activities
for file_name, activity_name in files.items():
    file_path = file_name
    activity_list = read_list(file_path)
    for student in activity_list:
        if student not in students_activities:
            students_activities[student] = []
        students_activities[student].append(activity_name)

print("Журнал по видам деятельности:")
for student, activities in students_activities.items():
    print(f'{student}: {", ".join(activities)}')


group_file_path = 'SpStGr.txt'
with open(group_file_path, 'w', encoding='utf-8') as file:
    file.write("Журнал по видам деятельности:\n")
    for student, activities in students_activities.items():
        file.write(f'{student}: {", ".join(activities)}\n')

print("\nЖурнал по видам деятельности записан в файл SpStGr.txt")

otlichniki = read_list('Sp4.txt')
hor = read_list('Sp7.txt')
prof_list = read_list('Sp9.txt')
not_prof = [student for student in hor if student in otlichniki and student not in prof_list]

print("\nУчастники хора, которые являются отличниками и не членами профсоюза:")
for student in not_prof:
    print(student)
