

class ParserFailure(Exception):
    pass


def str2vector(line, expected=3, skip=1, delim=" "):
    """Parses a vector out of a string."""

    try:
        return tuple(map(float, line.strip().split(delim)[skip:])[:expected])
    except:
        raise ParserFailure("str2vector tripped on a line.")
