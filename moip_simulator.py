import urllib
import httplib

SERVIDOR="http://www.amigosdobaleia.org.br"
URI="/donations/moip"

def do_notify_post(id_transaction, email, status=5, cod_moip=12345678, parcelas=None,valor=5000 ,forma_pagamento=3,tipo_pagamento="CartaoDeCredito"):
    params = urllib.urlencode({'id_transction': id_transaction,
                                'email': email,
                                'cod_moip':cod_moip,
                                'parcelas':parcelas,
                                'valor':valor,
                                'forma_pagamento':forma_pagamento,
                                'tipo_pagamento',tipo_pagamento,
                                'status':status})
    con = httplib.HTTPConnection(SERVIDOR+URI)
    con.request("POST",params)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data