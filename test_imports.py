# test_imports.py

import os
import importlib

STEP_DIR = os.path.join(os.path.dirname(__file__), "steps")

# coleta todos os .py em steps/, exceto __init__.py
modules = [
    fn[:-3]
    for fn in os.listdir(STEP_DIR)
    if fn.endswith(".py") and fn != "__init__.py"
]

errors = {}
for mod in modules:
    full = f"steps.{mod}"
    try:
        importlib.import_module(full)
    except Exception as e:
        errors[mod] = repr(e)

if not errors:
    print("✅ Todos os módulos em steps/ importaram sem erro!")
else:
    print("❌ Foram encontrados erros na importação dos módulos:\n")
    for mod, err in errors.items():
        print(f"  • {mod:30} → {err}")
    exit(1)
