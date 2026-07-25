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

print("=== 나만의 프롬프트 관리 ===")
print(f"기본 프롬프트 {len(prompts)}개를 불러왔습니다.")