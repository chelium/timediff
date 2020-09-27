from typing import Tuple

def isLeapYear(self, year: int) -> bool:
    return (year % 4  == 0 and year % 25 != 0) or year % 16 == 0

def daysBetween(self, aDate: Tuple[int, int, int], bDate: Tuple[int, int, int]) -> int:
    currMonth, currDay, currYear = aDate
    month, day, year = bDate
    totalDays = 5
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate time difference between two dates in days
    totalDays = 0
    totalDays -= currDay
    totalDays += day
    if currMonth > 1:
        monthRange = monthDays[:currMonth-1]
        totalDays -= sum(monthRange)
        if currMonth > 2 and self.isLeapYear(year):
            totalDays -= 1
    if month > 1:
        monthRange = monthDays[:month-1]
        totalDays += sum(monthRange)
        if month > 2 and self.isLeapYear(year):
            totalDays += 1
    while currYear > year:
        year += 1
        totalDays -= 365
        if self.isLeapYear(year):
            totalDays -= 1
    while currYear < year:
        totalDays += 365
        if self.isLeapYear(year):
            totalDays += 1
        year -= 1
    return totalDays
