import requests


def obter_resultados_loteria():
    url = "https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena"

    try:
        print("Buscando resultados da Mega-Sena...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        dados = response.json()

        concurso = dados.get("numero", "N/A")
        data = dados.get("dataApuracao", "N/A")
        numeros_sorteados = dados.get("dezenasSorteadasOrdemSorteio", [])
        ganhadores = dados.get("listaRateioPremio", [])

        print(f"\nConcurso: {concurso} - Data: {data}")
        print(f"Números Sorteados: {', '.join(numeros_sorteados)}")
        print("\nGanhadores:")

        for premio in ganhadores:
            descricao = premio.get("descricaoFaixa", "N/A")
            quantidade = premio.get("quantidadePremiada", 0)
            valor = premio.get("valorPremio", "0.00")
            valor_formatado = f"R$ {float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            print(f"{descricao}: {quantidade} ganhador(es) - {valor_formatado}")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter os dados: {e}")
    except ValueError:
        print("Erro ao processar os dados da API.")


if __name__ == "__main__":
    obter_resultados_loteria()