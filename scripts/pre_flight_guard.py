#!/usr/bin/env python3
"""
Pre-Flight Guard für QuantumVault AI
Prüft alle Test-Dependencies, führt die Testsuite aus und bricht bei Fehlern ab.
"""
import sys
import subprocess
import pkg_resources

REQUIRED_PACKAGES = ["fastapi", "pytest", "requests", "uvicorn"]

def check_dependencies():
    print("[Pre-Flight] Überprüfe Python-Abhängigkeiten...")
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = [pkg for pkg in REQUIRED_PACKAGES if pkg.lower() not in installed]
    if missing:
        print(f"[FEHLER] Fehlende Python-Module: {missing}", file=sys.stderr)
        print("Bitte ausführen: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)
    print("[Pre-Flight] Alle Abhängigkeiten vorhanden.")

def run_tests():
    print("[Pre-Flight] Starte Testsuite (pytest)...")
    result = subprocess.run([sys.executable, "-m", "pytest"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        print("[FEHLER] Testsuite fehlgeschlagen! Pre-Flight abgebrochen.", file=sys.stderr)
        sys.exit(1)
    print("[Pre-Flight] Testsuite erfolgreich bestanden.")

if __name__ == "__main__":
    check_dependencies()
    run_tests()
    print("[Pre-Flight] Alle Prüfungen erfolgreich bestanden. Ready for deployment.")
    sys.exit(0)
