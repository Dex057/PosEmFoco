# 🎓 PósEmFoco - Monitor de Editais UFPA (MVP)

Este projeto é uma ferramenta de automação (Web Scraping) desenvolvida em Python para monitorar a publicação de novos editais de pós-graduação e especialização no portal da **Universidade Federal do Pará (UFPA)**.

O sistema verifica periodicamente a página de editais, filtra os resultados com base em palavras-chave de interesse do usuário (ex: "Tecnologia", "Mestrado") e envia uma notificação por e-mail contendo os títulos e links diretos para os editais encontrados.

## 🚀 Funcionalidades (MVP)

* **Extração Automática:** Navega na página de editais da UFPA usando Selenium.
* **Paginação Inteligente:** Percorre múltiplas páginas para garantir que nenhum edital recente seja perdido.
* **Filtragem Personalizada:** Seleciona apenas editais que contenham palavras-chave definidas pelo usuário.
* **Notificação por E-mail:** Envia um relatório formatado em HTML com links clicáveis para o usuário.

## 🛠️ Tecnologias Utilizadas

* **Python 3.12+**
* **Selenium WebDriver:** Para automação do navegador e interação com elementos dinâmicos (JavaScript).
* **SMTP (Gmail):** Para envio de e-mails seguros.
* **Python-Dotenv:** Para gerenciamento seguro de credenciais.

## ⚙️ Pré-requisitos

Para rodar este projeto localmente, você precisará de:

1.  **Google Chrome** instalado.
2.  **Python 3** instalado.
3.  Uma conta **Gmail** com "Senha de App" configurada (para o envio de e-mails).

## 📦 Como Rodar o Projeto

### 1. Clone o repositório
```bash
git clone [https://github.com/Dex057/PosEmFoco.git](https://github.com/Dex057/PosEmFoco.git)
cd PosEmFoco