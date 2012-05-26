# -*- coding: utf-8 -*-
import urllib
import httplib

SERVIDOR="localhost:8000"
URI="notificador"

AUTORIZADO = 1	#Pagamento já foi realizado porém ainda não foi creditado na Carteira MoIP recebedora (devido ao floating da forma de pagamento)
INICIADO =	2	#Pagamento está sendo realizado ou janela do navegador foi fechada (pagamento abandonado)
BOLETO_IMPRESSO	= 3	#Boleto foi impresso e ainda não foi pago
CONCLUIDO = 4	#Pagamento já foi realizado e dinheiro já foi creditado na Carteira MoIP recebedora
CANCELADO = 5	#Pagamento foi cancelado pelo pagador, instituição de pagamento, MoIP ou recebedor antes de ser concluído
EM_ANALISE = 6	#Pagamento foi realizado com cartão de crédito e autorizado, porém está em análise pela Equipe MoIP. Não existe garantia de que será concluído
ESTORNADO = 7   #Pagamento foi estornado pelo pagador, recebedor, instituição de pagamento ou MoIP

#Formas de pagamento, a capitalização da letra importa!
DEBITO = "DebitoBancario" # Débito em conta no domicilio bancário do pagador
FINANCIAMENTO = "FinanciamentoBancario" # Financiamento obtido junto ao domicílio bancário do pagador e o montante total debitado diretamente da conta e creditado na Carteira MoIP do recebedor
BOLETO = "BoletoBancario" # Boleto bancário impresso pelo pagador
CARTAO_CREDITO = "CartaoDeCredito" #	Cartão de crédito
CARTAO_DEBITO = "CartaoDeDebito" # Cartão de débito Visa Electron (apenas para correntistas do Bradesco)
MOIP = "CarteiraMoIP" #	Diretamente da Carteira MoIP do pagador
NDEF = "NaoDefinida" #	Ainda não definida pelo pagador

def do_notify_post(id_transacao, email, status_pagamento = CONCLUIDO, cod_moip = 12345678,
                   parcelas = None, valor = 5000, forma_pagamento = 3, 
                   tipo_pagamento = CARTAO_CREDITO, extra_params = {}):
    
    dicionario = {'id_transacao': id_transacao,
                 'email_consumidor': email,
                'cod_moip': cod_moip,
                 'parcelas': parcelas,
                 'valor': valor,
                 'forma_pagamento': forma_pagamento,
                 'tipo_pagamento': tipo_pagamento,
                 'status_pagamento': status_pagamento}
      
    dicionario.update(extra_params)

    params = urllib.urlencode(dicionario)
    con = httplib.HTTPConnection(SERVIDOR)
    con.request("POST", URI+"?"+params)
    response = con.getresponse()
    print response.status, response.reason
    data = response.read()
    print data

    