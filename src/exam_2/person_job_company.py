from typing import List
# from my_datetime import Date
# from my_exceptions import PersonException, CompanyException, JobException
from money import Money
from my_exceptions import PersonException

class Person:
    def __init__(self, name: str, surname: str, age: int, gender: str, address: str,
                 friends: List["Person"] = None, job: List["Job"] = None):
        if not isinstance(name, str):
            raise PersonException("Surname must be string")
        if not isinstance(surname, str):
            raise PersonException("Name must be string")
        if not isinstance(age, int) or age < 0 or age > 99:
            raise PersonException("Age must be non-negative integer")
        if not isinstance(gender, str) or gender not in ["M", "F"]:
            raise PersonException("Gender must be string M for Male or F for Female")
        if not isinstance(address, str):
            raise PersonException("Address must be string")
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__age = age
        self.__address = address
        if friends:
            if not isinstance(friends, List):
                raise PersonException("Friends must be list objects")
            self.__friends = []
            for fr in friends:
                if not isinstance(fr, Person):
                    raise PersonException("Friend must be Person class")
                self.add_friend(fr)
        else:
            self.__friends = []
        if job:
            if not isinstance(job, List):
                raise PersonException("Jobs must be list objects")
            self.__job = []
            for jb in job:
                if not isinstance(jb, Job):
                    raise PersonException("Job must be Job class")
                self.add_job(jb)
        else:
            self.__job = []

    def __repr__(self):
        return f"{self.__name} {self.__surname}, age: {self.__age}, gender: {self.__gender}," \
               f"address: {self.__address}"

    """
    NAME, SURNAME,NAME AND SURNAME, AGE, GENDER, ADDRESS, FRIENDS, JOB getter setter
    """

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise PersonException("Name must be string")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        if isinstance(new_surname, str):
            self.__surname = new_surname
        else:
            raise PersonException("Surname must be string")

    @property
    def name_surname(self):
        return self.__name + " " + self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age >= 0:
            self.__age = new_age
        else:
            raise PersonException("Age must be non-negative integer")

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, new_gender):
        if isinstance(new_gender, str) and new_gender in ["M", "F"]:
            self.__gender = new_gender
        else:
            raise PersonException("Gender must be string M or F")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        if isinstance(new_address, str):
            self.__address = new_address
        else:
            raise PersonException("Address must be string")

    @property
    def friends(self):
        return [i.name_surname for i in self.__friends]

    @property
    def job(self):
        return [i.company.name for i in self.__job]

    def add_friend(self, new_friend: "Person"):
        if not isinstance(new_friend, Person):
            raise PersonException("Friend must be Person class")
        if new_friend not in self.__friends:
            self.__friends.append(new_friend)
            if self not in new_friend.__friends:
                new_friend.add_friend(self)
        else:
            raise PersonException(f"""{self.__name} and {new_friend.__name} are already friends.""")

    def remove_friend(self, rm_friend: "Person"):
        if not isinstance(rm_friend, Person):
            raise PersonException("Friend must be Person class")
        if rm_friend in self.__friends:
            self.__friends.remove(rm_friend)
            if self in rm_friend.__friends:
                rm_friend.remove_friend(self)
        else:
            raise PersonException(f"{self.__name} and {rm_friend.__name} are not friends.")

    def add_job(self, new_job: "Job"):
        if not isinstance(new_job, Job):
            raise PersonException("New Job must be Job class")
        if new_job not in self.__job:
            self.__job.append(new_job)
            new_job.company.employee_count += 1
        else:
            raise PersonException(f"New job is already in jobs")

    def remove_job(self, rm_job: "Job"):
        if not isinstance(rm_job, Job):
            raise PersonException("Job must be Job class")
        if rm_job in self.__job:
            self.__job.remove(rm_job)
            rm_job.company.employee_count -= 1
        else:
            raise PersonException(f"Job must be in jobs")


# class Company:
#     def __init__(self, company_name: str, founded_at: Date, employees_count: int = 0):
#         if not isinstance(company_name, str):
#             raise CompanyException("Company name must be string")
#         if not isinstance(founded_at, Date):
#             raise CompanyException("Company founding dare must be Date class")
#         if not isinstance(employees_count, int) or employees_count < 0:
#             raise CompanyException("Company employee count must be non-negative integer")
#         self.__company_name = company_name
#         self.__founded_at = founded_at
#         self.__employees_count = employees_count
#
#     def __repr__(self):
#         return f"company name: {self.__company_name}, founded at: {self.__founded_at}," \
#                f"employees count: {self.__employees_count}"
#
#     """
#     COMPANY NAME, COMPANY FOUNDING YEAR, EMPLOYEE COUNT setter getter
#     """
#
#     @property
#     def name(self):
#         return self.__company_name
#
#     @name.setter
#     def name(self, new_name):
#         if isinstance(new_name, str):
#             self.__company_name = new_name
#         else:
#             raise CompanyException("Company name must be string")
#
#     @property
#     def founding_year(self):
#         return self.__founded_at
#
#     @founding_year.setter
#     def founding_year(self, new_founding_year):
#         if isinstance(new_founding_year, Date):
#             self.__founded_at = new_founding_year
#         else:
#             raise CompanyException("Founding date must be Date class")
#
#     @property
#     def employee_count(self):
#         return self.__employees_count
#
#     @employee_count.setter
#     def employee_count(self, new_emp_count):
#         if isinstance(new_emp_count, int) and new_emp_count >= 0:
#             self.__employees_count = new_emp_count
#         else:
#             raise CompanyException("Employee count must be non-negative integer")
#
#
# class Job:
#     def __init__(self, company: Company, salary: Money, experience_year: int, position: str):
#         if not isinstance(company, Company):
#             raise JobException("Company must be Company class")
#         if not isinstance(salary, Money):
#             raise JobException("Salary must be Money class")
#         if not isinstance(experience_year, int) or experience_year < 0:
#             raise JobException("Experience year must be non-negative integer")
#         if not isinstance(position, str):
#             raise JobException("Position name must be string")
#         self.__company = company
#         self.__salary = salary
#         self.__experience_year = experience_year
#         self.__position = position
#
#     def __repr__(self):
#         return f"company: {self.__company.name}, salary: {self.__salary}, experience year:" \
#                f"{self.__experience_year}, position: {self.__position}"
#
#     """
#     COMPANY, SALARY, EXPERIENCE YEAR, POSITION getter
#     """
#
#     @property
#     def company(self):
#         return self.__company
#
#     @company.setter
#     def company(self, new_company: Company):
#         if isinstance(new_company, Company):
#             self.__company = new_company
#         else:
#             raise JobException("Company must be Company class")
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, new_selay):
#         if isinstance(new_selay, Money):
#             self.__salary = new_selay
#         else:
#             raise JobException("Salary must be Money class")
#
#     @property
#     def experience_year(self):
#         return self.__experience_year
#
#     @experience_year.setter
#     def experience_year(self, new_exp_year):
#         if isinstance(new_exp_year, int) and new_exp_year >= 0:
#             self.__experience_year = new_exp_year
#         else:
#             raise JobException("Experience year must be non-negative int")
#
#     @property
#     def position(self):
#         return self.__position
#
#     @position.setter
#     def position(self, new_position):
#         if isinstance(new_position, str):
#             self.__position = new_position
#         else:
#             raise JobException("Position must be string")


# c1 = Company(company_name="Pepsi", founded_at=Date(1913))
# c2 = Company(company_name="Apple", founded_at=Date(1960))
# c3 = Company(company_name="Facebook", founded_at=Date(1910))
# j1 = Job(company=c1, salary=Money(5000, "eur"), experience_year=5, position="CTO")
# j2 = Job(company=c1, salary=Money(3000, "eur"), experience_year=5, position="CMO")
# j3 = Job(company=c1, salary=Money(8000, "eur"), experience_year=2, position="CEO")
# j4 = Job(company=c2, salary=Money(9000, "usd"), experience_year=4, position="CTO")
# j5 = Job(company=c3, salary=Money(140000, "rub"), experience_year=2, position="CMO")
# j6 = Job(company=c3, salary=Money(200000, "rub"), experience_year=4, position="CEO")
# p1 = Person(name="Sam", surname='Smith', age=38, gender='M', address="add1", job=[j1, j4])
# p2 = Person(name="John", surname='Watt', age=28, gender='F', address="add2", friends=[p1], job=[j5])
# p3 = Person(name="Will", surname='Black', age=19, gender='M', address="add3", friends=[p2], job=[j2])
# p4 = Person(name="Alan", surname='Jonson', age=22, gender='F', address="add4", friends=[p1], job=[j6])
# p5 = Person(name="Dan", surname='Brown', age=29, gender='M', address="add5", friends=[p3, p2])
#
# print(f"Jobs of p4({p4.name_surname}): {p4.job}")
# print(f"Employee count for c2({c2.name}): {c2.employee_count}")
# print(f"List of p1({p1.name_surname}) friends: {p1.friends}")
# p4.add_friend(p2)
# print(f"p4({p4.name_surname}) and p2({p2.name_surname}) are now friends")
# print(f"List of p4({p4.name_surname}) friends: {p4.friends}")
