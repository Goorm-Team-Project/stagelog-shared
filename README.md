# Shared

`shared`는 서비스 간 공용 계약과 최소한의 런타임 헬퍼를 담는 레포입니다.

## 목적
- 서비스 간 이벤트 계약 통일
- 내부 API 요청/응답 계약 재사용
- 여러 서비스에서 공통으로 쓰는 얇은 헬퍼 제공
- 서비스별 코드베이스에 중복된 공통 로직 축소

## 현재 포함된 내용
- 이벤트 계약
  - [`shared/contracts/notification_events.py`](/home/woosupar/stagelog/shared/contracts/notification_events.py)
- 내부 API 계약
  - [`shared/contracts/internal_api_contracts.py`](/home/woosupar/stagelog/shared/contracts/internal_api_contracts.py)
- 공용 Django 유틸
  - [`shared/stagelog_shared/django_utils.py`](/home/woosupar/stagelog/shared/stagelog_shared/django_utils.py)
- 공용 내부 API 호출 헬퍼
  - [`shared/stagelog_shared/internal_api.py`](/home/woosupar/stagelog/shared/stagelog_shared/internal_api.py)
- 공용 미들웨어
  - [`shared/stagelog_shared/middleware.py`](/home/woosupar/stagelog/shared/stagelog_shared/middleware.py)

## 포함하면 안 되는 내용
- Django ORM 모델
- 특정 서비스가 소유하는 비즈니스 로직
- 서비스 전용 DB 접근 코드
- 서비스별 settings, deployment, infra 코드

## 사용 방식
- 각 서비스 이미지는 빌드 시점에 `stagelog-shared`를 함께 checkout 해서 설치합니다.
- 서비스 workflow는 기본적으로 자기 브랜치 이름과 같은 `shared` 브랜치를 참조합니다.
  - 예: `develop` 브랜치 빌드 시 `shared/develop`
  - 예: `main` 브랜치 빌드 시 `shared/main`

## 변경 원칙
- 계약 변경은 가능하면 하위 호환을 유지합니다.
- breaking change가 필요하면 단계적 배포가 가능하도록 버전 전환 경로를 함께 준비합니다.
- 공용 코드라고 해도 서비스 소유권 경계를 흐리는 로직은 넣지 않습니다.

## Notes
- `shared`는 서비스 간 결합도를 줄이기 위한 레포이지, 공용 잡동사니 저장소가 아닙니다.
- 새 코드를 추가할 때는 “두 개 이상 서비스가 실제로 재사용하는가”를 먼저 확인하는 것이 좋습니다.
