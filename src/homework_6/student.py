from my_exceptions import StudentException
from my_datetime import Date
from person_job_company import Person
from university import University
from city import City

class Student(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, address: str, university: University,
                 faculty: str, course: int, started_year: Date):
        super().__init__(name, surname, age, gender, address)
        if not isinstance(university, University):
            raise StudentException("University must be University class")
        if not isinstance(faculty, str):
            raise StudentException("Faculty must be string")
        if not isinstance(course, int) or course >= 0:
            raise StudentException("Course must be non-negative integer")
        if not isinstance(started_year, Date):
            raise StudentException("Starting year must be Date class")
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__started_year = started_year

    def __repr__(self):
        return f"{self.name_surname}, studying at {self.__university.name} university"\
               f" on {self.__faculty} faculty from {self.__started_year.year}."

    """
    UNIVERSITY, FACULTY, COURSE, STARTED YEAR setter, getter
    """

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, new_university):
        if isinstance(new_university, University):
            self.__university = new_university
        else:
            raise StudentException("University must be University class")

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, new_faculty):
        if isinstance(new_faculty, str):
            self.__faculty = new_faculty
        else:
            raise StudentException("Faculty must be string")

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, new_course):
        if isinstance(new_course, str):
            self.__course = new_course
        else:
            raise StudentException("Course must be integer")

    @property
    def started_at(self):
        return self.__started_year


# mayor1 = Person(name="John", surname="Simens", age=60, gender="M", address="Cambridge 24/44")
# city1 = City(name="Cambridge", founded_at=Date(1600), mayor=mayor1, population=30000000, language="English")
# rector1 = Person(name="Adam", surname="Johns", age=50, gender="M", address="San Marino 55/88")
# uni1 = University(name="Harvard", founded_at=Date(1800), rector=rector1, city=city1)
#
#
# student1 = Student(name="Eren", surname="Yeger", age=22, gender="M", address="San Paolo 36/99", university=uni1,
#                    faculty="Physics", course=4, started_year=Date(2020))
#
# print(student1)
