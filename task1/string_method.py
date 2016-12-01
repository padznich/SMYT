# string_method.py
def cut_s(s):

    try:

        splitted = s.split('(')
        if splitted[-1].find(')') >= 0:
            return s

        elif len(splitted) == 1:
            print 2, splitted
            return splitted[0]

        else:
            print 3, splitted
            return '('.join(splitted[:-1]).rstrip('(')

    # Type error handler
    except AttributeError:
        return "It must be a string."


if __name__ == "__main__":
    st = 'esdfd((esdf)(es)dsa(df'
    st = ""
    print cut_s(st)
