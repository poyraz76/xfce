#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("sed -i 's|/usr/local|/usr|g' Makefile")
    
def build():
    autotools.make("PREFIX='/usr'")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
