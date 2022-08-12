# load cargraph data from json file

from json import loads, dumps
from pathlib import Path
from datetime import datetime
from car import *

contents = Path('cargraph.json').read_text()
cg = loads(contents)
cars = []


def parse_date(s):
    input_format = '%m/%d - %H:%M'
    return datetime.strptime(s, input_format).replace(year=2018)


for car in cg[1:]:
    try:
        row = CarForSale(int(car[1]), float(car[3]), float(car[4]), parse_date(car[6]), car[2], car[5], car[7], car[8])
        cars.append(row)
    except:
        pass
average_prius = sum(cars, CarForSale.zero()) * (1 / len(cars))
print(average_prius.__dict__)
