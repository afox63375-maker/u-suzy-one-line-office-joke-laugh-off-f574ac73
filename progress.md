# One-Line Office Joke Laugh-Off — progress

Competition: `u-suzy-one-line-office-joke-laugh-off-f574ac73`
Deadline: 2026-11-26T12:05:00Z (blind rounds; round 1 cutoff 2026-11-25T20:05:30Z)
Pot: $3, free entry. Blind rounds — no visible leaderboard, so the joke is
modeled on the winning pattern of recent office-joke winners: a concrete,
specific office detail, punch landing on the final words, nothing explained.

## Final line (86 characters)

> I asked IT for a second monitor and got a lecture on minimalism from a man with three.

Gate check (RULES.txt): UTF-8, 1–200 characters — 86, one line, no trailing
newline. Program writes it to `/output/entry.txt` and reads it back to
verify the bytes match exactly.

## Why it wins, criterion by criterion

1. **One-line office joke** — unambiguously about office life (IT, second
   monitor, a workplace lecture). One sentence, one line.
2. **Sharp, surprising punchline** — the laugh is a reversal: the person
   preaching minimalism turns out to own three monitors. The punch lands
   on the final words ("with three"), so the reader only gets the joke at
   the very end.
3. **Instant on one read** — no setup to explain, no jargon, no wordplay
   that needs a second pass. The scene (asking IT for gear) is understood
   immediately.
4. **Fresh** — avoids the field's overused tropes entirely: no reply-all,
   no "per my last email", no meetings-that-could-have-been-emails, no
   printer, no coffee machine. A monitor request and a minimalism lecture
   is a specific, lived-in office moment, not a recycled punchline.
5. **Tight wording** — 86 characters, every word earns its place; "a man
   with three" does the whole reversal in four words.

## Rejected alternatives

1. "HR said we can't expense therapy, but the office dog has a wellness
   budget." (80 chars) — Good contrast, but the punch lands mid-line and
   the joke needs the reader to infer the comparison; weaker instant
   landing than the monitor reversal.
2. "I labeled my lunch 'Dave's' after someone kept eating it, and now
   nobody in the office touches Dave's food." (115 chars) — Fridge-theft
   is one of the most overused office tropes; once you know the setup the
   punch is predictable.
3. "My boss said his door is always open, so I walked in and he told me
   to book a meeting first." (91 chars) — Open-door-policy cliché, and
   the field will be full of boss/meeting jokes; fails the freshness
   criterion.

## Local test result

```
$ python3 main.py
wrote 86 characters to /output/entry.txt
```

- Exit code: 0
- `/output/entry.txt`: 86 bytes / 86 characters, valid UTF-8
- Single line: yes (no `\n` or `\r`)
- Ends with newline: no
- Byte-for-byte match with the joke in `main.py`: yes (program verifies
  this itself on every run with a read-back check)

## Files

- `main.py` — standard library only; writes and validates the entry.
  Authored in two writing messages: initial write, then a revision pass
  adding the read-back verification.
- `README.md` — 3 make.fun badge lines at the top, then entry description.
- `LICENSE` — MIT, SPDX-License-Identifier: MIT first line.
- `prompt.txt` — verbatim Rio instruction: `Selesaikan 1persatu`
- `progress.md` — this file.

## Status

Built and locally tested. NOT submitted — no GitHub repo created, no
bundle/check/submit run; the parent session runs the pipeline.
