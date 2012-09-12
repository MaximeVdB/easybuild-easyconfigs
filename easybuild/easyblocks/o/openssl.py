##
# Copyright 2012 Kenneth Hoste
# Copyright 2012 Jens Timmerman
#
# This file is part of EasyBuild,
# originally created by the HPC team of the University of Ghent (http://ugent.be/hpc).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for OpenSSL, implemented as an easyblock
"""

from easybuild.framework.application import Application
from easybuild.tools.filetools import run_cmd

class EB_OpenSSL(Application):
    """Support for building OpenSSL"""

    def configure(self, cmd_prefix=''):
         """
         Configure step
         """
 
         cmd = "%s %s./config --prefix=%s threads shared %s" % (self.getcfg('preconfigopts'), cmd_prefix,
                                                     self.installdir, self.getcfg('configopts'))
 
         (out, _) = run_cmd(cmd, log_all=True, simple=False)
 
         return out

    def sanitycheck(self):
        """Custom sanity check"""

        self.setcfg('sanityCheckPaths',{'files':["lib64/%s" % x for x in ['engines', 'libcrypto.a', 'libcrypto.so',
                                                                           'libcrypto.so.1.0.0', 'libssl.a',
                                                                           'libssl.so', 'libssl.so.1.0.0']] + \
                                                 ['bin/openssl'],
                                        'dirs': []
                                       })
        self.log.info("Customized sanity check paths: %s" % self.getcfg('sanityCheckPaths'))

        return Application.sanitycheck(self)
    
