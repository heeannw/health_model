import pandas as pd
import sys

wave = sys.argv[1] if len(sys.argv) > 1 else "w09_20260413.dta"

reader = pd.io.stata.StataReader(wave)
labels = reader.variable_labels()

target_vars = [
    "C009", "C014", "C020", "C025", "C030", "C035", "C040", "C050",
    "C203", "C205", "C208", "C209", "C212",
    "C106", "Cadd_01",
    "pid", "hhid",
    "w0Xhh", "mergid"
]

print(f"=== {wave} 핵심 변수 확인 ===")
for v in target_vars:
    lbl = labels.get(v, "-- 없음 --")
    print(f"  {v:15s}: {lbl}")

print()
print("=== C2xx / Cadd 계열 ===")
for v, l in sorted(labels.items()):
    if v.startswith("C2") or v.startswith("Cadd"):
        print(f"  {v:15s}: {l}")

print()
print("=== 개인 ID 관련 변수 ===")
for v, l in sorted(labels.items()):
    if any(k in v.lower() for k in ["pid", "id", "hhid", "merg"]):
        print(f"  {v:15s}: {l}")
