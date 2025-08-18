name: Atualizar Resultados Diariamente

on:
  schedule:
    - cron: '0 8 * * *'  # 08:00 UTC = 11:00 BRT
  workflow_dispatch:

jobs:
  update-data:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout do repositório
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependências
        run: |
          python -m pip install --upgrade pip
          pip install requests beautifulsoup4

      - name: Executar script de atualização
        run: |
          python update_results.py
          if [ $? -ne 0 ]; then
            echo "Erro ao executar update_results.py"
            exit 1
          fi

      - name: Validar data.json
        run: |
          python -c "import json; with open('data.json') as f: json.load(f)"

      - name: Commit e Push se houver mudanças
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add data.json
          git commit -m "Atualizado automaticamente: resultados dos jogos $(date)" || exit 0
          git push
