# https://bugs.python.org/issue32505

from typing import List
from dataclasses import dataclass, field


def foo():
    return List[int]


@dataclass
class C:
    mylist: foo() = field(default_factory=list)


print('asfdass')
c = C()
c.mylist += [1, 2, 3]
print(c)
