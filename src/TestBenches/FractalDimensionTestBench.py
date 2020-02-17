import os, sys

app_path = os.path.dirname(os.path.realpath('FractalDimension.py'))
sys.path.append(os.path.join(app_path,'src'))

import Util.FractalDimension as fd

fd.BoxCountingDimension(os.path.join(app_path, 'images', 'sierpinskiTriangle.png'), 10**-4)