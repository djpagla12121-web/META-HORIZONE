
cd ~/META-HORIZONE

cat > run.py <<'PY'
import os
import sys
import importlib.util

folder = os.path.dirname(os.path.abspath(__file__))
so_file = os.path.join(
    folder,
    "main.cpython-314-aarch64-linux-android.so"
)

if not os.path.isfile(so_file):
    print("[!] .so file not found:", so_file)
    sys.exit(1)

try:
    spec = importlib.util.spec_from_file_location("main", so_file)

    if spec is None or spec.loader is None:
        raise ImportError("Cannot load main module")

    module = importlib.util.module_from_spec(spec)
    sys.modules["main"] = module
    spec.loader.exec_module(module)

    if callable(getattr(module, "main", None)):
        module.main()

except Exception as e:
    print(f"[!] {type(e).__name__}: {e}")
PY
