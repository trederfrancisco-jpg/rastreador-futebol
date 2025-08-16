# update_results.py
import requests
import json
import time
from datetime import datetime

# Configuração de cabeçalho para parecer um navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.sofascore.com/"
}

# Mapeamento de ligas do Sofascore (IDs reais)
LEAGUE_IDS = {
    "71": {"name": "Brasileirão Série A", "sofascore_id": "103"},
    "39": {"name": "Premier League", "sofascore_id": "3"},
    "140": {"name": "La Liga", "sofascore_id": "8"},
    "78": {"name": "Bundesliga", "sofascore_id": "21"},
    "135": {"name": "Serie A", "sofascore_id": "19"},
    "61": {"name": "Ligue 1", "sofascore_id": "16"},
    "88": {"name": "Eredivisie", "sofascore_id": "11"},
    "94": {"name": "Primeira Liga", "sofascore_id": "18"},
    "262": {"name": "Liga MX", "sofascore_id": "26"},
    "10217": {"name": "Brasileirão Feminino", "sofascore_id": "1154"}
}

def get_last_match_result(team_name, tournament_id):
    try:
        url = f"https://www.sofascore.com/api/v1/tournament/{tournament_id}/standings/total"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return None

        data = response.json()
        for team in data.get("standings", []):
            if team_name.lower() in team["team"]["name"].lower():
                # Pega os últimos 2 jogos
                recent = team.get("recentResults", [])
                last_two = recent[:2] if len(recent) >= 2 else (recent + ["?"] * 2)[:2]
                # Converte: W=V, L=D, D=E
                result_map = {"W": "V", "L": "D", "D": "E: 1x1"}
                formatted = [result_map.get(r, r) for r in last_two]
                # Simula próximo adversário (em produção, pega de fixtures)
                next_opp = "Adversário"  
                return formatted + [next_opp]
        return ["?", "?", "Adversário"]
    except Exception as e:
        print(f"Erro ao buscar {team_name}: {e}")
        return ["?", "?", "Adversário"]

def main():
    print("🔄 Iniciando atualização de resultados...")
    data = {"2025": {}}

    # Times de exemplo por liga (você pode ajustar)
    teams_by_league = {
        "71": ["Flamengo", "Palmeiras", "Botafogo"],
        "39": ["Arsenal", "Liverpool", "Manchester City"],
        "140": ["Barcelona", "Real Madrid"],
        "78": ["Bayern", "Dortmund"],
        "135": ["Inter", "Juventus"],
        "61": ["PSG", "Marselha"],
        "88": ["Ajax", "Feyenoord"],
        "94": ["Benfica", "Porto"],
        "262": ["América", "Chivas"],
        "10217": ["Corinthians", "Flamengo"]
    }

    for league_id, team_list in teams_by_league.items():
        league_data = {}
        tournament_id = LEAGUE_IDS[league_id]["sofascore_id"]
        for team in team_list:
            print(f"Buscando dados de {team} ({LEAGUE_IDS[league_id]['name']})")
            result = get_last_match_result(team, tournament_id)
            league_data[team] = result
            time.sleep(1.5)  # Evita bloqueio
        data["2025"][league_id] = league_data

    # Salva o data.json atualizado
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("✅ data.json atualizado com sucesso!")
    print(f"📅 Atualizado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")

if __name__ == "__main__":
    main()
