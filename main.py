students = {}
classrooms = [i for i in range(1, 11 + 1)]
closed_classrooms = []

def add_student(name, grade):
    students[name] = grade
    if len(students) > 10:
        classrooms.remove(grade)
        closed_classrooms.append(grade)
        print('класс полон!')
        return students

def show_closed():
    return closed_classrooms

def delete(name):
    classrooms.append(students[name])
    closed_classrooms.remove(students[name])
    students.pop(name)
    return students

while True:
    a = input('введите имя ученика: ')
    b = input('услуги: 1)добавить, 2)удалить ученика, 3)показать список классов:   ')
    if b.lower() == 'добавить':
        classroom_value = int(input('введите номер класса: '))
        add_student(a, classroom_value)
        print('ученик успешно добавлен в класс!')
    elif b.lower() == 'удалить ученикa':
        if a in students:
            delete(a)
        else:
            print('такой ученик не найден!')
    elif b.lower() == 'показать список классов':
        print(show_closed())
    else:
        print('ERROR!')
