#!/usr/bin/env python3
"""
Module providing basic calendar API.
"""

import datetime
from tinydb import TinyDB, Query


class Kalendar():
    """
    Callendar class for PyKal
    """

    def __init__(self):
        self.elements = {}
        self.db = TinyDB('database/elements.json')

    @staticmethod
    def _get_key(date):
        """
        Return time key
        """
        return date.strftime("%Y-%m-%d")

    def add_element(self, element, date):
        """
        Add element to exact date
        """
        the_date = self.elements.setdefault(self._get_key(date), [])
        the_date.append(element)

        elem = Query()
        results = self.db.search(elem.key == the_date)
        for result in results:
            if result['value'] == element:
                break
        else:
            print("DEBUG: Adding new element to database: {} - {}".format(
                the_date, element))
            self.db.insert({'key': the_date, 'value': element})

    def add_now(self, element):
        """
        Add elemnent for today
        """
        self.add_element(element, datetime.datetime.now())

    def get_all_elements(self, date=None):
        """
        Return all elements
        """
        if date is not None:
            key = self._get_key(date)
            return self.elements.setdefault(key, [])

        return self.elements


if __name__ == "__main__":
    pass
