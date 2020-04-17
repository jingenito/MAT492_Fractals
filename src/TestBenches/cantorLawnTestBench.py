import os, sys

app_path = os.path.dirname(os.path.realpath('CantorLawn.py'))
sys.path.append(os.path.join(app_path,'src'))

from CantorLawn import CantorLawn

print("Creating the Cantor Lawn...")
cLawn = CantorLawn((1024,1024), 6)

print("Saving the boundary image...")
cLawn.save_boundaryImage(os.path.join(app_path,'bin','cantorLawnBoundary.png'))

# print("Saving Cantor Set x Cantor String image...")
# cLawn.save_cantorSetCrossStringImage(os.path.join(bin_path,'bin','cantorSetCrossStringImg.png'))

# print("Saving Cantor Set x Cantor String image...")
# cLawn.save_cantorStringCrossSetImage(os.path.join(bin_path,'bin','cantorStringCrossSetImg.png'))

print("Done!")
