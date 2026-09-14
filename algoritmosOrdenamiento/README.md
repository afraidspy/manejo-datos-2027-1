# Ordenamientos iterativos

Implementación y análisis de complejidad de cuatro algoritmos de ordenamiento
iterativos. Los elementos se ordenan de **menor a mayor**.

## Estructura

```
ordenamientos-iterativos/
├── main.py                 # genera los datos, ejecuta y mide
└── ordenamientos/
    ├── ordenable.py        # OrdenableIterativo (clase abstracta)
    ├── burbuja.py
    ├── burbuja_mejorado.py
    ├── seleccion.py
    └── insercion.py
```

Cada algoritmo vive en su propio archivo y expone un único método, `ordenar`,
que ordena la lista en sitio y la devuelve. La clase abstracta aporta el
contrato y la operación compartida `intercambiar`.

## Ejecución

```bash
python main.py
```

## Uso

```python
from ordenamientos import Seleccion

datos = [1, 7, 11, 2, 0, 5, 10, 3, 4]
Seleccion().ordenar(datos)
```

## Complejidad

| Algoritmo | Mejor caso | Peor caso | Intercambios (peor caso) |
|---|---|---|---|
| Burbuja | O(n²) | O(n²) | O(n²) |
| BurbujaMejorado | O(n) | O(n²) | O(n²) |
| Seleccion | O(n²) | O(n²) | O(n) |
| Insercion | O(n) | O(n²) | O(n²) |

Los cuatro son O(n²) en el peor caso, pero se distinguen en dos cosas: burbuja
mejorado e inserción bajan a O(n) cuando la lista ya viene ordenada, y selección
hace a lo sumo n−1 intercambios, aunque nunca deja de comparar n(n−1)/2 veces.

## Para agregar un algoritmo nuevo

Crear un archivo en `ordenamientos/`, heredar de `OrdenableIterativo`,
implementar `ordenar` y exportarlo en `__init__.py`.
