#!#!/usr/bin/env python3
import datetime

class Kalendar(object):
    def __init__(self):
        self.elements = {}

    def _getKey(self, date):
        return date.strftime("%Y-%m-%d")

    def addElement(self, element, date):
        theDate = self.elements.setdefault(self._getKey(date), [])
        theDate.append(element)

    def addNow(self, element):
        self.addElement(element, datetime.datetime.now())

    def getAllElements(self, date=None):
        if date is not None:
            key = self._getKey(date)
            return self.elements.setdefault(key, [])
        else:
            return self.elements

if __name__ == "__main__":
    pass
