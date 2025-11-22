def calc_arudha(n, lord_positions, house_lords):

    lord = house_lords[n]
    lord_house = lord_positions[lord]

    # ------------------------------------------------------
    # AL (A1)만 예외 규칙 적용
    # ------------------------------------------------------
    if n == 1:
        # lord가 ASC와 같은 하우스
        if lord_house == 1:
            return 10

        # lord가 ASC에서 7번째
        if house_distance(1, lord_house) == 7:
            return 4   # 또는 전통 따라 10 선택 가능

    # ------------------------------------------------------
    # A2~A12는 예외 규칙 없음
    # ------------------------------------------------------
    dist = house_distance(n, lord_house)

    # 기본 공식
    arudha = lord_house + dist
    if arudha > 12:
        arudha -= 12

    # doubling rule
    if arudha == n:
        arudha += dist
        if arudha > 12:
            arudha -= 12

    return arudha
