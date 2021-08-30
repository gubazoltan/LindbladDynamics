def demoprint():
	print("This function is used to check version control")

import time
import itertools
import multiprocessing
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import e, hbar, k
from numba import jit

class Measurement:
	def __init__(self,name):
		self.name = name
		self.setup = {
			"deltat" : None,
			"epsilon0" : None,
			"dV" :None,
			"Temp" : None,
			"w" : None,
			"dtnum": None,
			"tintnum" : None,
			"gammat" : None
		}
		self.ismeasured = False

class Result:
	def __init__(self,setupdata):
		self.setup = setupdata
		self.datas = {
		"Cg" : None,
		"Ce" : None,
		"Rinvg" : None,
		"Rinve" : None,
		"nRtg" : None,
		"nRte" : None,
		"rhotg" : None,
		"rhote" : None,
		"edotg" : None,
		"edote" : None
		}
