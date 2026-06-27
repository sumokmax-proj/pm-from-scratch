# PM From Scratch

> 주니어 PM의 솔직한 성장 노트 — Jekyll 기반 한/영 이중언어 블로그

## 배경 / 의도

PM 0년차부터 3년차까지의 경험(시행착오, 배운 것)을 기록하고 공유하기 위한 블로그.

> PM 0년차 - Project Manager가 무슨 일을 하는지도 몰랐습니다.
> PM 1년차 - 길을 잘못들었다고 생각했습니다.
> PM 2년차 - PMP 자격증에 도전했습니다.
> PM 3년차 - 배우면서 기록하고 나누면서 성장하고자 합니다.

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
