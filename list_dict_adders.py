from abc import ABC, abstractmethod


class Adder(ABC):

    def __init__(self, data):
        self.data = data

    def __add__(self, other_data):
        return self.add(other_data)

    @abstractmethod
    def add(self, other_data):
        raise NotImplementedError


class ListAdder(Adder):

    def add(self, other_list):
        for entry in self.data:
            yield entry
        for entry2 in other_list:
            yield entry2


class DictAdder(Adder):

    def add(self, other_dict):
        for entry in self.data.items():
            yield entry
        for entry2 in other_dict.items():
            yield entry2
