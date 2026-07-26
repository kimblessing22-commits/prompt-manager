prompts = [
    {
        "title": "비즈니스 미팅 요청 메일 작성 전문 비서",
        "content": """당신은 비즈니스 메일 작성 전문 비서입니다.

역할
- 사용자의 요청에 따라 비즈니스 메일 초안을 작성합니다.
- 사용자가 필요한 정보를 빠뜨리면 메일을 작성하기 전에 먼저 질문합니다.

규칙
1. 확정되지 않은 내용을 단정적으로 쓰지 않습니다.
2. 이모지를 사용하지 않습니다.
3. 지나치게 긴 문장을 사용하지 않습니다.
4. 사용자가 제공하지 않은 정보는 임의로 작성하지 않습니다.
5. 메일 본문은 원칙적으로 600자 이내로 작성합니다.

출력 형식
- 메일 제목
- 메일 본문: 인사, 자기소개, 목적, 안건, 일정과 장소, 마무리 인사
- 서명: 발신자명, 소속, 연락처, 이메일

톤앤매너
- 격식체
- 정중하되 간결하게
- CEO 또는 임원급 수신자에게 적합한 표현

날짜, 장소, 이름, 회사명, 연락처 등 필요한 정보가 부족하면
메일을 작성하기 전에 최대 5개의 확인 질문을 하세요.""",
        "category": "페르소나",
        "favorite": True
    },
    {
        "title": "Red Book 핫핑크 드레스 영상 생성",
        "content": """A cinematic musical teaser scene set in a foggy Victorian London street.
A bold young woman in a vivid hot pink Victorian dress is seen from behind,
walking forward with confidence.
Her dress and hair flow naturally in the wind as warm golden light breaks through the mist.
Distant brick buildings and gas lamps create an elegant 19th-century atmosphere.
Powerful, uplifting, theatrical mood.
Keep her face hidden.
No distorted body, no extra limbs, no horror.""",
        "category": "영상 생성",
        "favorite": False
    },
    {
        "title": "미국 테크 뉴스 자동 기록 워크플로우",
        "content": """Google News RSS Feed에서 새로운 뉴스가 감지되면 뉴스 정보를 가져옵니다.

뉴스 제목에 NVIDIA 또는 NVDA가 포함되어 있으면 NVIDIA 경로로 분류합니다.
뉴스 제목에 Microsoft 또는 MSFT가 포함되어 있으면 Microsoft 경로로 분류합니다.

분류된 뉴스의 날짜, 종목, 키워드, 뉴스 제목, 링크, 발행일을
Google Sheets의 새로운 행에 자동으로 기록합니다.""",
        "category": "자동화",
        "favorite": False
    }
]
categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
]
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("입력값을 비워둘 수 없습니다. 다시 입력해주세요.")


def choose_category():
    while True:
        print("\n카테고리 선택:")

        for number, category in enumerate(categories, start=1):
            print(f"{number}) {category}")

        choice = input("선택: ").strip()

        if choice.isdigit():
            category_number = int(choice)

            if 1 <= category_number <= len(categories):
                selected_category = categories[category_number - 1]

                if selected_category == "기타":
                    custom_category = input(
                        "직접 사용할 카테고리를 입력하세요: "
                    ).strip()

                    if custom_category:
                        return custom_category

                return selected_category

        print("올바른 카테고리 번호를 입력해주세요.")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    title = get_non_empty_input("제목: ")
    content = get_non_empty_input("내용: ")
    category = choose_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")
def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    for number, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f'{number}. [{prompt["category"]}] '
            f'{prompt["title"]}{favorite_mark}'
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")
def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    available_categories = []

    for prompt in prompts:
        if prompt["category"] not in available_categories:
            available_categories.append(prompt["category"])

    for number, category in enumerate(available_categories, start=1):
        print(f"{number}) {category}")

    choice = input("조회할 카테고리 번호: ").strip()

    if not choice.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    category_number = int(choice)

    if not 1 <= category_number <= len(available_categories):
        print("올바른 번호를 입력해주세요.")
        return

    selected_category = available_categories[category_number - 1]

    print(f"\n=== {selected_category} 프롬프트 ===")

    count = 0

    for prompt in prompts:
        if prompt["category"] == selected_category:
            count += 1
            favorite_mark = " ⭐" if prompt["favorite"] else ""
            print(f'{count}. {prompt["title"]}{favorite_mark}')

    print(f"\n총 {count}개의 프롬프트")    
def search_prompts():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어를 입력하세요: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []

    for prompt in prompts:
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            results.append(prompt)

    if not results:
        print(f"'{keyword}'에 해당하는 프롬프트가 없습니다.")
        return

    print(f"\n=== '{keyword}' 검색 결과 ===")

    for number, prompt in enumerate(results, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f'{number}. [{prompt["category"]}] '
            f'{prompt["title"]}{favorite_mark}'
        )

    print(f"\n총 {len(results)}개의 프롬프트")
def show_prompt_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("저장된 프롬프트가 없습니다.")
        return

    for number, prompt in enumerate(prompts, start=1):
        print(f'{number}. {prompt["title"]}')

    choice = input("확인할 프롬프트 번호: ").strip()

    if not choice.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    prompt_number = int(choice)

    if not 1 <= prompt_number <= len(prompts):
        print("올바른 번호를 입력해주세요.")
        return

    selected_prompt = prompts[prompt_number - 1]
    favorite_text = "예" if selected_prompt["favorite"] else "아니요"

    print("\n=== 프롬프트 정보 ===")
    print(f'제목: {selected_prompt["title"]}')
    print(f'카테고리: {selected_prompt["category"]}')
    print(f'즐겨찾기: {favorite_text}')
    print("내용:")
    print(selected_prompt["content"])
def main():
    print(f"기본 프롬프트 {len(prompts)}개를 불러왔습니다.")

    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompts()
        elif choice == "5":
            show_prompt_detail()
        elif choice in ["6", "7"]:
            print("해당 기능은 아직 준비 중입니다.")
        else:
            print("잘못된 번호입니다. 다시 선택해주세요.")


main()
