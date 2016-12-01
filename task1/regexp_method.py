# regexp_method.py
import re


def cut(s):
    '''Returns only covered text'''

    try:
        pattern = r"(.*\))*(\w*)(\(*\w*)"
        if re.match(pattern, s).group(1):
            return re.match(pattern, s).group(1) + re.match(pattern, s).group(2)
        elif re.match(pattern, s).group(2):
            return re.match(pattern, s).group(2)
        elif re.match(pattern, s).group(3):
            return ""

    # Type error handler
    except TypeError:
        return "It must be a string."

    # optional
    else:
        if s == '(':
            return ''
        else:
            return s


if __name__ == "__main__":
    st = 'esdfd((esdf)(es)dsa(df'
    print cut(st)
