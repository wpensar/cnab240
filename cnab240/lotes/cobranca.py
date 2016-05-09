# -*- coding: utf-8 -*-

from cnab240.tipos import Lote

class LoteCobranca(Lote):
    HeaderCls = Lote.banco.registros.HeaderLoteCobranca
    TrailerCls = Lote.banco.registros.TrailerLoteCobranca

