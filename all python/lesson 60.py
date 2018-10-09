""""""

"""Модули"""

"""NameSpase - пространсво имен, принцып файловой системы"""
"""Модуль - os, sys, random
   Подмодули - модуль os содержит подмодуль path
   Пакет - 
"""

import os # Просто импортировал модуль

import sys as s # Переименовали модуль в s

from math import sqrt as q # Из модуля math импортировали только sqrt и перименовали в
print(q(25))
from os.path import exists as e, join as j # Можно так же из вложеных импортировать и переименовывать, можно указать не один
print(e.__doc__)
print(j.__doc__)

from os.path import * # Таким способом можно импортировать все

