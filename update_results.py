async function loadData() {
  const leagueId = leagueSelect.value;
  if (!leagueId) {
    resultsDiv.innerHTML = "Selecione um campeonato e escolha uma opção.";
    sidebarInfo.textContent = "Selecione um campeonato.";
    tabelaLink.innerHTML = "";
    return;
  }

  resultsDiv.innerHTML = "<p class='loading'>🔄 Carregando dados...</p>";
  try {
    const response = await fetch('/data.json?' + new Date().getTime());
    if (!response.ok) throw new Error("Erro HTTP: " + response.status);
    const data = await response.json();
    const year = "2025";

    if (data[year] && data[year][leagueId]) {
      teamResults = data[year][leagueId];
      loadChanceOfWinOrDraw(leagueId); // Chama a função separada
    } else {
      resultsDiv.innerHTML = "<p class='error'>⚠️ Nenhum dado encontrado para este campeonato.</p>";
    }

    sidebarInfo.textContent = `Campeonato selecionado: ${leagueNames[leagueId]}`;
    updateTabelaLink(leagueId);

  } catch (err) {
    console.error("Erro ao carregar dados:", err);
    resultsDiv.innerHTML = `
      <p class='error'>
        ❌ Falha ao carregar dados.<br>
        Verifique:<br>
        1. Se o data.json está na raiz<br>
        2. Se o formato está correto (JSON válido)<br>
        3. Atualize com Ctrl + F5
      </p>`;
  }
}
