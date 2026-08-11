# TradingLab

TradingLab är ett Python-baserat analysverktyg för aktier. Projektet hämtar instrument-, rapport- och KPI-data från Börsdata API och använder separata strategier för **Quality**, **Value** och **Growth**.

Den nuvarande interaktiva huvudfunktionen analyserar ett valt instrument och presenterar ett sammanvägt **TradingLab Score**.

## Funktioner

### Aktieanalys

Programmet:

1. söker efter ett instrument via ticker eller företagsnamn,
2. låter användaren välja mellan flera träffar,
3. hämtar senaste rapporter,
4. beräknar centrala fundamentala mått,
5. kör tre analysstrategier,
6. presenterar respektive strategipoäng,
7. räknar fram ett sammanvägt TradingLab Score.

### Quality

Quality-strategin använder bland annat:

- Rörelsemarginal
- Skuldsättningsgrad
- Soliditet
- ROE
- ROIC
- Omsättningstillväxt
- Vinsttillväxt

### Value

Value-strategin använder bland annat:

- P/E
- P/S
- P/B
- Direktavkastning
- EV/EBIT
- EV/EBITDA
- ROIC
- PEG

### Growth

Growth-strategin använder:

- Omsättningstillväxt
- Vinsttillväxt
- PEG

PEG kommer i den nuvarande versionen från Börsdata API. Det innebär att PEG kan bli negativt när den underliggande vinsttillväxten är negativ. Ett negativt PEG bedöms därför inte som attraktivt i Growth-strategins poängsättning.

### Investment Score

`InvestmentStrategy` beräknar det totala TradingLab Score som genomsnittet av:

- Quality Score
- Value Score
- Growth Score

Varje delstrategi har en transparent poängfördelning som visas i rapporten.

## Datakälla

TradingLab använder Börsdata API.

API-basen som används av projektet är:

```text
https://apiservice.borsdata.se/v1
```

Projektet använder bland annat:

- instrumentlistan,
- rapportdata,
- KPI-data.

Instrumentlistan cachas under programmets körning och KPI-resultat cachas per KPI-anrop.

## Installation

TradingLab kräver Python och de externa Python-paketen:

- `requests`
- `python-dotenv`

Installera dem exempelvis med:

```bash
python3 -m pip install requests python-dotenv
```

## API-nyckel

API-nyckeln ska **inte** hårdkodas i Python-koden.

Skapa en fil med namnet:

```text
.env
```

i projektroten och lägg in:

```text
BORSDATA_API_KEY=din_api_nyckel
```

`.env` är exkluderad från Git via `.gitignore` och ska aldrig läggas i en publik release eller på GitHub.

## Köra TradingLab

Från projektroten:

```bash
python3 main.py
```

Programmet frågar:

```text
Vilken aktie vill du analysera?
```

Exempel:

```text
Vilken aktie vill du analysera? volvo
```

Om flera instrument hittas får användaren välja rätt instrument.

Därefter visas bland annat:

- senaste rapportår,
- omsättning,
- rörelseresultat,
- vinst,
- vinst per aktie,
- Quality Score,
- Value Score,
- Growth Score,
- detaljerad poängfördelning,
- slutligt TradingLab Score.

## Projektstruktur

```text
TradingLab/
│
├── main.py
├── analysis.py
├── api.py
├── config.py
├── fundamentals.py
├── metrics.py
├── metrics_loader.py
├── models.py
├── report.py
├── investment_strategy.py
│
├── screener.py
├── scanner.py
├── ranking.py
├── ranking_manager.py
│
├── portfolio.py
├── portfolio_entry.py
├── portfolio_builder.py
│
├── stock_lookup.py
├── stock_info.py
│
├── strategies/
│   ├── base_strategy.py
│   ├── quality_strategy.py
│   ├── value_strategy.py
│   └── growth_strategy.py
│
├── portfolio_strategies/
│   ├── base_portfolio_strategy.py
│   ├── quality_portfolio_strategy.py
│   └── total_portfolio_strategy.py
│
├── languages/
│   └── sv.py
│
├── tools/
│   └── package.py
│
└── tests och verifieringsskript
```

## Strategiarkitektur

Analysstrategierna bygger på en gemensam basklass:

```text
BaseStrategy
    ├── QualityStrategy
    ├── ValueStrategy
    └── GrowthStrategy
```

`BaseStrategy` hanterar bland annat:

- poäng,
- kommentarer,
- ScoreItems,
- resultatobjekt.

Det gör det möjligt att lägga till nya analysstrategier utan att behöva bygga om hela analysmotorn.

## Screening, ranking och portfölj

Projektet innehåller även komponenter för vidare analys:

### Screener

`Screener` kan analysera flera instrument och samla resultaten.

### Ranking

`Ranking` kan:

- sortera bolag efter score,
- returnera Top N,
- hitta ett bolags rankingposition.

### RankingManager

`RankingManager` hanterar flera separata rankingar, exempelvis:

- `quality`
- `value`
- `total`

### PortfolioBuilder

`PortfolioBuilder` kan bygga portföljer från rankingresultat eller screeningresultat.

Dessa komponenter finns i projektet och utgör grunden för den fortsatta utvecklingen mot mer avancerad screening och portföljkonstruktion.

## Säkerhet

TradingLab ska hantera API-nyckeln via miljövariabel:

```text
BORSDATA_API_KEY
```

Följande ska aldrig publiceras:

- `.env`
- API-nycklar
- andra tokens eller hemligheter
- `.git`-historik som innehåller hemligheter

Projektets `.gitignore` exkluderar bland annat:

```text
.env
__pycache__/
*.py[cod]
.venv/
venv/
.DS_Store
.vscode/
.idea/
```

## Paketering och release

Projektet innehåller:

```text
tools/package.py
```

Kör:

```bash
python3 tools/package.py
```

Package Tool:

1. kontrollerar projektets grundfiler,
2. varnar om `README.md` eller `requirements.txt` saknas,
3. stoppar om `.gitignore` saknas,
4. söker efter misstänkta hårdkodade hemligheter,
5. skapar en ZIP-release,
6. exkluderar bland annat `.env`, `.git`, `__pycache__` och virtuella miljöer,
7. verifierar ZIP-filen efter skapandet,
8. skriver en Release Report,
9. stoppar releasen om säkerhetskontrollen misslyckas.

Releasefiler placeras i:

```text
releases/
```

Exempel:

```text
releases/TradingLab_v0.4.1_2026-08-10.zip
```

## Tester och verifieringsskript

Projektet innehåller flera test- och verifieringsskript för bland annat:

- API
- KPI
- KPI-historik
- metadata
- rapporter
- ranking
- ranking manager
- screener
- portföljstrategier

Exempel:

```bash
python3 test_api.py
python3 test_kpi.py
python3 test_screener.py
```

## Nuvarande status

Den dokumenterade versionen är:

```text
TradingLab v0.4.1
```

I denna version är grundarkitekturen för:

- aktieanalys,
- Quality / Value / Growth,
- scoring,
- ranking,
- screening,
- portföljbyggande,
- säker paketering

på plats.

## Fortsatt utveckling

Planerade utvecklingsområden inkluderar bland annat:

- automatisk val av analysstrategi utifrån instrumentinformation,
- mer bolagstypsspecifika strategier,
- förbättrad PEG-hantering,
- vidareutvecklad screening,
- portföljstrategier,
- release- och GitHub-flöde.

Analysstrategin är förberedd för framtida val baserat på exempelvis sektor, bransch och bolagstyp.

## Säkerhetsprincip

TradingLab ska alltid kunna distribueras utan att känslig konfiguration följer med.

Före en större release bör följande arbetsflöde användas:

```text
Ändring
   ↓
Test
   ↓
Säkerhetsgranskning
   ↓
python3 tools/package.py
   ↓
ZIP-verifiering
   ↓
GitHub / Release
```

