"""Descarga explícita del benchmark público. No se consulta desde el navegador."""
from pathlib import Path
from urllib.request import urlopen
import hashlib

RAIZ = Path(__file__).resolve().parents[1]
URL = 'https://raw.githubusercontent.com/GonzaloBP/Almacen-de-datos-Walmart/main/Walmart.csv'
DEST = RAIZ / 'research' / 'Walmart.csv'

def main() -> Path:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(URL, timeout=60) as r:
        data = r.read()
    DEST.write_bytes(data)
    print(f"{DEST} · {len(data):,} bytes · sha256={hashlib.sha256(data).hexdigest()}")
    return DEST

if __name__ == "__main__":
    main()
