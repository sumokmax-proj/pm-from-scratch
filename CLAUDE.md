# PM From Scratch — 프로젝트 컨텍스트

Claude와 대화를 이어갈 때 이 파일을 참고해 배경을 빠르게 파악한다.

---

## 프로젝트 개요

- **사이트명:** PM From Scratch
- **주제:** PMP를 갓 취득한 주니어 PM의 솔직한 성장 노트
- **URL:** https://sumokmax-proj.github.io/pm-from-scratch/
- **GitHub 저장소:** https://github.com/sumokmax-proj/pm-from-scratch
- **기술 스택:** Jekyll (정적 사이트), GitHub Pages 자동 배포, SCSS
- **언어:** 한국어(KO) / 영어(EN) 이중 언어 지원

---

## 디렉토리 구조 (핵심)

```
pm-from-scratch/
├── _includes/
│   ├── header.html       # 내비게이션 바 (햄버거 메뉴 포함)
│   └── footer.html
├── _layouts/             # Jekyll 레이아웃 템플릿
├── _posts/               # 블로그 포스트
├── _sass/
│   └── main.scss         # 전체 스타일시트
├── _config.yml           # Jekyll 설정
├── ko/                   # 한국어 페이지 (홈, 소개, PDU 트래커)
├── en/                   # 영어 페이지
└── assets/css/           # 컴파일된 CSS
```

---

## 지금까지 한 작업

### 반응형 모바일 메뉴 구현 (2026-04-08)

**문제:** 모바일(768px 이하)에서 `.site-nav { display: none }` 처리만 되어 있고
햄버거 메뉴가 없어 내비게이션 링크에 접근 불가능했음.

**해결 방법:**

1. **`_includes/header.html`** 수정
   - `site-nav`와 `lang-switcher`를 `.nav-wrapper` div로 묶음
   - 햄버거 버튼(`.nav-toggle`) 추가 — `<span>` 3개로 구성
   - 버튼 클릭 시 `is-open` 클래스 토글하는 인라인 JS 추가
   - 헤더 밖 클릭 시 메뉴 자동 닫힘
   - `aria-label`, `aria-expanded` 접근성 속성 포함

2. **`_sass/main.scss`** 수정
   - `.nav-wrapper` 추가 (데스크톱: flex row, 모바일: 숨김)
   - `.nav-toggle` 햄버거 스타일 (데스크톱에서 `display: none`)
   - 클릭 시 ☰ → X 아이콘 CSS 애니메이션 (transform + opacity)
   - 모바일에서 `.nav-wrapper.is-open` → 헤더 바로 아래 드롭다운 펼쳐짐
   - `position: absolute; top: var(--header-h)` 로 sticky 헤더 아래 배치

**커밋:** `c338784` — main 브랜치에 push 완료

---

## 디자인 시스템

```css
--c-primary:    #1e4d8c   /* 메인 블루 */
--c-primary-lt: #2d6cbf   /* 밝은 블루 */
--c-primary-dk: #153a6b   /* 어두운 블루 */
--c-bg:         #ffffff
--c-text:       #1a1a2e
--max-w:        1080px     /* 최대 콘텐츠 너비 */
--header-h:     64px       /* 모바일: 56px */
```

- **폰트:** Noto Sans KR, Inter
- **반응형 브레이크포인트:** 768px

---

## 앞으로 논의할 수 있는 주제

- 새 포스트 작성 및 카테고리 구성
- PDU 트래커 기능 개선
- SEO 최적화 (메타태그, sitemap 등)
- 댓글 기능 추가 (Utterances 등)
- 다크모드 지원
- 포스트 검색 기능
- 영어 콘텐츠 번역/추가
