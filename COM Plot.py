# Brooks Brickley & Hector Hernandez CC: 2019
import matplotlib.pyplot as plt
name = input('What is the name of the file you want to open? : ') + '.csv'

file = open(name, 'r')

data = []
firstline = file.readline()
nextline = file.readline()

while nextline != '':
    data.append(nextline.split(','))
    nextline = file.readline()

time = []
px = []
py = []
vx = []
vy = []

for i in range(len(data)):
    time.append(float(data[i][0])/1000)
    px.append(float(data[i][1])/100)
    py.append(float(data[i][2])/100)
    vx.append(float(data[i][3])/100)
    vy.append(float(data[i][4])/100)

ax1 = plt.subplot(2, 2, 1)
ax1.plot(time, px, 'r-')
ax1.set(ylabel='Position (m)')
ax1.set(xlabel='Time (s)')
ax1.set_ylim(.5, 1)
ax1.set_title('Position of COM in X Direction')

ax2 = plt.subplot(2, 2, 2)
ax2.plot(time, py, 'y-')
ax2.set(ylabel='Position (m)')
ax2.set(xlabel='Time (s)')
ax2.set_ylim(.5, 1)
ax2.set_title('Position of COM in Y Direction')

ax3 = plt.subplot(2, 2, 3)
ax3.plot(time, vx, 'r-')
ax3.set(ylabel='Velocity (m/s)')
ax3.set(xlabel='Times (s)')
ax3.set_title('Velocity of COM in X Direction')

ax4 = plt.subplot(2, 2, 4)
ax4.plot(time, vy, 'y-')
ax4.set_ylim(-.008,.008)
ax4.set(xlabel='Velocity (m/s)')
ax4.set(ylabel='Time (s)')
ax4.set_title('Velocity of COM in Y Direction')

plt.suptitle('Position and Velocity of COM')
plt.show()
