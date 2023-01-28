from my_datetime import Date
from person_job_company import Person
from city import City
from my_exceptions import UniversityException

class University:
    def __init__(self, name: str, founded_at: Date, rector: Person, city: City):
        if not isinstance(name, str):
            raise UniversityException("University name must be string")
        if not isinstance(founded_at, Date):
            raise UniversityException("University founding date must be Date class")
        if not isinstance(rector, Person):
            raise UniversityException("University rector must be Person class")
        if not isinstance(city, City):
            raise UniversityException("City of university must be City class")

        self.__name = name
        self.__founded_at = founded_at
        self.__rector = rector
        self.__city = city

    def __repr__(self):
        return f"{self.__name} University, founded at: {self.__founded_at.year} in {self.__city.name}. " \
               f"Current rector: {self.__rector.name_surname}"

    """
    NAME, FOUNDED AT, RECTOR, CITY setter, getter
    """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise UniversityException("Name must be string")

    @property
    def year(self):
        return self.__founded_at

    @year.setter
    def year(self, new_date: Date):
        if isinstance(new_date, Date):
            self.__founded_at = new_date
        else:
            raise UniversityException("Founding year must be Date type")

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, new_rector: Person):
        if isinstance(new_rector, Person):
            self.__rector = new_rector
        else:
            raise UniversityException("Rector must be Person type")

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city: City):
        if isinstance(new_city, City):
            self.__city = new_city
        else:
            raise UniversityException("City must be City type")


# mayor1 = Person(name="John", surname="Simens", age=60, gender="M", address="Cambridge 24/44")
# city1 = City(name="Cambridge", founded_at=Date(1600), mayor=mayor1, population=30000000, language="English")
# rector1 = Person(name="Adam", surname="Johns", age=50, gender="M", address="San Marino 55/88")
# uni1 = University(name="Harvard", founded_at=Date(1800), rector=rector1, city=city1)
#
# print(uni1)
