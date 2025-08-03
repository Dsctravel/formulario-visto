# services/path_utils.py

import os

def get_client_data_path(cliente_id: str) -> str:
    """
    Retorna o caminho completo do JSON de dados para este cliente,
    garantindo que a pasta 'dados_clientes' exista.
    """
    base_dir = os.getcwd()                      # raiz do seu projeto
    data_dir = os.path.join(base_dir, "dados_clientes")
    os.makedirs(data_dir, exist_ok=True)        # cria se não existir
    return os.path.join(data_dir, f"{cliente_id}.json")
