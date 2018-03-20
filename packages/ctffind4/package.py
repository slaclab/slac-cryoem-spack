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

from spack import *


class Ctffind4(AutotoolsPackage):
    """CTFFIND is a widely-used program for the estimation of objective lens defocus parameters from transmission electron micrographs. Defocus parameters are estimated by fitting a model of the microscope's contrast transfer function (CTF) to an image's amplitude spectrum. Here we describe modifications to the algorithm which make it significantly faster and more suitable for use with images collected using modern technologies such as dose fractionation and phase plates. We show that this new version preserves the accuracy of the original algorithm while allowing for higher throughput. We also describe a measure of the quality of the fit as a function of spatial frequency and suggest this can be used to define the highest resolution at which CTF oscillations were successfully modeled."""

    homepage = "http://grigoriefflab.janelia.org/node/4918"
    url      = "http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.5.tar.gz"

    version('4.1.10', '4f3b1efbd7f2fa81096c5450db00ec01', url='http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.10.tar.gz' )
    version('4.1.8', '8ae9d9abe363141a3792981b5a2fae94', url='http://grigoriefflab.janelia.org/sites/default/files/ctffind-4.1.8.tar.gz' )
    version('4.1.5', '3c1b21f9b356b1327ab4938b31130105')

    depends_on('mkl')
    depends_on('wx', type=('build','link'))
    depends_on('cairo')
    depends_on('fftw')

    patch('4.1.5_compilation.patch', when='@4.1.5')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args

