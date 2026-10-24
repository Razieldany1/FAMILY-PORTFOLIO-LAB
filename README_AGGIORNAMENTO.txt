FAMILY PORTFOLIO LAB v1.1 — Aggiornamento Cloudflare Workers

NOVITA'
- Nuova scheda «Crisi storiche» con scenari IPOTETICI ispirati a 1929, 1973, 1987, 2000, 2008, 2020, 2022.
- Confronto per ciascun anno del piano, Leo e Bianca, PAC mantenuto/sospeso, scenario senza crisi.
- Drawdown Monte Carlo corretto: indice di rendimento separato dai flussi PAC.
- VaR mostrato come perdita non negativa; migliorati i controlli sul backup.
- Service Worker aggiornato per la root Cloudflare; cache aggiornata.

IMPORTANTE: Non si tratta di backtest reali. I rendimenti delle crisi sono valori illustrativi assunti, NON serie storiche documentate. Nessuna stima dimostra la capacità reale di sopportare perdite.

INSTALLAZIONE: esportare prima il backup JSON dalla PWA installata. Nel repository GitHub sostituire i file con quelli contenuti in questo ZIP, conservando la struttura nella radice. Verificare deployment automatico Cloudflare, quindi riaprire la PWA online. Non cancellare dati del browser o disinstallare FAMILY CFO.

La struttura JSON rimane version:1 e localStorage key fpl_data_v1. Nessuna migrazione o reset automatico dei dati.

NOTA: L'app attuale non registra ancora quote ETF, operazioni reali o costi e non offre backtest storici con serie di mercato certificate. Sono funzionalita' successive.
