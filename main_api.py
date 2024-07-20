from typing import Union
import whois
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

def consultar_dominio(dominio):
    domain_info = whois.whois(dominio)
    return domain_info

# Configuração de CORS para permitir todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/site/{dom}")
def ler_dominio(dom: str, desc: Union[str, None] = None):
    result = consultar_dominio(dom)
    dic_info = {
        "descrição": desc,
        "domínio": result.domain_name,
        "e-mails": result.emails,
        "data de criação": result.creation_date,
        "data de expiração": result.expiration_date,
        "servidores de nome": result.name_servers,
        "status": result.status
    }
    return dic_info
