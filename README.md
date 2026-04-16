# Pipeline de Dados Público

Este projeto é um pipeline de dados desenvolvido para extrair, transformar e carrega (ETL). Seguindo o fluxo **Gitflow**.

## Ambiente de Desenvolvimento
1. Clone e entre na branch **develop** : **git branch develop**
2. Instale a dependências: **pip install -r requirements.txt**

## Fluxo de Trabalho (GitFlow)
* **main:** Apenas código em produção (estável).
* **develop:** Integração de novas funcionalidades.
* **feature/:\*** Desenvolvimento de novas tasks.

### Como contribuir:
1. Puxe a `develop` atualizada: `git pull origin develop`
2. Crie sua branch: `git checkout -b feature/sua-task`
3. Siga o padrão de commits: `feat: ...`, `fix: ...`, `chore: ...`
4. Abra um Pull Request para a branch `develop`.

## Testes
Rodar os testes antes de abrir um PR:

