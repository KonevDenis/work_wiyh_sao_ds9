import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import numpy as np
# import astropy
def summ(a, b):
    V = a + b
    W = V*2
    return W
print(summ(4, 5))
summ = 0
print(summ)

hdulist = pyfits.open("C:/v523cas60s-001.fit")
#hdulist.info()
#exp = hdulist[0].header['exptime']
#print(exp)
#obj = hdulist[0].header['object']
#print(obj)
#print(hdulist[0].header[:10])
scidata = hdulist[0].data
#print(scidata[0])
print(scidata[1036][1092])
Y_value = scidata[1962][440:454]
X_value = []
for i in range(440,454):
    X_value.append(i)
print(Y_value)
print(X_value)
hdulist.close()
fig = plt.figure()  # создали область Figure
ax = fig.add_subplot(111)
fig.set_facecolor('yellow')
ax.set(facecolor = 'blue')
ax.set_title("Заголовок")
ax.set_xlabel('ось абцис (XAxis)')
ax.set_ylabel('ось ординат (YAxis)')
ax.plot(X_value, Y_value, color = 'pink', linewidth = 5)
#plt.show()
scidata = np.transpose(scidata)
Y1_value = scidata[446][1956:1968]    #1954:1970
X1_value = []
for i in range(1956,1968):
    X1_value.append(i)
print(X1_value)
print(Y1_value)
fig1 = plt.figure()  # создали область Figure
ax1 = fig1.add_subplot(111)
fig.set_facecolor('yellow')
ax1.set(facecolor = 'blue')
ax1.set_title("Заголовок")
ax1.set_xlabel('ось абцис (XAxis)')
ax1.set_ylabel('ось ординат (YAxis)')
ax1.plot(X1_value, Y1_value, color = 'pink', linewidth = 5)
plt.show()