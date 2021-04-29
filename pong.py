import numpy as np
import random as rd
import statistics as st
import matplotlib.pyplot as plt
import pylab as py
import statsmodels.api as sm
data=np.random.normal(0,1,1000)
class project:
    def __init__(self,data):
        self.data=data

    def tinh_mean(self, data):
        mean = np.mean(data)
        return mean

    def mean(self):
        gttb = self.tinh_mean(self.data)
        return gttb

    def tinh_med(self,data):
        med = np.median(data)
        return med
    def med(self):
        gttv = self.tinh_med(self.data)
        return gttv

    def tinh_mod(self, data):
        mod = st.mode(data)
        return mod

    def mod(self):
        mode = self.tinh_mod(data)
        return mode

    def tinh_max(self, data):
        max = np.max(data)
        return max

    def max(self):
        mx = self.tinh_max(self.data)
        return mx

    def tinh_min(self, data):
        min = np.min(data)
        return min

    def min(self):
        mn = self.tinh_min(self.data)
        return mn

    def tinh_quantile(self, q):
        quantiles = np.quantile(self.data, q)
        return quantiles

    def quantile(self, q):
        percentile = self.tinh_quantile(q)
        return percentile

    def hist_draw(self, data):
        plt.hist(data, bins=200, color="pink")

    def hist(self):
        self.hist_draw(self.data)

    def qq_plot(self):
        sm.qqplot(self.data, line='45')
        plt.show()

    pass

proj=project(data)
print("mean = ", proj.mean())
print("median =", proj.med())
print("mode =", proj.mod())
print("max =", proj.max())
print("min =", proj.min())
print("quantile (0.02) =", proj.quantile(0.02))
proj.hist()
proj.qq_plot()


   