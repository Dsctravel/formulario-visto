# formulario.py
import secrets
import datetime
import streamlit as st

st.set_page_config(page_title="Gerador de Link Personalizado", layout="centered")
st.title("Gerador de Link Personalizado")
st.info("BUILD: " + datetime.datetime.utcnow().isoformat() + "Z")

# ------------------ helpers ------------------
def get_cliente_from_url():
    # API nova
    try:
        v = st.query_params.get("cliente", None)
        if isinstance(v, list):
            return v[0] if v else None
        return v
    except Exception:
        pass
    # Fallback experimental (versões antigas)
    try:
        qp = st.experimental_get_query_params()
        if "cliente" in qp and qp["cliente"]:
            return qp["cliente"][0]
    except Exception:
        pass
    return None

def set_cliente_in_url(cid: str) -> bool:
    # API nova
    try:
        st.query_params.update({"cliente": cid})
        return True
    except Exception:
        pass
    # Fallback experimental
    try:
        st.experimental_set_query_params(cliente=cid)
        return True
    except Exception:
        return False

def force_param_with_js(cid: str):
    # Força o parâmetro na barra do navegador e recarrega
    st.markdown(
        f"""
        <script>
        (function() {{
          try {{
            var url = new URL(window.location.href);
            if (!url.searchParams.get('cliente')) {{
              url.searchParams.set('cliente', '{cid}');
              window.history.replaceState(null, '', url.toString());
              window.location.reload();
            }}
          }} catch (e) {{
            console.error('param fallback error', e);
          }}
        }})();
        </script>
        """,
        unsafe_allow_html=True,
    )

# ------------------ lógica principal ------------------
cliente = get_cliente_from_url()
if not cliente:
    novo_id = secrets.token_urlsafe(6)
    # 1) tenta via API do Streamlit
    set_cliente_in_url(novo_id)
    # 2) fallback JS (garante no Render)
    force_param_with_js(novo_id)
    # evita renderizar o resto antes do reload
    st.stop()

# se chegou aqui, a URL já deve conter ?cliente=
cliente = get_cliente_from_url()
link_completo = f"https://formulario.dsctravel.com.br/?cliente={cliente}"

st.success(f"ID do cliente: {cliente}")
st.markdown("Link completo para este cliente:")
st.code(link_completo, language="text")

# Botão para gerar outro ID (útil para testar)
if st.button("Gerar novo ID"):
    novo_id = secrets.token_urlsafe(6)
    set_cliente_in_url(novo_id)
    force_param_with_js(novo_id)
    st.stop()
