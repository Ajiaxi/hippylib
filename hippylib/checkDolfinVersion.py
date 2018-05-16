# Copyright (c) 2016-2018, The University of Texas at Austin & University of
# California, Merced.
#
# All Rights reserved.
# See file COPYRIGHT for details.
#
# This file is part of the hIPPYlib library. For more information and source code
# availability see https://hippylib.github.io.
#
# hIPPYlib is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License (as published by the Free
# Software Foundation) version 2.0 dated June 1991.

from __future__ import absolute_import, division, print_function

import dolfin as dl

if not hasattr(dl, "DOLFIN_VERSION_MAJOR"):
    dl.DOLFIN_VERSION_MAJOR = 2018
    dl.DOLFIN_VERSION_MINOR = 1
    dl.DOLFIN_VERSION_MICRO = 0

def dlversion():
    return (dl.DOLFIN_VERSION_MAJOR, dl.DOLFIN_VERSION_MINOR, dl.DOLFIN_VERSION_MICRO)

supported_versions = [(1,6,0), (2016,1,0), (2016,2,0), (2017,1,0), (2017,2,0), (2018,1,0)]

def checkdlversion():
    if dlversion() not in supported_versions:
        print("The version of FEniCS (FEniCS {0}.{1}.{2}) you are using is not supported.".format(*dlversion()) )
        exit()
        
def show_dl_plots():
    if dlversion() < (2017,2,0):
        dl.interactive()