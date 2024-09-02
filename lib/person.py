#!/usr/bin/env python3

class Person:

    approved_jobs = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General"
    ]

    def __init__(self, name="Unknown", job="Unknown"):
        self._name = None  # Initialize _name to None
        self._job = None  # Initialize _job to None
        self.name = name
        if self._name is not None:  # Only set job if name is valid
            self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert name to title case
        else:
            self._name = None  # Ensure _name is None if invalid
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
