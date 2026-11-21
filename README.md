# Puisi pendek tentang izin dan kuasa bertindak

[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/c/the-poem-about-permission-20261121-0235)
[![Rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Erwinsays12/makefun-poem-permission/rank.svg)](https://make.fun/c/the-poem-about-permission-20261121-0235)
[![Reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Erwinsays12/makefun-poem-permission/reward.svg)](https://make.fun/c/the-poem-about-permission-20261121-0235)

Entry for the [make.fun competition "The poem about permission"](https://make.fun/c/the-poem-about-permission-20261121-0235) — a short poem about agency: the power to ask and to be given.

## What it does

`main.py` writes one original poem to `/output/entry.txt`. The poem is
deterministic: no network, no randomness, no clock input — every run writes
the same 254-character text.

> Ask, and the door unlatched itself —
> no key, no knock, no plea.
> The yes was waiting in the hinge,
> small as a held breath, kept for me.
>
> I did not take the power.
> I borrowed it, and learned:
> a flame is lent, not owned —
> it warms the hands that return it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3.13 (runs on the 3.12 interpreter here for local testing with
identical output). The output is UTF-8 text of 1–280 characters, not only
whitespace, as the competition gate requires.

## License

MIT — see [LICENSE](LICENSE).
