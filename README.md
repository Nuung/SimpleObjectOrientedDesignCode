# SimpleObjectOrientedDesignCode

이 프로젝트는 "객체지향 설계의 원칙" 서적의 Java 예제 코드를 Python으로 포팅한 것입니다. 원본 Java 프로젝트의 구조와 디자인 패턴을 최대한 유지하면서 Pythonic한 코드로 변환하는 데 중점을 두었습니다.

## 프로젝트 구조

이 저장소는 크게 두 부분으로 나뉩니다:

1.  **`PeopleGrow/`**: Spring Boot 기반의 Java 프로젝트로, Python 포팅의 원본 소스코드 중 하나입니다.
2.  **`sources/`**: 책의 각 챕터별 Java 예제 코드를 포함하는 디렉토리로, Python 포팅의 주요 원본 소스코드입니다.
3.  **`python/`**: 원본 Java 코드가 포팅된 Python 프로젝트입니다. 원본 Java 프로젝트의 챕터 및 버전 구조를 따릅니다.

    *   **`python/chX/vY/`**: 각 챕터(chX)와 버전(vY)에 해당하는 Python 코드가 위치합니다.
    *   **`python/peoplegrow/`**: `PeopleGrow` Spring Boot 프로젝트의 핵심 로직이 Python으로 포팅된 코드입니다.

## 주요 변경 사항 및 포팅 원칙

*   **언어 변환**: 모든 Java 코드는 Python으로 변환되었습니다.
*   **객체 지향 구조 유지**: 클래스, 인터페이스(Python의 `abc` 모듈 사용), Enum 등 Java의 객체 지향 설계 원칙을 Python에서도 동일하게 유지했습니다.
*   **데이터 타입 매핑**:
    *   Java의 `String`, `int`, `boolean` 등은 Python의 `str`, `int`, `bool` 등으로 변환되었습니다.
    *   `java.time.LocalDate` 및 `java.time.LocalDateTime`는 Python의 `datetime.date` 및 `datetime.datetime`으로 변환되었습니다.
    *   Java의 `List`, `Set`, `Optional`은 Python의 `typing.List`, `typing.Set`, `typing.Optional`로 변환되었습니다.
*   **예외 처리**: Java의 `try-catch` 블록은 Python의 `try-except` 블록으로 변환되었으며, 사용자 정의 예외 클래스도 Python 스타일로 정의되었습니다.
*   **컬렉션 및 스트림 API**: Java의 컬렉션(`ArrayList`, `HashSet`) 및 스트림 API(`stream().anyMatch()`, `stream().filter().count()`)는 Python의 리스트, 세트, `any()`, `sum()` 및 리스트 컴프리헨션과 같은 Pythonic한 방식으로 변환되었습니다.
*   **Spring Framework 관련 코드**: `@Entity`, `@Id`, `@Component`, `@Service`와 같은 Spring Framework 관련 어노테이션은 Python에 직접적인 동등물이 없으므로, 해당 로직의 의도를 Python 클래스 및 함수로 구현하는 데 중점을 두었습니다. (예: 의존성 주입은 `__init__` 메서드를 통한 명시적 전달로 처리)
*   **`var` 키워드**: Java의 `var` 키워드는 Python의 동적 타이핑 또는 명시적인 타입 힌트로 대체되었습니다.
*   **불변성**: Java의 `record` 타입이나 `Collections.unmodifiableCollection`과 같이 불변성을 강조하는 부분은 Python에서 `dataclasses` 또는 `tuple`, `frozenset` 등을 사용하여 유사한 불변성을 유지하도록 노력했습니다.

