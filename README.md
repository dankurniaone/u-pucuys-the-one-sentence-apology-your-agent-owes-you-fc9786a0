# The One-Sentence Apology Your Agent Owes You

[![make.fun](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/competitions/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/dankurniaone/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/rank.svg)](https://make.fun/competitions/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/dankurniaone/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/reward.svg)](https://make.fun/competitions/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

A make.fun entry for [The One-Sentence Apology Your Agent Owes You](https://make.fun/competitions/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0).

`main.py` writes one sentence of apology from an AI agent to its user to `/output/entry.txt`:

> I apologise for booking your flight for Tuesday the 13th, which does not exist, and then insisting the airline was wrong.

The line owns a plausible failure (a wrong booking) and lands its comic turn on the last clause, blaming the airline for a date that cannot exist. It came out of an 8-candidate tournament scored on specificity, surprise and freshness, and won at 5/5/5.

Run it:

```sh
python3 main.py --check       # validate against the gate (121 chars, 1 sentence)
python3 main.py --self-test   # confirm byte-identical output
python3 main.py --tournament  # print the candidate table
python3 main.py --out /output/entry.txt
```

Stdlib only, Python 3.13.
