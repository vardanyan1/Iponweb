from person_job_company import Person
from typing import Dict
from datetime import datetime, timedelta
from my_exceptions import DoctorException, PatentException


class Patient(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, address: str = ""):
        super().__init__(name, surname, age, gender, address)
        if self.age < 18:
            raise "Age must be between 18 and 100"

    def __repr__(self):
        return f"{self.name_surname} - {self.gender}, {self.age} years old."

    def __ne__(self, other: "Patient"):
        if not isinstance(other, Patient):
            raise PatentException("Can check equality only between Patient classes")
        if self.name_surname != other.name_surname or self.age != other.age or \
                self.gender != other.gender or self.address != other.address:
            return True
        else:
            return False

    def __eq__(self, other: "Patient"):
        # if not isinstance(other, Patient):
        #     raise PatentException("Can check equality only between Patient classes")
        if self.name_surname != other.name_surname or self.age != other.age or \
                self.gender != other.gender or self.address != other.address:
            return False
        else:
            return True


class Doctor(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, address: str = "",
                 schedule: Dict[datetime, Patient] = None):
        super().__init__(name, surname, age, gender, address)
        if schedule:
            if not isinstance(schedule, Dict):
                raise DoctorException("Schedule must be Dict class")
            if not all(isinstance(item, datetime) for item in schedule.keys()):
                raise DoctorException("Schedule items must be DateTime class")
            if not all(isinstance(item, Patient) for item in schedule.values()):
                raise DoctorException("Schedule items must be Patient class")
            self.__schedule = schedule
        else:
            self.__schedule = {}

    def __repr__(self):
        schedule_str = '\n'.join([f"{k}: {v.name_surname}" for k, v in self.__schedule.items()])
        return f"Doctor {self.name_surname} schedule:\n{schedule_str}"

    def register_patient(self, datetime_book: datetime, patient: Patient):
        if not isinstance(patient, Patient):
            raise DoctorException("Patient must be Patient class object")
        if not isinstance(datetime_book, datetime):
            raise DoctorException("Booked date must be datetime class object")

        if patient in self.__schedule.values():
            raise DoctorException(f"Patient:{patient.name_surname} already registered")

        if self.is_free(datetime_book):
            self.__schedule[datetime_book] = patient
            print(f"Patient {patient} successfully registered at {datetime_book}")
        else:
            print(f"Doctor is not free")

    def is_free(self, datetime_book: datetime):
        for key in self.__schedule.keys():
            if key + timedelta(minutes=30) >= datetime_book >= key:
                return False
            else:
                return True

    def is_registered(self, patient: Patient):
        for other_pat in self.__schedule.values():
            if patient == other_pat:
                return True
        return False


def patient_doc():
    patient1 = Patient("Artur", "Sargsyan", 19, "M")
    patient2 = Patient("Anna", "Margaryan", 19, "F")
    patient3 = Patient("Ashot", "Margaryan", 22, "M")
    doctor1 = Doctor("Karen", "Makunc", 45, 'M', schedule={datetime(2020, 2, 12, 12, 40): patient1})
    doctor1.register_patient(datetime(2020, 2, 13, 12, 40), patient3)
    doctor1.register_patient(datetime(2020, 2, 12, 13, 20), patient2)
    print(f"Is registered: {doctor1.is_free((datetime(2020, 2, 12, 12, 55)))}")
    print(doctor1)
    print(f"Is registered: {doctor1.is_registered(patient2)}")
    # print(doctor1)


patient_doc()
