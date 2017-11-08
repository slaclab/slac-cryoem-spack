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

import os

class Eman2(CMakePackage):
    """is a broadly based greyscale scientific image processing suite with a primary focus on processing data from transmission electron microscopes. EMAN's original purpose was performing single particle reconstructions (3-D volumetric models from 2-D cryo-EM images) at the highest possible resolution, but the suite now also offers support for single particle cryo-ET, and tools useful in many other subdisciplines such as helical reconstruction, 2-D crystallography and whole-cell tomography. """

    homepage = "http://blake.bcm.edu/emanwiki/EMAN2"
    url      = "https://github.com/cryoem/eman2"

    version('master', git=url )
    #version('2.12', '5fbdd11135e446de15a5e8e9c7e60904', url='http://ncmi.bcm.edu/ncmi/software/counter_222/software_133/eman2.12.source.tar.gz')

    variant('mpi', default=False, description="Builds with support for MPI")
    variant('cuda', default=False, description="Build with CUDA support")

    depends_on('mpi', when='+mpi')

    depends_on('fftw')
    depends_on('gsl')
    depends_on('python', type=('build','run'))
    depends_on('py-numpy')
    depends_on('boost+python', type=('build','run'), when='~mpi')
    depends_on('boost+python+mpi', type=('build','run'), when='+mpi')
    depends_on('cmake', type=('build'))
    depends_on('py-pyqt', type=('run',))
    depends_on('py-sip', type=('run',))
    depends_on('py-nose', type=('run',))
    depends_on('freetype')
    depends_on('ftgl')
    depends_on('zlib')
    depends_on('libx11')
    depends_on('py-bsddb3', type=('run',) )
    depends_on('py-py-open-g-l', type=('run',))    

    depends_on('py-matplotlib+ipython', type=('run'))
    depends_on('py-ipython', type=('run'))

    # optional
    depends_on('hdf5')
    depends_on('libtiff')
    depends_on('libpng')

    depends_on('cuda', when='+cuda')
    # depends_on('miniconda2')

    def cmake_args(self):

        os.environ['CONDA_BUILD_STATE'] = 'BUILD'
        os.environ['PREFIX'] = prefix
        os.environ['LIBRARY_PREFIX'] = prefix
        os.environ['SP_DIR'] = prefix + '/lib/'

        spec = self.spec
        args = std_cmake_args

        if '+mpi' in spec:
            args.extend([ '-DCMAKE_CXX_COMPILER:STRING=%s' % spec['mpi'].mpicxx ])

        args.extend([ 
            '-DCMAKE_INSTALL_PREFIX=%s' % prefix,
            '-DEMAN_PREFIX=%s' % prefix,
            # '-DEMAN_INSTALL_PREFIX=%s' % prefix,
            '-DENABLE_OPTIMIZE_X86_64:BOOL=ON',
            # ENABLE_OPTIMIZE_MACHINE
            # '-DBoost_DEBUG=ON',
            '-DBOOST_ROOT=' + spec['boost'].prefix,
            '-DBOOST_INCLUDEDIR=' + spec['boost'].prefix.include,
            # '-DBOOST_INCLUDE_PATH=' + spec['boost'].prefix.include,
            '-DBOOST_LIBRARYDIR=' + spec['boost'].prefix.lib,

            # '-DFREETYPE_INCLUDE_PATH=' + spec['freetype'].prefix.include + '/freetype2/',
            # '-DGSL_CBLAS_INCLUDE_PATH=' + spec['gsl'].prefix.include,
            # '-DGSL_INCLUDE_PATH=' + spec['gsl'].prefix.include,
            '-DHDF5_INCLUDE_PATH=' + spec['hdf5'].prefix.include,
            # '-DPNG_INCLUDE_PATH=' + spec['libpng'].prefix.include,
            # '-DTIFF_INCLUDE_PATH=' + spec['libtiff'].prefix.include,

            # '-DCONDA_PREFIX=' + spec['miniconda2'].prefix,
            '-DPYTHON_EXECUTABLE=' + spec['python'].prefix.bin + '/python',
            '-DPYTHON_LIBRARY=' + spec['python'].prefix + '/lib/libpython2.7.so',
            '-DPYTHON_INCLUDE_PATH=' + spec['python'].prefix.include + '/python2.7/',
            '-DPYTHON_INCLUDE_DIRS=' + spec['python'].prefix.include + '/python2.7/',
            '-DPYTHON_INCLUDE_DIR=' + spec['python'].prefix.include + '/python2.7/',
            # '-DNUMPY_INCLUDE_PATH=' + spec['py-numpy'].prefix.include,
            '-DNUMPY_INCLUDE_DIR=' + spec['py-numpy'].prefix.lib + '/python2.7/site-packages/numpy/core/include/',

            # '-DFFTW3_INCLUDE_PATH=' + spec['fftw'].prefix.include,
            '-DFFTW3F_INCLUDE_PATH=' + spec['fftw'].prefix.include,
            '-DFFTW3D_INCLUDE_PATH=' + spec['fftw'].prefix.include,

            '-DFTGL_INCLUDE_PATH=' + spec['ftgl'].prefix.include,
        ])

        #if '+cuda' in spec:
        # ENABLE_SPARX_CUDA
        # ENABLE_EMAN_CUDA
        #    args.extend([ '-DENABLE_EMAN_CUDA:BOOL=ON', '-DENABLE_SPARX_CUDA:BOOL=ON' ])
        
        return args

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path( 'PYTHONPATH', self.prefix + '/lib' )
        # run_env.prepend_path( 'PYTHONPATH', self.spec['miniconda2'].prefix + '/lib/python2.7/site-packages/' )

