import re
from datetime import datetime
from time import mktime, gmtime


def countryUri(x):
    "Return a URI for a country given its name."
    import re

    x = re.sub('[^A-Za-z0-9]+', '', x)
    return x.lower()


def toTitleCaseIfUpper(x):
    "Return the string in title case if it is all upper, otherwise leave capitalization alone."
    x = x.strip()
    if x.isupper():
        return x.title()
    else:
        return x


def nonWhitespace(x):
    "Return the string removing all spaces."
    import re

    y = re.sub(r'\s+', '', x.strip())
    return y


def toTitleCaseCleaned(x):
    "Return the string in title case cleaning spaces."
    import re

    y = re.sub(r'\s+', ' ', x.strip())
    return y.title()


def asciiChars(x):
    "Remove non-ascii chars in x replacing consecutive ones with a single space"
    import re

    return re.sub(r'[^\x00-\x7F]+', ' ', x)


def alphaNumeric(x):
    "Replace consecutive non-alphanumeric bya single space"
    return re.sub('[^A-Za-z0-9]+', ' ', x)


def numericOnly(x):
    "Remove non-numeric chars from the string x"
    return re.sub('[^0-9]+', '', x)


def alphaOnly(x):
    "Remove non-alphabetic chars from the string x"
    return re.sub('[^A-Za-z]+', '', x)


def md5Hash(x):
    "Return md5 hash of x"
    import hashlib

    return hashlib.md5(x).hexdigest()


def iso8601date(date, format="%Y-%m-%d %H:%M:%S %Z"):
    """Convert a date to ISO8601 date format

input format: YYYY-MM-DD HH:MM:SS GMT (works less reliably for other TZs)
or            YYYY-MM-DD HH:MM:SS.0
or            YYYY-MM-DD
or            MM/DD/YY
or            epoch (13 digit, indicating ms)
or            epoch (10 digit, indicating sec)
output format: iso8601

"""

    try:
        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S %Z").isoformat()
    except Exception:
        pass

    try:
        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S.0").isoformat()
    except:
        pass

    try:
        return datetime.strptime(date, "%Y-%m-%d").isoformat()
    except:
        pass

    try:
        return datetime.strptime(date, "%m/%d/%y").isoformat()
    except:
        pass

    try:
        date = int(date)
        if 1000000000000 < date and date < 9999999999999:
            # 13 digit epoch
            return datetime.fromtimestamp(mktime(gmtime(date / 1000))).isoformat()
    except:
        pass

    try:
        date = int(date)
        if 1000000000 < date and date < 9999999999:
            # 10 digit epoch
            return datetime.fromtimestamp(mktime(gmtime(date))).isoformat()
    except:
        pass
    # If all else fails, return input
    return date


def clean_localite(x):
    "Clean the localite field of data-ebola-public"
    clean = x = x.strip()
    clean = re.sub('[\(\)]+', '', x)
    clean = clean.replace(" and ", ", ")
    clean = clean.replace(" ", "")
    return clean
