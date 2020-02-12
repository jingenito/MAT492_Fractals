import os, sys

app_path = os.path.dirname(os.path.realpath('imageModsTestBench.py'))
sys.path.append(os.path.join(app_path,'src'))

import Util.ImageMods

Util.ImageMods.ReverseImage(os.path.join(app_path,'bin','cantorLawnBoundary.png'), os.path.join(app_path,'bin','cantorLawnBoundaryFlipped.png'))