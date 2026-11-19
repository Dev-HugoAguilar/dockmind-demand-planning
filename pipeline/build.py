"""Empaqueta la aplicación de web/ en un HTML autocontenido dentro de legacy/."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
WEB = RAIZ / "web"
SALIDA = RAIZ / "legacy" / "DockMind_prototipo.html"

MONTURAS = (
    '<link rel="stylesheet" href="styles.css">',
    '<script src="vendor/d3.min.js"></script>',
    '<script src="app.js"></script>',
)


def main() -> Path:
    html = (WEB / "index.html").read_text(encoding="utf-8")
    for montura in MONTURAS:
        if montura not in html:
            raise RuntimeError(f"No se encontró el punto de montaje en web/index.html: {montura}")
    html = html.replace(
        MONTURAS[0],
        "<style>" + (WEB / "styles.css").read_text(encoding="utf-8") + "</style>",
    )
    html = html.replace(
        MONTURAS[1],
        "<script>" + (WEB / "vendor/d3.min.js").read_text(encoding="utf-8") + "</script>",
    )
    html = html.replace(
        MONTURAS[2],
        '<script id="data" type="application/json">'
        + (WEB / "data.json").read_text(encoding="utf-8")
        + "</script><script>"
        + (WEB / "app.js").read_text(encoding="utf-8")
        + "</script>",
    )
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(html, encoding="utf-8", newline="\n")
    print(f"Prototipo autocontenido: {SALIDA} · {len(html):,} caracteres")
    print(f"Origen: {WEB}")
    return SALIDA


if __name__ == "__main__":
    main()
