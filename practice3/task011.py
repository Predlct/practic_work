
import math

data_input = input('Введите стороны треугольника:\n')

data = data_input.split()

result1 = math.acos((int(data[1])**2 + int(data[2])**2 - int(data[0])**2)/(2*int(data[1])*int(data[2])))*57.2958

result2 = math.acos((int(data[0])**2 + int(data[2])**2 - int(data[1])**2)/(2*int(data[0])*int(data[2])))*57.2958

result3 = math.acos((int(data[1])**2 + int(data[0])**2 - int(data[2])**2)/(2*int(data[1])*int(data[0])))*57.2958


print(f'Угол a = {result1:.0f} градусов')

print(f'Угол b = {result2:.0f} градусов')

print(f'Угол a = {result3:.0f} градусов')
