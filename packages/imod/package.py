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
#     spack install imod
#
# You can edit this file again by typing:
#
#     spack edit imod
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import os

import shutil
import glob

class Imod(Package):
    """IMOD is a set of image processing, modeling and display programs used for tomographic reconstruction and for 3D reconstruction of EM serial sections and optical sections. The package contains tools for assembling and aligning data within multiple types and sizes of image stacks, viewing 3-D data from any orientation, and modeling and display of the image files. IMOD was developed primarily by David Mastronarde, Rick Gaudette, Sue Held, Jim Kremer, Quanren Xiong, and John Heumann at the University of Colorado."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://bio3d.colorado.edu/imod/"
    #url      = "http://www.slac.stanford.edu/~ytl/imod-4.9.4-source.tar.gz"
    url = 'http://bio3d.colorado.edu/imod/AMD64-RHEL5/imod_4.9.4_RHEL6-64_CUDA8.0.sh'

    version('4.9.4', '0298eac521cdc76fbb3578751acc6c96', expand=False)

    # FIXME: Add dependencies if required.
    #depends_on('qt@4.8.6')
    depends_on('libtiff')
    depends_on('cuda@.0:8.99', when="@4.9.4")
    depends_on('fftw')
    depends_on('hdf5')
    depends_on('jdk')

# if (! $?IMOD_CALIB_DIR) setenv IMOD_CALIB_DIR /usr/local/ImodCalib
# if (-r $IMOD_CALIB_DIR/IMOD.csh) source $IMOD_CALIB_DIR/IMOD.csh

# alias subm 'submfg \!* &'

    def setup_environment(self, spack_env, run_env):

        run_env.prepend_path( 'PATH', join_path( self.spec.prefix, 'bin' ) )
        run_env.prepend_path( 'LD_LIBRARY_PATH', join_path( self.spec.prefix, 'lib' ) )

        run_env.set('IMOD_DIR', self.spec.prefix)
        run_env.set('IMOD_PLUGIN_DIR', join_path( self.spec.prefix, 'lib/imodplug' ))

        run_env.set('IMOD_JAVADIR', join_path( self.spec['jdk'].prefix, 'bin' ))

        run_env.set('FOR_DISABLE_STACK_TRACE', '1')
        run_env.set('IMOD_QTLIBDIR', join_path( self.spec.prefix, 'qtlib' ))



    def install(self, spec, prefix):
        """ install from binary """
        # deps on libGLU: yum install -y mesa-libGLU
        
        cmd = 'sh ./imod_4.9.4_RHEL6-64_CUDA8.0.sh -yes -dir %s -skip' % (prefix,)
        # logging.error( cmd )
        os.system( cmd )
        # flatten
        for f in glob.glob('%s/imod_4.9.4/*' % (prefix,)):
            shutil.move( f, prefix )
        os.remove( '%s/IMOD' % prefix )
        shutil.rmtree( '%s/imod_4.9.4' % prefix )
        
