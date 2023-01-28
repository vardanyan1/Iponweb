from my_exceptions import TeacherException
from my_datetime import Date
from money import Money
from person_job_company import Person
from university import University
from city import City

class Teacher(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, address: str, university: University,
                 faculty: str, experience: int, started_year: Date, subject: str, salary: Money):
        super().__init__(name, surname, age, gender, address)
        if not isinstance(university, University):
            raise TeacherException("University must be University class")
        if not isinstance(faculty, str):
            raise TeacherException("Faculty must be string")
        if not isinstance(experience, int) or experience < 0:
            raise TeacherException("Experience must be non-negative integer")
        if not isinstance(started_year, Date):
            raise TeacherException("Starting Year must be Date class")
        if not isinstance(subject, str):
            raise TeacherException("Subject must be string")
        if not isinstance(salary, Money):
            raise TeacherException("Salary must be Money class")
        self.__university = university
        self.__faculty = faculty
        self.__experience = experience
        self.__started_year = started_year
        self.__subject = subject
        self.__salary = salary

    def __repr__(self):
        return f"{'Mr.' if self.gender == 'M' else 'Ms.'} {self.name_surname}, working at {self.__faculty} faculty"\
               f" of {self.__university.name} university from {self.__started_year.year}. Salary: {self.__salary}"

    """
    UNIVERSITY, FACULTY, EXPERIENCE, STARTED YEAR, SUBJECT, SALARY setter, getter
    """

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, new_university: University):
        if isinstance(new_university, University):
            self.__university = new_university
        else:
            raise TeacherException("University must be University class")

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, new_faculty: str):
        if isinstance(new_faculty, str):
            self.__faculty = new_faculty
        else:
            raise TeacherException("Faculty must be string")

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, new_experience: int):
        if isinstance(new_experience, int) and new_experience >= 0:
            self.__experience = new_experience
        else:
            raise TeacherException("Experience must be non-negative integer")

    @property
    def started_work_at(self):
        return self.__started_year

    @property
    def subject(self):
        return self.__subject

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary: Money):
        if isinstance(new_salary, Money):
            self.__salary = new_salary
        else:
            raise TeacherException("Salary must be Money class")


mayor1 = Person(name="John", surname="Siemens", age=60, gender="M", address="Cambridge 24/44")
city1 = City(name="Cambridge", founded_at=Date(1600), mayor=mayor1, population=30000000, language="English")
rector1 = Person(name="Adam", surname="Johns", age=50, gender="M", address="San Marino 55/88")
uni1 = University(name="Harvard", founded_at=Date(1800), rector=rector1, city=city1)

teacher1 = Teacher(name="Sam", surname="Rogers", age=60, gender="M", address="San Andreas 55/88", university=uni1,
                   faculty="Economics", experience=40, started_year=Date(1960), subject="Macroeconomics",
                   salary=Money(48000, "usd"))

# print(teacher1)
