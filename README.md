# sqlite-trigger-effect-ledger

## Français

Observer les effets indirects des déclencheurs SQLite.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m sqlite_trigger_effect_ledger examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Déclenche un vrai audit SQLite puis injecte une violation CHECK ; compare compteur de changements tentés et état réellement conservé après rollback.

### Limites

Schéma stock fixe, pas analyseur général de triggers. Les compteurs ne prouvent pas des effets validés.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Observe indirect SQLite trigger effects.

Synthetic data; no network access or secret required.

```sh
python -m sqlite_trigger_effect_ledger examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Triggers actual SQLite auditing then injects a CHECK violation; compares attempted-change counters with state actually retained after rollback.

### Limits

Fixed stock schema, not a general trigger analyzer. Counters do not prove committed effects.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Observar efectos indirectos de disparadores SQLite.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m sqlite_trigger_effect_ledger examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Activa auditoría SQLite real e inyecta violación CHECK; compara contadores de cambios intentados con estado retenido tras rollback.

### Límites

Esquema de existencias fijo, no analizador general de triggers. Los contadores no prueban efectos confirmados.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.sqlite.org/lang_createtrigger.html
