# isim soyisimle listeye öğrenci ekleme
# isim soy isimle listeden öğrenci silme
# listeye birden fazla öğrenci ekleme
# listeden birden fazla öğrenci silme (döngü kullanarak)
# listedeki tüm öğrencileri tek tek ekrana yazdırma
# listedeki index numarası öğrencinin numarası olsun. Öğrencinin numarasını öğrenme

students = []


def add_student():
    newStudent = input("Enter the student's name and surname : ")
    students.append(newStudent)
    print("The student has been added to the list.")


def remove_student():
    student = input("Name and surname of the student to be removed : ")
    students.remove(student)
    print("The student has been removed from the list.")


def add_multiple_students():
    while True:
        newStudent = input("Enter the student's name and surname (Type 'finish' to finish.): ")
        if newStudent == "finish":
            print("Students have been added to the list.")
            break
        else:
            students.append(newStudent)


def remove_multiple_students():
    while True:
        student = input("Name and surname of the students to be removed : ")
        if newStudent == "finish":
            print("Students have been removed to the list.")
            break
        else:
            students.remove(student)


def list_students():
    print("****** Students List ******")
    for i in students:
        print(i)


def student_number():
    student = input("Student name surname : ")

    for i in range(len(students)):
        if students[i] == student:
            number = i
            break
    print("Student number : ",number+1)


# add_student()
add_multiple_students()
# list_students()
remove_student()
# list_students()
student_number()
