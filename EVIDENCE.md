# Git 및 프로젝트 실행 증빙

## 1. 개발 환경

프로젝트 개발에 사용한 환경은 다음과 같습니다.

- Python 3.10.8
- Git 2.53.0.windows.1
- Visual Studio Code
- Windows PowerShell

버전 확인 명령어:

```bash
python --version
git --version
```

## 2. Git 사용자 설정

프로젝트 커밋을 위해 다음과 같이 Git 사용자 정보를 설정했습니다.

```text
user.name: Seowon Kim
user.email: kimblessing22@gmail.com
```

확인 명령어:

```bash
git config user.name
git config user.email
```

## 3. GitHub 저장소 복제 확인

저장소가 정상적으로 복제되는지 다음 명령어로 확인했습니다.

```bash
git clone https://github.com/kimblessing22-commits/prompt-manager.git ../prompt-manager-clone-test
```

실행 결과, 바탕화면에 `prompt-manager-clone-test` 폴더가 생성되었으며 저장소 파일이 정상적으로 복제되었습니다.

## 4. 브랜치 생성 및 병합

프롬프트 목록 기능은 `main` 브랜치에서 바로 작업하지 않고 별도의 기능 브랜치에서 개발했습니다.

사용한 브랜치:

```text
main
feature/prompt-list
```

사용한 주요 명령어:

```bash
git checkout -b feature/prompt-list
git checkout main
git merge --no-ff feature/prompt-list -m "merge: add prompt list feature"
```

실제 병합 기록:

```text
* c196d55 merge: add prompt list feature
|\
| * 9670127 feat: add prompt list
|/
```

목록 기능의 구현과 실행 테스트가 끝난 후 `main` 브랜치로 병합했습니다.

## 5. 기능 단위 커밋

프로젝트는 한 번에 전체 코드를 커밋하지 않고 기능별로 나누어 커밋했습니다.

주요 커밋:

```text
chore: initialize project
feat: add initial prompt data
feat: add main menu
feat: add menu loop and exit
feat: add prompt creation
feat: add prompt list
merge: add prompt list feature
feat: add category filtering
feat: add prompt search
feat: add prompt detail view
feat: add favorite management
feat: add favorite list
docs: update project README
docs: add environment and design documentation
feat: prevent duplicate prompt titles
```

커밋 기록 확인 명령어:

```bash
git log --oneline --graph --all --decorate
```

## 6. 입력 충돌 처리

같은 제목의 프롬프트가 이미 존재하는 경우 중복으로 추가되지 않도록 처리했습니다.

제목을 비교할 때 영문 대소문자를 구분하지 않으며, 중복된 제목이 발견되면 다음 메시지를 출력합니다.

```text
같은 제목의 프롬프트가 이미 존재합니다.
```

이를 통해 기존 프롬프트와 새 프롬프트 사이의 제목 충돌을 방지합니다.
