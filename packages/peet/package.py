##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install peet
#
# You can edit this file again by typing:
#
#     spack edit peet
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Peet(Package):
    """PEET (Particle Estimation for Electron Tomography) is an open-source package for aligning and averaging particles in 3-D subvolumes extracted from tomograms. It seeks the optimal alignment of each particle against a reference volume through several iterations. If PEET and IMOD are both installed, most PEET operations are available from the eTomo graphical user interface in IMOD. PEET uses the parallel processing framework within IMOD, so that the lengthy computations can be distributed to multiple cores on one computer, to a set of linked workstations, or to a cluster. PEET is written in Matlab and a compiled version is distributed along with the Matlab runtime environment needed to run it."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "http://bio3d.colorado.edu/ftp/PEET/linux/Particle_1.11.1_linux.tar.bz2"

    version('1.11.1', '8d0cc187fd91e58c20188b0078529430')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
