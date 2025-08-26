from us_visa.logger import logging
from us_visa.exception import USvisaException
import os, sys

try:
    a = 1/0
    print(a)
except Exception as e:
    raise USvisaException(e,sys)    