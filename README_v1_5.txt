FAMILY PORTFOLIO LAB v1.5 — integrazione archivio automatico (fase 1)

L’app cerca /historical-data.json all’apertura. Il file distribuito è intenzionalmente
PENDING, senza rendimenti inventati. Il backtest automatico diventa operativo
solo dopo la pubblicazione di dati verificati e autorizzati alla redistribuzione.

Formato: status=ready, source (stringa), methodology (stringa), currency=EUR,
rows (array di almeno 12 mesi consecutivi): date YYYY-MM, stock/bond/gold/cash
come rendimenti decimali (0.01 = +1%). Tutte e quattro le serie obbligatorie.

Mantiene importazione CSV manuale e backup v1.4. Non cambia dati locali.
