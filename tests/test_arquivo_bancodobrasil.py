# -*- coding: utf-8 -*-

try:                                                                             
    import unittest2 as unittest
except ImportError:                                                              
    import unittest

import os
import codecs
from cnab240 import errors
from cnab240.bancos import bancodobrasil
from cnab240.tipos import Arquivo
from tests.data.bancodobrasil_data import (
    get_bancodobrasil_data_from_dict,
    get_bancodobrasil_data_from_file,
    ARQS_DIRPATH)


class TestCnab240(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCnab240, self).__init__(*args, **kwargs)
        self.maxDiff = None 

    def setUp(self):
        self.bancodobrasil_data = get_bancodobrasil_data_from_dict()
        self.arquivo = Arquivo(bancodobrasil, **self.bancodobrasil_data['arquivo'])

    @unittest.skip
    def test_unicode(self):
        self.arquivo.incluir_cobranca(**self.bancodobrasil_data['cobranca'])
        self.assertEqual(str(self.arquivo), get_bancodobrasil_data_from_file())

    @unittest.skip
    def test_empty_data(self):
        arquivo = Arquivo(bancodobrasil)
        self.assertRaises(errors.ArquivoVazioError, str, arquivo)

    @unittest.skip
    def test_leitura_bancodobrasil(self):
        return_file_path = os.path.join(ARQS_DIRPATH, 'cobranca.bancodobrasil.ret')
        ret_file = codecs.open(return_file_path, encoding='ascii')
        arquivo = Arquivo(bancodobrasil, arquivo=ret_file)

        ret_file.seek(0)
        self.assertEqual(ret_file.read(), str(arquivo))
        ret_file.close()


if __name__ == '__main__':
    unittest.main()
