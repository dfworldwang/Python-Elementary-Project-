


d = {'Amy': 45, 'Bob': 50, 'Cathy': 62, 'David': 45,
     'Eason': 63, 'Fred': 78}

# Invert the Key, Value pairs

d2 = {v:k for k, v in d.items()}

print(d2)


e = {'foo': 1, 'bar': 2, '123abc': 3}
print(e)

e2 = dict(e, foo = 555, abc = 999)
print(e2)

k = ['foo', 'bar']; v = [101, 102]
e3 = dict(zip(k, v), abc = 999)
print(e3)
