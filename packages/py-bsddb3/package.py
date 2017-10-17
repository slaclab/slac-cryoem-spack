##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
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
import platform


class PyBsddb3(PythonPackage):
    """This module provides a nearly complete wrapping of the Oracle/Sleepycat C API for the Database Environment, Database, Cursor, Log Cursor, Sequence and Transaction objects, and each of these is exposed as a Python type in the bsddb3.db module. The database objects can use various access methods: btree, hash, recno, and queue. Complete support of Berkeley DB distributed transactions. Complete support for Berkeley DB Replication Manager. Complete support for Berkeley DB Base Replication. Support for RPC."""

    homepage = "https://www.jcea.es/programacion/pybsddb.htm"
    url      = "https://pypi.python.org/packages/ba/a7/131dfd4e3a5002ef30e20bee679d5e6bcb2fcc6af21bd5079dc1707a132c/bsddb3-6.2.5.tar.gz"

    install_time_test_callbacks = ['install_test', 'import_module_test']

    version('6.2.5', '610267c189964c905a931990e1ba438c')

    depends_on('python@2.7:2.8,3.4:')
    depends_on('py-setuptools', type='build')
    depends_on('berkeley-db@5.3.28')

    def build_args(self, spec, prefix):
        return [ '--berkeley-db=%s' % spec['berkeley-db'].prefix ]

    def install_args(self, spec, prefix):
        return [ '--prefix=%s' % prefix, '--berkeley-db=%s' % spec['berkeley-db'].prefix ]

    def install_test(self):
        with working_dir('..'):
            python('-c', 'import bsddb3')
