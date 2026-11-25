[![make.fun](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/afox63375-maker/u-suzy-one-line-office-joke-laugh-off-f574ac73/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/afox63375-maker/u-suzy-one-line-office-joke-laugh-off-f574ac73/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)

# One-Line Office Joke Laugh-Off

Entry for the [One-Line Office Joke Laugh-Off](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73) on make.fun.

## The joke

> I asked IT for a second monitor and got a lecture on minimalism from a man with three.

## How it works

`main.py` (Python standard library only) writes that one line to
`/output/entry.txt` and checks it first against the competition gate:
UTF-8 text, 1 to 200 characters, exactly one line, no trailing newline.
After writing, it reads the file back and confirms the bytes match the
joke exactly.

## Why this line

The joke is built on one concrete office detail everyone recognises —
asking IT for a second monitor — and the laugh comes from a reversal
that lands on the very last words: the person preaching minimalism is
the one with three monitors. No setup needs explaining, no office
cliché is recycled, and every word earns its place.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
