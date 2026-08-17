# TradingLab – Idébank

Detta dokument samlar produktidéer, framtida funktioner och koncept för
TradingLab. Idéer behöver inte vara beslutade eller prioriterade.
Syftet är att inget viktigt ska tappas bort under utvecklingen.

---

## 1. Strategiranking och topplistor

TradingLab ska kunna rangordna bolag utifrån olika investeringsstrategier.

### Strategier

- Quality
- Value
- Growth
- Total / kombinerad strategi

### Exempel

Quality Top 10:

1. Atlas Copco
2. Investor
3. Lifco
4. Volvo
5. Assa Abloy

Ranking ska kunna visa både:

- totalpoäng
- rank
- ScoreItems
- styrkor
- svagheter
- förändring över tid

Målet är att göra TradingLab till ett verktyg för att hitta intressanta
bolag, inte bara analysera ett bolag som användaren redan valt.

---

## 2. Transparent scoring

En central princip för TradingLab.

Användaren ska inte bara få:

> Investor: 86/100

utan kunna se varför.

Exempel:

- ROIC: 18/20
- Rörelsemarginal: 17/20
- Skuldsättning: 14/15
- Tillväxt: 8/10

Varje poäng ska kunna kopplas till en begriplig förklaring.

---

## 3. Benchmark-modell

TradingLabs resultat ska kunna jämföras mot relevanta externa referenser.

Möjliga benchmark-källor:

- OMXS30
- bredare svenska index
- relevanta sektorindex
- etablerade investeringsmodeller
- akademiska faktormodeller

Möjliga jämförelsemått:

- totalavkastning
- riskjusterad avkastning
- volatilitet
- maximal drawdown
- Sharpe ratio
- hit rate / andel vinnande innehav
- turnover

### Grundfråga

> Tillför TradingLabs ranking faktiskt värde jämfört med ett relevant
> benchmark?

---

## 4. Historisk uppföljning

TradingLab ska kunna följa hur en analys eller ranking utvecklas över tid.

Exempel:

Investor:

- 2024: 78
- 2025: 82
- 2026: 86

Det ska gå att se:

- score över tid
- förändringar i enskilda ScoreItems
- förändringar i ranking
- förändringar i fundamentala nyckeltal

---

## 5. Självkalibrerande modell

Långsiktig idé.

TradingLab ska kunna analysera hur olika faktorer historiskt har fungerat
och använda resultatet för att förbättra modellens kalibrering.

Exempel:

Initial viktning:

- Quality: 33 %
- Value: 33 %
- Growth: 33 %

Efter historisk utvärdering:

- Quality: 45 %
- Value: 30 %
- Growth: 25 %

### Viktig princip

Modellen måste skyddas mot:

- overfitting
- look-ahead bias
- survivorship bias
- data leakage

Kalibrering ska därför använda:

- träningsperiod
- valideringsperiod
- out-of-sample-period
- tydliga benchmark

Målet är en modell som kan förbättras utan att börja optimera
för historiska data på ett missvisande sätt.

---

## 6. Daglig 5-minutersgenomgång

En möjlig framtida kärnfunktion.

### Produktidé

> "Fem minuter om dagen för att få koll på din portfölj."

Användaren startar en kort, strukturerad genomgång.

TradingLab presenterar:

### Portföljstatus

- Quality Score
- Value Score
- Growth Score
- Total Score
- förändring sedan föregående period

### Viktiga förändringar

Exempel:

> Investor: Quality Score ökar från 86 till 89.

Förklaring:

- förbättrad marginal
- stabil ROIC
- minskad skuldsättning

### Varningssignaler

Exempel:

> Volvo: fallande marginal två kvartal i rad.

### Möjligheter

Exempel:

> Ett bolag har fått lägre värdering utan motsvarande försämring
> av fundamentala faktorer.

### Sammanfattning

Exempel:

> Dagens slutsats:
>
> - Portföljkvaliteten är fortsatt hög.
> - Två innehav bör bevakas.
> - Ett innehav har förbättrad värderingsprofil.
> - Ingen omedelbar åtgärd identifierad.

TradingLab ska ge underlag och förklaringar, inte låtsas veta framtiden.

---

## 7. Personlig investeringsprofil

Användaren ska kunna välja eller skapa en investeringsprofil.

Exempel:

### Kvalitetsinvesterare

- Quality: 60 %
- Value: 20 %
- Growth: 20 %

### Tillväxtinvesterare

- Quality: 30 %
- Value: 20 %
- Growth: 50 %

På längre sikt kan användaren skapa en egen strategi.

---

## 8. Portföljanalys

Användaren ska kunna analysera sin befintliga portfölj.

TradingLab kan identifiera:

- Quality
- Value
- Growth
- sektor-exponering
- koncentrationsrisk
- värderingsrisk
- kvalitetsförändringar
- gemensamma riskfaktorer

Exempel:

> "Din portfölj har hög kvalitet men är kraftigt exponerad mot industri."

---

## 9. Automatisk bevakning

TradingLab kan bevaka förändringar i portföljens innehav.

Exempel på signaler:

- försämrad ROIC
- fallande marginaler
- stigande skuldsättning
- försämrad tillväxt
- förändrad värdering
- större förändringar i ranking

Målet är att uppmärksamma användaren på sådant som faktiskt förändrats.

---

## 10. Förklarande investeringsassistent

Framtida AI-funktion.

Användaren kan ställa frågor som:

> "Varför har Investor fallit?"

eller:

> "Vilka av mina innehav har fått försämrad kvalitet?"

TradingLab ska svara genom att använda den underliggande analysen och
visa vilka faktorer som ligger bakom slutsatsen.

Grundprincip:

**Förklara först – rekommendera aldrig utan kontext.**

---

## 11. "Find my strategy"

Användaren beskriver vad han eller hon söker.

Exempel:

> "Jag vill hitta stabila kvalitetsbolag med rimlig värdering."

TradingLab kan översätta detta till relevanta filter och strategiviktningar.

Exempel:

- Quality > 80
- Value > 70
- låg skuldsättning
- stabil tillväxt

---

## 12. Professionell benchmark

TradingLab bör på sikt jämföras med etablerade analysramverk.

Möjliga referenspunkter:

- Morningstar
- Seeking Alpha
- Bloomberg
- S&P Capital IQ
- akademiska faktormodeller

Syftet är inte att kopiera andra modeller utan att förstå:

- hur professionella modeller är uppbyggda
- vilka faktorer de använder
- hur resultat kan utvärderas
- var TradingLab skiljer sig

---

## 13. Lovable / webbapp

Framtida användargränssnitt.

Möjliga funktioner:

- söka bolag
- analysera bolag
- visa Quality / Value / Growth
- visa ScoreItems
- visa ranking
- jämföra bolag
- visa portfölj
- visa daglig brief
- visa historik

Backend och analysmotor ska vara separerade från gränssnittet.

---

## 14. Produktpositionering

TradingLab ska inte primärt beskrivas som:

> "En aktiescreener."

Möjlig positionering:

> **"Ett transparent investeringsbeslutsstöd."**

eller:

> **"Från finansiell data till investeringsinsikt."**

En viktig del av produktens identitet är:

**TradingLab förklarar varför.**

---

## 15. Framtida frågor till professionella investerare

Frågor som kan hjälpa oss utveckla produkten:

- Vilka faktorer skulle du kräva i en professionell analysmodell?
- Vilka nyckeltal är mest relevanta?
- Vilka nyckeltal är överskattade?
- Hur skulle du vikta Quality, Value och Growth?
- Hur skulle du vilja använda en transparent aktieranking?
- Vilka krav skulle du ställa på en benchmark-modell?
- Vilka förändringar i en portfölj vill du bli uppmärksammad på?
- Om du fick en fem minuters automatisk portföljgenomgång varje morgon,
  vilken information skulle vara mest värdefull?
- Vilka signaler skulle få dig att undersöka ett innehav närmare?
- Vilken information skulle hjälpa dig inför ett eventuellt köp- eller
  säljbeslut?
- Vad vill du absolut inte att ett automatiserat investeringsverktyg ska göra?

---

## 16. Grundprinciper

TradingLab ska eftersträva:

1. Transparens
2. Förklarbarhet
3. Testbarhet
4. Historisk validering
5. Reproducerbarhet
6. Tydlig separation mellan data och tolkning
7. Minimera överanpassning
8. Användaren fattar det slutliga investeringsbeslutet

---

## Status

Detta dokument är en idébank.

Idéer här är **inte automatiskt beslutade funktioner**.

Prioritering sker i `ROADMAP.md`.