
import streamlit as st
import pandas as pd
import inspect

from lista_hibrida import ListaHibrida


st.set_page_config(
    page_title="Lista Híbrida",
    page_icon="🔎",
    layout="wide"
)

st.title("Lista Híbrida - Busca e Intercalação")

st.write(
    "Aplicação com região ordenada, busca binária "
    "e cauda não ordenada com busca sequencial."
)

# Manter os dados entre as interações
if "lista" not in st.session_state:
    st.session_state.lista = ListaHibrida(semente=42)

if "resultado" not in st.session_state:
    st.session_state.resultado = None

lista = st.session_state.lista


# Painel de informações
st.subheader("Estado da estrutura")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Região ordenada",
    len(lista.regiao_ordenada)
)

col2.metric(
    "Cauda",
    f"{len(lista.cauda)}/10"
)

col3.metric(
    "Intercalações",
    lista.total_intercalacoes
)

st.progress(len(lista.cauda) / 10)


# Inserção
st.divider()
st.subheader("Inserir uma chave")

chave_insercao = st.number_input(
    "Digite um número inteiro para inserir:",
    step=1,
    value=0,
    key="entrada_insercao"
)

if st.button("Inserir chave"):
    sucesso, mensagem = lista.inserir(
        int(chave_insercao)
    )

    if sucesso:
        st.success(mensagem)
    else:
        st.warning(mensagem)


# Busca
st.divider()
st.subheader("Buscar uma chave")

chave_busca = st.number_input(
    "Digite o número que deseja buscar:",
    step=1,
    value=0,
    key="entrada_busca"
)

if st.button("Buscar chave"):
    st.session_state.resultado = lista.buscar(
        int(chave_busca)
    )

    st.session_state.chave_pesquisada = int(chave_busca)

resultado = st.session_state.resultado

if resultado is not None:

    st.write(
        "Chave pesquisada:",
        st.session_state.chave_pesquisada
    )

    if resultado.encontrado:
        st.success(
            f"Chave encontrada em: {resultado.local}"
        )
        st.write(
            f"Posição (índice iniciado em zero): "
            f"{resultado.posicao}"
        )
    else:
        st.error("Chave não encontrada.")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Iterações binárias",
        resultado.iteracoes_binaria
    )

    c2.metric(
        "Iterações sequenciais",
        resultado.iteracoes_sequencial
    )

    c3.metric(
        "Total de iterações",
        resultado.total_iteracoes
    )


# Visualização dos dados
st.divider()
st.subheader("Visualização das regiões")

aba1, aba2 = st.tabs([
    "Região ordenada",
    "Cauda não ordenada"
])

with aba1:
    st.write(
        "Total de elementos:",
        len(lista.regiao_ordenada)
    )

    tabela_ordenada = pd.DataFrame({
        "Índice": range(len(lista.regiao_ordenada)),
        "Chave": lista.regiao_ordenada
    })

    st.dataframe(
        tabela_ordenada,
        hide_index=True,
        use_container_width=True
    )

with aba2:
    if lista.cauda:
        tabela_cauda = pd.DataFrame({
            "Índice": range(len(lista.cauda)),
            "Chave": lista.cauda
        })

        st.dataframe(
            tabela_cauda,
            hide_index=True,
            use_container_width=True
        )
    else:
        st.info("A cauda está vazia.")


# Componentes e código correspondente
st.divider()
st.subheader("Componentes utilizados")

st.write(
    "Abaixo estão os principais componentes "
    "da solução e seus códigos-fonte."
)

componentes = {
    "Geração da região ordenada":
        ListaHibrida.__init__,

    "Inserção de chaves":
        ListaHibrida.inserir,

    "Busca binária e sequencial":
        ListaHibrida.buscar,

    "Ordenação e intercalação":
        ListaHibrida.intercalar
}

for nome, metodo in componentes.items():
    with st.expander(nome):
        st.code(
            inspect.getsource(metodo),
            language="python"
        )


# Reiniciar aplicação
st.divider()

if st.button("Reiniciar estrutura"):
    st.session_state.lista = ListaHibrida(semente=42)
    st.session_state.resultado = None
    st.rerun()
