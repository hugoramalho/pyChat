#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyChat.py
#
#  Ramalho <Ramalho@DESKTOP-MEI8G7T>
#

__author__ = "Ramalho, Hugo"
__copyright__ = "Copyright 2017, Trabalho de Redes -  myWhats_app.py"
__credits__ = ["Instituto Federal do Espirito Santo, Campus SERRA", "Professor Gilmar Vassoler"]
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Hugo Ramalho"
__email__ = "ramalho.hg@gmail.com"
__status__ = "Testing"

from pyChat.ClientSide.SessionController import Session


class myWhats_app:
    """
        SUPER CLASSE DO PROGRAMA.
        Unidade funcional do programa encapsulada numa classe.
    """
    def __init__(self):
        self.sessao_atv = Session.Session()

def main():
    app = myWhats_app()

if __name__ == '__main__':
    import sys
    sys.exit(main())
