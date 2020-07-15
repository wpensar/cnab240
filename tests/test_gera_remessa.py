# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import codecs
import os
from cnab240 import errors
from cnab240.bancos import itau
from cnab240.tipos import Arquivo
from tests.data.itau_data import get_itau_data_from_dict, get_itau_file_remessa, \
    ARQS_DIRPATH


class TestRemessa(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRemessa, self).__init__(*args, **kwargs)
        self.maxDiff = None

    def setUp(self):
        self.itau_data = get_itau_data_from_dict()
        self.arquivo = Arquivo(itau, **self.itau_data['arquivo'])

    def test_unicode(self):
        self.arquivo.incluir_cobranca(**self.itau_data['cobranca'])
        self.assertEqual(str(self.arquivo), get_itau_file_remessa())

    def test_empty_data(self):
        arquivo = Arquivo(itau)
        self.assertRaises(errors.ArquivoVazioError, str, arquivo)

    def test_leitura(self):
        return_file_path = os.path.join(ARQS_DIRPATH, 'cobranca.itau.ret')
        ret_file = codecs.open(return_file_path, encoding='ascii')
        arquivo = Arquivo(itau, arquivo=ret_file)
        ret_file.seek(0)
        self.assertEqual(ret_file.read(), str(arquivo))
        ret_file.close()


if __name__ == '__main__':
    unittest.main()
