from Tempeature_Module import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    MODULE_VERSION,
)
from random import uniform
import datetime

c=[uniform(15,40) for i in range(4)]  # 4 floating point element between 15 and 40 is stored in c


#every element in list of celcius is converted using map
print(f'''
Temperature Report - {datetime.date.today()}
Temperature in Celcius - {c}
Temperature in Fahrenheit - {list(map(celsius_to_fahrenheit,c))}  
MODULE VERSION - {MODULE_VERSION}
''')







