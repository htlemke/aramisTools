import xrayutilities as xu
from .utilities import DummyClassDict

# This module holds relevant materials of the
# xrayutilities materials class,

amorphous = DummyClassDict()
crystal = DummyClassDict()


crystal['Si'] = xu.materials.Si
crystal['GaAs'] = xu.materials.GaAs
amorphous['B4C'] = xu.materials.material.Amorphous('B4C',2520,[('B',4),('C',1)])
amorphous['Mo'] = xu.materials.material.Amorphous('Mo',10220,[('Mo',1)])


