# PM From Scratch

> Project Management, et cetera — Jekyll 기반 한/영 이중언어 블로그

## 배경 / 의도

PM(Project Management) 기초를 중심으로 하되, 그 밖의 주제도 가끔 다루는 블로그.
모든 글은 직접 씁니다.

## 현재 상태

🔵 개발 중 — GitHub Pages로 배포 예정 (`https://sumokmax-proj.github.io/pm-from-scratch`)

## 사용 기술

- Jekyll (kramdown, rouge)
- jekyll-sitemap, jekyll-feed, jekyll-seo-tag
- 한/영 이중언어 (`_posts/ko/`, `_posts/en/`)

## 실행 방법

```bash
bundle install
bundle exec jekyll serve
```

## 글 작성 규칙

- 한국어 글: `_posts/ko/`
- 영어 글: `_posts/en/`
- 레이아웃/permalink는 `_config.yml`의 `defaults`에서 언어별로 자동 적용됨

## TODO

- [ ] 첫 포스트 publish
- [ ] GitHub Pages 배포 설정 확인
