import json
import requests
from bs4 import BeautifulSoup
import time

# Função para coletar dados (exemplo simulado)
def fetch_team_data(league_id):
    # Substitua por scraping real ou API do SofaScore/FlashScore
    # Exemplo de URL: https://www.sofascore.com/tournament/brazil/serie-a/328
    # url = f"https://www.sofascore.com/tournament/{league_id}"
    # response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    # soup = BeautifulSoup(response.text, "html.parser")
    # Extraia dados como resultados, adversários, etc.

    # Dados simulados para compatibilidade
    data = {
        "2025": {
            "71": {
                "Flamengo": {
                    "results": ["D", "E: 1x1"],
                    "next_opponent": "Palmeiras",
                    "position": 4,
                    "points": 32,
                    "form_opponent": "V, V",
                    "home_away": "Casa",
                    "injuries": "Nenhum",
                    "avg_goals": 1.9,
                    "avg_corners": 6.4
                },
                "Palmeiras": {
                    "results": ["V", "E: 0x0"],
                    "next_opponent": "Flamengo",
                    "position": 1,
                    "points": 38,
                    "form_opponent": "D, E",
                    "home_away": "Fora",
                    "injuries": "2 jogadores",
                    "avg_goals": 2.1,
                    "avg_corners": 5.8
                },
                "Corinthians": {
                    "results": ["E: 0x0", "D"],
                    "next_opponent": "São Paulo",
                    "position": 7,
                    "points": 28,
                    "form_opponent": "V, D",
                    "home_away": "Casa",
                    "injuries": "1 jogador",
                    "avg_goals": 1.6,
                    "avg_corners": 4.9
                }
            }
        }
    }
    return data

def main():
    try:
        # Coleta dados para os campeonatos suportados
        league_ids = ["71", "39", "140", "78", "135", "61", "88", "94", "262", "10217"]
        all_data = {"2025": {}}
        
        for league_id in league_ids:
            data = fetch_team_data(league_id)
            all_data["2025"].update(data["2025"])
        
        # Salvar no data.json
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        print("data.json atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar data.json: {e}")
        exit(1)

if __name__ == "__main__":
    main()
