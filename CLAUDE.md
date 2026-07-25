# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`Conqueror-Mod/Conqueror-Mod` is the **GitHub profile README** — the magic repo
whose `README.md` renders at <https://github.com/Conqueror-Mod>. There is no
build, no test, and no application code: a banner, a LICENSE, and one markdown
file that is the most public artifact Chris owns.

**Every push is immediately live.** There is no staging step and no preview
environment. Treat a change here the way you would treat publishing, because it
is publishing. Show the diff and get an explicit yes before pushing.

## Content rules

These are not stylistic preferences — they are the reason to slow down:

- **No private client or work project names.** Employer names are acceptable;
  internal project names are not. Describe client work generically ("consulting
  on architecture, security, and quality"), never by project.
- **No franchise references.** Where a name has become a product's own identity
  it stays, but never re-attach it to its source franchise in writing.
- **Identity claims must match reality.** The roles listed in About are load
  bearing — a recruiter or client reads them. Don't embellish them, and don't
  quietly drop one during a rewrite.
- **Only link repositories that are actually public.** A link to a private repo
  is a 404 for every visitor. Verify before linking:

  ```bash
  gh repo view Conqueror-Mod/<name> --json visibility --jq .visibility
  ```

- **Describe a project the way its own repo describes it.** The profile is
  downstream of the projects; if the two disagree, one of them is wrong and it
  is worth resolving rather than papering over.

## Third-party badge services

The README leans on external image services — shields.io, komarev profile
views, github-profile-summary-cards, streak-stats, capsule-render. **They break
without warning.** The shared `github-readme-stats` instance started returning
503 `DEPLOYMENT_PAUSED` and had to be swapped out (commit `3c24800`).

When a card renders blank, the service is usually down rather than the URL being
wrong — check the endpoint directly before rewriting markup. Prefer services
with an alternative already identified over adding a new dependency.

## Assets

`assets/banner.svg` is the source; `assets/banner.png` is the rendered artifact
the README actually references (GitHub's markdown pipeline is unreliable with
SVG). **Edit the SVG, re-render the PNG, commit both** — a PNG that no longer
matches its source is how the banner becomes unmaintainable.

## Verifying a change

Rendered markdown is the only test that matters. After pushing, load
<https://github.com/Conqueror-Mod> and confirm images resolve, links land where
intended, and nothing collapsed — GitHub's renderer sanitizes HTML more
aggressively than a local preview, so `<div align="center">` behavior and image
sizing are worth an actual look.
