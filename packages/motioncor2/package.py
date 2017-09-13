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
#     spack install motioncor
#
# You can edit this file again by typing:
#
#     spack edit motioncor
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import shutil
import os

class Motioncor2(Package):
    """Correction of electron beam-induced sample motion is one of the major factors contributing to the recent resolution breakthroughs in cryo-electron microscopy. Based on observations that the electron beam induces doming of the thin vitreous ice layer, we developed an algorithm to correct anisotropic image motion at the single pixel level across the whole frame, suitable for both single particle and tomographic images. Iterative, patch-based motion detection is combined with spatial and temporal constraints and dose weighting. The multi-GPU accelerated program, MotionCor2, is sufficiently fast to keep up with automated data collection. The result is an exceptionally robust strategy that can work on a wide range of data sets, including those very close to focus or with very short integration times, obviating the need for particle polishing. Application significantly improves Thon ring quality and 3D reconstruction resolution."""

    homepage = "http://msg.ucsf.edu/em/software/index.html"
    url      = "http://msg.ucsf.edu/MotionCor2/MotionCor2-01-30-2017.tar.gz"

    #version('10-19-2016',    '26eea5dc24269da499f1059f3677307a')
    version('01-30-2017',    'aec2f2653ba948e6d9a91a851171ce27', url='http://msg.ucsf.edu/MotionCor2/MotionCor2-01-30-2017.tar.gz')

    depends_on('cuda', when='@01-30-2017', type=('link','run'))
    depends_on('libtiff', type=('link','run'))
    # still needs libcuda.so.1 to be symlinked

    def install(self, spec, prefix):

        # TODO: deal with mapping of arch etc to path and version
        bin_dir = prefix + '/bin/'
        if not os.path.exists( bin_dir ):
            os.makedirs( bin_dir )
        os.chmod( 'MotionCor2-01-30-2017', 0555 )
        shutil.copyfile( 'MotionCor2-01-30-2017', bin_dir + '/MotionCor2' )
