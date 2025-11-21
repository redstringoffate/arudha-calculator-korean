# ======================================================
#   Arudha Pada Calculator (A1 ~ A12)
#   Jaimini 방식 기반 Arudha 계산 엔진
# ======================================================

# ------------------------------------------------------
#   하우스 거리 계산 (1~12 순환)
# ------------------------------------------------------
def house_distance(start, end):
    """
    start → end 까지 몇 칸 떨어졌는지 계산.
    예: 3 → 6 = 3칸
    """
    if end >= start:
        return end - start
    return (12 - start) + end


# ------------------------------------------------------
#   Arudha Pada 계산 함수 A(n)
# ------------------------------------------------------
def calc_arudha(n, lord_positions, house_lords):
    """
    A(n) 계산 함수
    n: 기준 하우스 번호 (1~12)
    lord_positions: 행성 위치 dict (ex: {"Moon": 11, ...})
    house_lords: 각 하우스 로드 dict (ex: {1: "Moon", ...})
    """

    # 1) 기준 하우스 로드 찾기
    lord = house_lords[n]
    lord_house = lord_positions[lord]

    # 2) 거리 계산
    dist = house_distance(n, lord_house)

    # 0칸이면 1칸 처리
    if dist == 0:
        dist = 1

    # 3) Arudha = lord_house + dist
    arudha = lord_house + dist
    if arudha > 12:
        arudha -= 12

    # 4) doubling rule:
    if arudha == n:
        arudha = arudha + dist
        if arudha > 12:
            arudha -= 12

    return arudha


# ------------------------------------------------------
#   A1 ~ A12 전체 계산
# ------------------------------------------------------
def calc_all_arudhas(lord_positions, house_lords):
    result = {}

    # AL (A1) 처리
    result["AL"] = calc_arudha(1, lord_positions, house_lords)

    # A2~A12
    for n in range(2, 13):
        result[f"A{n}"] = calc_arudha(n, lord_positions, house_lords)

    return result

