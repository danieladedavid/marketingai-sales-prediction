# 🚀 MarketingAI – Previsão de Vendas Mensais por Loja e Item

O **MarketingAI** é um sistema completo de previsão de vendas mensais por loja e item, integrando análise de dados, clusterização, modelagem preditiva e uma aplicação interativa em Streamlit.

O projeto foi desenvolvido como parte de um **Programa de Formação de Cientista de Dados**, demonstrando domínio técnico aplicado ao varejo.

---

## 🧾 Requisitos

O projeto foi desenvolvido e testado com:

- **Python 3.11.9 (recomendado)**  
- Compatível com:
  - **Windows 10/11**
  - **Linux (Ubuntu 20.04+)**
  - **macOS (Intel e Apple Silicon)**

Recomenda-se criar o ambiente virtual usando:

```
python -m venv .venv
```

E ativar:

- Windows:
  ```
  .\.venv\Scripts\Activate.ps1
  ```
- Linux / macOS:
  ```
  source .venv/bin/activate
  ```

Certifique-se de que o VS Code está usando este ambiente virtual como interpretador principal.

---
## 🌐 Visão Geral

O MarketingAI entrega:

- previsão de vendas mensais por loja e item  
- clusterização inteligente  
- interface Streamlit para uso imediato  
- pipelines organizados para EDA, modelagem e deploy  

Ideal para planejamento comercial e análise estratégica.

---

## 🧩 Arquitetura da Solução

### 🔍 1. Análise Exploratória (EDA) e Processamento dos dados
- comportamento temporal  
- sazonalidade  
- análise por loja, item, região, categoria 
- identificação e análise de missing, NAN e outliers  

### 🧠 2. Clusterização (K-Means)
- escolha de número de clusters (método do cotovelo)  
- uso de variáveis temporais + mean_price  
- geração de `cluster_id` como feature  

### 📈 3. Modelagem Preditiva
Modelos avaliados:
- Ridge Regression  
- Random Forest  
- LightGBM  
- XGBoost  

**Modelo final:** Ridge Regression  
Selecionado por equilíbrio entre desempenho, robustez e interpretabilidade.

### 🖥 4. Aplicação Web (Streamlit)
- entrada de loja, item, mês, ano e preço médio  
- previsão em tempo real  
- exibição de cluster, séries históricas e médias  
- interface intuitiva  

---

## 📁 Estrutura do Repositório

```
marketingai-sales-prediction/
├── app/                # Aplicação Streamlit
├── notebooks/          # EDA, clustering e modelagem
├── src/                # Código-fonte e pipelines (data,features, models, visualization)
├── tests/              # Testes automatizados
├── requirements.txt    # Dependências
├── README.md           # Documentação principal
└── LICENSE             # Licença MIT
```

---

## ⚙️ Instalação

### 1. Clonar o repositório

git clone https://github.com/seu-usuario/marketingai-sales-prediction.git  
cd marketingai-sales-prediction  

### 2. Criar ambiente virtual

python -m venv .venv  
.\.venv\Scripts\Activate.ps1  

### 3. Instalar dependências

pip install -r requirements.txt  

---

## ▶️ Como Usar

### 🔵 1. Executar os notebooks

No diretório *notebooks/*:

1. 1_analysis.ipynb  
2. 2_clustering.ipynb  
3. 3_prediction.ipynb  

Eles geram os arquivos `.pkl` usados na aplicação.

### 🔴 2. Executar a aplicação Streamlit

streamlit run app/streamlit_app.py  

Abrir no navegador:

http://localhost:8501  

A interface permite:

- selecionar loja, item, ano e mês  
- ajustar mean_price  
- visualizar cluster estimado  
- consultar médias históricas  
- gerar previsão final  

---

## 🛠 Metodologia

### ✨ Features utilizadas
- time_index  
- codificação cíclica (month_sin, month_cos)  
- mean_price  
- médias históricas:
  - item_mean_sales  
  - store_mean_sales  
  - store_item_mean_sales  
- cluster_id  

### 📉 Métricas avaliadas
- RMSE  
- MAE  
- R²  

O Ridge Regression apresentou o melhor equilíbrio geral.

---

## 📊 Resultados

### Modelo final: Ridge Regression

- **RMSE ≈ 43,6**  
- **MAE ≈ 16,8**  
- **R² ≈ 0,74**  

A combinação de variáveis temporais + clusterização + médias históricas produziu previsões consistentes até **2 anos de horizonte**.

---

## ☁️ Deploy

### Deploy pelo Streamlit Cloud

1. Publicar no GitHub  
2. Conectar Streamlit Cloud  
3. Selecionar repositório  
4. Definir app/streamlit_app.py como arquivo inicial  
5. Usar requirements.txt  

### CI/CD (opcional)

- testes automáticos  
- validação contínua  
- GitHub Actions  

---

## 🤝 Contribuição

1. Fazer fork  
2. Criar branch de feature  
3. Implementar melhorias  
4. Adicionar testes  
5. Abrir Pull Request com descrição clara  

Contribuições são bem-vindas!

---

## 👩‍💻 Autora

**Daniela de David**  
Autora do Projeto *MarketingAI: Sistema de Previsão de Vendas Mensais por Loja, Item e Período*

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License**.

---

## 🎉 Agradecimentos

- Ao Programa de Formação CDPro (Cientista de Dados Profissional) que tem como grande Mestre, Eduardo Rocha (obrigada por ensinar sem complicar!) 
- À comunidade open source (pandas, scikit-learn, Streamlit etc.)


