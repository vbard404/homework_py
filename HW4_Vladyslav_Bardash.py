from operator import itemgetter
# Task 1
a = 32.34341
b = 12
try:
    print('a/b = ', a/b)
except:
    if b == 0:
        print('ZeroDivisionError', ZeroDivisionError)
    else:
        print('TypeError: ', TypeError)
# Task 2
cars = [{"brand": "ford", "model": "MusTAng Gt500", "year": 2018},
        {"brand": "ZAZ", "model": "Fortza", "year": 2001},
        {"brand": "VW", "model": "Golf GTI", "year": 1999}]

# Sorted list by year key
cars_sorted = sorted(cars, key=itemgetter('year'))
print(cars_sorted)

for d in cars_sorted:
    if d['brand'].istitle():  # Check if brand is in title or uppercase
        continue
    elif d['brand'].isupper():
        pass
    else:
        d['brand'] = d['brand'].title()
    # Split value in 2 elements to edit per selected word
    d["model"] = str(d["model"]).split()
    if len(d['model']) == 2:
        d['model'][1] = d['model'][1].upper()
    d['model'][0] = d['model'][0].title()
    d['model'] = ' '.join(map(str, d['model']))  # Joined back into string

print(cars_sorted)
