# Historial de cambios

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y
las versiones usan [Versionado Semántico](https://semver.org/lang/es/).

## [1.0.0] — 2026-11-26

### Añadido

- Primera publicación como repositorio independiente.
- Aplicación con cinco pantallas exclusivas: resumen, demanda, inventario,
  compras y modelos, con navegación por teclado y estado compartido.
- Pronóstico a 12 semanas con banda de cuantiles 10/90 y cobertura medida en test.
- Matriz de cobertura, calendario de compras, balance semanal, cascada de compra,
  matriz de modelos, distribución de errores, ABC/variabilidad, alternativas
  capital/servicio y 120 escenarios de estrés.
- Cuatro familias de modelos (estacional 52, Holt, Ridge y Random Forest
  multisalida) con artefactos `joblib` y selección por WAPE de validación.
- Benchmark independiente de 45 tiendas × 143 semanas, en USD y ajeno al catálogo
  sintético.
- Verificación de interfaz con jsdom: 36 escenarios de simulación, regresión de
  faltantes previos a recepción y comprobaciones de *layout* y SVG.
- Integración continua que ejecuta ambas verificaciones node.
- Auditoría, referencias y documentación de diseño.
