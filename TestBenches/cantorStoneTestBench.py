import os, sys

app_path = os.path.dirname(os.path.realpath('CantorStone.py'))
sys.path.append(os.path.join(app_path,'src'))

from CantorStone import CantorStone

bin_path = os.path.dirname(os.path.realpath('cantorLevels.json'))

print("Creating the Cantor Stone...")
cStone = CantorStone((1024,1024), 6)

print("Saving the boundary image...")
cStone.save_boundaryImage(os.path.join(bin_path,'bin','cantorLawnBoundary.png'))

# print("Saving Cantor Set x Cantor String image...")
# cStone.save_cantorSetCrossStringImage(os.path.join(bin_path,'bin','cantorSetCrossStringImg.png'))

# print("Saving Cantor Set x Cantor String image...")
# cStone.save_cantorStringCrossSetImage(os.path.join(bin_path,'bin','cantorStringCrossSetImg.png'))

print("Done!")
