
from itertools import chain

class PrintableList(list):
    # for a list of dicts
    def __str__(self):
        return '. '.join(' '.join(str(x) for x in
            chain.from_iterable(zip((item[0], 'is', 'and'), item[1])))
                for item in (item.items()[0] for item in self)) + '.'

class Foo(object):
    def __init__(self):
        self.l = PrintableList([{"Susan": ("Boyle", 50, "alive")},
                                {"Albert": ("Speer", 106, "dead")}])

#     def __getattribute__(self, name):
#         return PrintableList(l)
#         attr = super(Foo, self).__getattribute__(name)
#         items = sum([x.items() for x in attr], [])
#         return ' '.join([' '.join([k, v[0], 'is', str(v[1]), 'and', v[2] + '.']) for k, v in items])


f = Foo()
print(f.l)


