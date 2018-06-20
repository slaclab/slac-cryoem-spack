##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
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

import shutil
import os

class IconGpu(MakefilePackage):
    """Electron tomography (ET) plays an important role in revealing biological structures, ranging from macromolecular to subcellular scale. Due to limited tilt angles, ET reconstruction always suffers from the 'missing wedge' artifacts, thus severely weakens the further biological interpretation. We developed an algorithm called Iterative Compressed-sensing Optimized Non-uniform fast Fourier transform reconstruction (ICON) based on the theory of compressed-sensing and the assumption of non-negativity density of biological specimen. ICON can significantly restore the missing information in comparison with other reconstruction algorithms. More importantly, we also provided a practical method to verify the validity of these restored information. We expect a great potential of ICON in the future application of high-resolution structural determination of macromolecules in situ."""

    homepage = "http://feilab.ibp.ac.cn/LBEMSB/ICON.html"
    url      = "http://feilab.ibp.ac.cn/software/ICON/ICON-GPU_v1.2.5_CentOS64.tar.gz"

    version('1.2.7', '1da8987b7f579eacf7500385092a49aa', url='http://feilab.ibp.ac.cn/software/ICON/ICON-GPU_v1.2.7_CentOS64.tar.gz')
    version('1.2.5', '25f3db95535b617d152966e1ac4f22e9')

    depends_on('fftw@3.3.4+openmp+float~mpi', type=('build', 'link', 'run'))
    depends_on('cuda@8.0.61', type=('build', 'run'))

    # add makefile
    patch('icon-gpu_makefile.patch', when='@1.2.5')
    patch('icon-gpu_1.2.7_makefile.patch', when='@1.2.7')

    def install(self, spec, prefix):
        # for f in os.listdir('.'):
        #     if f in ('bin', 'lib'):
        #         shutil.move( f, prefix )
        install_tree('bin', prefix.bin)
        install_tree('lib', prefix.lib)
