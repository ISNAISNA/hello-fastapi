## 😀 fast api 시작하기

### 패키지 셋팅
- 가상환경 만들고 꼭 활성화 후에 설치하기
```py
python -m venv <가상환경이름>
<가상환경이름>/Scripts/activate.bat # 가상환경 활성화
pip install fastapi==0.74.1 # fastapi 설치
pip install "uvicorn[standard]" # uvicorn 설치
```

#### 정상 가상환경 접속 시 가상환경 이름 확인
![image](https://github.com/user-attachments/assets/a62b42c1-c705-4c04-b62d-17b74cb6a91b)

### 코드
```py
from fastapi import FastAPI # fastapi 클래스를 불러옵니다. 

app = FastAPI() # FastAPI 클래스를 바탕으로 app이란 인스턴스를 만듭니다. 


@app.get("/") # GET 메소드로 가장 루트 url로 접속할 경우
async def root(): # root() 함수를 실행하고
    return {"message": "Hello World"} # Hello World란 메시지 반환합니다.
```

- python -m uvicorn <파일이름>:app --reload
- http://127.0.0.1:8000

---

### Swagger
- http://127.0.0.1:8000/docs
- 엔드포인트 숨기기
    - @app.get("...", `include_in_schema=False`)
- Swagger URL 변경
    - app = FastAPI(docs_url='/api/docs')

---
### 패키지 매니저(정리 예정)
### 📌 1. Python 패키지 매니저 종류
Python 패키지 매니저는 크게 기본 패키지 매니저, 가상 환경 관리자, 의존성 관리 도구로 나눌 수 있다.

### ✅ 1.1 기본 패키지 매니저
### 1. pip (Python Package Installer)
#### 🔹특징
- Python 표준 패키지 매니저
- PyPI(Python Package Index)에서 패키지를 설치
- requirements.txt 파일을 이용한 의존성 관리 가능
- 가상 환경과 함께 사용하는 것이 일반적 (venv 또는 virtualenv와 조합)

#### 🔹사용법
```bash
pip install requests  # 패키지 설치
pip uninstall requests  # 패키지 삭제
pip list  # 설치된 패키지 목록 확인
pip freeze > requirements.txt  # 현재 환경 패키지를 requirements.txt로 저장
pip install -r requirements.txt  # requirements.txt 기반 패키지 설치
```

### 2. pipx
#### 🔹특징
- 독립된 가상 환경에서 Python 패키지를 실행
- CLI(Application) 도구를 설치할 때 유용 (예: black, httpie)
- pip과 달리 전역적으로 설치해도 가상 환경을 사용하기 때문에 환경이 깨지지 않음

#### 🔹사용법
```bash
pipx install black  # black (Python 코드 포매터) 설치
pipx run httpie  # httpie 실행 (설치 없이 한 번 실행)
pipx uninstall black  # black 제거
```

#### 📌 pip과의 차이점
- pip은 현재 가상 환경이나 시스템 환경에 직접 설치
- pipx는 별도의 가상 환경을 자동으로 생성하여 패키지를 실행

#### 📌 언제 사용할까?
- black, mypy, flake8, httpie 같은 CLI 도구를 설치할 때 적합
- 일반적인 라이브러리(requests, numpy 등)는 pip을 사용

### ✅ 1.2 가상 환경 관리 도구
Python에서는 가상 환경을 사용하여 프로젝트별로 독립된 패키지 환경을 만들 수 있어.

### 3. venv (Python 내장 가상 환경)
#### 🔹 특징
- Python 3.3+에 기본 포함된 가상 환경 도구
- 가볍고 빠름
- Python 표준 라이브러리로 제공되므로 추가 설치가 필요 없음

#### 🔹 사용법
```bash
python -m venv myenv  # 가상 환경 생성
source myenv/bin/activate  # (Mac/Linux) 가상 환경 활성화
myenv\Scripts\activate  # (Windows) 가상 환경 활성화
deactivate  # 가상 환경 비활성화
```

#### 📌 언제 사용할까?
- 단순한 프로젝트에서 가상 환경만 필요할 때
- 별도의 복잡한 의존성 관리 도구(pipenv, poetry)가 필요하지 않을 때

### 4. virtualenv
#### 🔹 특징
- venv보다 더 다양한 기능을 제공
- Python 2 지원 (Python 2.7에서도 사용 가능)
- 여러 개의 Python 버전을 지원

#### 🔹 사용법
```bash
pip install virtualenv  # virtualenv 설치
virtualenv myenv  # 가상 환경 생성
source myenv/bin/activate  # 가상 환경 활성화 (Mac/Linux)
```

#### 📌 언제 사용할까?
- Python 2를 지원해야 할 때
- 다양한 Python 버전을 다룰 필요가 있을 때

### ✅ 1.3 의존성 및 패키지 관리 도구
Python 프로젝트에서 의존성 관리를 체계적으로 하고 싶다면, pipenv 또는 poetry 같은 도구를 고려해야 해.

### 5. pipenv
#### 🔹 특징
- Pipfile을 사용하여 의존성을 관리
- 가상 환경을 자동으로 생성
- requirements.txt를 사용하지 않고 보다 깔끔하게 패키지 관리

#### 🔹 사용법
```bash
pip install pipenv  # pipenv 설치
pipenv install requests  # 패키지 설치 (자동으로 가상 환경 생성)
pipenv shell  # 가상 환경 활성화
pipenv lock  # 의존성 버전 고정
pipenv install --dev pytest  # 개발 의존성 추가
```

#### 📌 언제 사용할까?
- requirements.txt보다 더 편리한 의존성 관리를 원할 때
- 프로젝트마다 가상 환경을 자동으로 생성하고 싶을 때

### 6. poetry
#### 🔹 특징
- pyproject.toml을 사용하여 의존성 및 패키지 빌드까지 관리
- 가상 환경을 자동으로 생성
- pipenv보다 패키징과 배포가 용이함
- pip, setuptools, wheel을 대체할 수 있음

#### 🔹 사용법
```bash
pip install poetry  # poetry 설치
poetry init  # 프로젝트 초기화 (pyproject.toml 생성)
poetry add requests  # 패키지 설치
poetry install  # 의존성 설치
poetry shell  # 가상 환경 활성화
poetry build  # 패키지 빌드
poetry publish  # 패키지 배포
```

#### 📌 언제 사용할까?
- 패키징까지 고려한 배포 가능한 프로젝트를 만들 때
- 복잡한 의존성을 쉽게 관리하고 싶을 때

### 7. conda
#### 🔹 특징
- Python뿐만 아니라 비-Python 라이브러리도 관리 가능
- 데이터 과학, 머신러닝 분야에서 주로 사용
- pip과 달리 파이썬 버전도 함께 관리 가능

#### 🔹 사용법
```bash
conda create -n myenv python=3.9  # Python 3.9 환경 생성
conda activate myenv  # 가상 환경 활성화
conda install numpy pandas matplotlib  # 패키지 설치
```

#### 📌 언제 사용할까?
- 데이터 과학, 머신러닝 프로젝트 (numpy, pandas, scikit-learn 등)
- 다양한 언어(C, C++, Fortran 등)로 작성된 라이브러리와 함께 사용해야 할 때

###  📌 2. 패키지 매니저 선택 가이드
![image](https://github.com/user-attachments/assets/e7ee9b01-de94-4b30-aadb-cd77a4c623b6)

### 🚀 최종 정리
- 1️⃣ 단순한 프로젝트 → venv + pip
- 2️⃣ 가상 환경 자동 관리 & 의존성 관리 → pipenv
- 3️⃣ 패키징과 배포까지 고려 → poetry
- 4️⃣ 데이터 과학 & 머신러닝 → conda
- 5️⃣ CLI 도구 설치 → pipx
