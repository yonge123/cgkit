# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is the Python Computer Graphics Kit.
#
# The Initial Developer of the Original Code is Matthias Baas.
# Portions created by the Initial Developer are Copyright (C) 2004
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
# $Id: noise.py,v 1.3 2006/02/14 19:29:39 mbaas Exp $

"""Dummy noise module for cgkit light.

This module will allow importing the module without an error. An error will
only be triggered when the module is actually used.
This means the sl module can be imported and all non-noise related functions
can still be used in the light version.
"""

def noise(*args, **kwargs):
    raise NotImplementedError("This function is not yet implemented in the light version of cgkit")

snoise = noise
cellnoise = noise
scellnoise = noise
fBm = noise
turbulence = noise
pnoise = noise
spnoise = noise

vnoise = noise
vsnoise = noise
vcellnoise = noise
vscellnoise = noise
vfBm = noise
vturbulence = noise
vpnoise = noise
vspnoise = noise
