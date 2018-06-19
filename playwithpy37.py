""" new Python 3.7 features in one file based on
https://www.python.org/downloads/release/python-370rc1/
"""

# new modules in standard library
from dataclasses import dataclass, field, InitVar, asdict, \
    astuple, is_dataclass

# and new methods/types
from typing import ClassVar, Any, TypeVar, \
    Union, Generic, Any, Callable, Tuple, Dict, List


# uuid used to show how work default_factory - generator for default values of
# fields
import uuid

from collections import namedtuple

# dataclasses, fields
@dataclass(unsafe_hash=True, order=True, frozen=False)
class DataClassTest(object):
    # init variable what can be passed to the init

    # but will not become a field
    init_var: InitVar[Any]
    # any class variables with type annotation become fields(object fields)
    id_user: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
    name: str = field(compare=True, default=0)
    age: int = field(default=0)
    sex: str = field(default="f")
    children: tuple = field(compare=True, default=0)




    # to define class var with type annotation

    class_variable: ClassVar[int]

    # New magic method: __post_init__
    def __post_init__(self, init_var):
        """ this method will be called after __init__
        and it can't changed any fields in dataclass
        if it defined like frozen """

        print("Post Init. Oh, we got init_var: {}".format(init_var))

# init dataclass object

a = DataClassTest(init_var="random")

namedClass= namedtuple("iMJustTuple",["name"])
b = namedClass("Noname")
# dataclasses have additional methods
# what can be used only with dataclasses types,
# so before use them we need to check is this object is dataclassed
for item in [a, b]:
    if not is_dataclass(item):
        print("Oh, you are not cool dataclass, sorry: {}".format(
            item.__class__.__name__))
    else:
        # and if it dataclass we can do some useful things
        # asdict convert dataclass in json-like dict
        # example:
        #  {'id_user': UUID('c9bdf071-6ec3-419f-ae2c-9e62b34cd46b'),
        #  'name': 0, 'age': 0, 'sex': True, 'children': 0}
        print(asdict(item))


        # astuple, example:
        # (UUID('71cee640-04d5-497c-a8bd-702bfb13901e'), 0, 0, True, 0)
        print(astuple(item))


# default encoding in Python 3.7 if UTF-8
# and now we have coercion which mean what:
# if locale is POSIX "C" standard, assume UTF-8 encoding, not ASCII
# if you want to disable this - env variable:
# PYTHONCOERCECLOCALE=0

# PYTHONBREAKPOINT=pudb.set_trace - to use breakpoint() with pudb module
# or web-pdb PYTHONBREAKPOINT=web_pdb.set_trace()
#

from time import time_ns
# we can get now time with nano secs

print("Nanosec time: {}".format(time_ns()))


# example with type annotation for functions

pupilClass = namedtuple("Pupil", ["name", "sex"])

# create pupils objects
Jesica = pupilClass("Jesica", "f")
Frank = pupilClass("Frank", "m")

class SchoolClass(object):

    def __init__(self, pupils: List[pupilClass]) -> None:
        self.pupils = pupils

    def girls(self) -> List[pupilClass]:
        return [girl for girl in self.pupils if girl.sex == "f"]

classInSchool = SchoolClass([Jesica, Frank])

print(classInSchool.girls())
