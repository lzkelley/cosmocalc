"""
"""
import os

import astropy as ap
import astropy.constants  # noqa
import astropy.units  # noqa

_here = os.path.abspath(os.path.dirname(__file__))
__version__ = os.path.join(_here, os.path.pardir, "VERSION.txt")
__author__ = "Luke Zoltan Kelley <lkelley@cfa.harvard.edu>"
__license__ = "MIT"


NWTG = ap.constants.G.cgs.value
SPLC = ap.constants.c.cgs.value
MSOL = ap.constants.M_sun.cgs.value
LSOL = ap.constants.L_sun.cgs.value
RSOL = ap.constants.R_sun.cgs.value
PC = ap.constants.pc.cgs.value
AU = ap.constants.au.cgs.value

ARCSEC = ap.units.arcsec.cgs.scale       # arcsecond in radians
YR = ap.units.year.to(ap.units.s)       # year in seconds

U_SEC = ap.units.Unit('s')       # second unit
U_CM = ap.units.Unit('cm')       # centimeter unit


from . __main__ import get_cosmology, api  # noqa
