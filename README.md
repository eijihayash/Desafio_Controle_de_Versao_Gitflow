# Pipeline de Dados Público

Este projeto é um pipeline de dados desenvolvido para extrair, transformar e carrega (ETL). Seguindo o fluxo **Gitflow**.

## Arquitetura e Tecnologias
A solução foi projetada utilizando Programação Orientada a Objetos (POO) para garantir a modularidade e o gerenciamento de estado entre as etapas do pipeline.
- **Linguagem**: Python 3.8.18
- **Gestão de Versão**: .tool-versions (asdf)
- **Bibliotecas Principais**:
    - ``pandas`` (v1.5.3): Manipulação e limpeza de dados tabulares.
    - ``requests`` (v2.32.4): Interface HTTP para consumo de API.

## Configuração do Ambiente
O projeto utiliza um ambiente virtual isolado para garantir a consistência das dependências.

### Pré-requisitos
Certifique-se de possuir o Python 3.8 instalado. Caso utilize gestores de versão, o arquivo `.tool-versions` já está configurado.

### Instalação
1. Clone o repositório:

    ```bash
        git clone <url>
    ```

2. Crie e ative o ambiente virtual:

    ``` bash
        python3 -m venv .venv
        source .venv/bin/activate  # Linux/macOS
         ou
        .venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:

    ```bash
        pip install -r requirements.txt
    ```

## Fluxo de Trabalho (GitFlow)
O projeto segue rigorosamente o modelo de ramificação GitFlow para garantir a integridade do código em produção:
- **main**: Armazena o código estável e funcional (produção).
- **develop**: Branch de integração para funcionalidades concluídas.
- **feature/**: Branches temporárias para desenvolvimento de novas funcionalidades ou correções.

#### Padrão de Contribuição
- Atualize a branch local: git pull origin develop
- Crie a branch da task: git checkout -b feature/nome-da-task
- Utilize Commits Semânticos:
    - `feat`: Nova funcionalidade.
    - `chore`: Atualizações de build, dependências ou ferramentas.

## Estrutura do Pipeline
A classe Pipeline gerencia o ciclo de vida dos dados através de estados internos:
 - **Extração**: Realiza a requisição HTTP e armazena o conteúdo bruto no atributo raw_data.

 - **Transformação**: Processa o dado bruto, realiza a limpeza (deduplicação e tratamento de nulos) e armazena o resultado em um objeto DataFrame no atributo dados_tabular.

 - **Monitoramento**: Gera métricas estatíticas e volumétricas sobre o processamento.

 - **Carregamento**: Permite os dados processados em um arquivo físico no formato `.csv`, garantindo a integridade codificação (`utf-8`).

## Testes e Validação
É obrigatória a execução e passagem dos testes antes da abertura de qualquer Pull Request para a branch develop.

Para executar a suíte de testes unitários e de integração:
```bash
python -m tests.test_pipeline
```
As validações incluem:

- Verificação de conectividade e integridade do retorno da API.
- Consistência volumétrica dos dados após transformação.
- Validação de tipos e estados internos da classe.