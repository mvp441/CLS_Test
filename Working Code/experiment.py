#from commonFunctions import checkForEvironmentVariablePYEPICS_LIBCA
import functools
import matplotlib.pyplot as plt
import time
from epics import caget, PV
import datetime
import numpy as np
import pandas as pd

#Name of PVs in pyEpics from archiver.or
PV_BPM_x = 'BPM1402-04:TruncatedTbTDataX' #BPM tbt in horizontal x
PV_BPM_y = 'BPM1402-04:TruncatedTbTDataY' #BPM tbt in Vertical y
PV_tuneY = 'QFF:tuneFB:ytune:waveform:tune'
PV_tuneX = 'QFF:tuneFB:xtune:waveform:tune'

pvnamelist = {PV_BPM_x, PV_BPM_y }
df = pd.DataFrame(columns=pvnamelist)
datetime.datetime.now()

#try:
    #dfx = caget('BPM1402-04:TruncatedTbTDataX')
#except Exception:
#    print(Exception.message)

#dfy = caget('BPM1402-04:TruncatedTbTDataY')

# save file names
test_filename = "../Data/BPM1402-04_Data.txt"
x_filename = "../Data/420MVP441BPM140204X.txt"
y_filename = "../Data/420MVP441BPM140204Y.txt"

# initialize lists for data
dft = []
dfx1 = []
dfy1 = []

# open save files and read data into lists
ft = open(test_filename, 'r')
dft = ft.read().split()[2:]
ft.close()
fx = open(x_filename, 'r')
for x in fx:
    dfx1.append(x.replace("\n",""))
fx.close()
fy = open(y_filename, 'r')
for y in fy:
    dfy1.append(y.replace("\n",""))
fy.close()

# convert string lists to integer arrays
dft2 = np.asarray(dft, dtype=float)
dfx2 = np.asarray(dfx1, dtype=int)
dfy2 = np.asarray(dfy1, dtype=int)

# calculate fourier transforms
dft3 = np.fft.fft(dft2)
dft3r = np.fft.rfft(dft2)
dfx3 = np.fft.fft(dfx2)

# create x arrays for plotting data
t0 = np.linspace(0, len(dft)-1, len(dft))
ts = np.linspace(0, len(dfx1)-1, len(dfx1))
tr = np.linspace(0, len(dft3r)-1, len(dft3r))

# calculate max value
ymax = max(dft3r)
xmax = dft3r.argmax()
print("max value is: " + str(dft3r[xmax]))

df = {'PV_BPM_x':dfx1, 'PV_BPM_y':dfy1}
the_now = datetime.datetime.now()
print(the_now.strftime('%Y-%m-%d_%H-%M-%S'))

# save raw data
filenamex = 'TuneChange_x' + the_now.strftime('%Y-%m-%d_%H-%M-%S') + '.csv'  # or .txt
filenamey = 'TuneChange_y' + the_now.strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
#np.savetxt(r'BPM140204X.txt', dfx*1e6, fmt='%d')
#np.savetxt(r'BPM140204Y.txt', dfy*1e6, fmt='%d')
print('Data Saved, Done!')

# plot x data and fourier transforms
f1 = plt.figure(1)
f1.clear()
af1 = f1.add_subplot(311)
plt.title("BPM1402-04_Data")
af1.plot(t0, dft2)
af2 = f1.add_subplot(312)
plt.title("BPM1402-04_Data Fast Fourier Transform")
af2.plot(t0, dft3)
af3 = f1.add_subplot(313)
plt.title("BPM1402-04_Data Real Fourier Transform")
af3.plot(tr, dft3r)
plt.draw()
filename1 = 'FTs' + the_now.strftime('%Y-%m-%d_%H-%M-%S')
#plt.savefig(filename1)
plt.show(block = False)

# plot (zoomed in) x and y data
f2 = plt.figure(2)
f2.clear()
bf1 = f2.add_subplot(311)
plt.title("BPM140204X Data")
bf1.plot(ts, dfx2)
bf2 = f2.add_subplot(312)
plt.title("BPM140204Y Data (first 350 points)")
#bf2.set_xlim([0, 100])
bf2.plot(ts[:250], dfx2[:250])
bf3 = f2.add_subplot(313)
plt.title("BPM140204Y Data")
bf3.plot(ts, dfy2)
plt.draw()
filename2 = 'X_and_Y' + the_now.strftime('%Y-%m-%d_%H-%M-%S')
#plt.savefig(filename2)
plt.show(block = False)

# plot x vs y data
f3 = plt.figure(3)
f3.clear()
cf1 = f3.add_subplot(121)
plt.title("BPM140204X vs BPM140204Y Data")
cf1.plot(dfx2, dfy2)
cf2 = f3.add_subplot(122)
plt.title("BPM140204X vs BPM140204Y Data (first 200 points)")
cf2.plot(dfx2[:200], dfy2[:200])
plt.draw()
filename3 = 'X_vs_Y' + the_now.strftime('%Y-%m-%d_%H-%M-%S')
#plt.savefig(filename3)
plt.show(block = False)

# plot both fourier transforms
f4 = plt.figure(4)
f4.clear()
df1 = f4.add_subplot(111)
plt.title("Fourier Transform")
df1.plot(tr, dft3r)
df1.annotate('local max = ' + str(ymax), xy=(xmax, ymax), xytext=(xmax-750, ymax))
plt.draw()
filename4 = 'FT_with_max' + the_now.strftime('%Y-%m-%d_%H-%M-%S')
#plt.savefig(filename4)
plt.show(block = False)

plt.show()