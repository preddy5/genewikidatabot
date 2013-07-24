#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Erik Clarke (eclarke@scripps.edu)

#    This file is part of pygenewiki.
#
#    pygenewiki is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pygenewiki is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pygenewiki.  If not, see <http://www.gnu.org/licenses/>.

import pygenewiki.uniprot as uniprot

class TestUniprot(object):

    def testUniprotAccForEntrezId_real(self):
        entrez = '28'
        u_acc = uniprot.uniprotAccForEntrezId(entrez)
        assert u_acc == 'P16442'

    def testUniprotAccForEntrezId_fake(self):
        entrez = '-1'
        u_acc = uniprot.uniprotAccForEntrezId(entrez)
        assert not u_acc

