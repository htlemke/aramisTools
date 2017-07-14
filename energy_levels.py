import xraylib as xl
import matplotlib.pyplot as plt
import numpy as np
import adjustText

ElementRange = range(1,100)
Erange = [2,12]
edge = 0
edgenames = ['K1','L1','L2', 'L3', 'M1']
plt.figure('energy levels')
plt.clf()
tx = []
ty = []
tt = []

for n,edge in enumerate(range(5)):
    E = []
    Elements = []
    for el in ElementRange:
      tE = xl.EdgeEnergy(el,edge)
      if tE>np.min(Erange) and tE<np.max(Erange):
          E.append(tE)
          Elements.append(el)
    l = plt.plot(E,Elements,'+',label=edgenames[n])
    for el,tE in zip(Elements,E):
        tx.append(tE)
        ty.append(el)
        tt.append(\
            plt.text(tE,el,xl.AtomicNumberToSymbol(el),\
                     bbox={'pad':0, 'alpha':0},
                     color=l[0].get_color()))

plt.xlim(2,12)
plt.legend()
plt.xlabel('Photon Energy / keV')
plt.ylabel('Atomic Number')
plt.minorticks_on()
plt.grid(which='both')


plt.show()

