import xrayutilities as xu
import numpy as np

def getKBMirrorLayer():
    subst = xu.simpack.Layer(xu.materials.Si, np.inf)
    highZ = xu.simpack.Layer(xu.materials.Mo, 250)
    return subst+highZ

