import json
import socket
from funcoes_aux.api_client import ASSETS, get_asset
import logging


def main():
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0",5000))
    s.listen(1)
    conn, addr = s.accept()     # conn = a conexao, addr = endereço do cliente

    # 1. pega as chaves do ASSETS e junta em string
    assets_string = ",".join(ASSETS.keys())

    # 2. converte para bytes e envia
    assets_bytes   = assets_string.encode("utf-8")

    # 3 Envio dos dados:
    try:
        conn.send(assets_bytes)

    except OSError:
        logging.error("Erro ao enviar lista de ativos ao cliente")
        raise

    receive_bytes = conn.recv(1024)
    receive_string = receive_bytes.decode("utf-8")
    assets_receive = [a.strip() for a in receive_string.split(",")]

    valid_assets = [asset for asset in assets_receive if asset in ASSETS]
    invalid_assets = [asset for asset in assets_receive if asset not in ASSETS]
    # 4 Ler dados reais:

    asset_dic = {asset:get_asset(ASSETS[asset]) for asset in valid_assets}

    # 5 Envio dos resultados dos ativos:
    response = {
        "rates": asset_dic,
        "invalid": invalid_assets
    }
    
    response = json.dumps(response).encode("utf-8")

    try:
        conn.send(response)

    except OSError:
        logging.error("Erro ao enviar lista dos resultados dos ativos pedidos")
        raise

    # 6 Encerrando conexão:
    conn.close()

if __name__ == "__main__":
    main()
    