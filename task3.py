def get_students_from_list():
    # [name, age, faculty]
    Porpington = ['Porpington', 11, 'Hufflepuff']
    Mimsey = ['Mimsey', 12, 'Ravenclaw']
    Tamseen = ['Tamseen', 13, 'Slytherin']
    Midgeon = ['Midgeon', 13, 'Gryffindor']
    students = [Porpington, Mimsey, Tamseen, Midgeon]
    return students

def get_students_from_dict():
    Mimsey = {'name': 'Mimsey', 'age': 12, 'faculty': 'Ravenclaw'}
    Tamseen = {'name': 'Tamseen', 'age': 13, 'faculty': 'Slytherin'}
    Midgeon = {'name': 'Midgeon', 'age': 13, 'faculty': 'Gryffindor'}
    Porpington = {'name': 'Porpington', 'age': 11, 'faculty': 'Hufflepuff'}
    students = [Mimsey, Tamseen, Midgeon, Porpington]
    return students

def find_students_from_list(faculty):
    students = get_students_from_list()
    for i in range(len(students)):
        if faculty in students[i]:
            print(students[i])

def find_students_from_dict(faculty):
    students = get_students_from_dict()
    for student in students:
        if student.get('faculty') == faculty:
            print(student)

def run():
    print('***Hogwarts Student Journal***')
    owl = r"""
          /\_/\
         ((@v@))
         ():::()
          VV-VV
          """
    print(owl)
    
    print("To search for students, select a faculty.")
    print("Gryffindor, Slytherin, Ravenclaw, Hufflepuff")
    faculty_key = input("(g, s, r, h): ")
    options = {'g': 'Gryffindor', 's': 'Slytherin', 
            'r': 'Ravenclaw', 'h': 'Hufflepuff'}
    faculty = options[faculty_key]
    data_type = input("Use list or dictionary? \n(l, d): ")
    if data_type == 'l':
        find_students_from_list(faculty)
    elif data_type == 'd':
        find_students_from_dict(faculty)
    else:
        print("Error!", data_type, " not found!")

if __name__ == '__main__':
    run()

