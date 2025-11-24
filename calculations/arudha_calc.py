# ======================================================
#   Arudha Pada Calculator — Clean Version (No Hidden Chars)
#   Jaimini 방식 기반
# ======================================================

def house_distance(start, end):
    """start → end 거리계산 (1~12 cycle)"""
    if end >= start:
        return end - start
    return (12 - start) + end


def calc_arudha(n, lord_positions, house_lords):
    """
    n: 기준 하우스 번호 (1~12)
    lord_positions: {"Sun": 5, "Moon": 11, ...}  # planet → house
    house_lords:    {1:"Mars", 2:"Venus", ...}
    """

    lord = house_lords[n]
    lord_house = lord_positions[lord]

    dist = house_distance(n, lord_house)

    # 1) 기본 계산
    arudha = lord_house + dist
    if arudha > 12:
        arudha -= 12

    # 2) 예외 — 원래 하우스와 동일하면 +10
    if arudha == n:
        arudha += 10
        if arudha > 12:
            arudha -= 12

    # 3) 예외 — 원래 하우스의 7번째면 +10
    seventh = ((n + 6 - 1) % 12) + 1
    if arudha == seventh:
        arudha += 10
        if arudha > 12:
            arudha -= 12

    return arudha


def calc_all_arudhas(lord_positions, house_lords):
    """
    모든 Arudha Pada 계산
    """
    result = {}
    result["AL"] = calc_arudha(1, lord_positions, house_lords)

    for n in range(2, 13):
        result[f"A{n}"] = calc_arudha(n, lord_positions, house_lords)

    return result
