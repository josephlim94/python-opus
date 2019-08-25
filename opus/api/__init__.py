import ctypes
from ctypes.util import find_library
from sys import platform

if platform == "linux" or platform == "linux2":
    libopus = ctypes.CDLL(find_library('opus'))
elif platform == "win32":
    if find_library('libopus-0'):
        libopus = ctypes.CDLL(find_library('libopus-0'))
    elif find_library('opus'):
        libopus = ctypes.CDLL(find_library('opus'))

c_int_pointer = ctypes.POINTER(ctypes.c_int)
c_int16_pointer = ctypes.POINTER(ctypes.c_int16)
c_float_pointer = ctypes.POINTER(ctypes.c_float)
