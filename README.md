# aplicativo_recebimento: Consulta de Agendamentos de Notas Fiscais

![Badge de Status](https://img.shields.io/badge/status-ativo-brightgreen)
![Versão](https://img.shields.io/badge/vers%C3%A3o-1.0.0-blue)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green) Um aplicativo desktop desenvolvido em Python para facilitar a consulta rápida de informações de agendamento de notas fiscais diretamente no SQL Server. Ele permite que o usuário verifique a data de entrada do produto na loja, auxiliando na gestão estratégica do estoque e armazenamento no Centro de Distribuição (CD).

## 🚀 Funcionalidades

* **Consulta por Chave de NFe:** Insira a chave da Nota Fiscal Eletrônica para buscar dados relevantes.
* **Visualização da Data de Entrada:** Obtenha rapidamente a data prevista ou real de entrada do produto na loja.
* **Otimização do Armazenamento:** Utilize a informação da data de entrada para planejar o armazenamento de forma estratégica no CD, garantindo o fluxo ideal de produtos.
* **Interface Simples e Intuitiva:** Desenvolvido para ser fácil de usar, mesmo por usuários não técnicos.

## 📦 Como Obter e Executar (Executável Windows)

Este aplicativo é distribuído como um executável para Windows. Não é necessário ter Python instalado na sua máquina para utilizá-lo.

1.  **Baixe a Última Versão:**
    Acesse a página de Releases do projeto e baixe o arquivo executável (`.exe`) da versão mais recente:
    ➡️ [**BAIXE AQUI A VERSÃO MAIS RECENTE**](https://github.com/[ADRIANO_MORRISON]/aplicativo_recebimento/releases/latest)

    * *Nota:* Ao baixar arquivos executáveis da internet, seu navegador ou antivírus pode emitir um aviso de segurança. Confirme que deseja manter/executar o arquivo, pois ele é seguro.

2.  **Execute o Aplicativo:**
    Após o download, localize o arquivo `[SEU_NOME_DO_ARQUIVO_EXE].exe` (ex: `consulta_nfe.exe`) e dê um duplo clique para executá-lo.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **`pyodbc`:** Biblioteca para conexão com bancos de dados ODBC, incluindo SQL Server.
* **PyInstaller:** Utilizado para empacotar o aplicativo em um executável.

## 📂 Estrutura do Projeto
