
import os
import sys
import importlib.util

def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    so_file = os.path.join(
        folder,
        "main.cpython-314-aarch64-linux-android.so"
    )

    if not os.path.isfile(so_file):
        print("[!] Shared library not found:")
        print(so_file)
        return

    try:
        spec = importlib.util.spec_from_file_location(
            "main", so_file
        )

        if spec is None or spec.loader is None:
            raise ImportError("Unable to load shared library")

        module = importlib.util.module_from_spec(spec)
        sys.modules["main"] = module
        spec.loader.exec_module(module)

        print("[+] Module loaded successfully")

        if callable(getattr(module, "main", None)):
            module.main()

    except Exception as error:
        print(f"[!] {type(error).__name__}: {error}")

if __name__ == "__main__":
    main()
