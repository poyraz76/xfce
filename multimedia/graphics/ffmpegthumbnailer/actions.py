#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
    cmaketools.configure("\
	                     -DCMAKE_BUILD_TYPE=Release \
	                     -DCMAKE_INSTALL_PREFIX=/usr \
                         -DCMAKE_INSTALL_LIBDIR=lib \
                         -DENABLE_GIO=ON \
                         -DENABLE_THUMBNAILER=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    # Empty files: NEWS, TODO
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
