#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules


def install():
    pisitools.insinto("/usr/bin/", "xterm_colour_chart.py")
    shelltools.chmod(get.installDIR() + "/usr/bin/xterm_colour_chart.py", mode=0755)
    pisitools.dosym("/usr/bin/xterm_colour_chart.py", "/usr/bin/xtermcolourchart")
