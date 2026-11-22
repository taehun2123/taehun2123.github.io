# taehun2123.github.io

> **요약** (기준일 2026-11-22)
>
> - 포트폴리오 단일 페이지: 넉터, 에게, 버스트래커 3개 프로젝트의 트러블슈팅과 기여도
> - 지원 대상: 당근 2027 프로덕트 빌더 인턴십 커뮤니티 팀(서류 마감 2026-12-06)
> - 공개 정보 기준: 사진 제외, 학력은 하단 이력 구역에만 표기, 영상의 발표자 얼굴 구간 제외
> - 정적 파일 배포: GitHub Pages `main` 브랜치 루트, 빌드 단계 없음
> - 기술 블로그는 별도 저장소(`/blog`)에서 배포
>
> | 항목 | 값 | 비교 기준 |
> |---|---|---|
> | 소개 프로젝트 | 3개 | 과제 최소 기준 1개 |
> | 트러블슈팅 카드 | 13건 | 넉터 5건, 에게·버스트래커 각 4건 |
> | 시연 영상 합계 | 약 45MB | GitHub 파일 권장 상한 50MB(파일당) |
> | 이력서 PDF | A4 2쪽 | 없음 |
>
> **다음 작업**: 넉터 회원 수 등 운영 지표 갱신 시 `index.html`과 이력서 PDF 동시 수정

- 배포 주소: https://taehun2123.github.io/
- 블로그: https://taehun2123.github.io/blog/

## 1. 파일 구성: 페이지 1개와 에셋

**1-1. 페이지는 `index.html` 1개이며 스타일은 `assets/site.css`에 있습니다.**

| 경로 | 내용 |
|---|---|
| `index.html` | 포트폴리오 본문(요약, 프로젝트 3개, 이력, 연락처) |
| `assets/site.css` | 디자인 토큰(빨강 1색, 잉크, 회색 단계), IBM Plex Sans KR, 반응형 규칙 |
| `assets/video/` | 시연 영상 3개(`nuktu-demo.mp4`, `ege-demo.mp4`, `bbb-demo.mp4`) |
| `assets/taehun-clay-bold.svg` | 가로형 워드마크 로고. 상단 바와 이력서 머리에 사용 |
| `assets/th-clay-bold.svg` | 정사각형 심볼 로고. 파비콘에 사용 |
| `assets/img/` | 영상 포스터 이미지 3개 |
| `assets/kim-taehun-resume.pdf` | 다운로드용 이력서 |
| `assets/kim-taehun-portfolio.pdf` | 당근 제출용 서비스 소개 PDF(A4 6쪽). 팀 구성과 담당, 지표, 사용자 문제와 변경, 기술 선택 순서 |
| `_resume/portfolio.html` | 서비스 소개 PDF 원본. 밑줄 폴더라 배포 대상에서 제외됨 |
| `_resume/resume.html` | 이력서 원본. 밑줄 폴더라 Jekyll 배포 대상에서 제외됨 |
| `google*.html`, `naver*.html`, `robots.txt`, `sitemap.xml` | 검색 엔진 소유 확인 파일 |

**1-2. 페이지에는 드롭다운, 토글, 모달을 넣지 않습니다.**

모든 내용은 펼친 상태로 배치합니다. 상호작용 요소는 링크와 영상 재생 컨트롤뿐입니다.

## 2. 이력서 PDF 생성: Chrome 인쇄

**2-1. `_resume/resume.html`을 고친 뒤 아래 명령으로 PDF를 다시 생성하십시오.**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf=assets/kim-taehun-resume.pdf "file://$PWD/_resume/resume.html"
```

서비스 소개 PDF는 같은 명령에서 입력을 `_resume/portfolio.html`, 출력을 `assets/kim-taehun-portfolio.pdf`로 바꿔 생성하십시오.

생성 후 `pdffonts`로 IBM Plex Sans KR 포함 여부를 확인하십시오.

## 3. 시연 영상 원본: 프로젝트별 출처

**3-1. 영상은 H.264로 인코딩했습니다. `+faststart` 옵션으로 재생 시작 지연을 단축했습니다.**

| 파일 | 원본 | 처리 |
|---|---|---|
| `nuktu-demo.mp4` | 넉터 앱 화면 녹화 `rec-*.mp4` 10개 | 720×1440, 30fps, CRF 27, 무음 연결(119초) |
| `ege-demo.mp4` | `에게_시연영상_4분_2026-11-21.mp4` | 재인코딩 없이 `+faststart`(239초) |
| `bbb-demo.mp4` | CoShow 발표·시연 영상(2025-11-25) | 발표자 얼굴 구간(0~93.6초) 제외, 1280×720, CRF 25, AAC 96kbps(67초) |

## 4. 다음 작업

| 작업 | 기한 | 담당 |
|---|---|---|
| 넉터 운영 지표(회원 485명, 2026-11-22) 갱신 | 미정 | 김태훈 |
| 수상·학력 변경 시 `index.html`과 `_resume/resume.html` 동시 수정 | 미정 | 김태훈 |
