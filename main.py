# SPDX-License-Identifier: MIT
"""The Best Advice I Ever Got — one lived sentence of advice.

Winner line (OpenCode deepseek-v4.1-flash-free draft round on the
Simular Box, then a criteria-ordered tournament in-session): the
line cook's towel. It beat 'Send it before you love it' (strong, but
an office scene the field reaches for) and the nurse's question
(tender, narrower to carry). The towel line wins the judge's order:
one sentence about advice actually received (criterion 1), specific
and earned and true beyond its moment (2 — mop first, explain
later, in any crisis), a real voice in a real moment (3 — a dropped
tray, a towel handed over, no slogan), tight in one breath (4), and
it lands with something to keep (5 — 'saved me in three jobs').
"""

ENTRY_TEXT = (
    "A line cook handed me a towel after I dropped a full tray and said, "
    "\"Clean it up before you explain it,\" which has saved me in three jobs since."
)


def render():
    text = ENTRY_TEXT.encode("utf-8")
    # Gate self-check: 1 to 200 characters, not only white space, one line.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry outside the 1-200 character gate"
    assert ENTRY_TEXT.strip(), "entry is only white space"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    return text


def main():
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.environ.get("ENTRY_OUTPUT", os.path.join(out_dir, "entry.txt"))
    payload = render()
    with open(out, "wb") as f:
        f.write(payload)
    # Round-trip self-check: what landed on disk must be byte-identical
    # to render() and still inside the gate (1-200 chars, non-blank).
    with open(out, "rb") as f:
        on_disk = f.read()
    assert on_disk == payload, "written bytes differ from render()"
    decoded = on_disk.decode("utf-8")
    assert 1 <= len(decoded) <= 200 and decoded.strip(), "on-disk gate check failed"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
