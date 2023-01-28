from my_exceptions import MyRangeException

class MyRange:
    def __init__(self, current: int, end: int, step: int = 1):
        if isinstance((current, end, step), int):
            raise MyRangeException("Arguments must be integer")
        if step > 0 and current >= end:
            raise MyRangeException(f"Current can't be bigger than end when step is positive")
        elif step < 0 and current <= end:
            raise MyRangeException(f"Current can't be smaller than end when step is negative")
        self.__current = current
        self.__end = end
        self.__step = step

    def __repr__(self):
        return f"MyRange with current state: {self.__current}, end: {self.__end} and step: {self.__step}"

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.__current <= self.__end and self.__step > 0:
            self.__current += self.__step
            return self.__current - self.__step
        elif self.__current >= self.__end and self.__step < 0:
            self.__current += self.__step
            return self.__current - self.__step
        else:
            raise StopIteration

    def __len__(self) -> int:
        length = 0
        if self.__step > 0:
            while self.__current + length * self.__step <= self.__end:
                length += 1
        else:
            while self.__current + length * self.__step >= self.__end:
                length += 1
        return length

    def __getitem__(self, item) -> int:
        if not isinstance(item, int) or (item > len(self) or item < -len(self)):
            raise MyRangeException("Item must be in range")
        if len(self) > item >= 0:
            return self.__current + item * self.__step
        elif -len(self) <= item < 0:
            return self.__current + (len(self) + item) * self.__step

    def __reversed__(self) -> "MyRange":
        return MyRange(self.__end, self.__current, -self.__step)

    """
    CURRENT END STEP setter getter
    """

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, new_current):
        if isinstance(new_current, int):
            if (self.__step > 0 and new_current <= self.__end) or (self.__step < 0 and new_current >= self.__end):
                self.__current = new_current
            else:
                raise MyRangeException(f"Current must be {'bigger' if self.__step < 0 else 'smaller'} than end")
        else:
            raise MyRangeException("Current must be integer")

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, new_end):
        if isinstance(new_end, int):
            if (self.__step > 0 and new_end >= self.__current) or (self.__step < 0 and new_end <= self.__current):
                self.__end = new_end
            else:
                raise MyRangeException(f"End must be {'bigger' if self.__step > 0 else 'smaller'} than current")
        else:
            raise MyRangeException("End must be integer")

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, new_step):
        if isinstance(new_step, int):
            if (self.__step < 0 and new_step < 0) or (self.__step > 0 and new_step > 0):
                self.__step = new_step
            else:
                raise MyRangeException("New step must be same sign as the old one.")
        else:
            raise MyRangeException("Step must be integer")


a = MyRange(1, 4, 1)
b = reversed(a)
print(f"a: {a}\nb: {b}")
b.current = 10
print(f"Change state of b to: {b.current}")
print(f"Get b end: {b.end}")
print(f"Get b length: {len(b)}")
print(f"Get last item: {a[-1]}")
print(f"Get length: {len(a)}")
print(f"a: {[i for i in b]}")
print(f"b: {[i for i in a]}")
