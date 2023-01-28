from person_job_company import Person
from my_datetime import Date
from my_exceptions import CityException


class City:
    def __init__(self, name: str, founded_at: Date, mayor: Person, population: int, language: str):
        if not isinstance(name, str):
            raise CityException("City name must be string")
        if not isinstance(founded_at, Date):
            raise CityException("City founding date must be Date class")
        if not isinstance(mayor, Person):
            raise CityException("City mayor must be Person class")
        if not isinstance(population, int) or population < 0:
            raise CityException("City population must be non-negative integer")
        if not isinstance(language, str):
            raise CityException("City language must be string")
        self.__name = name
        self.__founded_at = founded_at
        self.__mayor = mayor
        self.__population = population
        self.__language = language

    def __repr__(self):
        return f"The {self.__name} city, founded at {self.__founded_at}, current mayor is {self.__mayor.name_surname}," \
               f" with population of {self.__population} people. Official language is {self.__language}"

    """
    NAME, FOUNDING YEAR, MAYOR, POPULATION, LANGUAGE setter getter
    """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise CityException("Name must be string")

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, new_founded_at):
        if isinstance(new_founded_at, Date):
            self.__founded_at = new_founded_at
        else:
            raise CityException("Founding date must be Date class")

    @property
    def mayor(self):
        return self.__mayor

    @mayor.setter
    def mayor(self, new_mayor):
        if isinstance(new_mayor, Person):
            self.__mayor = new_mayor
        else:
            raise CityException("Mayor name must be Person class")

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, new_population):
        if isinstance(new_population, int) and new_population >= 0:
            self.__population = new_population
        else:
            raise CityException("Population must be non-negative integer")

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language):
        if isinstance(new_language, str):
            self.__language = new_language
        else:
            raise CityException("language must be string")


# mayor1 = Person(name="Hayk", surname="Marutyan", age=45, gender="M", address="Hyusisayin st. 23")
# city1 = City(name="Yerevan", founded_at=Date(100, 1, 1), mayor=mayor1, population=1800000, language="Armenian")
# print(f"New City: {city1}")
# city1.population = 1000000
# print(f"Changed population to {city1.population}")
