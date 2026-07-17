from my_package.student import Student
from my_package.human import Human
from my_package.exceptions import GroupError
from my_package.group import Group

gr = Group('PD1')
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr.add_student(st1)
gr.add_student(st2)

print(f"The group after adding 2 students:")
print(gr)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(f"Group after deletion 'Taylor'")
print(gr)  # Only one student

try:

    for i in range(10):
        st = Student('Male', 20 + i, f'Name{i}', f'LastName{i}', f'AN{i}')
        gr.add_student(st)
except GroupError as e:
    print(f"Error: {e}")

print("\nFinal group:")
print(gr)
