import pandas as pd
import sys

wave = sys.argv[1] if len(sys.argv) > 1 else "w09_20260413.dta"
prefix = sys.argv[2] if len(sys.argv) > 2 else "w09"

reader = pd.io.stata.StataReader(wave)
labels = reader.variable_labels()

def decode(s):
    if not s:
        return s
    try:
        return s.encode('latin1').decode('cp949')
    except:
        return s

print(f"=== {wave} - C 섹션 (질환/건강) ===")
for v, l in sorted(labels.items()):
    if v.startswith(f"{prefix}C") or v.startswith(f"{prefix}c"):
        print(f"  {v:30s}: {decode(l)}")

print()
print(f"=== {wave} - ADL/IADL 섹션 ===")
for v, l in sorted(labels.items()):
    # Bb 섹션이나 ADL 관련
    if "169" in v or "Bb16" in v or "Bb17" in v:
        print(f"  {v:30s}: {decode(l)}")

print()
print(f"=== {wave} - 기본 정보 (나이/성별/키/몸무게) ===")
keywords_demo = ["나이", "연령", "성별", "키", "몸무게", "체중", "신장", "age", "gender", "height", "weight"]
for v, l in sorted(labels.items()):
    dl = decode(l)
    if any(k in dl for k in keywords_demo) or any(k in v.lower() for k in ["age", "sex", "height", "weight", "bmi"]):
        print(f"  {v:30s}: {dl}")
