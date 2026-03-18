import json
import socket
import logging

def main():
    # 1 Conectar ao server
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1",5000))

    # 2 Receber dados das litas de ativos do server
    receive_bytes = s.recv(1024)
    receive_string = receive_bytes.decode("utf-8")
    assets_receive = receive_string.split(",")

    # 3 Pedir pro usuário escolher um ativo
    selected_assets = input(f"Lista de ativos{assets_receive}\n" \
                    f"Escolha um(s) tipo(s) de ativo(s) para ver a sua taxa\n"
                    f"Use ',' como Separador!!\n")

    # 4 Envio dos dados escolhidos:
    try:
        s.send(selected_assets.encode("utf-8"))

    except OSError:
        logging.error("Erro ao enviar lista de ativos ao server")
        raise

    # 5 Ler dados reais trazidos pelo server:

    assets_data = s.recv(1024)
    assets_rates = assets_data.decode("utf-8")

    try:
        assets_rates = json.loads(assets_rates)
    except json.JSONDecodeError:
        logging.error("Erro! Esse ativos não existe em ASSESTS")
        s.close()
        return
    
    valid_assets_receive = assets_rates["rates"]
    invalid_assets_receive = assets_rates["invalid"]
    

    # 6 Mostrar informações para o usuário existe em ASSETS:
    print(f"Informações dos Ativos pedidos\n")
    for asset, rate in valid_assets_receive.items():
        print(f"Ativo: {asset} -> Taxa: {rate}")

     # 6 Mostrar informações para o usuário não existe em ASSETS:
    for asset in invalid_assets_receive:
        print(f"Ativo inexistente em ASSETS: {asset}")

    # 7 Fecha conexão:
    s.close()

if __name__ == "__main__":
    main()