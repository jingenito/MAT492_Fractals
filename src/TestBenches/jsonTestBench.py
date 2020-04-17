import os, sys

app_path = os.path.dirname(os.path.realpath('JSONSerializer.py'))
sys.path.append(os.path.join(app_path,'src'))

from Util.JSONSerializer import JSONSerializer

testSet = [[[0 for x in range(256)] for y in range(256)] for z in range(256)]

j = JSONSerializer(os.path.join(app_path,'bin','listoflisttest.json'))

print("Serializing a list of lists...")
j.SerializeJSON(testSet)

print('Done!')