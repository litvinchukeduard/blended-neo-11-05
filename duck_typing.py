from collections import UserString

# class MyUserString:

#     def __init__(self, seq):
#         if isinstance(seq, str):
#             self.data = seq
#         elif isinstance(seq, UserString):
#             self.data = seq.data[:]
#         else:
#             self.data = str(seq)

#     def __str__(self):
#         return str(self.data)

#     def __repr__(self):
#         return repr(self.data)

#     def __int__(self):
#         return int(self.data)

#     def __float__(self):
#         return float(self.data)

#     def __complex__(self):
#         return complex(self.data)

#     def __hash__(self):
#         return hash(self.data)

#     def __getnewargs__(self):
#         return (self.data[:],)

#     def __eq__(self, string):
#         if isinstance(string, UserString):
#             return self.data == string.data
#         return self.data == string

#     def __lt__(self, string):
#         if isinstance(string, UserString):
#             return self.data < string.data
#         return self.data < string

#     def __le__(self, string):
#         if isinstance(string, UserString):
#             return self.data <= string.data
#         return self.data <= string

#     def __gt__(self, string):
#         if isinstance(string, UserString):
#             return self.data > string.data
#         return self.data > string

#     def __ge__(self, string):
#         if isinstance(string, UserString):
#             return self.data >= string.data
#         return self.data >= string

#     def __contains__(self, char):
#         if isinstance(char, UserString):
#             char = char.data
#         return char in self.data

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, index):
#         return self.__class__(self.data[index])

#     def __add__(self, other):
#         if isinstance(other, UserString):
#             return self.__class__(self.data + other.data)
#         elif isinstance(other, str):
#             return self.__class__(self.data + other)
#         return self.__class__(self.data + str(other))

#     def __radd__(self, other):
#         if isinstance(other, str):
#             return self.__class__(other + self.data)
#         return self.__class__(str(other) + self.data)

#     def __mul__(self, n):
#         return self.__class__(self.data * n)

#     __rmul__ = __mul__

#     def __mod__(self, args):
#         return self.__class__(self.data % args)

#     def __rmod__(self, template):
#         return self.__class__(str(template) % self)

#     # the following methods are defined in alphabetical order:
#     def capitalize(self):
#         return self.__class__(self.data.capitalize())

#     def casefold(self):
#         return self.__class__(self.data.casefold())

#     def center(self, width, *args):
#         return self.__class__(self.data.center(width, *args))

#     def count(self, sub, start=0, end=_sys.maxsize):
#         if isinstance(sub, UserString):
#             sub = sub.data
#         return self.data.count(sub, start, end)

#     def removeprefix(self, prefix, /):
#         if isinstance(prefix, UserString):
#             prefix = prefix.data
#         return self.__class__(self.data.removeprefix(prefix))

#     def removesuffix(self, suffix, /):
#         if isinstance(suffix, UserString):
#             suffix = suffix.data
#         return self.__class__(self.data.removesuffix(suffix))

#     def encode(self, encoding='utf-8', errors='strict'):
#         encoding = 'utf-8' if encoding is None else encoding
#         errors = 'strict' if errors is None else errors
#         return self.data.encode(encoding, errors)

#     def endswith(self, suffix, start=0, end=_sys.maxsize):
#         return self.data.endswith(suffix, start, end)

#     def expandtabs(self, tabsize=8):
#         return self.__class__(self.data.expandtabs(tabsize))

#     def find(self, sub, start=0, end=_sys.maxsize):
#         if isinstance(sub, UserString):
#             sub = sub.data
#         return self.data.find(sub, start, end)

#     def format(self, /, *args, **kwds):
#         return self.data.format(*args, **kwds)

#     def format_map(self, mapping):
#         return self.data.format_map(mapping)

#     def index(self, sub, start=0, end=_sys.maxsize):
#         return self.data.index(sub, start, end)

#     def isalpha(self):
#         return self.data.isalpha()

#     def isalnum(self):
#         return self.data.isalnum()

#     def isascii(self):
#         return self.data.isascii()

#     def isdecimal(self):
#         return self.data.isdecimal()

#     def isdigit(self):
#         return self.data.isdigit()

#     def isidentifier(self):
#         return self.data.isidentifier()

#     def islower(self):
#         return self.data.islower()

#     def isnumeric(self):
#         return self.data.isnumeric()

#     def isprintable(self):
#         return self.data.isprintable()

#     def isspace(self):
#         return self.data.isspace()

#     def istitle(self):
#         return self.data.istitle()

#     def isupper(self):
#         return self.data.isupper()

#     def join(self, seq):
#         return self.data.join(seq)

#     def ljust(self, width, *args):
#         return self.__class__(self.data.ljust(width, *args))

#     def lower(self):
#         return self.__class__(self.data.lower())

#     def lstrip(self, chars=None):
#         return self.__class__(self.data.lstrip(chars))

#     maketrans = str.maketrans

#     def partition(self, sep):
#         return self.data.partition(sep)

#     def replace(self, old, new, maxsplit=-1):
#         if isinstance(old, UserString):
#             old = old.data
#         if isinstance(new, UserString):
#             new = new.data
#         return self.__class__(self.data.replace(old, new, maxsplit))

#     def rfind(self, sub, start=0, end=_sys.maxsize):
#         if isinstance(sub, UserString):
#             sub = sub.data
#         return self.data.rfind(sub, start, end)

#     def rindex(self, sub, start=0, end=_sys.maxsize):
#         return self.data.rindex(sub, start, end)

#     def rjust(self, width, *args):
#         return self.__class__(self.data.rjust(width, *args))

#     def rpartition(self, sep):
#         return self.data.rpartition(sep)

#     def rstrip(self, chars=None):
#         return self.__class__(self.data.rstrip(chars))

#     def split(self, sep=None, maxsplit=-1):
#         return self.data.split(sep, maxsplit)

#     def rsplit(self, sep=None, maxsplit=-1):
#         return self.data.rsplit(sep, maxsplit)

#     def splitlines(self, keepends=False):
#         return self.data.splitlines(keepends)

#     def startswith(self, prefix, start=0, end=_sys.maxsize):
#         return self.data.startswith(prefix, start, end)

#     def strip(self, chars=None):
#         return self.__class__(self.data.strip(chars))

#     def swapcase(self):
#         return self.__class__(self.data.swapcase())

#     def title(self):
#         return self.__class__(self.data.title())

#     def translate(self, *args):
#         return self.__class__(self.data.translate(*args))

#     def upper(self):
#         return self.__class__(self.data.upper())

#     def zfill(self, width):
#         return self.__class__(self.data.zfill(width))


class Duck:
    def quack(self):
        print('Quack!')

    def swim(self):
        print('Duck is swimming!')


class Person:
    def quack(self):
        print('This person is quacking!')

    def swim(self):
        print('This person is swimming!')


duck_one = Duck()
person_one = Person()
duck_two = Duck()
person_two = Person()

ducks = [duck_one, person_one, duck_two, person_two]
for duck in ducks:
    duck.quack()
    duck.swim()
