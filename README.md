# extracao-diesel-loginteli

📌 Sobre o Projeto

Este projeto realiza a extração automatizada de preços médios de diesel por estado a partir do portal Loginteli, transformando os dados em uma base estruturada para análise e armazenamento em banco de dados SQLite.

O objetivo é demonstrar habilidades em:

Python
Web Scraping
ETL (Extract, Transform, Load)
Banco de Dados SQLite
SQLAlchemy
Automação de Processos
Tratamento de Erros
Logging
Boas Práticas de Desenvolvimento

O projeto foi desenvolvido com foco em cenários reais de Supply Chain, Transportes e Análise de Dados.

🚀 Funcionalidades
Consulta automática de preços médios de diesel por estado.
Processamento de múltiplos períodos semanais.
Replicação dos preços para todas as unidades de negócio vinculadas ao estado.
Armazenamento estruturado em banco SQLite.
Registro de logs de execução.
Tratamento de falhas e tentativas automáticas de reconexão.
Arquitetura modular para fácil manutenção.
🏗 Arquitetura
Fonte Web (Loginteli)
          │
          ▼
     Extração
          │
          ▼
   Transformação
          │
          ▼
    Pandas DataFrame
          │
          ▼
       SQLite
          │
          ▼
    Power BI / SQL

    
📂 Estrutura do Projeto

extracao-diesel-loginteli/
│
├── data/
│   └── diesel.db
│
├── logs/
│   └── app.log
│
├── src/
│   ├── config.py
│   ├── extractor.py
│   ├── database.py
│   ├── logger.py
│   └── main.py
│
├── tests/
│   └── test_extractor.py
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore


⚙️ Tecnologias Utilizadas
Python 3.11+
Pandas
Requests
SQLAlchemy
SQLite
Tenacity
Pytest
Python Dotenv


📥 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/extracao-diesel-loginteli.git

Entre na pasta:

cd extracao-diesel-loginteli

Crie o ambiente virtual:

python -m venv venv

Ative o ambiente:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt


▶️ Execução

Execute o projeto:

python src/main.py

Ao final da execução será criado:

data/diesel.db

e os logs serão registrados em:

logs/app.log
🗄 Estrutura da Tabela

Tabela:

tb_preco_diesel

Campos:

Campo	Tipo
UNIDADE	TEXT
ESTADO	TEXT
PERIODO	TEXT
SEMANA	INTEGER
VALOR_MEDIA	REAL
DATA_INICIO	DATE
DATA_FIM	DATE


🔍 Exemplo de Consulta SQL

Preço médio por estado:

SELECT
    ESTADO,
    AVG(VALOR_MEDIA) AS PRECO_MEDIO
FROM tb_preco_diesel
GROUP BY ESTADO;

Evolução semanal:

SELECT
    SEMANA,
    AVG(VALOR_MEDIA) AS PRECO_MEDIO
FROM tb_preco_diesel
GROUP BY SEMANA
ORDER BY SEMANA;


📊 Possíveis Evoluções

Integração com Power BI.
Dashboard de acompanhamento do preço do diesel.
Agendamento automático com Task Scheduler.
Persistência incremental.
API para consulta dos preços.
Containerização com Docker.
Pipeline CI/CD com GitHub Actions.


🧪 Testes

Executar os testes:

pytest
💼 Aplicação de Negócio

Este projeto simula uma rotina comum em operações de Supply Chain e Transportes, onde indicadores externos, como o preço do combustível, precisam ser capturados automaticamente para análises de custos, planejamento logístico e tomada de decisão.


👨‍💻 Autor

Natan Gleison

Analista de Dados com experiência em:

Supply Chain
Transportes
Power BI
SQL
Python
Automação de Processos
Desenvolvimento de Dashboards

[LinkedIn:](https://www.linkedin.com/in/natan-silva-3a14b6262/)

GitHub: inserir perfil
