# ======================================================
#   Arudha Pada Calculator (A1 ~ A12)
#   정통 Jaimini 방식 기반 — 예외 규칙 올바르게 적용
# ======================================================

def house_distance(start, end):
    """start → end까지의 거리 (1~12 순환)"""
    if end >= start:
        return end - start
    return (12 - start) + end


def calc_arudha(n, lord_positions, house_lords):
    """
    A(n) 계산 함수
    n: 기준 하우스 번호 (1~12)
    lord_positions: {"Moon": 11, ...}
    house_lords: {1: "Moon", ...}
    """

    lord = house_lords[n]
    lord_house = lord_positions[lord]

    # ------------------------------------------------------
    # 🔥 예외 규칙 — AL(A1)에만 적용
    # ------------------------------------------------------
    if n == 1:
        # 1) lord가 ASC와 동일한 하우스
        if lord_house == 1:
            return 10

        # 2) lord가 7번째 하우스에 있을 경우
        if house_distance(1, lord_house) == 7:
            return 4   # (일반적으로 4th 사용)

    # ------------------------------------------------------
    # A2~A12는 예외 규칙 없음
    # ------------------------------------------------------

    # 기본 거리
    dist = house_distance(n, lord_house)

    # 기본 Arudha 공식
    arudha = lord_house + dist
    if arudha > 12:
        arudha -= 12

    # doubling rule — 결과가 원래 하우스와 동일할 때 다시 이동
    if arudha == n:
        arudha += dist
        if arudha > 12:
            arudha -= 12

    return arudha


def calc_all_arudhas(lord_positions, house_lords):
    result = {}
    result["AL"] = calc_arudha(1, lord_positions, house_lords)

    for n in range(2, 13):
        result[f"A{n}"] = calc_arudha(n, lord_positions, house_lords)

    return result
