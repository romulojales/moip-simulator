moip-simulator
==============
Simulador simples e direto de notificações do MoIP <http://moip.com.br> para testes em ambientes local ou qualquer outro em uma view
de processamento da aplicação.

 *** Não subistitui o sandbox do moip. ***

Dependencias
===============
python > 2.6

Configurações
==============
 * SERVIDOR: o endereço do servidor com a porta se for diferente da 80
   exemplos: localhost:8000, www.seuservidor.com.br

 * URI: endereço do serviço para receber a notificação
   exemplos: notificado, moip

A composição dos dois forma a url de serviço que você em sua aplicação
recebe o post

www.seuservidor.com.br/moip

	Função:
 		do_notify_post(id_transaction, email, status=5, cod_moip=12345678,\
                parcelas=None,valor=5000 ,forma_pagamento=3,\
                tipo_pagamento="CartaoDeCredito")

 Os parametros contem os valores que o moip vai enviar para você em
sua simulação. O unicos obrigatórios passar é o id_transaction, que é 
o id que você criou em sua aplicação e o e-mail, para identificar o
usuário.

USO
==============
python
import moip_simulator
moip_simulator.do_notify_post(123, fulano@servidor.com.br)
