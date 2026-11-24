# 포트폴리오 사이트 운영 문서

저장소 첫 화면의 [README](../README.md)는 외부 방문자용 소개입니다. 이 문서는 사이트 수정, PDF 생성, 영상 출처, 남은 작업을 기록합니다.

> **요약** (기준일 2026-11-24)
>
> - 포트폴리오 단일 페이지: 넉터, 에게, BBB(BusBuddyBuddy) 3개 프로젝트의 트러블슈팅과 담당 업무
> - 공개 정보 기준: 프로필 사진은 첫 화면과 이력서에 표기(사용자 결정, 2026-11-22), 학력은 하단 이력 구역에만 표기, 영상의 발표자 얼굴 구간 제외
> - 정적 파일 배포: GitHub Pages `main` 브랜치 루트, 빌드 단계 없음
> - 기술 블로그는 별도 저장소(`/blog`)에서 배포
> - 방문 분석: Cloudflare Web Analytics(4절)
>
> | 항목 | 값 | 비교 기준 |
> |---|---|---|
> | 소개 프로젝트 | 3개 | 과제 최소 기준 1개 |
> | 트러블슈팅 카드 | 7건 | 넉터 3건, 에게, BBB 각 2건 |
> | 시연 영상 합계 | 약 50MB | GitHub 파일 권장 상한 50MB(파일당) |
> | 이력서 PDF, 서비스 소개 PDF | A4 2쪽, A4 8쪽 | 제출 형식(PDF) |
>
> **다음 작업**: 넉터 회원 수 등 운영 지표 갱신 시 `index.html`, 이력서, 서비스 소개 PDF 원본을 함께 수정하고 PDF 재생성

- 배포 주소: https://taehun2123.github.io/
- 블로그: https://taehun2123.github.io/blog/

## 1. 파일 구성: 페이지 1개와 에셋

**1-1. 페이지는 `index.html` 1개이며 스타일은 `assets/site.css`에 있습니다.**

| 경로 | 내용 |
|---|---|
| `index.html` | 포트폴리오 본문(요약, 프로젝트 3개, 이력, 연락처) |
| `assets/site.css` | 디자인 토큰(강조색 #0070CC, 잉크, 회색 단계), IBM Plex Sans KR, 반응형 규칙(1024px 미만 상단 가로 스크롤 구역 줄) |
| `assets/video/` | 시연 영상 3개(`nuktu-demo.mp4`, `ege-demo.mp4`, `bbb-demo.mp4`) |
| `assets/taehun-blue-clay.svg` | 가로형 워드마크 로고. 웹 상단 바, 이력서, 포트폴리오 PDF 머리에 사용 |
| `assets/th-blue-clay.svg` | 정사각형 심볼 로고. 파비콘에 사용 |
| `assets/img/` | 영상 포스터 이미지 3개, 프로젝트 아이콘 3개, 프로필 사진 `profile.webp`(480px, 메타데이터 제거), 넉터 서버 구성도 `nuktu-architecture.svg`(가로형), `nuktu-architecture-tall.svg`(모바일 세로형), 에게 서버 구성도 `ege-architecture.png`(2880×1400, 흰 바탕 합성, PDF용)와 `ege-architecture.webp`(웹용). 넉터 구성도는 웹과 PDF에 SVG 본문을 직접 넣어 사용 |
| `assets/kim-taehun-resume.pdf` | 다운로드용 이력서 |
| `assets/kim-taehun-portfolio.pdf` | 서비스 소개 PDF(A4 8쪽, 쪽 번호 포함). 팀 구성과 담당, 지표, 사용자 문제와 변경, 기술 선택 순서 |
| `_resume/portfolio.html` | 서비스 소개 PDF 원본. 밑줄 폴더라 배포 대상에서 제외됨 |
| `_resume/resume.html` | 이력서 원본(A4 2쪽). 밑줄 폴더라 Jekyll 배포 대상에서 제외됨 |
| `_docs/maintenance.md` | 이 문서. 밑줄 폴더라 배포 대상에서 제외됨 |
| `README.md` | 저장소 방문자용 소개 |
| `_resume/build_portfolio.py` | 포트폴리오 PDF 생성 스크립트. 목차 쪽 번호를 채우려고 2회 생성, 공개본과 제출본 생성 |
| `_resume/portfolio.html`의 `<!-- @SUBMIT -->` | 제출본에서만 지원 기업 줄로 바뀌는 자리표시 |
| `google*.html`, `naver*.html` | 검색 엔진 소유 확인 파일. 네이버는 `index.html` 머리의 `naver-site-verification` 메타 태그로도 확인 |
| `robots.txt` | 전체 허용, 사이트맵 2개(루트, `/blog/`) 안내 |
| `sitemap.xml` | 첫 페이지, 포트폴리오 PDF, 이력서 PDF 3개 주소. 내용을 바꾸면 `lastmod` 날짜를 갱신 |
| `301a4763aac1fcfe66eba3aeded16807.txt` | IndexNow 키 파일(Bing, 네이버 등에 변경 주소 알림용). 파일 이름과 내용이 같아야 함 |
| `assets/img/og-image.jpg` | 링크 공유 미리보기 이미지(1200×630) |

**1-2. 페이지에는 드롭다운, 토글, 모달을 넣지 않습니다.**

모든 내용은 펼친 상태로 배치합니다. 상호작용 요소는 링크와 영상 재생 컨트롤뿐입니다.
모바일 상단의 구역 이동 줄은 링크 목록이며 펼침, 접힘 동작이 없습니다.
움직임은 첫 화면 제목 타이핑(글자당 55ms), 구역 등장(24px 아래에서 0.62초), 핵심 수치 숫자 증가(1.2초) 3가지입니다. 넉터 마케팅 사이트와 에게의 움직임 기준을 따르며, 동작 줄이기 설정, JS 미동작, 인쇄에서는 효과 없이 바로 표시됩니다. 타이핑 커서는 절대 위치로 배치해 줄바꿈에 영향을 주지 않습니다. 인라인 블록으로 바꾸면 커서 위치마다 제목 줄 수가 바뀌어 레이아웃 이동(CLS)이 발생합니다.

## 2. 이력서 PDF 생성: Chrome 인쇄

**2-1. `_resume/resume.html`을 고친 뒤 아래 명령으로 PDF를 다시 생성하십시오.**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --no-pdf-header-footer --virtual-time-budget=15000 \
  --print-to-pdf=assets/kim-taehun-resume.pdf "file://$PWD/_resume/resume.html"
```

서비스 소개 PDF는 `python3 _resume/build_portfolio.py`로 생성하십시오.
스크립트는 1쪽 목차 표의 쪽 번호 자리표시(`@P1`~`@P3`)를 실제 쪽으로 채우려고 Chrome 인쇄를 2회 실행합니다.
결과물은 2개입니다.

| 파일 | 지원 기업 줄 | 공개 여부 |
|---|---|---|
| `assets/kim-taehun-portfolio.pdf` | 없음 | 웹에서 내려받기 |
| `_resume/out/kim-taehun-portfolio-submit.pdf` | `_resume/submit.txt` 한 줄을 1쪽 이름 아래에 표시 | 커밋 제외(`.gitignore`), 제출용 |

`_resume/submit.txt`가 없으면 제출본은 만들지 않습니다.

생성 후 `pdffonts`로 IBM Plex Sans KR 포함 여부를 확인하십시오.

## 3. 시연 영상 원본: 프로젝트별 출처

**3-1. 영상은 H.264로 인코딩했습니다. `+faststart` 옵션으로 재생 시작 지연을 단축했습니다.**

| 파일 | 원본 | 처리 |
|---|---|---|
| `nuktu-demo.mp4` | 넉터 앱 화면 녹화 `rec-*.mp4` 10개, 배경음악 `Gently Buoyant2.m4a` | 1920×1080 가로형(BBB 영상과 같은 비율). 세로 원본 720×1600(위쪽 160px 자막 띠, 아래 720×1440 앱 화면)을 432×960으로 축소해 배경 #F2F6F9 가운데에 둥근 모서리로 배치, 30fps, CRF 23, AAC 160kbps. 클럽 운영 녹화의 정지 구간 10.6초 제외(109초) |
| `ege-demo.mp4` | `에게_시연영상_4분_2026-11-21_GentlyBuoyant.mp4`(배경음악 교체본) | 재인코딩 없이 `+faststart`(239초) |
| `bbb-demo.mp4` | 사용자 앱 화면 녹화 2개, 화면 캡처 19장, 홍보 이미지 4장, CoShow 시연 영상 99~136초(관리자 웹, 운전자 앱), 배경음악 `Gently Buoyant2.m4a` | 1920×1080, 30fps, CRF 18, AAC 192kbps, 구간별 기능 설명 자막(240초) |

## 4. 방문 분석: Cloudflare Web Analytics

**4-1. `index.html` 끝의 Cloudflare beacon 스크립트로 방문을 집계합니다.**

2026-11-24에 도입했습니다. 쿠키와 `localStorage`를 쓰지 않으므로 동의 배너는 두지 않습니다.
스크립트의 토큰은 페이지에 공개되는 값이며 비밀 정보가 아닙니다.

| 항목 | 값 |
|---|---|
| 대시보드 | Cloudflare 계정 > Analytics & Logs > Web Analytics > `taehun2123.github.io` |
| site_tag | `174556ae4205462a85ff8ecfc7540d13` |
| 집계 항목 | 페이지 조회 수, 방문 수, Referer host(유입 경로), 국가, 기기, 브라우저, Core Web Vitals |
| 집계 제외 | PDF 다운로드(스크립트가 HTML 페이지에서만 실행됨), `/blog/`(별도 저장소) |

**4-2. 유입 경로는 Referer host로 구분하십시오.**

검색 유입은 `google.com`, `naver.com` 등으로 표시됩니다.
PDF 이력서, 메일, 메신저 앱에서 연 링크는 Referer가 전달되지 않는 경우가 많습니다. 이 경우 직접 유입(Referer 없음)으로 집계됩니다.
대시보드의 Exclude Bots를 `Yes`로 두고 확인하십시오.

## 5. 다음 작업

| 작업 | 기한 | 담당 |
|---|---|---|
| 넉터 운영 지표(회원 500+, 2026-11-22) 갱신 | 미정 | 김태훈 |
| 수상, 학력 변경 시 `index.html`과 `_resume/resume.html` 동시 수정 | 미정 | 김태훈 |
