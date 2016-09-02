#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools


def setup():
    shelltools.system("./autogen.sh")
    #autotools.autoreconf("-fiv")
    shelltools.system('sed -i "s/ -ggdb//g" configure')
    shelltools.system('sed -i "/docs:/ s/doxygen-doc//" Makefile.in')
    
    autotools.configure("--disable-doxygen-doc \
                         --with-pic \
                         --with-zlib \
                         --with-bzlib \
                         --with-openssl \
                         --with-log4cpp \
                         --with-plugins=/usr/lib/pion/plugins")

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()
'''
def check():
    autotools.make("check")
'''

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPY*", "NEWS", "README*")
