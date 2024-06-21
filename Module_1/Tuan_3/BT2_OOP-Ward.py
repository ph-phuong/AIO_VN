from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: float):
        self._name = name
        self._yob = yob

    def getName(self):
        return self._name

    def getYob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: float, grade: str):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: float, subject: str):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: float, specialist: str):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__nameList = list()

    def addPerson(self, person: Person):
        self.__nameList.append(person)

    def describe(self):
        print(f"Name of Ward: {self.__name}")
        for p in self.__nameList:
            p.describe()

    def countDoctor(self):
        count_doctor = 0
        for p in self.__nameList:
            if isinstance(p, Doctor):
                count_doctor += 1
        return count_doctor

    def sortAge(self):
        sorted_list = sorted(
            self.__nameList, key=lambda x: x.getYob(), reverse=True)
        return sorted_list

    def computeAvgTeacher(self):
        counter = 0
        total = 0
        for p in self.__nameList:
            if isinstance(p, Teacher):
                counter += 1
                total += p.getYob()
        return total / counter


print('-------')
print('Câu a: ')
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()

print('-------')
print('Câu b: ')
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB ", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1.addPerson(doctor2)
ward1.describe()

print('-------')
print('Câu c: ')
print(f"Number of doctors : {ward1.countDoctor()}")

print('-------')
print('Câu d: ')
print('After sorting Age of Ward1 people')
sorted_persons = ward1.sortAge()
for person in sorted_persons:
    person.describe()


print('-------')
print('Câu e: ')
print(f"Average year of birth (teachers): {ward1.computeAvgTeacher()}")
