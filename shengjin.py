# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/21 18:30
@Auth ： KajiMaCN
@File ：shengjin.py
@IDE ：PyCharm
"""
import numpy as np


class Shengjin:
    def compute(self, a, b, c, d):
        A, B, C = self.discriminant_param(a, b, c, d)
        if A == 0 and B == 0:
            X_1 = -b / 3 * a
            X_2 = -c / b
            X_3 = -3 * d / c
        else:
            delta = self.discriminant(A, B, C)
            if delta > 0:
                Y_1 = A * b + 3 * a * ((-B + np.sqrt((B ** 2) - 4 * A * C)) / 2)
                Y_2 = A * b + 3 * a * ((-B - np.sqrt((B ** 2) - 4 * A * C)) / 2)
                X_1 = (-b - (np.cbrt(Y_1) + np.cbrt(Y_2))) / (3 * a)
                real = (-2 * b + np.cbrt(Y_1) + np.cbrt(Y_2)) / (6 * a)
                virtual = ((np.sqrt(3) * (np.cbrt(Y_1) - np.cbrt(Y_2))) / (6 * a)) * 1j
                X_2 = real + virtual
                X_3 = real - virtual
            elif delta == 0:
                K = B / A
                X_1 = -b / a + K
                X_2 = X_3 = -K / 2
            else:
                T = (2 * A * b - 3 * a * B) / (2 * np.sqrt(A ** 3))
                theta = np.arccos(T)
                X_1 = (-b - 2 * np.sqrt(A) * np.cos(theta / 3)) / (3 * a)
                X_2 = (-b + np.sqrt(A) * (np.cos(theta / 3) + np.sqrt(3) * np.sin(theta / 3))) / (3 * a)
                X_3 = (-b + np.sqrt(A) * (np.cos(theta / 3) - np.sqrt(3) * np.sin(theta / 3))) / (3 * a)
        return X_1, X_2, X_3

    @staticmethod
    def discriminant_param(a, b, c, d):
        A = b ** 2 - 3 * a * c
        B = b * c - 9 * a * d
        C = c ** 2 - 3 * b * d
        return A, B, C

    @staticmethod
    def discriminant(A, B, C):
        delta = B ** 2 - 4 * A * C
        return delta


if __name__ == '__main__':
    a, b, c, d = 1, 8, 16, 10
    shengjin = Shengjin()
    x1, x2, x3 = shengjin.compute(a, b, c, d)
    print(f'x1:{x1} x2:{x2} x3:{x3}')
