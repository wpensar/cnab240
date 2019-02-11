# -*- coding: utf-8 -*-

import os
import codecs
from decimal import Decimal
from cnab240.bancos import santander
from cnab240.tipos import Lote, Evento

TESTS_DIRPATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
ARQS_DIRPATH = os.path.join(TESTS_DIRPATH, 'arquivos')
print(ARQS_DIRPATH)


def get_santander_data_from_file():
    santander_data = dict()
    arquivo_remessa = codecs.open(os.path.join(ARQS_DIRPATH, 'cobranca.santander.rem'), encoding='ascii')

    santander_data['remessa'] = arquivo_remessa.read()
    arquivo_remessa.seek(0)

    santander_data['header_arquivo'] = santander.registros.HeaderArquivo()
    santander_data['header_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    santander_data['header_arquivo'].carregar(santander_data['header_arquivo_str'])

    santander_data['header_lote'] = santander.registros.HeaderLoteCobranca()
    santander_data['header_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    santander_data['header_lote'].carregar(santander_data['header_lote_str'])

    santander_data['seg_p1'] = santander.registros.SegmentoP()
    santander_data['seg_p1_str'] = arquivo_remessa.readline().strip('\r\n')
    santander_data['seg_p1'].carregar(santander_data['seg_p1_str'])

    santander_data['seg_q1'] = santander.registros.SegmentoQ()
    santander_data['seg_q1_str'] = arquivo_remessa.readline().strip('\r\n')
    santander_data['seg_q1'].carregar(santander_data['seg_q1_str'])

    santander_data['seg_p2'] = santander.registros.SegmentoP()
    santander_data['seg_p2_str'] = arquivo_remessa.readline().strip('\r\n')
    santander_data['seg_p2'].carregar(santander_data['seg_p2_str'])

    santander_data['seg_q2'] = santander.registros.SegmentoQ()
    santander_data['seg_q2_str'] = arquivo_remessa.readline().strip('\r\n')
    santander_data['seg_q2'].carregar(santander_data['seg_q2_str'])

    santander_data['trailer_lote'] = santander.registros.TrailerLoteCobranca()
    santander_data['trailer_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    santander_data['trailer_lote'].carregar(santander_data['trailer_lote_str'])

    santander_data['trailer_arquivo'] = santander.registros.TrailerArquivo()
    santander_data['trailer_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    santander_data['trailer_arquivo'].carregar(santander_data['trailer_arquivo_str'])

    santander_data['lote_cob'] = Lote(santander, santander_data['header_lote'],
                                      santander_data['trailer_lote'])
    santander_data['evento_cob1'] = Evento(santander, 1)
    santander_data['evento_cob1'].adicionar_segmento(santander_data['seg_p1'])
    santander_data['evento_cob1'].adicionar_segmento(santander_data['seg_q1'])

    santander_data['evento_cob2'] = Evento(santander, 1)
    santander_data['evento_cob2'].adicionar_segmento(santander_data['seg_p2'])
    santander_data['evento_cob2'].adicionar_segmento(santander_data['seg_q2'])

    arquivo_remessa.close()
    return santander_data


def get_santander_data_from_dict():
    santander_data = dict()
    dict_arquivo = {
        'cedente_inscricao_tipo': 2,
        'cedente_inscricao_numero': 15594050000111,
        'cedente_agencia': 4459,
        'cedente_conta': 17600,
        'cedente_agencia_conta_dv': 6,
        'cedente_nome': "TRACY TECNOLOGIA LTDA ME",
        'arquivo_data_de_geracao': 27062012,
        'arquivo_hora_de_geracao': 112000,
        'arquivo_sequencia': 900002
    }

    dict_cobranca = {
        'cedente_agencia': 4459,
        'cedente_conta': 17600,
        'cedente_agencia_conta_dv': 6,
        'carteira_numero': 109,
        'nosso_numero': 99999999,
        'nosso_numero_dv': 9,
        'numero_documento': '9999999999',
        'vencimento_titulo': 30072012,
        'valor_titulo': Decimal('100.00'),
        'especie_titulo': 8,
        'aceite_titulo': 'A',
        'data_emissao_titulo': 27062012,
        'juros_mora_taxa_dia': Decimal('2.00'),
        'valor_abatimento': Decimal('0.00'),
        'identificacao_titulo': 'BOLETO DE TESTE',
        'codigo_protesto': 3,
        'prazo_protesto': 0,
        'codigo_baixa': 0,
        'prazo_baixa': 0,
        'sacado_inscricao_tipo': 1,
        'sacado_inscricao_numero': 83351622120,
        'sacado_nome': 'JESUS DO CEU',
        'sacado_endereco': 'RUA AVENIDA DO CEU, 666',
        'sacado_bairro': 'JD PARAISO',
        'sacado_cep': 60606,
        'sacado_cep_sufixo': 666,
        'sacado_cidade': 'PARAISO DE DEUS',
        'sacado_uf': 'SP',
    }

    santander_data['arquivo'] = dict_arquivo
    santander_data['cobranca'] = dict_cobranca

    return santander_data
