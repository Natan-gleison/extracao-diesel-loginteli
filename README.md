# Monitoramento de Preços de Diesel (Python)

Robô em Python para coletar o preço médio semanal de diesel (S10) por estado, no site público [loginteli.com.br](https://www.loginteli.com.br/), e consolidar o resultado por unidade/filial em uma planilha Excel.

Este projeto é a tradução completa para Python de uma consulta originalmente feita em **Power Query (M)**, mantendo a mesma lógica de negócio:

- 1 requisição por **estado** e por **semana** (nunca por unidade, evitando chamadas duplicadas quando várias unidades ficam no mesmo estado).
- Junção (`merge`) do preço do estado com a tabela de unidades — cada unidade do estado recebe o mesmo preço médio.
- Quebra do período em colunas `Inicio Periodo` / `Fim Periodo`.
- Cálculo de "semana do ano" equivalente ao `Date.WeekOfYear` padrão do Power Query (semana começando no domingo).

## 📂 Estrutura do projeto

```
monitoramento-precos-diesel-python/
│
├── data/
│   └── output/               # Planilhas Excel geradas
│
├── logs/
│   └── execucao.log          # Log de cada execução
│
├── src/
│   ├── config.py             # Unidades por estado, semanas a consultar, parâmetros da requisição
│   ├── scraper.py            # Requisição HTTP e extração do valor (equivalente à função Consulta1/fnBuscarDiesel)
│   ├── parser.py             # Junção com unidades, seleção/ordenação de colunas, split de período
│   ├── exporter.py           # Exportação do resultado final para Excel
│   └── utils.py              # Logging, timestamp e cálculo de semana do ano
│
├── tests/
│   ├── test_utils.py
│   ├── test_scraper.py
│   └── test_parser.py
│
├── main.py                    # Ponto de entrada (orquestra todo o fluxo)
├── requirements.txt
└── README.md
```

## 🔁 Equivalência com o Power Query original

| Power Query (M)                                   | Python                                  |
|-----------------------------------------------------|------------------------------------------|
| `Consulta1` / query `fnBuscarDiesel`                | `src/scraper.py::buscar_preco_diesel`    |
| `TabelaUnidades`                                    | `src/config.py::UNIDADES_POR_ESTADO`     |
| `Semanas`                                           | `src/config.py::SEMANAS`                 |
| `Estados` (`List.Distinct`)                         | `src/parser.py::estados_distintos`       |
| `Registros` (`List.Combine`/`List.Transform`)       | `main.py::coletar_registros`             |
| `ComUnidades` (`Table.Join`, `JoinKind.Inner`)      | `src/parser.py::montar_tabela_final` (merge) |
| `Selecionada` / `Tipada` / `Ordenada`               | `src/parser.py::montar_tabela_final`     |
| `Dividir Coluna por Delimitador` (`PERIODO` → datas)| `src/parser.py::montar_tabela_final`     |
| `Date.WeekOfYear`                                   | `src/utils.py::semana_do_ano`            |

## 🚀 Como usar

1. Clone o repositório e crie um ambiente virtual (recomendado):

   ```bash
   git clone https://github.com/seu-usuario/monitoramento-precos-diesel-python.git
   cd monitoramento-precos-diesel-python
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Ajuste, se necessário, as unidades e os períodos em `src/config.py`.

4. Execute:

   ```bash
   python main.py
   ```

5. O resultado será gerado em `data/output/Precos_Diesel_<data-hora>.xlsx`.

O andamento da execução fica registrado em `logs/execucao.log`, incluindo eventuais falhas de requisição (nesse caso, a linha correspondente fica com `VALOR_MEDIA` vazio, em vez de interromper toda a coleta).

## 🧩 Adaptando para o seu cenário

- **Unidades/estados**: edite `UNIDADES_POR_ESTADO` em `src/config.py`.
- **Períodos**: edite `SEMANAS` em `src/config.py` (ou gere essa lista programaticamente, se preferir).
- **Produto consultado**: ajuste `PRODUTO_PADRAO` em `src/config.py`.
- **Velocidade da coleta**: ajuste `DELAY_ENTRE_REQUISICOES_SEGUNDOS` em `src/config.py` — um intervalo entre requisições ajuda a não sobrecarregar o site consultado.

## ✅ Testes

Os testes usam HTML simulado e não fazem chamadas de rede reais:

```bash
pytest
```

## ⚠️ Uso responsável

Este robô faz requisições HTTP simples (sem burlar proteções) a uma página pública. Antes de rodar em produção ou aumentar o volume de chamadas, vale revisar os termos de uso do site consultado e manter um intervalo razoável entre requisições (`DELAY_ENTRE_REQUISICOES_SEGUNDOS`).

## 🛣️ Possíveis melhorias futuras

- Cache local dos resultados já coletados, para não repetir requisições em re-execuções.
- Retry automático com backoff em caso de falha de rede.
- Suporte a múltiplos produtos em uma única execução.
- Mover `UNIDADES_POR_ESTADO` e `SEMANAS` para um arquivo de configuração externo (YAML/JSON).




