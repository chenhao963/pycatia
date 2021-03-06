#! /usr/bin/python3.6

import os

from .catia_application import CATIAApplication
from .csv_tools import create_points
from .csv_tools import csv_reader
from .context import CATIADocHandler
from .document import Document
from .document import Documents
from .drawing import DrawingRoot
from .drawing import DrawingSheet
from .drawing import Views
from .drawing import DrawingView
from .drawing import paper_sizes
from .drawing import drawing_orientation
from .exceptions import CATIAApplicationException
from .general_functions import create_measurable
from .hybridshapefactory import HybridShapeFactory
from .measurable import CATIAMeasurable
from .part import Part
from .product import Product
from .workbenches import create_spa_workbench


__author__ = 'Paul Bourne'
__author_email = 'evereux@gmail.com'
__description__ = 'A python module to access the CATIA Measurable object.'
__name__ = "pycatia"
__version__ = "0.1.4"
__url__ = "https://github.com/evereux/pycatia"

name = __name__

macro_path = os.path.join(os.path.realpath(__file__), r'macros')
