# TradingLab – Roadmap

Detta dokument beskriver TradingLabs planerade utveckling.

Roadmapen är prioriterad och ska hjälpa oss att skilja mellan:
- vad som redan är byggt
- vad som är nästa steg
- vad som är planerat
- vad som är långsiktig vision

En idé i `IDEAS.md` blir inte automatiskt en del av roadmapen.

---

# Fas 1 – Stabil analysmotor

## Status: KLAR

TradingLab har etablerat en grundläggande analysmotor med separata strategier.

### Quality

Analyserar bland annat:

- rörelsemarginal
- skuldsättning
- soliditet
- ROE
- ROIC
- tillväxt

### Value

Analyserar bland annat:

- P/E
- P/B
- EV/EBIT
- EV/EBITDA
- direktavkastning
- ROIC

### Growth

Analyserar bland annat:

- omsättningstillväxt
- vinsttillväxt
- PEG

### Investment

Kombinerar:

- Quality
- Value
- Growth

till en totalpoäng.

---

# Fas 2 – Transparent scoring

## Status: KLAR

TradingLab har implementerat `ScoreItem`.

Varje strategisk bedömning kan innehålla:

- namn
- poäng
- maxpoäng
- kommentar

Exempel:

```text
ROIC
17 / 20
Stark ROIC