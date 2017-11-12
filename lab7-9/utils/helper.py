def dateValidation(date):
    '''
    Validates a date
    :param date:
    :return: None if the date is correct, else returns a list with errors
    '''
    errors = []
    try:
        day, month, year = getDate(date)
        if day < 1 or day > 31:
            errors.append("The day must be between 1 and 31")
        if month < 1 or month > 12:
            errors.append("The month must be between 1 and 12")
        if year < 2010 or year > 2050:
            errors.append("The year must be between 2010 and 2050")
        return errors
    except ValueError:
        errors.append("Date format incorrect!")
        return errors
    except IndexError:
        errors.append("Date format incorrect!")
        return errors



def getDate(date):
    '''
    gets a date from a string if it exists
    :param date:
    :return: int values day, month, year if they are correct
    '''
    date.split("/")
    day = int(date[0])
    day = day * 10 + int(date[1])
    month = int(date[3])
    month = month * 10 + int(date[4])
    year = int(date[6])
    year = year * 10 + int(date[7])
    year = year * 10 + int(date[8])
    year = year * 10 + int(date[9])
    return day, month, year


def hourValidation(hour):
    '''
    Validates if an hour is correct
    :param hour:
    :return: None if the hour is correct else returns erros
    '''
    errors = []
    try:
        hh, mm = getHour(hour)
        if hh < 1 or hh > 24:
            errors.append("The hour must be an integer between 1 and 24")
        if mm < 0 or mm > 59:
            errors.append("The minute must be an integer between 0 and 59")
        return errors
    except ValueError:
        errors.append("The hour format is incorrect!")
        return errors
    except IndexError:
        errors.append("The hour format is incorrect!")
        return errors

def getHour(hour):
    '''
    gets hour from a string if it exists
    :param hour:
    :return: two values hh, mm representing the hour and the minute
    '''
    hour.split(":")
    hh = int(hour[0])
    hh = hh * 10 + int(hour[1])
    mm = int(hour[3])
    mm = mm * 10 + int(hour[4])

    return hh, mm
