def compare_date_with_heute(heute, enddate):
    """
    :param heute: Das heutige Datum geschrieben im Format YYYY-MM-ZZ
    :param enddate: Das Enddatum einer Reservierung geschrieben im Format ZZ/MM/YYYY

    Die Methode vergleicht die zwei Daten und returniert 1, falls 'enddate' grosser ist als 'heute'. Andernfalls, returniert
    die Methode den Wert 0
    """
    day1,month1,year1 = date_split_heute(str(heute))
    day2,month2,year2 = date_split(enddate)
    if year1 > year2:
        return 0
    elif year2 > year1:
        return 1
    else:
        if month1 > month2:
            return 0
        elif month2 > month1:
            return 1
        else:
            if day1 > day2:
                return 0
            elif day2 > day1:
                return 1
            else:
                return 0

def compare_two_dates(date1,date2):
    """
    :param date1: Ein erstes Datum geschrieben im Format ZZ/MM/YYYY
    :param date2: Ein zweites Datum geschrieben im Format ZZ/MM/YYYY

    Die Methode vergleicht die zwei Daten und returniert 1, falls 'date2' grosser ist als 'date1'. Andernfalls, returniert
    die Methode den Wert 0
    """
    day1, month1, year1 = date_split(date1)
    day2, month2, year2 = date_split(date2)
    if year1 > year2:
        return 0
    elif year2 > year1:
        return 1
    else:
        if month1 > month2:
            return 0
        elif month2 > month1:
            return 1
        else:
            if day1 > day2:
                return 0
            elif day2 > day1:
                return 1
            else:
                return 0

def date_split(date):
    """
    :param date: Ein Datum geschrieben im Format ZZ/MM/YYYY

    Die Methode spaltet das Datum in mehrere Teile und returniert das Jahr, die Monat und den Tag die in dem Datum vorkommen
    """
    p = date.split('/')
    day = int(p[0])
    month = int(p[1])
    year = int(p[2])
    return day,month,year

def date_split_heute(heute):
    """
    :param heute: Ein Datum geschrieben im Format YYYY-MM-ZZ

    Die Methode spaltet das Datum in mehrere Teile und returniert das Jahr, die Monat und den Tag die in dem Datum vorkommen
    (am meisten wird diese Methode mit dem heutigen Datum benutzt)
    """
    p = heute.split('-')
    year = int(p[0])
    month = int(p[1])
    day = int(p[2])
    return day,month,year
