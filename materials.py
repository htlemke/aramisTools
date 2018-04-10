import xrayutilities as xu
from .utilities import DummyClassDict
from . import consts as _consts

# This module holds relevant materials of the
# xrayutilities materials class,

amorphous = DummyClassDict()
crystal = DummyClassDict()


crystal['Si'] = xu.materials.Si
crystal['Ge'] = xu.materials.Ge
crystal['GaAs'] = xu.materials.GaAs
amorphous['B4C'] = xu.materials.material.Amorphous('B4C',2520,[('B',4),('C',1)])
amorphous['Mo'] = xu.materials.material.Amorphous('Mo',10220,[('Mo',1)])
amorphous['polyimide'] = xu.materials.material.Amorphous('polyimide',1430,[('C',22),('H',10),('N',2),('O',5)])
amorphous['air'] = xu.materials.material.Amorphous('air',1000,[('N',1.562),('O',.42),('C',.0003),('Ar',.0094)])



# more useful values and constants
elementName = DummyClassDict(_consts.elementName)
meltPoint = DummyClassDict(_consts.meltPoint)
density = DummyClassDict(_consts.Density)

class Gas(xu.materials.material.Amorphous)
    def __init__(name, pressure=750)


