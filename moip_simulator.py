import urllib
import httplib

SERVIDOR="localhost:8000"
URI="notificador"

def do_notify_post(id_transaction, email, status=5, cod_moip=12345678, parcelas=None,valor=5000 ,forma_pagamento=3,tipo_pagamento="CartaoDeCredito"):
    params = urllib.urlencode({'id_transction': id_transaction,
                                'email': email,
                                'cod_moip':cod_moip,
                                'parcelas':parcelas,
                                'valor':valor,
                                'forma_pagamento':forma_pagamento,
                                'tipo_pagamento':tipo_pagamento,
                                'status':status})
    con = httplib.HTTPConnection(SERVIDOR)
    con.request("POST",URI,params)
    response = con.getresponse()
    print response.status, response.reason
    data = response.read()
    print data