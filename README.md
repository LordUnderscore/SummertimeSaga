# SummertimeSaga-fork

![Unofficial Fork](https://img.shields.io/badge/Unofficial-Fork-blueviolet)
![Fanmade](https://img.shields.io/badge/Fanmade-Project-orange)
![Purpose](https://img.shields.io/badge/Purpose-Learning-green)
![Engine](https://img.shields.io/badge/Engine-Ren'Py-lightgrey)
![Not for Distribution](https://img.shields.io/badge/Distribution-Prohibited-red)
![18+](https://img.shields.io/badge/Content-18%2B-black)

> **Unofficial, fan-made fork of *Summertime Saga*, built for learning and educational study only.**
> Not affiliated with Kompas Productions or DarkCookie. Not for distribution or monetization.

> [!CAUTION]
> **Adult content (18+ / NSFW).** The original *Summertime Saga* contains explicit sexual content and mature themes. This repository may include such material. **You must be of legal age in your jurisdiction** to view or work with it. Not suitable for minors.

---

## About

This repository is an **unofficial fork** of *Summertime Saga*, cloned for **educational and learning purposes only**. It is **not affiliated** with Kompas Productions or DarkCookie, and is **not intended** to distribute, monetize, or replace the original game.

It exists as a sandbox to study a large, real-world Ren'Py project.

---

## Legal Disclaimer

> [!WARNING]
> All rights to the original game — characters, story, images, audio, and assets — belong to **Kompas Productions**.

This repository **may contain original game assets**, since it was cloned for analysis. Before making it public or redistributing it, you **must** remove all copyrighted content. See [Publishing a Safe Public Version](#publishing-a-safe-public-version).

---

## Goals

What this fork is used to explore:

| Area | Focus |
|------|-------|
| **Ren'Py scripting** | Language syntax, screens, labels, transitions |
| **Game structure** | How a large VN codebase is organized |
| **Game logic** | Routes, event triggers, variables, flags |
| **Assets** | How sprites, audio, and images are wired in |
| **Modding** | Safe modification and experimentation workflows |
| **Reverse engineering** | Reading and understanding existing code |

> [!NOTE]
> This is **not** a replacement for the official game and provides **no** playable alternative.

---

## Requirements

- **[Ren'Py SDK](https://www.renpy.org/latest.html)** — latest stable version
- A machine capable of running Ren'Py
- Basic **Python** and visual-novel scripting knowledge

---

## Getting Started

1. Install the **Ren'Py SDK**.
2. Clone this repository:
   ```bash
   git clone --depth=1 https://github.com/albertolicea00/SummertimeSaga-fork
   ```
   > `--depth=1` skips the heavy `.git` history.

    Strip large files from history (destructive — work on a copy):

    - **[git-filter-repo](https://github.com/newren/git-filter-repo)** (recommended)
    - **[BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)**
3. Open the **Ren'Py Launcher**.
4. Add / select this project folder.
5. Run the project, or open the scripts to explore.

---

## Publishing a Safe Public Version

> [!CAUTION]
> Do not publish this repository as-is. It may contain copyrighted assets.

Before making any fork public:

- [ ] Remove `/game/` assets (images, sprites, audio)
- [ ] Remove the original game's Ren'Py scripts
- [ ] Remove any build containing playable content
- [ ] Keep **only your own original code**
- [ ] Require users to supply their own copy of the game files
- [ ] Add a clear disclaimer

This keeps your project legal and safe.

---

## Credits

- **Summertime Saga** — [Kompas Productions](https://summertimesaga.com/)
- **DarkCookie** — original creator
- **[@LordUnderscore](https://github.com/LordUnderscore/)** — source repo this fork was cloned from
- Community contributors and modders

---

*This fork exists only for **learning**, **study**, and **experimentation**.*
