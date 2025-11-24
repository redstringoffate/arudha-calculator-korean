# ======================================================
#   UL 계산용 하우스 거리 함수 (독립형)
# ======================================================
def house_distance(start, end):
    if end >= start:
        return end - start
    return (12 - start) + end


# ======================================================
#   Upapada Lagna (UL) – 완전 수정된 최종버전
# ======================================================
def calc_UL(lord_positions, house_lords):

    # 1) 12H 로드
    lord = house_lords[12]
    lord_house = lord_positions[lord]

    # 2) 거리 계산
    dist = house_distance(12, lord_house)

    # 0 → 1 처리 (UL 고유 규칙)
    if dist == 0:
        dist = 1

    # 3) 기본 UL 계산
    ul = lord_house + dist
    if ul > 12:
        ul -= 12

    # 4) UL 전용 예외: 결과가 12H면 1H로 이동
    if ul == 12:
        ul = 1

    # 5) UL 전용 예외: UL = 1H → 7H로 이동
    #    (가장 널리 쓰이는 전통 규칙)
    if ul == 1:
        ul = 7

    return ul
