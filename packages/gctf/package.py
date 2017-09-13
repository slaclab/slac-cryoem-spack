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
#     spack install gctf-v0-50-and-examples
#
# You can edit this file again by typing:
#
#     spack edit gctf-v0-50-and-examples
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import os
import stat
import shutil

class Gctf(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.mrc-lmb.cam.ac.uk/kzhang/"
    url      = "http://www.mrc-lmb.cam.ac.uk/kzhang/Gctf/Gctf_v0.50_and_examples.tar.gz"

    version('0.50', 'ceacc727defc192d0ee0c6ae03c58965', url=url )

    depends_on('cuda@7.5.18', when='@0.50', type='run')

    def install(self, spec, prefix):

        # TODO: deal with mapping of arch etc to path and version
        bin_dir = prefix + '/bin/'
        if not os.path.exists( bin_dir ):
            os.makedirs( bin_dir )
        path = 'bin/Gctf-v0.50_sm_30_cu7.5_x86_64'
        #st = os.stat(path)
        #os.chmod( path, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH )
        os.chmod( path, 0777 )
        shutil.copyfile( path, bin_dir + '/Gctf' )
