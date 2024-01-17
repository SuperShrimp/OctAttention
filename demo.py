from ctypes import *
import os
import numpy as np
import numpy.ctypeslib as npct

libpath = r'C:\Users\xizhe\Documents\OctAttention\OctreeCPP\Octree_python_lib.so'
lib = cdll.LoadLibrary(libpath)