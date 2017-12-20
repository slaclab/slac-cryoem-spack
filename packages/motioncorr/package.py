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
import os

class Motioncorr(Package):
    """ TODO """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://cryoem.ucsf.edu/software/driftcorr.html"
    url      = "http://cryoem.ucsf.edu/software/motioncorr_v2.1.tar"

    version('2.1', 'f82e9738a3382a62a7e4eb675553c13a')

    # FIXME: Add dependencies if required.
    depends_on('cuda@8.0.61', type=('build','link','run'))

    def install(self, spec, prefix):
        old_pwd = os.getcwd()
        os.chdir('./src')
        make()
        # make('install')
        os.chdir(old_pwd)
        #bin_dir = prefix + '/bin/'
        #if not os.path.exists( bin_dir ):
        #    os.makedirs( bin_dir )
        install_tree( 'bin', prefix + '/bin/'  )
