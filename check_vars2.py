import pandas as pd
import sys

wave = sys.argv[1] if len(sys.argv) > 1 else "w09_20260413.dta"

reader = pd.io.stata.StataReader(wave)
labels = reader.variable_labels()

# 모든 변수 출력 (질환/ADL 관련 키워드 필터)
print(f"=== {wave} 전체 변수 수: {len(labels)} ===\n")

# 관련 키워드로 필터링
keywords = ["질환", "병", "질병", "고혈압", "당뇨", "암", "심장", "뇌", "관절", "폐", "간", "신장",
            "치매", "ADL", "일상", "도움", "이동", "목욕", "몸단장", "외출", "복약", "약",
            "체중", "키", "몸무게", "나이", "성별", "연령"]

print("=== 질환/건강 관련 변수 ===")
for v, l in sorted(labels.items()):
    try:
        decoded = l.encode('latin1').decode('cp949') if l else l
    except:
        decoded = l
    if any(kw in decoded for kw in keywords):
        print(f"  {v:20s}: {decoded}")

print()
# w09 고유 변수 패턴 확인 (앞 3글자 패턴)
prefixes = {}
for v in labels.keys():
    p = v[:3] if len(v) >= 3 else v
    prefixes[p] = prefixes.get(p, 0) + 1
print("=== 변수명 앞 3자 패턴 (많은 순) ===")
for p, cnt in sorted(prefixes.items(), key=lambda x: -x[1])[:30]:
    print(f"  {p}: {cnt}개")
