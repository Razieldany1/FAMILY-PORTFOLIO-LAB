FAMILY PORTFOLIO LAB v1.6A — AUTOMATED DEVELOPED-EQUITY PROXY

1. Backup JSON dalla PWA prima di aggiornare.
2. Pubblica TUTTI i file di questa cartella nella root del repository.
   In particolare includi scripts/build_history.py e .github/workflows/update-history.yml.
3. GitHub > Actions > Update validated equity history > Run workflow.
4. Controlla il log. Solo se il job termina correttamente historical-data.json
   viene aggiornato e committato. Cloudflare esegue il deployment del nuovo commit.
5. In app > Historical Risk Engine > Aggiorna archivio.
6. Per il confronto storico crea DUE portafogli azionari globali di prova: i
   confronti 60/40 restano DISATTIVATI finché mancano le obbligazioni.

ATTENZIONE: al momento della consegna non è incluso alcun dato scaricato.
Il workflow genera i dati sulla tua infrastruttura GitHub. Se non riesce
a scaricarli, lascia historical-data.json in stato pending.

Kenneth French Developed Markets è un proxy dei mercati sviluppati, NON
VWCE, non include emergenti. Conversione valutaria con cambio BCE di fine
mese (ultimo giorno disponibile), non NAV dell'ETF. Dati senza costi e tasse.
Verificare le condizioni di redistribuzione dei dati prima di rendere pubblico
l'archivio.
