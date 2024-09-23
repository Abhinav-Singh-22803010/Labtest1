import numpy as np
import scipy.signal as sgl
import matplotlib.pyplot as plt

               

def avgveh(graph):
    arr = np.array(0)
    for i in range(24):
        av = sum(graph[60*i: 60*(i+1)]) / 60
        
        arr = np.append(arr, np.array(av))
        
        
    return arr
            

vehicle_count = np.random.randint(1, 100, 1440)
noise = np.random.randint(0, 25, 1440)
vehicle_count = vehicle_count + noise
x = np.arange(1, 1441)
plt.plot(x, vehicle_count, label="vehicles/minute")
plt.legend()
plt.show()

cutoff = 40/1440
newsig = sgl.butter(2, cutoff, btype="lowpass")
smoothsig = sgl.filtfilt(newsig[0], newsig[1], vehicle_count)
plt.plot(x, smoothsig, label="smooth vehicles/minute")
plt.legend()
plt.show()

xn = np.arange(1, 24)
plt.plot(xn, avgveh(smoothsig)[1:24], label="avg vehicle/hour")
plt.legend()
plt.show()
