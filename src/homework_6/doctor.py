from person_job_company import Person
from money import Money
from my_exceptions import DoctorException


class Doctor(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, address: str,
                 department: str, profession: str, patronymic: str, salary: Money):
        super().__init__(name, surname, age, gender, address)
        if not isinstance(department, str):
            raise DoctorException("Department must be string")
        if not isinstance(profession, str):
            raise DoctorException("Profession must be string")
        if not isinstance(patronymic, str):
            raise DoctorException("Patronymic must be string")
        if not isinstance(salary, Money):
            raise DoctorException("Salary must be Money class")
        self.__department = department
        self.__profession = profession
        self.__patronymic = patronymic
        self.__salary = salary

    def __repr__(self):
        return f"Dr. {super().__repr__()}, department: {self.__department}, profession: {self.__profession}," \
               f"salary: {self.__salary}"

    """
    DEPARTMENT, PROFESSION, PATRONYMIC, SALARY setter, getter
    """

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, new_department):
        if isinstance(new_department, str):
            self.__department = new_department
        else:
            raise DoctorException("Department must be string")

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, new_profession):
        if isinstance(new_profession, str):
            self.__profession = new_profession
        else:
            raise DoctorException("Profession must be string")

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, new_patronymic):
        if isinstance(new_patronymic, str):
            self.__patronymic = new_patronymic
        else:
            raise DoctorException("Patronymic must be string")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, Money):
            self.__salary = new_salary
        else:
            raise DoctorException("Salary must be Money class")


# doc1 = Doctor(name='John', surname='Conor', age=34, gender="M", address="Palm Dail 1233",
#               department="Cardio", profession="surgeon", patronymic="Alan", salary=Money(12000, "usd"))
#
# doc2 = Doctor(name='Cris', surname='Peters', age=32, gender="M", address="Palm Dail 1666",
#               department="Cardio", profession="surgeon", patronymic="Rick", salary=Money(10000, "usd"))
#
# print(f"Create new Doctor: {doc1}")
# print(f"Create new Doctor: {doc2}")
# doc1.add_friend(doc2)
# print(f"Make {doc1.name} and {doc2.name} friends")
# print(f"show friends list of {doc2.name}: {doc2.friends}")
# doc1.salary = Money(13000, "eur")
# print(f"Set salary to new salary: {doc1.salary}")
