# -*- coding: utf-8 -*-
# Copyright (C) 2016 - 2021 Oscar Gerardo Lazo Arjona
# mailto: oscar.lazoarjona@physics.ox.ac.uk
r"""This is a repository for solvers for the Maxwell-Bloch equations of \
various quantum memories, and calculations using them.
"""

__version__ = "0.2"

from orca_memories.misc import (time_bandwith_product, build_mesh_fdm,
                                rayleigh_range, rel_error, glo_error)

from orca_memories.orca import set_parameters_ladder
#
from orca_memories.graphical import sketch_frame_transform, plot_solution
