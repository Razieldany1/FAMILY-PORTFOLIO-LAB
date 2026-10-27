FAMILY PORTFOLIO LAB v1.5.1 — validazione provenienza archivio

Questa release NON include ancora un dataset mensile completo e verificato.
Il file historical-data.json rimane pending e l’app rifiuta di calcolare
backtest fittizi.

Per pubblicare dati occorre un JSON con:
status=ready, currency=EUR, source, methodology, provider_url (https),
as_of (YYYY-MM-DD), asset_sources (stock,bond,gold,cash) e rows.
rows: almeno 12 osservazioni mensili contigue, con date YYYY-MM e
stock,bond,gold,cash in rendimenti DECIMALI (es. -0.05 = -5%).

IMPORTANTE: la validazione strutturale NON verifica autonomamente la
veridicita' dei dati o il diritto di redistribuirli. Verificare a monte.
Non usare dati USA/USD come proxy EUR senza conversione appropriata.

Aggiornamento GitHub/Cloudflare: sostituire app.js e sw.js, conservando
historical-data.json e gli altri file. Esportare prima backup JSON.
