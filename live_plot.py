
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['instance']
    y1 = data["speed"]
    y2 = data['rpm']
    y3 = data['engine_load']
    y4 = data['coolant_temp']
    y5 = data['throttle']

    plt.cla()

    plt.plot(x, y1, label='SPEED')
    plt.plot(x, y2, label='RPM')
    plt.plot(x, y3, label='ENGINE_LOAD')
    plt.plot(x, y4, label='COOLANT_TEMPERATURE')
    plt.plot(x, y5, label='THROTTLE_PERCENT')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
