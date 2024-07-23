
def determine_flammability(flash_point):
    """
    인화점을 기준으로 가연성 점수를 결정합니다.
    flash_point: 인화점 (°C)
    반환값: 가연성 (1-5)
    """
    if flash_point <= 0:
        return 5
    elif flash_point <= 50:
        return 4
    elif flash_point <= 100:
        return 3
    elif flash_point <= 150:
        return 2
    else:
        return 1

def calculate_fire_risk(ignition_sources, fire_load, temperature, humidity, flammability):
    """
    화재 위험 점수를 계산합니다.
    ignition_sources: 점화원 수 (1-5)
    fire_load: 화재 하중 (1-5)
    temperature: 온도 (°C)
    humidity: 습도 (%)
    flammability: 가연성 (1-5)
    """
    # 온도와 습도의 영향
    temperature_factor = temperature / 30  # 임의의 스케일링, 최대 30°C
    humidity_factor = (100 - humidity) / 50  # 습도가 낮을수록 위험 증가, 최대 50% 습도 감소
    weather_factor = temperature_factor * humidity_factor

    return flammability * ignition_sources * fire_load * weather_factor

def get_input(prompt, value_type=int):
    """
    사용자 입력을 받아 특정 타입의 값을 반환합니다.
    올바른 값이 입력될 때까지 반복합니다.
    """
    while True:
        try:
            value = value_type(input(prompt))
            return value
        except ValueError:
            print("올바른 값을 입력해주세요.")

def get_ranged_input(prompt, min_value, max_value):
    """
    사용자 입력을 받아 특정 범위 내의 정수를 반환합니다.
    """
    while True:
        value = get_input(prompt)
        if min_value <= value <= max_value:
            return value
        else:
            print(f"값은 {min_value}에서 {max_value} 사이여야 합니다. 다시 입력해주세요.")

def main():
    # 사용자 입력
    print("화재 위험 평가 프로그램입니다.")
    flash_point = get_input("인화점 (°C): ", float)
    flammability = determine_flammability(flash_point)
    ignition_sources = get_ranged_input("점화원 수 (1-5): ", 1, 5)
    fire_load = get_ranged_input("화재 하중 (1-5): ", 1, 5)
    temperature = get_input("온도 (°C): ", float)
    humidity = get_ranged_input("습도 (%): ", 0, 100)

    # 화재 위험 계산
    fire_risk_score = calculate_fire_risk(ignition_sources, fire_load, temperature, humidity, flammability)

    # 결과 출력
    print(f"화재 위험 점수: {fire_risk_score:.2f}")

# 유닛 테스트
def test_calculate_fire_risk():
    assert calculate_fire_risk(1, 1, 1, 20, 50, 1) == 0.4
    assert calculate_fire_risk(5, 5, 5, 30, 0, 5) == 125.0
    assert calculate_fire_risk(3, 3, 4, 25, 20, 3) == 16.8
    print("모든 테스트 통과")

if __name__ == "__main__":
    main()
    test_calculate_fire_risk()