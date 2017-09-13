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
#     spack install jspr
#
# You can edit this file again by typing:
#
#     spack edit jspr
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *
import os
import shutil

class Jspr(Package):
    """ jspr is a collection of the programs developed in Wen Jiang group
        in the Markey Center for Structural Biology, Department of 
        Biological Sciences, Purdue University. """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://jiang.bio.purdue.edu/jspr"
    url      = "http://jiang.bio.purdue.edu/download/Pics/download.php?f=jspr.2016-5-4.tar.gz"

    version('2016-5-4', '89afdd01e767b697df5b527fe25cb3f4')

    depends_on('jdk')
    depends_on('relion')
    depends_on('mpi')


    def setup_environment(self, spack_env, run_env):
        run_env.set('EMANDIR', self.spec.prefix + '/EMAN')
        run_env.prepend_path( 'PATH', join_path( self.spec.prefix, 'EMAN', 'bin' ) )
        run_env.set('EMAN2DIR', self.spec.prefix + '/EMAN2')
        run_env.prepend_path( 'PATH', join_path( self.spec.prefix, 'EMAN2', 'bin' ) )
        run_env.set('OPAL_PREFIX', self.spec.prefix)
        run_env.set('OMP_NUM_THREADS', '1')
        run_env.set('OPAL_PREFIX', self.spec.prefix)
        run_env.prepend_path( 'PYTHONPATH', join_path( self.spec.prefix, 'EMAN', 'lib' ) )
        run_env.prepend_path( 'LD_LIBRARY_PATH', join_path( self.spec.prefix, 'EMAN', 'lib' ) )
        run_env.prepend_path( 'PYTHONPATH', join_path( self.spec.prefix, 'EMAN2', 'lib' ) )
        run_env.prepend_path( 'LD_LIBRARY_PATH', join_path( self.spec.prefix, 'EMAN2', 'lib' ) )
        run_env.prepend_path( 'PYTHONPATH', join_path( self.spec.prefix, 'lib', 'python' ) )

    def install(self, spec, prefix):

        shutil.copytree( 'x86_64/EMAN', prefix + '/EMAN' )
        shutil.copytree( 'x86_64/EMAN2', prefix + '/EMAN2' )
        # bin
        shutil.copytree( 'x86_64/bin', prefix + '/bin', symlinks=True )
        for f in os.listdir( 'x86_64/jiang' ):
            shutil.copy( 'x86_64/jiang/%s' % f, '%s/bin/%s' % (prefix,f) )
        shutil.copytree( 'x86_64/lib', prefix + '/lib', symlinks=True )
        shutil.copytree( 'x86_64/lib64', prefix + '/lib64', symlinks=True )

