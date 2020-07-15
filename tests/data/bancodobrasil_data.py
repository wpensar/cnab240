# -*- coding: utf-8 -*-

import os
import codecs
from decimal import Decimal
from cnab240.bancos import bancodobrasil
from cnab240.tipos import Lote, Evento

TESTS_DIRPATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
ARQS_DIRPATH = os.path.join(TESTS_DIRPATH, 'arquivos')
print(ARQS_DIRPATH)


def get_bancodobrasil_data_from_file():
    bancodobrasil_data = dict()
    arquivo_remessa = codecs.open(os.path.join(ARQS_DIRPATH, 'cobranca.bancodobrasil.rem'), encoding='ascii')

    bancodobrasil_data['remessa'] = arquivo_remessa.read()
    arquivo_remessa.seek(0)

    bancodobrasil_data['header_arquivo'] = bancodobrasil.registros.HeaderArquivo()
    bancodobrasil_data['header_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    bancodobrasil_data['header_arquivo'].carregar(bancodobrasil_data['header_arquivo_str'])

    bancodobrasil_data['header_lote'] = bancodobrasil.registros.HeaderLoteCobranca()
    bancodobrasil_data['header_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    bancodobrasil_data['header_lote'].carregar(bancodobrasil_data['header_lote_str'])

    bancodobrasil_data['seg_p1'] = bancodobrasil.registros.SegmentoP()
    bancodobrasil_data['seg_p1_str'] = arquivo_remessa.readline().strip('\r\n')
    bancodobrasil_data['seg_p1'].carregar(bancodobrasil_data['seg_p1_str'])

    bancodobrasil_data['seg_q1'] = bancodobrasil.registros.SegmentoQ()
    bancodobrasil_data['seg_q1_str'] = arquivo_remessa.readline().strip('\r\n')
    bancodobrasil_data['seg_q1'].carregar(bancodobrasil_data['seg_q1_str'])

    bancodobrasil_data['seg_p2'] = bancodobrasil.registros.SegmentoP()
    bancodobrasil_data['seg_p2_str'] = arquivo_remessa.readline().strip('\r\n')
    bancodobrasil_data['seg_p2'].carregar(bancodobrasil_data['seg_p2_str'])

    bancodobrasil_data['seg_q2'] = bancodobrasil.registros.SegmentoQ()
    bancodobrasil_data['seg_q2_str'] = arquivo_remessa.readline().strip('\r\n')
    bancodobrasil_data['seg_q2'].carregar(bancodobrasil_data['seg_q2_str'])

    bancodobrasil_data['trailer_lote'] = bancodobrasil.registros.TrailerLoteCobranca()
    bancodobrasil_data['trailer_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    bancodobrasil_data['trailer_lote'].carregar(bancodobrasil_data['trailer_lote_str'])

    bancodobrasil_data['trailer_arquivo'] = bancodobrasil.registros.TrailerArquivo()
    bancodobrasil_data['trailer_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    bancodobrasil_data['trailer_arquivo'].carregar(bancodobrasil_data['trailer_arquivo_str'])

    bancodobrasil_data['lote_cob'] = Lote(bancodobrasil, bancodobrasil_data['header_lote'],
                                      bancodobrasil_data['trailer_lote'])
    bancodobrasil_data['evento_cob1'] = Evento(bancodobrasil, 1)
    bancodobrasil_data['evento_cob1'].adicionar_segmento(bancodobrasil_data['seg_p1'])
    bancodobrasil_data['evento_cob1'].adicionar_segmento(bancodobrasil_data['seg_q1'])

    bancodobrasil_data['evento_cob2'] = Evento(bancodobrasil, 1)
    bancodobrasil_data['evento_cob2'].adicionar_segmento(bancodobrasil_data['seg_p2'])
    bancodobrasil_data['evento_cob2'].adicionar_segmento(bancodobrasil_data['seg_q2'])

    arquivo_remessa.close()
    return bancodobrasil_data


def get_bancodobrasil_data_from_dict():
    bancodobrasil_data = dict()
    dict_arquivo = {
        'cedente_inscricao_tipo': 2,
        'cedente_inscricao_numero': 12760233000171,
        'cedente_agencia': 3009,
        'cedente_conta': 29929,
        'cedente_agencia_conta_dv': '4',
        'cedente_nome': "LADDER TECNOLOGIA EIRELI",
        'arquivo_data_de_geracao': 11022019,
        'arquivo_hora_de_geracao': 112000,
        'arquivo_sequencia': 900002
    }

    dict_cobranca = {
        'cedente_agencia': 3009,
        'cedente_conta': 29929,
        'cedente_agencia_conta_dv': '4',
        'carteira_numero': 1,
        'nosso_numero': 99999999,
        'nosso_numero_dv': 9,
        'numero_documento': '9999999999',
        'vencimento_titulo': 28022019,
        'valor_titulo': Decimal('100.00'),
        'especie_titulo': 4,
        'aceite_titulo': 'N',
        'data_emissao_titulo': 11022019,
        'juros_mora_taxa_dia': Decimal('2.00'),
        'valor_abatimento': Decimal('0.00'),
        'identificacao_titulo': 'BOLETO DE TESTE',
        'codigo_protesto': 0,
        'prazo_protesto': 0,
        'codigo_baixa': 0,
        'prazo_baixa': 0,
        'sacado_inscricao_tipo': 1,
        'sacado_inscricao_numero': 83351622120,
        'sacado_nome': 'JESUS DO CEU',
        'sacado_endereco': 'RUA DR VALERIO, 145',
        'sacado_bairro': 'SANTA RITA',
        'sacado_cep': 29785,
        'sacado_cep_sufixo': 000,
        'sacado_cidade': 'VILA VALERIO',
        'sacado_uf': 'ES',
    }

    bancodobrasil_data['arquivo'] = dict_arquivo
    bancodobrasil_data['cobranca'] = dict_cobranca

    return bancodobrasil_data
