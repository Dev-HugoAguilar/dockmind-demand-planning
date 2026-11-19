# Pipeline de datos y modelos

Todos los scripts resuelven rutas de forma explícita desde la **raíz del
repositorio** (`RAIZ = Path(__file__).resolve().parents[1]`). Se pueden ejecutar
desde cualquier directorio: los artefactos siempre caen en el mismo lugar. Los
JSON se leen y escriben siempre como UTF-8 explícito, para que la codificación no
dependa del *locale* de la máquina.

## Orden de ejecución

```bash
# desde la raíz del repositorio
python pipeline/prepare_data.py      # 1. catálogo sintético  -> web/data.json
python pipeline/train_models.py      # 2. entrenamiento       -> web/data.json, models/, research/model_report.json
python pipeline/build.py             # 3. prototipo offline   -> legacy/DockMind_prototipo.html
```

El orden importa: `prepare_data.py` **regenera** `web/data.json` y borra la
sección `ml` que consume la demo. `train_models.py` la vuelve a escribir. Si se
ejecuta `prepare_data.py` después del entrenamiento, el prototipo y las
verificaciones quedan sin resultados de modelos hasta repetir el paso 2.

### Paso 1 · `prepare_data.py`

Fixture determinista (semilla 37): 48 SKU, 104 semanas de historia, 12 semanas de
horizonte y 26 cortes de *backtest* por SKU. Escribe `web/data.json` con
`label`, `history`, `horizon` y `products`.

### Paso 2 · `train_models.py`

Entrena Ridge y Random Forest multisalida más las referencias estacional y Holt,
con ventanas que terminan antes de cada corte. Escribe:

- `web/data.json` — añade `ml` (métricas, ganador por WAPE de validación,
  intervalos empíricos 10/90 y pronósticos por SKU).
- `models/synthetic/*.joblib` — artefactos del catálogo sintético.
- `models/walmart/*.joblib` — solo si se aporta el CSV del benchmark.
- `research/model_report.json` — resultados, cortes y procedencia.

Sin argumentos entrena **solo** el catálogo sintético. El benchmark público es
**opcional**:

```bash
python pipeline/download_benchmark.py                    # crea research/Walmart.csv (requiere red)
python pipeline/train_models.py research/Walmart.csv     # ruta opcional al CSV
```

`download_benchmark.py` crea `research/` si no existe. El CSV crudo no se
redistribuye en el repositorio. Si se pasa una ruta que no existe,
`train_models.py` falla con `FileNotFoundError` en lugar de continuar en
silencio.

### Paso 3 · `build.py`

Lee `web/index.html`, `web/styles.css`, `web/vendor/d3.min.js`, `web/data.json` y
`web/app.js`, y escribe el prototipo autocontenido en
`legacy/DockMind_prototipo.html`. Falla si no encuentra los puntos de montaje
esperados en `web/index.html`.

## Verificación

Desde la raíz:

```bash
npm ci
npm run verify
```

`qa/verify_runtime.cjs` y `qa/verify_ui.cjs` trabajan sobre el runtime publicado
en `web/`, no sobre el prototipo de `legacy/`. Este repositorio no incluye una
suite `pytest`.

## Entorno verificado

Los comandos de este documento se ejecutaron en Windows con PowerShell, Python
3.12.6 y las versiones fijadas en `requirements.txt` (numpy 2.3.5, pandas 2.2.3,
scikit-learn 1.8.0, joblib 1.6.0). Con ese entorno los artefactos regenerados
coinciden con los publicados salvo la cadena de procedencia `python`
(3.12.6 local frente a 3.12.14 del artefacto anterior) y los bytes de los
archivos `joblib`.
