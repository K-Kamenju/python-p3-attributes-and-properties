#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        self._name = None
        self._job = None

        self.name = name
        self.job = job

    def get_name(self):
        print(self._name)
        return self._name
    
    def set_name(self, name):
        if (type(name) == str) and (1 < len(name) < 25):
            name_title_case = name.title()
            self._name = name_title_case
            print(name_title_case)
        else:
            error_message = "Name must be string between 1 and 25 characters."
            print(error_message)
            return error_message

    def get_job(self):
        print(self._job)
        return self._job
    
    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
            print(job)
        else:
            error_message ="Job must be in list of approved jobs."
            print(error_message)
            return error_message
    
    name = property(get_name, set_name,)
    job = property(get_job, set_job)


# test cases
x = Person()
x.name = 'ALI' # Invalid name, prints: "Name must be a string under 25 characters."
x.job = "" # Invalid name, prints:  "Job must be in list of approved jobs."

x.name = 'Guido'  # Valid name
x.job = 'Sales'  # Valid job