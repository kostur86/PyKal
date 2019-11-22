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
        return date.strftime("%Y-%m-%d %H:%M:%S")

    def add_element(self, element, date):
        """
        Add element to exact date
        """
        full_date = self._get_key(date)
        the_date = full_date.split()[0]

        element = [element]

        elem = Query()
        results = self.db.search(elem.key.matches(the_date))
        if results:
            for result in results:
                self.db.remove(doc_ids=[result.doc_id])
                element += result["value"]

        print("DEBUG: Adding new element to database: {} - {}".format(
            full_date, element))
        self.db.insert({'key': full_date, 'value': element})

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
            elem = Query()
            results = self.db.search(elem.key.matches(key))
            return results

        return self.db.all()

    def get_all_day_elements(self, date=None):
        """
        Return all elements from exact day.
        """
        if date is None:
            date = datetime.datetime.now()

        key = self._get_key(date)
        key = key.split()[0]

        elem = Query()
        results = self.db.search(elem.key.matches(key))

        return results


if __name__ == "__main__":
    pass
