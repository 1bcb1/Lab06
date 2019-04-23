# Brooks Brickley & Hector Hernandez CC: 2019
from statistics import mean
from math import sqrt
before = input('What is the name of the before file? : ') + '.csv'
after = input('What is the name of the after file? : ') + '.csv'

beforeID = open(before, 'r')

data = []
firstline = beforeID.readline()
nextline = beforeID.readline()

while nextline != '':
    data.append(nextline.split(','))
    nextline = beforeID.readline()

bvx = []
bvy = []
for i in range(len(data)):
    bvx.append(float(data[i][0])/100)
    bvy.append(float(data[i][1])/100)

afterID = open(after, 'r')

data = []
firstline = afterID.readline()
nextline = afterID.readline()

while nextline != '':
    data.append(nextline.split(','))
    nextline = afterID.readline()

avx = []
avy = []
for i in range(len(data)):
    avx.append(float(data[i][0])/100)
    avy.append(float(data[i][1])/100)

magnitude_before = sqrt((mean(bvx))**2 + (mean(bvy))**2)
magnitude_after = sqrt((mean(avx))**2 + (mean(avy))**2)

radius1 = float(input('What is the radius from the point tracked to the center of mass in cm? : ')) / 100
radius2 = float(input('What is the distance of the 20-gram mass from the center of mass in cm? : ')) /100

w_before = magnitude_before/radius1
w_after = magnitude_after/radius1
I_weight = 2.34 * 10 ** -6
mass = 20/1000

Interia = abs(((I_weight + mass * radius2 ** 2) * w_after) / (w_before - w_after))

print('The moment of inertia of the board is', Interia)
