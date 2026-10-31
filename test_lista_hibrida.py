
import pytest
from lista_hibrida import ListaHibrida


def test_quantidade_inicial():
    lista = ListaHibrida()

    assert len(lista.regiao_ordenada) == 1024
    assert len(lista.cauda) == 0


def test_regiao_ordenada():
    lista = ListaHibrida()

    assert lista.regiao_ordenada == sorted(
        lista.regiao_ordenada
    )


def test_numeros_distintos():
    lista = ListaHibrida()

    assert len(set(lista.regiao_ordenada)) == 1024


def test_semente_reprodutivel():
    lista1 = ListaHibrida(semente=42)
    lista2 = ListaHibrida(semente=42)

    assert lista1.regiao_ordenada == lista2.regiao_ordenada


def test_insercao():
    lista = ListaHibrida()

    sucesso, _ = lista.inserir(-100)

    assert sucesso is True
    assert lista.cauda == [-100]


def test_rejeitar_repetidos():
    lista = ListaHibrida()

    lista.inserir(-100)
    sucesso, _ = lista.inserir(-100)

    assert sucesso is False
    assert len(lista.cauda) == 1


def test_rejeitar_repetido_na_regiao():
    lista = ListaHibrida()

    chave = lista.regiao_ordenada[0]
    sucesso, _ = lista.inserir(chave)

    assert sucesso is False
    assert len(lista.cauda) == 0


def test_busca_binaria():
    lista = ListaHibrida()

    chave = lista.regiao_ordenada[500]
    resultado = lista.buscar(chave)

    assert resultado.encontrado is True
    assert resultado.local == "Região ordenada"
    assert resultado.iteracoes_binaria > 0
    assert resultado.iteracoes_sequencial == 0


def test_busca_sequencial():
    lista = ListaHibrida()

    lista.inserir(-100)
    resultado = lista.buscar(-100)

    assert resultado.encontrado is True
    assert resultado.local == "Cauda não ordenada"
    assert resultado.iteracoes_sequencial == 1


def test_chave_inexistente():
    lista = ListaHibrida()

    resultado = lista.buscar(-999)

    assert resultado.encontrado is False
    assert resultado.local == "Não encontrada"
    assert resultado.iteracoes_sequencial == 0


def test_total_iteracoes():
    lista = ListaHibrida()

    lista.inserir(-100)
    resultado = lista.buscar(-100)

    assert resultado.total_iteracoes == (
        resultado.iteracoes_binaria
        + resultado.iteracoes_sequencial
    )


def test_intercalacao_automatica():
    lista = ListaHibrida()

    for numero in range(-10, 0):
        lista.inserir(numero)

    assert len(lista.regiao_ordenada) == 1034
    assert len(lista.cauda) == 0
    assert lista.total_intercalacoes == 1

    assert lista.regiao_ordenada == sorted(
        lista.regiao_ordenada
    )


def test_novas_insercoes_apos_intercalacao():
    lista = ListaHibrida()

    for numero in range(-10, 0):
        lista.inserir(numero)

    sucesso, _ = lista.inserir(-20)

    assert sucesso is True
    assert lista.cauda == [-20]


def test_busca_apos_intercalacao():
    lista = ListaHibrida()

    for numero in range(-10, 0):
        lista.inserir(numero)

    resultado = lista.buscar(-5)

    assert resultado.encontrado is True
    assert resultado.local == "Região ordenada"
    assert resultado.iteracoes_sequencial == 0


def test_cauda_preserva_ordem_insercao():
    lista = ListaHibrida()

    lista.inserir(-3)
    lista.inserir(-1)
    lista.inserir(-2)

    assert lista.cauda == [-3, -1, -2]
