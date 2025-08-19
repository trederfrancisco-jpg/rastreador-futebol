import json
import requests

# Exemplo: atualiza manualmente com base em dados reais
def update_data():
    data = {
        "2025": {
            "71": {
                "Flamengo": {
                    "results": ["D", "E: 1x1"],
                    "next_opponent": "Palmeiras",
                    "opponent_table": "Top 4",
                    "form_opponent": "V, V",
                    "position": 4,
                    "points": 32,
                    "avg_goals": 1.9,
                    "avg_corners": 6.4,
                    "home_away": "Casa",
                    "injuries": "Nenhum",
                    "new_coach": False,
                    "last_5_summary": "1V, 1E, 3D"
                }
            }
        }
    }
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    update_data()
