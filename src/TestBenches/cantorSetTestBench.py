import os, sys


app_path = os.path.dirname(os.path.realpath('cantorSetTestBench.py'))
sys.path.append(os.path.join(app_path,'src'))

from CantorSet import CantorSet

cSet = CantorSet((0,1920), 6)

print("Cantor Set: ")
print(cSet.get_cantorSet())

print("Cantor Set - Level 1 :")
print(cSet.get_cantorSetLevel(1))

print("Cantor String: ")
print(cSet.get_cantorString())

print("Cantor String - Level 1")
print(cSet.get_cantorLevelstring(1))