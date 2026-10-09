cat > run.py <<'PY'
import os
import sys
import importlib.util

BASE = os.path.dirname(os.path.realpath(__file__))
SO = os.path.join(
    BASE, "main.cpython-314-aarch64-linux-android.so"
)

print("[*] Python:", sys.executable)
print("[*] Module:", SO)

if not os.path.isfile(SO):
    print("[!] .so file not found")
    sys.exit(1)

try:
    spec = importlib.util.spec_from_file_location("main", SO)
    if spec is None or spec.loader is None:
        raise ImportError("Cannot create module loader")

    module = importlib.util.module_from_spec(spec)
    sys.modules["main"] = module
    spec.loader.exec_module(module)

    if callable(getattr(module, "main", None)):
        module.main()

except Exception as e:
    print(f"[!] {type(e).__name__}: {e}")
PY
