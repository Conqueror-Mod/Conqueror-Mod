<div align="center">

![banner](./assets/banner.png)

**AI Engineer · Consultant · Point-of-Sale Engineer**
I build AI-driven systems and point-of-sale platforms, ship secure desktop software, and advise teams on getting it right — with an artist's eye for how it all comes together.

[![Email](https://img.shields.io/badge/Email-conqueror.conqueredtime%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:conqueror.conqueredtime@gmail.com)
![Focus](https://img.shields.io/badge/Focus-AI%20%C2%B7%20Point--of--Sale%20%C2%B7%20Security%20%C2%B7%20Desktop-blueviolet?style=flat-square)
![Profile views](https://komarev.com/ghpvc/?username=Conqueror-Mod&style=flat-square&color=blueviolet&label=Profile+views)

🚀 **Currently:** **LANcast 1.0 is out** — a self-hosted media server for films, TV, music, photos, comics, audiobooks and retro games. Next up: a native Roku app.

</div>

---

## 👋 About

I take systems apart to understand them, then rebuild them harder and cleaner. Fifteen years as an IT engineer and technical-support specialist taught me how real systems fail; the rest of my path — game design, competitive gaming, creative teaching, and now AI — taught me how to make them hold.

- 🤖 **AI Engineer** — I design and build AI-driven tooling and automation, wiring models into real workflows that ship.
- 🧭 **Consultant** — I advise teams on architecture, security, and quality, then help them execute — not just diagnose.
- 🛒 **Point-of-Sale Engineer** — I build and integrate point-of-sale systems, from the transaction flow to the hardware it runs on.
- 🔒 **Security-minded builder** — encryption-at-rest, hardened desktop apps, and adversarial QA tooling are my default, not an afterthought.
- 🎨 **Artist & art teacher** — a former full-time artist and art instructor; I still lead small classes now and then, and that eye for design carries into everything I build.

---

## 🔥 What I'm building

### 📺 [LANcast](https://github.com/Conqueror-Mod/LANcast) — *v1.0, stable*
**Your own media server.** Films, TV, music, photos, comics, audiobooks and retro games — on your hardware, under your control, with nothing phoning home. Plex's streamlined polish, Kodi's customizability, and neither one's compromises: no subscription, no account with anybody, no relay you rent.

<p align="center">
  <a href="https://github.com/Conqueror-Mod/LANcast"><img src="https://raw.githubusercontent.com/Conqueror-Mod/LANcast/main/docs/screenshots/home.jpg" alt="The LANcast home screen" width="80%"></a>
</p>

- 🎬 **Films and TV that look after themselves** — collections build themselves, intros and credits are found by listening to and looking at the episodes, and any field you correct is locked against every refresh and rescan
- ▶️ **Plays almost anything** — libmpv in the desktop app; everywhere else the server chooses direct play, remux or transcode and *tells you why*, with hardware encoding picked by a real test encode
- 🍿 **Watch Together across the internet** — synchronised rooms, paired servers that see what friends are watching, and *Play on another device* from your phone to the TV-room PC
- 🎵 **Music done properly** — gapless playback, crossfades, synced lyrics, ReplayGain, MusicBrainz albums, and full **MilkDrop** visualizers with their shaders
- 🕹️ **Retro games** — identified by hash, played in the app or a browser, saves kept server-side, with **RetroAchievements** pop-ups in-game
- 👥 **Built for a household** — per-person accounts, private-by-default viewing, content-rating limits, passkeys and two-factor sign-in
- 🔒 **Secure by default** — loopback-only until the first account exists, then HTTPS with a pinned key, server-side sessions, double CSRF defence, and a sandboxed **WebAssembly plugin runtime** (deny-by-default)
- 🐹 **Under the hood** — Go · pure-Go SQLite (no cgo) · React + TypeScript · one documented HTTP API with an OpenAPI spec · Windows app + service, Linux systemd · self-updating, signed releases · 125 decision records

### ⏱️ [Conquered Time](https://github.com/Conqueror-Mod/conquered-time)
**Professional time-intelligence for remote pros juggling multiple clients.** A secure desktop time tracker where everything lives in an **AES-256-encrypted local vault** — no cloud, no account server, no outbound calls.

- 🔒 **Security-first** — AES-256-GCM at rest, PBKDF2 (310k) key derivation, TOTP MFA + Windows Hello, one-time recovery, hardened sandboxed Electron with a strict CSP
- 🌌 **Company Galaxy** — your client network as an interactive packed-bubble map, with identity colors that follow each company across the whole app
- 🧾 **Invoicing & audit** — turn tracked hours into numbered PDF invoices; an audit engine flags punch discrepancies; scheduled email reports over your own SMTP
- ⚡ **Lives in the tray** — global clock-in/out hotkey, idle nudges, and a self-updater that ships new versions straight from GitHub Releases
- 🛠️ **Under the hood** — Electron · TypeScript (strict) · sql.js (WASM SQLite, zero native deps) · property-tested crypto paths

### 🧪 The Crucible *(private)* — *RCA › DMAIC › PDCA*
The adversarial QA tooling I use to keep apps like Conquered Time honest — a method and a runnable tool. Point it at any website, Electron app, or **native desktop app**; it crawls every reachable state, runs adversarial probes, and emits a **ranked defect register**. The name reads inside-out: **RCA** on every individual defect, sitting inside a **DMAIC** campaign, whose Improve phase is made of **PDCA** fix loops.

- 🦀 Rust core · 🌲 native accessibility walkers (Windows UIA · macOS AX · Linux AT-SPI) · 🎭 Playwright adapter for web/Electron over CDP

### 🔐 Project-Gambit *(private)*
**A research design toward a successor to MFA / passkeys.** Passkeys fixed phishing but froze the credential: one keypair, valid until revoked, and a theft you never see. Gambit mutates the credential on *every* successful handshake — so a cloned one desyncs the moment either copy is used, making cloning self-expiring and detectable — and pairs it with a glyph handshake ceremony that turns server authentication into something a human can actually *see*.

- 🎯 Aims at the **fallback downgrade** ("passkeys unavailable, enter your backup code"), the dominant real-world passkey bypass
- 🔬 Conceptual, with both load-bearing protocols machine-checked in **Tamarin** — not cryptographically reviewed, and not a library to deploy

---

## 🧰 Toolbox

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Electron](https://img.shields.io/badge/Electron-47848F?style=for-the-badge&logo=electron&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![WebAssembly](https://img.shields.io/badge/WebAssembly-654FF0?style=for-the-badge&logo=webassembly&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Windows](https://img.shields.io/badge/Win32%2FUIA-0078D4?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/AT--SPI-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Apple](https://img.shields.io/badge/macOS%20AX-000000?style=for-the-badge&logo=apple&logoColor=white)

---

## 📊 Stats

| | 📺 [LANcast](https://github.com/Conqueror-Mod/LANcast) | ⏱️ [Conquered Time](https://github.com/Conqueror-Mod/conquered-time) |
|---|---|---|
| **Latest release** | v1.0.1 | v3.27.1 |
| **Started** | Jul 2026 | Jun 2026 |
| **Commits** | ~3,000 | ~480 |
| **Merged PRs** | 1,170 | 172 |
| **Tests** | 4,400+ Go · 2,400+ client | 160+, property tests on the crypto paths |
| **Code** | ~280k lines of Go | ~12k lines of TypeScript |
| **Design records** | 125 ADRs | 6 feature plans + a vault-format spec |

<sub>Project figures as of November 2026.</sub>

<div align="center">

![Stats](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Conqueror-Mod&theme=tokyonight&v=202611)
<img src="./assets/languages.svg" alt="Languages by bytes of code across all my repositories">

![Streak](https://streak-stats.demolab.com?user=Conqueror-Mod&theme=tokyonight&hide_border=true&v=202611)

</div>

---

<div align="center">

*"Melt it down under adversarial load, and prove what survives."*

**Reach me**

[![Email](https://img.shields.io/badge/Email-conqueror.conqueredtime%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:conqueror.conqueredtime@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-Conqueror--Mod-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Conqueror-Mod)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-Support%20my%20work-FF5E5B?style=for-the-badge&logo=kofi&logoColor=white)](https://ko-fi.com/christheconqueror)

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer)

</div>
