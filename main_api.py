from typing import Union
import whois
from fastapi import FastAPI

app = FastAPI()


def consultar_dominio(dominio):
    domain_info = whois.whois(dominio)
    return domain_info


@app.get("/site/{dom}")
def ler_dominio(dom: str, desc: Union[str, None] = None):
    result = consultar_dominio(dom)
    dic_info = {
        "descrição": desc,
        "domínio": result.domain_name,
        "registrante": result.registrar,
        "data de criação": result.creation_date,
        "data de espiração": result.expiration_date,
        "servidores de nome": result.name_servers,
        "status": result.status
    }
    return dic_info
