import json
import os

def salvar_dados(form, id_unico):
    caminho = f"dados/salvo_{id_unico}.json"
    os.makedirs("dados", exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(form, f, ensure_ascii=False, indent=4)

def carregar_dados(id_unico):
    caminho = f"dados/salvo_{id_unico}.json"
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
