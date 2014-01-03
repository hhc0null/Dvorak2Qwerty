#!/usr/bin/python2

__qwerty_keys = tuple("1234567890-=\\`qwertyuiop[]asdfghjkl;'zxcvbnm,./")+tuple("!@#$%^&*()_+|~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>? ")
__dvorak_keys = tuple("1234567890[]\\`',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz")+tuple("!@#$%^&*(){}|~\"<>PYFGCRL?+AOEUIDHTNS_:QJKXBMWVZ ")
qwerty_dvorak_table = dict(zip(__qwerty_keys, __dvorak_keys))
dvorak_qwerty_table = dict(zip(__dvorak_keys, __qwerty_keys))

def q2d(strings):
    """Convert a string typed in Qwerty to Dvorak"""
    if strings[-1] == '\n':
        strings = strings[:-1]
    __qwerty_to_dvorak = lambda c: qwerty_dvorak_table[c]
    return "".join(map(__qwerty_to_dvorak, list(strings)))

def d2q(strings):
    """Convert a string typed in Dvorak to Qwerty"""
    if strings[-1] == '\n':
        strings = strings[:-1]
    __dvorak_to_qwerty = lambda c: dvorak_qwerty_table[c]
    return "".join(map(__dvorak_to_qwerty, list(strings)))


if __name__ == '__main__':
    import shlex
    from sys import argv, exit, stdin, stdout

    __version__ = """ 1.0.0 """
    __author__ = "dvorakqwerty"+str(__version__)+"""(https://github.com/)
Author: Matsukuma Hiroki (a.k.a. hhc0null) <dev.hhc0null@gmail.com>"""
    __usage__ = """Usage:
    [stdin]|./dvorakqwerty.py [Convert options]
    ./dvorakqwerty.py [Misc options]
CONVERT:
    -d: Convert a string typed in Dvorak to Qwerty. (without newline charactors)
    -q: Convert a string typed in Qwerty to Dvorak. (without newline charactors)
MISC:
    -v: Print version number. 
    -h: Print this help summary page.

EXAMPLES:
    % echo "Jrbk.py a oypcbi yfl.e cb EKRPAT yr "<>PYF"|./dvorakqwerty.py -q
    Convert a string typed in DVORAK to QWERTY
    % echo "jRBK>PY A OYPCBI YFL>E CB ekrpat YR ',.pyf"|./dvorakqwerty.py -q
    cONVERT A STRING TYPED IN dvorak TO qwerty"""

    def print_usage():
        print __author__
        print __usage__
        exit(0)

    def print_version():
        print __author__
        exit(0)

    argc = len(argv)

    if argc != 2 :
        print_usage()
    else:
        if argv[1] == '-h':
            print_usage()
        elif argv[1] == '-v':
            print_version()
        elif argv[1] == '-d':
            stdout.write(q2d(stdin.read()))
        elif argv[1] == '-q':
            stdout.write(d2q(stdin.read()))
        else:
            print "Error!"

