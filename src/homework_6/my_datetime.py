from my_exceptions import TimeException, DateException


class Time:
    def __init__(self, h: int = 0, m: int = 0, s: int = 0):
        if isinstance((h, m, s), int):
            raise TimeException("Args Must be Int type")

        if h >= 24 or h < 0:
            raise TimeException(f"Hour must be in between 0 and 24, you passed: {h}")
        if m >= 60 or m < 0:
            raise TimeException(f"Minute must be in between 0 and 60, you passed: {m}")
        if s >= 60 or s < 0:
            raise TimeException(f"Second must be in between 0 and 60, you passed: {s}")
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __repr__(self):
        return f"{self.__hour}h/{self.__minute}m/{self.__second}s"

    def __add__(self, other: "Time"):
        new_time = Time(self.__hour, self.__minute, self.__second)
        new_time.add_second(other.__second)
        new_time.add_minute(other.__minute)
        new_time.add_hour(other.__hour)
        return new_time

    def __sub__(self, other: "Time"):
        new_time = Time(self.__hour, self.__minute, self.__second)
        new_time.sub_second(other.__second)
        new_time.sub_minute(other.__minute)
        new_time.sub_hour(other.__hour)
        return new_time

    def sub_second(self, s: int):
        self.__second -= s
        while self.__second < 0:
            self.__second += 60
            self.sub_minute(1)

    def sub_minute(self, m: int):
        self.__minute -= m
        while self.__minute < 0:
            self.__minute += 60
            self.sub_hour(1)

    def sub_hour(self, h: int):
        self.__hour = (self.__hour - h) % 24
        return (self.__hour - h) // 24

    def add_second(self, s: int):
        self.__second += s
        while self.__second >= 60:
            self.__second -= 60
            self.add_minute(1)

    def add_minute(self, m: int):
        self.__minute += m
        while self.__minute >= 60:
            self.__minute -= 60
            self.add_hour(1)

    def add_hour(self, h: int):
        self.__hour = (self.__hour + h) % 24
        return (self.__hour + h) // 24

    """
    HOUR MINUTE SECOND setter getter
    """

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, new_hour):
        if isinstance(new_hour, int) and 24 > new_hour >= 0:
            self.__hour = new_hour
        else:
            raise TimeException("Hour must be non-negative integer and less than 24")

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, new_minute):
        if isinstance(new_minute, int) and 60 > new_minute >= 0:
            self.__minute = new_minute
        else:
            raise TimeException("Minute must be non-negative integer and less than 60")

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, new_second):
        if isinstance(new_second, int) and 60 > new_second >= 0:
            self.__second = new_second
        else:
            raise TimeException("Second must be non-negative integer and less than 60")


class Date:
    def __init__(self, y: int = 0, m: int = 1, d: int = 1):
        if isinstance((y, m, d), int):
            raise DateException("Args Must be Int type")
        if y < 0:
            raise DateException(f"Year must be positive number, you passed {y}")
        if m > 12 or m < 1:
            raise DateException(f"Month must be in between 1 and 12, you passed {m}")
        max_day = self.days_in_month(m, y)
        if d > max_day or d < 1:
            raise DateException(f"Day must be in between 1 and {max_day}, you passed {d}")
        self.__year = y
        self.__month = m
        self.__day = d

    def __repr__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def __add__(self, other):
        new_date = Date(self.__year, self.__month, self.__day)
        new_date.add_day(other.__day)
        new_date.add_month(other.__month)
        new_date.add_year(other.__year)
        return new_date

    def __sub__(self, other):
        new_date = Date(self.__year, self.__month, self.__day)
        new_date.sub_day(other.__day)
        new_date.sub_month(other.__month)
        new_date.sub_year(other.__year)
        return new_date

    def sub_day(self, days):
        self.__day -= days
        while self.__day < 1:
            self.sub_month(1)
            self.__day += self.days_in_month(self.__month, self.__year)

    def sub_month(self, months):
        self.__month -= months
        while self.__month < 1:
            self.sub_year(1)
            self.__month += 12

    def sub_year(self, years):
        self.__year -= years

    def add_day(self, days):
        self.__day += days
        while self.__day > self.days_in_month(self.__month, self.__year):
            self.__day -= self.days_in_month(self.__month, self.__year)
            self.add_month(1)

    def add_month(self, months):
        self.__month += months
        while self.__day > self.days_in_month(self.__month, self.__year):
            self.__day -= self.days_in_month(self.__month, self.__year)
            self.__month += 1
        while self.__month > 12:
            self.__month -= 12
            self.add_year(1)

    def add_year(self, years):
        self.__year += years

    @staticmethod
    def check_int_tuple(t):
        for value in t:
            if not isinstance(value, int):
                return False
        return True

    @staticmethod
    def is_leap_year(year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    @staticmethod
    def days_in_month(month, year):
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if Date.is_leap_year(year):
                return 29
            else:
                return 28
        else:
            return 31

    """
    YEAR MONTH DAY setter getter
    """

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if isinstance(new_year, int) and new_year >= 0:
            self.__year = new_year
        else:
            raise DateException("Year must be integer non-negative integer")

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, new_month):
        if isinstance(new_month, int) and 12 >= new_month > 0:
            self.__month = new_month
        else:
            raise DateException("Month must be positive integer and less or equal than 12")

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, new_day):
        if isinstance(new_day, int) and self.days_in_month(self.__month, self.__year) > new_day > 0:
            self.__day = new_day
        else:
            raise DateException(f"Day must be positive integer and less than"
                                f" {self.days_in_month(self.__month, self.__year)}")


class DateTime:
    def __init__(self, year=0, month=1, day=1, hour=0, minute=0, second=0):
        self.__date = Date(year, month, day)
        self.__time = Time(hour, minute, second)

    def __repr__(self):
        return f"{self.__date.__repr__()} {self.__time.__repr__()}"

    def __add__(self, other: "DateTime"):
        new_date_time = DateTime()

        new_time = self.time
        new_time.add_second(other.time.second)
        new_time.add_minute(other.time.minute)
        extra_day = new_time.add_hour(other.time.hour)

        new_date = self.date
        new_date.add_day(extra_day)
        new_date.add_day(other.date.day)
        new_date.add_month(other.date.month)
        new_date.add_year(other.date.year)
        new_date_time.time, new_date_time.date = new_time, new_date

        return new_date_time

    def __sub__(self, other):
        new_date_time = DateTime()

        new_time = self.time
        new_time.sub_second(other.time.second)
        new_time.sub_minute(other.time.minute)
        extra_day = new_time.sub_hour(other.time.hour)

        new_date = self.date
        new_date.add_day(extra_day)
        new_date.sub_day(other.date.day)
        new_date.sub_month(other.date.month)
        new_date.sub_year(other.date.year)

        new_date_time.time, new_date_time.date = new_time, new_date

        if new_date_time.date.year < 0:
            raise DateException("Can't subtract lower date from bigger")
        return new_date_time

    """
    TIME DATE Setter Getter Properties
    """

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time_object: Time):
        if isinstance(time_object, Time):
            self.__time = time_object
        else:
            raise TimeException("Time must be Time type object")

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date_object: Date):
        if isinstance(date_object, Date):
            self.__date = date_object
        else:
            raise TimeException("Date must be Date type object")

    def add_year(self, y: int):
        self.date.add_year(y)

    def add_month(self, m: int):
        self.date.add_year(m)

    def add_day(self, d: int):
        self.date.add_day(d)

    def add_hour(self, h: int):
        self.time.add_hour(h)

    def add_minute(self, m: int):
        self.time.add_minute(m)

    def add_second(self, s: int):
        self.time.add_second(s)

    def sub_year(self, y: int):
        self.date.sub_year(y)

    def sub_month(self, m: int):
        self.date.sub_year(m)

    def sub_day(self, d: int):
        self.date.sub_day(d)

    def sub_hour(self, h: int):
        self.time.sub_hour(h)

    def sub_minute(self, m: int):
        self.time.sub_minute(m)

    def sub_second(self, s: int):
        self.time.sub_second(s)


# date1 = DateTime(2000, 2, 21, 1)
# date2 = DateTime(1968, 1, 1, 23)
# print(f"date1: {date1}, date2: {date2}")
# print(f"date1 - date2: {date1 - date2}")
# date1.date = Date(2000, 2, 12)
# print(f"Change date1.date to: {date1.date}")
# date1.add_year(100)
# print(f"Add date1 100 year: {date1.date}")
