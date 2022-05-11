

"""
三次样条函数实现
"""

import numpy as np
import matplotlib.pyplot as plt

class Polynomial:

    def __init__(self, t1, t2, y1, y2, z1, z2):
        assert t2 > t1, "t2 > t1 needed..."
        self.z = (z1, z2)
        self.y = (y1, y2)
        self.t = (t1, t2)
        self.h = t2 - t1

    def __call__(self, x):
        if x < self.t[0] or x > self.t[1]:
            return 0.
        reduce1_t2_x = self.t[1] - x
        reduce1_x_t1 = x - self.t[0]

        return self.z[0] / (6 * self.h) * reduce1_t2_x ** 3 + \
                self.z[1] / (6 * self.h) * reduce1_x_t1 ** 3 + \
               (self.y[1] / self.h - self.z[1] * self.h / 6) * reduce1_x_t1 + \
               (self.y[0] / self.h - self.z[0] * self.h / 6) * reduce1_t2_x


class Spline3:

    def __init__(self, t, y):
        self.n = len(t) - 1
        assert len(y) == self.n + 1, "t and y not match"
        self.t = np.array(t, dtype=float)
        self.y = np.array(y, dtype=float)
        self.h = np.diff(t)
        assert np.all(self.h > 0), "Invalid t"
        self.b = np.diff(y) * 6 / self.h
        self.calc_z()  #计算z
        self.generate_splines()  #生成分段多项式函数

    def calc_z(self):
        u = []
        v = []
        z = [0.]
        u.append((self.h[0] + self.h[1]) / 2)
        v.append(self.b[1] - self.b[0])
        for i in range(1, self.n-1): #对角化
            u_i = 2 * (self.h[i] + self.h[i-1]) - \
                  self.h[i-1] ** 2 / u[-1]
            v_i = self.b[i] - self.b[i-1] - \
                  self.h[i-1] * v[i-1] / u[-1]
            u.append(u_i)
            v.append(v_i)
        z.append(v[-1] / u[-1])
        for i in reversed(range(self.n-2)): #计算解
            z.append((v[i] - self.h[i] * z[-1]) / u[i])
        z.append(0.)
        z.reverse()
        self.z = z
        return z

    def generate_splines(self):
        s = []
        for i in range(self.n):
            t1 = self.t[i]
            t2 = self.t[i+1]
            y1 = self.y[i]
            y2 = self.y[i+1]
            z1 = self.z[i]
            z2 = self.z[i+1]
            s.append(Polynomial(t1, t2, y1,
                                y2, z1, z2))
        self.s = s
        return s

    def __call__(self, x):
        def f(x):
            if x < self.t[0] or x > self.t[-1]:
                return 0.
            for item in self.s:
                result = item(x)
                if result:
                    return result
            raise ValueError("Something wrong happened...")

        if not hasattr(x, "__len__"):
            return f(x)
        else:
            y = []
            for item in x:
                y.append(f(item))
            return np.array(y)


    def plot(self):
        t = np.linspace(self.t[0], self.t[-1], 100)
        y = self(t)
        fig, ax = plt.subplots()
        ax.plot(t, y, "b--")
        ax.set(xlabel="x", ylabel="y")
        ax.scatter(self.t, self.y, color="red")
        plt.show()

