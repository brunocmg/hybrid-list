
import random
from dataclasses import dataclass


@dataclass
class ResultadoBusca:
    encontrado: bool
    local: str
    posicao: int | None
    iteracoes_binaria: int
    iteracoes_sequencial: int
    total_iteracoes: int


class ListaHibrida:

    def __init__(self, semente=42):
        self.semente = semente

        gerador = random.Random(semente)

        self.regiao_ordenada = sorted(
            gerador.sample(range(1, 100000), 1024)
        )

        self.cauda = []
        self.limite_cauda = 10
        self.total_intercalacoes = 0

    def inserir(self, chave):
        if not isinstance(chave, int):
            raise TypeError("A chave deve ser um inteiro.")

        if self.buscar(chave).encontrado:
            return False, "Chave repetida! Inserção rejeitada."

        self.cauda.append(chave)

        if len(self.cauda) == self.limite_cauda:
            self.intercalar()
            return True, (
                "10ª inserção realizada! "
                "A cauda foi ordenada e intercalada."
            )

        return True, "Chave inserida na cauda com sucesso."

    def buscar(self, chave):
        inicio = 0
        fim = len(self.regiao_ordenada) - 1
        iteracoes_binaria = 0

        # Primeiro: busca binária
        while inicio <= fim:
            iteracoes_binaria += 1
            meio = (inicio + fim) // 2

            valor = self.regiao_ordenada[meio]

            if valor == chave:
                return ResultadoBusca(
                    True,
                    "Região ordenada",
                    meio,
                    iteracoes_binaria,
                    0,
                    iteracoes_binaria
                )

            elif chave < valor:
                fim = meio - 1

            else:
                inicio = meio + 1

        # Segundo: busca sequencial na cauda
        iteracoes_sequencial = 0

        for indice, valor in enumerate(self.cauda):
            iteracoes_sequencial += 1

            if valor == chave:
                return ResultadoBusca(
                    True,
                    "Cauda não ordenada",
                    indice,
                    iteracoes_binaria,
                    iteracoes_sequencial,
                    iteracoes_binaria + iteracoes_sequencial
                )

        return ResultadoBusca(
            False,
            "Não encontrada",
            None,
            iteracoes_binaria,
            iteracoes_sequencial,
            iteracoes_binaria + iteracoes_sequencial
        )

    def intercalar(self):
        cauda_ordenada = sorted(self.cauda)

        resultado = []
        i = 0
        j = 0

        while (
            i < len(self.regiao_ordenada)
            and j < len(cauda_ordenada)
        ):
            if self.regiao_ordenada[i] < cauda_ordenada[j]:
                resultado.append(self.regiao_ordenada[i])
                i += 1
            else:
                resultado.append(cauda_ordenada[j])
                j += 1

        resultado.extend(self.regiao_ordenada[i:])
        resultado.extend(cauda_ordenada[j:])

        self.regiao_ordenada = resultado
        self.cauda.clear()
        self.total_intercalacoes += 1
