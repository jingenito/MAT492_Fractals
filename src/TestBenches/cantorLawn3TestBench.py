import os, sys

app_path = os.path.dirname(os.path.realpath('CantorLawn3.py'))
sys.path.append(os.path.join(app_path,'src'))

from CantorLawn3 import CantorLawn3
from Util.JSONSerializer import JSONSerializer

print("Creating the Cantor Lawn 3D...")
cLawn3 = CantorLawn3((128,128,128), 3)
print("Created the Cantor Lawn 3D.")

print("Assigning bitmap to a variable")
blah = cLawn3.get_cantorLawn3()

# print("Serializing JSON...")
# j = JSONSerializer(os.path.join(app_path,'bin','cantorLawn3Test.json'))
# j.SerializeJSON(blah)

print("Done!")