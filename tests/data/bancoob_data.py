# -*- coding: utf-8 -*-

import os
import codecs
from decimal import Decimal
from cnab240.bancos import bancoob
from cnab240.tipos import Lote, Evento

TESTS_DIRPATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
ARQS_DIRPATH = os.path.join(TESTS_DIRPATH, 'arquivos')
print(ARQS_DIRPATH)


def get_bancoob_data_from_file():
    bancoob_data = dict()
    arquivo_remessa = codecs.open(os.path.join(ARQS_DIRPATH, 'cobranca.bancoob.rem'), encoding='ascii')

    bancoob_data['remessa'] = arquivo_remessa.read()
    arquivo_remessa.seek(0)

    bancoob_data['header_arquivo'] = bancoob.registros.HeaderArquivo()
    bancoob_data['header_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    bancoob_data['header_arquivo'].carregar(bancoob_data['header_arquivo_str'])

    bancoob_data['header_lote'] = bancoob.registros.HeaderLoteCobranca()
    bancoob_data['header_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    bancoob_data['header_lote'].carregar(bancoob_data['header_lote_str'])

    bancoob_data['seg_p1'] = bancoob.registros.SegmentoP()
    bancoob_data['seg_p1_str'] = arquivo_remessa.readline().strip('\r\n')
    bancoob_data['seg_p1'].carregar(bancoob_data['seg_p1_str'])

    bancoob_data['seg_q1'] = bancoob.registros.SegmentoQ()
    bancoob_data['seg_q1_str'] = arquivo_remessa.readline().strip('\r\n')
    bancoob_data['seg_q1'].carregar(bancoob_data['seg_q1_str'])

    # bancoob_data['trailer_lote'] = bancoob.registros.TrailerLoteCobranca()
    # bancoob_data['trailer_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    # bancoob_data['trailer_lote'].carregar(bancoob_data['trailer_lote_str'])
    #
    # bancoob_data['seg_p2'] = bancoob.registros.SegmentoP()
    # bancoob_data['seg_p2_str'] = arquivo_remessa.readline().strip('\r\n')
    # bancoob_data['seg_p2'].carregar(bancoob_data['seg_p2_str'])
    #
    # bancoob_data['seg_q2'] = bancoob.registros.SegmentoQ()
    # bancoob_data['seg_q2_str'] = arquivo_remessa.readline().strip('\r\n')
    # bancoob_data['seg_q2'].carregar(bancoob_data['seg_q2_str'])

    bancoob_data['trailer_lote'] = bancoob.registros.TrailerLoteCobranca()
    bancoob_data['trailer_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    bancoob_data['trailer_lote'].carregar(bancoob_data['trailer_lote_str'])

    bancoob_data['trailer_arquivo'] = bancoob.registros.TrailerArquivo()
    bancoob_data['trailer_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    bancoob_data['trailer_arquivo'].carregar(bancoob_data['trailer_arquivo_str'])

    bancoob_data['lote_cob'] = Lote(bancoob, bancoob_data['header_lote'],
                                      bancoob_data['trailer_lote'])
    bancoob_data['evento_cob1'] = Evento(bancoob, 1)
    bancoob_data['evento_cob1'].adicionar_segmento(bancoob_data['seg_p1'])
    bancoob_data['evento_cob1'].adicionar_segmento(bancoob_data['seg_q1'])

    # bancoob_data['evento_cob2'] = Evento(bancoob, 1)
    # bancoob_data['evento_cob2'].adicionar_segmento(bancoob_data['seg_p2'])
    # bancoob_data['evento_cob2'].adicionar_segmento(bancoob_data['seg_q2'])

    arquivo_remessa.close()
    return bancoob_data


def get_bancoob_data_from_dict():
    bancoob_data = dict()
    dict_arquivo = {
        'cedente_inscricao_tipo': 2,
        'cedente_inscricao_numero': 12760233000171,
        'cedente_agencia': 3009,
        'cedente_agencia_dv': '0',
        'cedente_conta': 29929,
        'cedente_conta_dv': '4',
        'cedente_agencia_conta_dv': '4',
        'cedente_nome': "LADDER TECNOLOGIA LTDA ME",
        'arquivo_data_de_geracao': 11022019,
        'arquivo_hora_de_geracao': 112000,
        'arquivo_sequencia': 900002
    }

    dict_cobranca = {
        'cedente_agencia': 3009,
        'cedente_agencia_dv': '0',
        'cedente_conta': 29929,
        'cedente_conta_dv': '4',
        'cedente_agencia_conta_dv': '4',
        'carteira_numero': 1,
        'nosso_numero': '99999999',
        'nosso_numero_dv': 9,
        'numero_documento': '9999999999',
        'vencimento_titulo': 28022019,
        'valor_titulo': Decimal('65.00'),
        'especie_titulo': 4,
        'aceite_titulo': 'N',
        'data_emissao_titulo': 11022019,
        'juros_mora_taxa_dia': Decimal('0.00'),
        'valor_abatimento': Decimal('0.00'),
        'identificacao_titulo': 'BOLETO DE TESTE',
        'codigo_protesto': 0,
        'prazo_protesto': 0,
        'codigo_baixa': 0,
        'prazo_baixa': 0,
        'sacado_inscricao_tipo': 2,
        'sacado_inscricao_numero': 27116318002302,
        'sacado_nome': 'MITRA DIOCESANA DE SAO MATEUS',
        'sacado_endereco': 'RUA VITOR TREVIZANI, 45',
        'sacado_bairro': 'CENTRO',
        'sacado_cep': 29785,
        'sacado_cep_sufixo': 000,
        'sacado_cidade': 'VILA VALERIO',
        'sacado_uf': 'ES',
    }

    bancoob_data['arquivo'] = dict_arquivo
    bancoob_data['cobranca'] = dict_cobranca

    return bancoob_data
