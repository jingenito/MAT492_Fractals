from PIL import Image
from CantorString import CantorString
from JSONSerializer import JSONSerializer

_resolution = (1920,1080)
# tested 6 levels works best for 1080p
cString = CantorString((0, _resolution[0]), 6)

j = JSONSerializer("bin/cantorString.json")
j.SerializeJSON(cString.getCantorString())

j = JSONSerializer("bin/cantorSet.json")
j.SerializeJSON(cString.getCantorSet())

j = JSONSerializer("bin/cantorLevels.json")
j.SerializeJSON(cString.cantorLevels)