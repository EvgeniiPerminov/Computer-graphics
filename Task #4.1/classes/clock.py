import time
import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt
from tools.tools import  draw_number


class Clock():
    def __init__(self, digits, tr_steps, third_order_bezier_steps,
                 n_segments, size,  clock_color, digits_color):

        self.digits = digits
        self.size = size
        self.clock_color = clock_color
        self.digits_color = digits_color

        self.xdelta = self.size[0] // 6
        self.ydelte = self.size[1] // 2
        self.xindent = self.size[0] // 12


        self.fig = plt.figure()
        self.dial = np.zeros((size[1], size[0], 3), dtype=np.uint8)
        self.im = plt.imshow(self.dial, animated=True)

        self.tr_steps = tr_steps
        self.n_segments = n_segments
        self.third_order_bezier_steps = third_order_bezier_steps

        self.tr_counter = np.full(6, self.tr_steps, dtype=np.int32)
        self.time = self.convert_time(self.get_time())

    @staticmethod
    def get_time():
        return time.strftime("%H%M%S", time.localtime())

    @staticmethod
    def convert_time(t):
        return np.array(list(map(int, list(t))), dtype=np.int32)


    def clear_dial(self):
        self.dial[:, :] = self.clock_color

    def draw_numbers(self, digits):
        self.clear_dial()
        for i in range(6):
            draw_number(digits[i], self.n_segments, self.digits_color, self.dial, self.third_order_bezier_steps)


    def mechanism(self):
        cur_time = self.convert_time(self.get_time())
        self.bool_check = cur_time != self.time
        self.tr_counter[self.bool_check] = 0

        self.time = cur_time
        self.cur_digits = []

        for i, num in enumerate(cur_time):
            delta = np.array([self.xindent + i * self.xdelta, self.ydelte])

            if self.tr_counter[i] == self.tr_steps:
                self.cur_digits.append(self.digits[num, 0] + delta)

            else:
                self.cur_digits.append(self.digits[(num - 1) % 10, self.tr_counter[i]] + delta)
                self.tr_counter[i] += 1

        self.draw_numbers(self.cur_digits)
        self.im.set_array(self.dial)

    def update_clock(self, par):
        self.mechanism()
        return self.im,

    # Функция старта часов
    def start(self):
        ani = animation.FuncAnimation(self.fig, self.update_clock,  save_count=0, repeat=False, blit=True, interval=1)
        plt.show()



