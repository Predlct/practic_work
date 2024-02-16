
from math import pi

result = abs((int(input('Радиус слепой зоны\n'))**2 - int(input('Радиус дальности приема\n'))**2)) * pi

print(result)