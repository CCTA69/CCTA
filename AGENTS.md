# AGENTS.md

## Cursor Cloud specific instructions

### Repository structure

This is a hobby/experimental project collection. The `main` branch contains only a `README.md`. Actual projects live on feature branches:

| Branch | Project | Tech | Run command |
|---|---|---|---|
| `3D-roguelike-zombie-punching-game` | 3D zombie arena game | Single HTML file | Open in browser or serve with `python3 -m http.server` |
| `codex/create-rpg-game-project` | Text-based RPG "Aeria's Trial" | Python 3 (no deps) | `python3 game.py` |
| `puppeteer-mcp-11575993454368217764` | Puppeteer MCP server | Node.js / TypeScript | `npm install && npm run build && npm start` |

### Development notes

- **No shared dependencies**: Each branch is an independent mini-project. There is no monorepo tooling, no shared `package.json`, and no top-level build system.
- **No lint/test framework on main**: The `main` branch has no configured linters or test runners. Individual branches may have their own.
- **Puppeteer MCP server**: Uses TypeScript 6.x. Build with `npm run build` (runs `tsc`). The server communicates via stdio (not HTTP). On headless VMs, Puppeteer will auto-download Chromium during `npm install`.
- **Python RPG game**: Pure stdlib Python, no `requirements.txt` needed. The game uses `input()` for terminal interaction; for non-interactive testing, pipe choices via stdin (e.g., `echo -e "1\n1\n1" | python3 game.py`).
- **HTML game**: Self-contained single HTML file with inline JS/CSS. Serve from any static HTTP server or open directly in a browser.
