import os, sys

app_path = os.path.dirname(os.path.realpath('JSONSerializer.py'))
sys.path.append(os.path.join(app_path,'src'))

from Util.JSONSerializer import JSONSerializer
from ComplimentableSet import ComplimentableSet

testSet = [3, 4, 6, 8, 9]
cSet = ComplimentableSet((0,10), testSet)

j = JSONSerializer(os.path.join(app_path,'bin','complimentableSetTest.json'))
j.SerializeJSON(cSet)

print('Done')