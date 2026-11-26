# Hábitos (loop-habits)

App de hábitos em uma página só (PWA): instala no celular, funciona offline e guarda tudo no próprio aparelho
(`localStorage`). Sem servidor e sem conta.

## Rodar

Abra `index.html` no navegador, ou sirva a pasta (`python -m http.server`) para testar o modo offline (`sw.js`).

## Publicar

Cloudflare Pages (`npx wrangler pages deploy . --project-name loop-habits`).

## Arquivos

| Arquivo | O que é |
|---|---|
| `index.html` | App inteiro (HTML, CSS e JS) |
| `sw.js` | Service worker (offline) |
| `manifest.webmanifest`, `icon-*.png` | Instalação como app |
| `make_icons.py` | Gera os ícones |
