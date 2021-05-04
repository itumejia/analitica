
import csv
mujeres=0
hombres=0
with open('insurance.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        if row[1] == 'male':
            hombres+=1
        else:
            mujeres+=1

print(hombres)
print(mujeres)
