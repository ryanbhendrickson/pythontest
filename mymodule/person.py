from enum import Enum

__all__ = ['Person']

EXAMPLE_ARGS = [
    ('Ryan', 'Hendrickson', 'MALE'),
    ('Anthony', 'Hendrickson', 'MALE'),
    ('John', 'Doe', 'MALE'),
    ('Jane', 'Doe', 'FEMALE'),
]

class Person(object):

    class Gender(Enum):
        MALE = 'M'
        FEMALE = 'F'

    def __init__(self, first_name: str, last_name: str, gender: Gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def __repr__(self):
        return '{name} ({gender})'.format(name=self.full_name, gender=self.gender.value)

    @property
    def full_name(self):
        return '{fname} {lname}'.format(fname=self.first_name, lname=self.last_name)

    @classmethod
    def provide_definition():
        return 'People are just humans. Plain and simple.'
