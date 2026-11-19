"""Regenerate assets/languages.svg from GitHub's own language byte counts.

Run from the repo root with an authenticated `gh`:

    python scripts/languages.py

It sums the bytes GitHub's linguist reports for every repository this
account owns (forks excluded, private ones included). Only the aggregate
is drawn: no repository name appears in the image. It replaces the
third-party language cards, which counted each public repo's single
primary language rather than the code in it.
"""

import json
import subprocess
from datetime import date
from pathlib import Path

OWNER = "Conqueror-Mod"
TOP = 6

# Linguist's colours, so the card agrees with GitHub's own language bars.
COLOURS = {
    "Go": "#00ADD8", "TypeScript": "#3178c6", "JavaScript": "#f1e05a",
    "CSS": "#663399", "HTML": "#e34c26", "Rust": "#dea584",
    "Shell": "#89e051", "C": "#555555", "C++": "#f34b7d",
    "Brightscript": "#662D91", "NSIS": "#cccccc", "PowerShell": "#012456",
}
OTHER = "#8b949e"

# tokyonight, to sit beside the summary cards.
BG, TITLE, TEXT, MUTED = "#1a1b27", "#70a5fd", "#38bdae", "#a9b1d6"


def gh(*args):
    return json.loads(subprocess.check_output(["gh", *args], text=True, encoding="utf-8"))


def totals():
    repos = gh("repo", "list", OWNER, "--limit", "200", "--json", "name,isFork")
    sums = {}
    for repo in repos:
        if repo["isFork"]:
            continue
        for lang, n in gh("api", f"repos/{OWNER}/{repo['name']}/languages").items():
            sums[lang] = sums.get(lang, 0) + n
    return sums


def svg(sums):
    total = sum(sums.values())
    ranked = sorted(sums.items(), key=lambda kv: -kv[1])
    shown = ranked[:TOP]
    rest = sum(n for _, n in ranked[TOP:])
    if rest:
        shown.append(("Other", rest))

    w, h, pad, bar_w = 340, 200, 25, 290
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">',
        f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="6" fill="{BG}"/>',
        f'<text x="{pad}" y="34" font-family="Segoe UI,Helvetica,Arial,sans-serif" '
        f'font-size="18" fill="{TITLE}">Languages by Code</text>',
        f'<clipPath id="bar"><rect x="{pad}" y="50" width="{bar_w}" height="10" rx="5"/></clipPath>',
        '<g clip-path="url(#bar)">',
    ]
    x = pad
    for lang, n in shown:
        seg = bar_w * n / total
        out.append(f'<rect x="{x:.2f}" y="50" width="{seg + 0.5:.2f}" height="10" '
                   f'fill="{COLOURS.get(lang, OTHER)}"/>')
        x += seg
    out.append("</g>")

    for i, (lang, n) in enumerate(shown):
        col, row = i % 2, i // 2
        lx, ly = pad + col * 150, 88 + row * 26
        out.append(f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{COLOURS.get(lang, OTHER)}"/>')
        out.append(f'<text x="{lx + 16}" y="{ly}" font-family="Segoe UI,Helvetica,Arial,sans-serif" '
                   f'font-size="12" fill="{TEXT}">{lang} '
                   f'<tspan fill="{MUTED}">{100 * n / total:.1f}%</tspan></text>')

    out.append(f'<text x="{pad}" y="{h - 14}" font-family="Segoe UI,Helvetica,Arial,sans-serif" '
               f'font-size="10" fill="{MUTED}">Bytes of code across all my repos · '
               f'{date.today():%b %Y}</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    sums = totals()
    Path("assets/languages.svg").write_text(svg(sums), encoding="utf-8", newline="\n")
    total = sum(sums.values())
    for lang, n in sorted(sums.items(), key=lambda kv: -kv[1]):
        print(f"{lang:14} {100 * n / total:5.1f}%")
