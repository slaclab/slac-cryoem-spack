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
#     spack install summovie
#
# You can edit this file again by typing:
#
#     spack edit summovie
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Summovie(AutotoolsPackage):
    """Movie frame sums can also be calculated using Summovie, which uses the 
       alignment results from a prior run of Unblur. The idea for this procedure 
       was originally developed by Brilot et al. and Campbell et al"""

    homepage = "http://grigoriefflab.janelia.org/unblur"
    url      = "http://grigoriefflab.janelia.org/sites/default/files/summovie_1.0.2.tar.gz"

    version('1.0.2', '170b42d194c20d66b5de7d09e574bb89')

    variant('openmp', default=False, description='Enable OpenMP support')

    configure_directory = 'src'

    depends_on('gsl')
    depends_on('zlib')
    depends_on('libtiff')
    depends_on('jpeg')
    depends_on('fftw')
    depends_on('libjpeg-turbo')

    parallel = False

    def configure_args(self):
        spec = self.spec
        args = [
            'FC=ifort',
            'F77=ifort',
        ]
        if( '+openmp' in spec ):
            args.append('--enable-openmp')
        #    pass
        return args


