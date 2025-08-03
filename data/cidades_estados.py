import requests

# URLs da API do IBGE
IBGE_ESTADOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
IBGE_MUNICIPIOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/municipios"


def fetch_states():
    """
    Busca a lista de estados brasileiros (com IDs e siglas) na API do IBGE.
    Retorna uma lista de dicionários com informações de cada estado.
    """
    resp = requests.get(IBGE_ESTADOS_URL)
    resp.raise_for_status()
    return resp.json()


def fetch_municipios(uf_id):
    """
    Busca a lista de municípios para o estado especificado pelo ID (uf_id).
    Retorna uma lista de dicionários com informações de cada município.
    """
    url = IBGE_MUNICIPIOS_URL.format(uf_id)
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def get_cidades_por_estado():
    """
    Retorna um dicionário mapeando cada sigla de estado a uma lista
    ordenada de nomes de municípios.
    Exemplo: { 'SP': ['Adamantina', 'Adolfo', ...], 'RJ': [...] }
    """
    estados = fetch_states()
    cidades_por_estado = {}
    for est in estados:
        uf_sigla = est["sigla"]
        uf_id = est["id"]
        municipios = fetch_municipios(uf_id)
        nomes = [m["nome"] for m in municipios]
        cidades_por_estado[uf_sigla] = sorted(nomes)
    return cidades_por_estado


def get_todas_cidades():
    """
    Retorna uma lista ordenada contendo todas as cidades do Brasil.
    """
    cidades_por_estado = get_cidades_por_estado()
    todas = []
    for lista in cidades_por_estado.values():
        todas.extend(lista)
    return sorted(todas)


if __name__ == "__main__":
    # Exemplo de uso: imprime todas as cidades no console
    for cidade in get_todas_cidades():
        print(cidade)
