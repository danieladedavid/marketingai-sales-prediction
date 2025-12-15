# MarketingAI – Sistema de Previsão de Vendas Mensais

## 1. Visão Geral do Projeto

O **MarketingAI** é um sistema completo de previsão de vendas mensais por loja e item, integrando análise de dados, clusterização, modelagem preditiva e uma aplicação interativa em Streamlit. O objetivo é fornecer uma ferramenta capaz de apoiar decisões comerciais com base em dados históricos, padrões temporais e técnicas modernas de machine learning.

O projeto foi desenvolvido como parte do Programa de Formação de Cientista de Dados Profissional (CDPro).


A solução combina:

- Análise exploratória de dados (EDA)
- Engenharia de features
- Clusterização com K-Means
- Modelos preditivos de regressão
- Pipeline estruturado
- Aplicação web desenvolvida em Streamlit
- Repositório organizado para facilitar manutenção e reprodutibilidade

---

## Contexto do Problema e Objetivo do Negócio

O projeto **MarketingAI** foi desenvolvido para atender uma cadeia fictícia de shoppings denominada *MarketingAI*, com o objetivo de apoiar decisões estratégicas por meio da análise preditiva de vendas. 

A organização possui diversas lojas distribuídas por regiões distintas, com grande variedade de produtos e histórico extenso de vendas mensais. Esse cenário torna desafiador o entendimento manual do comportamento de vendas e a identificação de padrões relevantes que auxiliem no planejamento comercial.

Diante disso, o projeto busca responder perguntas como:

- Quais padrões de venda podem ser identificados automaticamente?
- Existem grupos de produtos com comportamentos semelhantes?
- Como o preço médio influencia o volume de vendas?
- É possível prever as vendas futuras de forma consistente para apoiar decisões de estoque e estratégia comercial?

---

## Organização do Repositório

O repositório foi estruturado de forma modular, seguindo boas práticas de projetos de ciência de dados, permitindo fácil entendimento, manutenção e reprodutibilidade.

Os diretórios principais são:

- **data/**: contém os dados do projeto  
  - `raw/`: dados brutos, sem tratamento  
  - `processed/`: dados tratados e prontos para análise e modelagem  

- **notebooks/**: notebooks Jupyter utilizados para análise exploratória, clusterização e modelagem preditiva  

- **src/**: código-fonte do projeto, incluindo modelos treinados e scripts auxiliares  

- **app/**: aplicação web desenvolvida em Streamlit para visualização e predição interativa  

- **tests/**: testes automatizados utilizados no pipeline de integração contínua  

- **.github/**: configurações de CI/CD com GitHub Actions  

Essa organização facilita tanto a avaliação acadêmica quanto a evolução futura do projeto.

---

## Metodologia de Análise Preditiva

A metodologia adotada baseia-se na aplicação de técnicas de **machine learning** para extrair conhecimento da base de dados de vendas da MarketingAI.

Inicialmente, foi realizada uma **análise exploratória dos dados (EDA)** para compreensão da distribuição das vendas, comportamento temporal, sazonalidade e possíveis outliers.

Em seguida, aplicou-se o algoritmo **K-Means**, com o objetivo de realizar a **clusterização automática dos dados**, permitindo identificar grupos de produtos com padrões semelhantes de preço e comportamento ao longo do tempo. Essa etapa trouxe novos insights para a análise, ao segmentar os dados de forma não supervisionada.

Posteriormente, os clusters gerados foram incorporados como uma variável explicativa no modelo preditivo, enriquecendo a capacidade do modelo em capturar padrões complexos.

Para a etapa de previsão de vendas, foram avaliados diferentes algoritmos de regressão. O modelo final selecionado foi a **Ridge Regression**, por apresentar bom desempenho preditivo, estabilidade e maior interpretabilidade, características importantes em um contexto acadêmico e de negócio.

---

## Resultados Obtidos

Os resultados da etapa de clusterização indicaram a formação de **cinco grupos distintos**, cada um representando um perfil específico de produtos e comportamento de vendas.

Entre os clusters identificados, dois se destacaram de forma mais evidente:

- Um cluster composto por produtos de **alto valor unitário**, porém com **baixo volume de vendas**, caracterizando um perfil de produtos premium.
- Outro cluster composto por produtos de **baixo valor unitário**, mas com **alto volume de vendas**, representando itens de giro elevado.

Os demais três clusters apresentaram comportamentos intermediários, com valores médios tanto de preço quanto de vendas, evidenciando padrões mais equilibrados.

Na etapa preditiva, a combinação de variáveis temporais, médias históricas e informações de cluster permitiu gerar previsões consistentes de vendas mensais, fornecendo suporte para análises de tendência e planejamento comercial.

---

## Aplicação Web e Visualização dos Resultados

Como etapa final do projeto, foi desenvolvida uma **aplicação web interativa em Streamlit**, que permite a exploração prática dos resultados obtidos.

A aplicação possibilita:

- Seleção de loja, item, ano e mês
- Visualização de informações agregadas por cluster
- Análise das características gerais de cada cluster
- Geração de previsões de vendas mensais com base no modelo treinado

Essa interface transforma os resultados técnicos do projeto em uma ferramenta acessível, aproximando a análise de dados do contexto real de tomada de decisão.

---


Diante disso, o projeto busca responder perguntas como:

- Quais padrões de venda podem ser identificados automaticamente?
- Existem grupos de produtos com comportamentos semelhantes?
- Como o preço médio influencia o volume de vendas?
- É possível prever as vendas futuras de forma consistente para apoiar decisões de estoque e estratégia comercial?

---

## 2. Estrutura do Repositório

```
marketingai-sales-prediction/
│
├── data/
│   ├── raw/
│   │   └── base_mensal.csv
│   │
│   └── processed/
│       ├── df_processed.parquet
│       └── df_cluster_id.parquet
│
├── src/
│   ├── models/
│   │   ├── best_model.pkl
│   │   ├── preprocess_predicao.pkl
│   │   ├── kmeans_cluster.pkl
│   │   └── scaler_cluster.pkl
│   │
│   ├── features/
│   └── visualization/
│
├── app/
│   └── streamlit_app.py
│
├── notebooks/
│   ├── 1_analysis.ipynb
│   ├── 2_clustering.ipynb
│   └── 3_prediction.ipynb
│
├── tests/
│   ├── test_data_integrity.py
│   └── test_models.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 3. Estrutura dos Dados

### Dados brutos
```
data/raw/base_mensal.csv
```

### Dados processados
```
data/processed/df_processed.parquet
data/processed/df_cluster_id.parquet
```

Esses arquivos garantem reprodutibilidade total da análise e permitem executar os notebooks exatamente como no projeto original.

---

## 4. Instalação

### 4.1 Requisitos

- Python 3.11+
- pip instalado
- Git

Principais bibliotecas (listadas em `requirements.txt`):

- pandas  
- numpy  
- scikit-learn  
- lightgbm  
- xgboost  
- matplotlib  
- seaborn  
- joblib  
- streamlit  
- pytest  

---

### 4.2 Instalando o projeto

Clone o repositório:

```
git clone https://github.com/SEU-USUARIO/marketingai-sales-prediction.git
cd marketingai-sales-prediction
```

Crie e ative o ambiente virtual:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1   (Windows PowerShell)
```

Instale as dependências:

```
pip install -r requirements.txt
```

---

## 5. Uso do Projeto

### 5.1 Executar Análise e Modelagem nos Notebooks

Abra os notebooks em:

```
notebooks/
```

Execute na ordem:

1. `1_analysis.ipynb` – Análise exploratória  
2. `2_clustering.ipynb` – Clusterização  
3. `3_prediction.ipynb` – Treinamento e avaliação dos modelos  

### Caminhos usados na leitura dos dados:

```python
df = pd.read_csv('data/raw/base_mensal.csv')
df_processed = pd.read_parquet('data/processed/df_processed.parquet')
df_cluster = pd.read_parquet('data/processed/df_cluster_id.parquet')
```

Todos os notebooks funcionam com caminhos relativos, garantindo reprodutibilidade no ambiente do usuário.

---

## 6. Executar a Aplicação Streamlit

Com o ambiente virtual ativado:

```
streamlit run app/streamlit_app.py
```

A aplicação abre no navegador em:

```
http://localhost:8501
```

A aplicação permite:

- escolher loja, item, ano e mês
- inserir preço médio
- consultar médias históricas
- verificar cluster atribuído
- gerar a previsão do modelo final

Caminho interno do dataset usado pela aplicação:

```python
df = pd.read_parquet('data/processed/df_cluster_id.parquet')
```

---

## 7. Metodologia

A metodologia segue as boas práticas de ciência de dados e aprendizado de máquina, envolvendo:

### 7.1 Análise Exploratória (EDA)

- distribuição temporal das vendas  
- sazonalidade  
- análise por loja e item  
- detecção de valores misising, outliers  
- correlações  

### 7.2 Engenharia de Features

- `time_index`  
- `month_sin`, `month_cos` (codificação cíclica)
- `mean_price`  
- médias históricas:
  - `item_mean_sales`
  - `store_mean_sales`
  - `store_item_mean_sales`

### 7.3 Clusterização com K-Means

- definição de número de clusters (método do cotovelo)
- clusterização com:
  - mean_price
  - time_index
  - month_sin / month_cos  
- incorporação do `cluster_id` ao modelo final
- interpretação visual dos clusters

### 7.4 Modelagem Preditiva

Modelos avaliados:

- Ridge Regression  
- Random Forest  
- LightGBM  
- XGBoost  

Métricas:

- RMSE  
- MAE  
- R²  
- tempo de treinamento  

O modelo final selecionado foi:

**Ridge Regression**, por:

- desempenho consistente  
- interpretabilidade  
- baixo risco de overfitting  
- simplicidade operacional  

### 7.5 Deploy

O modelo final é utilizado via aplicação Streamlit, permitindo interação com os dados e previsão instantânea.

---

## 8. Deploy da Aplicação

Para publicar no **Streamlit Community Cloud**:

1. Suba todo o repositório no GitHub  
2. Acesse https://streamlit.io/cloud  
3. Conecte sua conta ao GitHub  
4. Selecione este repositório  
5. Defina o arquivo principal:

```
app/streamlit_app.py
```

6. Confirme o uso do `requirements.txt`

A plataforma realizará o build automático e exibirá a URL final da aplicação.

---

## 9. CI/CD com GitHub Actions

O repositório contém um fluxo de trabalho automático:

```
.github/workflows/ci.yml
```

Ele executa:

- instalação das dependências  
- testes unitários  
- validação do projeto a cada push ou pull request  

Testes mock garantem estabilidade e boa prática sem exigir datasets grandes.

---

## 10. Contribuição

Fluxo sugerido:

1. Fazer fork do repositório  
2. Criar uma nova branch:  
```
git checkout -b feature/nova-feature
```
3. Implementar mudanças  
4. Incluir testes, quando aplicável  
5. Enviar um Pull Request descrevendo claramente a contribuição  

---

## 11. Autora

**Daniela de David**  
Projeto desenvolvido como parte do Programa de Formação Cientista de Dados Profissional (CDPro), com o objetivo de aplicar técnicas de ciência de dados e machine learning em um problema de negócio realista. 

---

## 12. Licença

Este projeto é distribuído sob a licença **MIT**, permitindo:

- uso  
- modificação  
- distribuição  
- estudo  

Os termos completos estão no arquivo `LICENSE`.

---

## 13. Agradecimentos

- Ao Programa de Formação CDPro (Cientista de Dados Profissional) que tem como grande Mestre, Eduardo Rocha (obrigada por ensinar sem complicar!)   
- À comunidade open source (pandas, scikit-learn, streamlit etc.), cujas bibliotecas e ferramentas tornaram este trabalho possível.

