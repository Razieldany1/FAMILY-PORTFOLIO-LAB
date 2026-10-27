#!/usr/bin/env python3
"""Build monthly EUR developed-equity proxy; fail closed. Python stdlib only."""
import csv, datetime as dt, io, json, re, sys, urllib.request, zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FRENCH='https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Developed_3_Factors_CSV.zip'
ECB='https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=1990-01-01&format=csvdata'
UA={'User-Agent':'FamilyPortfolioLab/1.6A (historical research; public data)'}
def fetch(url):
 with urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=45) as r:
  data=r.read(5_000_001)
  if len(data)>5_000_000:raise ValueError('Download exceeds 5MB')
  return data

def french_monthly(raw):
 with zipfile.ZipFile(io.BytesIO(raw)) as z:
  names=[n for n in z.namelist() if n.lower().endswith('.csv')]
  if len(names)!=1:raise ValueError('Unexpected French ZIP structure')
  lines=z.read(names[0]).decode('utf-8-sig',errors='replace').splitlines()
 out={}; in_monthly=False
 for line in lines:
  fields=[x.strip() for x in line.split(',')]
  if fields and re.fullmatch(r'\d{6}',fields[0]) and len(fields)>=5:
   in_monthly=True
   ym=fields[0]; m=int(ym[4:]);
   if not 1<=m<=12:raise ValueError('Invalid French month')
   try:excess=float(fields[1]);rf=float(fields[4])
   except ValueError:raise ValueError('Invalid French market/risk-free returns')
   if abs(excess)>100 or abs(rf)>100:raise ValueError('Out-of-range French return')
   key=ym[:4]+'-'+ym[4:]
   if key in out:raise ValueError('Duplicate French month')
   out[key]=(excess+rf)/100
  elif in_monthly:
   break
 if len(out)<120:raise ValueError('Insufficient French history')
 return out

def ecb_month_end(raw):
 content=raw.decode('utf-8-sig');reader=csv.DictReader(io.StringIO(content))
 if not reader.fieldnames or not {'TIME_PERIOD','OBS_VALUE'}.issubset(reader.fieldnames):raise ValueError('ECB CSV columns missing')
 out={}; dates={}
 for r in reader:
  date=r['TIME_PERIOD']; val=r['OBS_VALUE']
  if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',date) or not val:continue
  ym=date[:7]; fx=float(val)
  if fx<=0:raise ValueError('Invalid FX')
  if ym not in dates or date>dates[ym]:dates[ym]=date;out[ym]=fx
 if len(out)<120:raise ValueError('Insufficient ECB FX')
 return out

def build(stocks,fx):
 months=sorted(set(stocks)&set(fx))
 rows=[];prev=None
 for ym in months:
  year,month=map(int,ym.split('-'))
  prior=f'{year-1}-12' if month==1 else f'{year}-{month-1:02d}'
  if prior not in fx:continue
  # USD per EUR: convert total-return wealth via FX previous/current.
  ret=(1+stocks[ym])*fx[prior]/fx[ym]-1
  if not (-1<ret<10):raise ValueError('Invalid EUR return '+ym)
  n=year*12+month
  if prev is not None and n!=prev+1:raise ValueError('Gap in EUR return series '+ym)
  prev=n;rows.append({'date':ym,'stock':round(ret,10)})
 if len(rows)<120:raise ValueError('Too few consecutive months')
 today=dt.datetime.now(dt.timezone.utc).date().isoformat()
 return {'status':'ready','schema_version':2,'source':'Kenneth French Developed Markets 3 Factors + ECB reference FX',
 'methodology':'Developed Markets market return = (Mkt-RF)+RF (monthly, USD, dividends included), converted to EUR with ECB last available daily reference FX in each month; unhedged. Proxy for developed equities, NOT VWCE/FTSE All-World. No emerging markets, ETF TER, taxes or trading costs. ECB rates are reference rates, not executable transaction rates.',
 'currency':'EUR','available_assets':['stock'],'provider_url':'https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html',
 'as_of':today,'asset_sources':{'stock':FRENCH+' ; '+ECB},'rows':rows}

def main():
 data=build(french_monthly(fetch(FRENCH)),ecb_month_end(fetch(ECB)))
 target=ROOT/'historical-data.json';temp=target.with_suffix('.json.tmp')
 temp.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
 temp.replace(target)
 print('Validated:',len(data['rows']),'months',data['rows'][0]['date'],'to',data['rows'][-1]['date'])
if __name__=='__main__':
 try:main()
 except Exception as exc:
  print('ARCHIVE NOT UPDATED:',exc,file=sys.stderr);sys.exit(1)
