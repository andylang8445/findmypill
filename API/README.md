# API 서버 여는법:

**(만약 MariaDB 셋업을 아직 하지 않았다면 /DB/Setup.md 를 읽고 데이터베이스 셋업을 선행하는걸 추천한다, 안그러면 API 서버 설정 과정에서 에러가 일어날수도 있음.)**

### 윈도우 사용시
1. 파이썬이 설치 안되있을 경우 https://www.python.org/downloads/ 에 접속해서 파이썬 3.0 이상 버전을 다운받아 설치한다. (꼭 Add to Path 는 체크 해주도록 한다.)
2. 윈도우 키를 눌러 `cmd` 를 치면 나오는 커맨드 프롬프트를 실행후 `python -V` 를 쳤을때 정상적으로 `Python <버전>` 이 뜨는지 확인한다.
3. 현재 이 API 폴더 경로를 찾아서 `cd <경로>` 명령어로 들어온다.
4. 해당 위치에서 `python -m venv api` 를 쳐서 가상환경울 구축해준다.
5. 곧바로 `api\Scripts\activate.bat` 를 쳐서 가상환경을 활성화 시켜준다.
6. 그리고 `pip install -r requirements.txt` 를 쳐서 실행에 필요한 모듈을 전부 다운받아 준다.
7. 이 후 서버를 열어놓으려면 가상환경이 활성화 된 상태에서 `python app.py` 를 치면 된다.
8. 서버를 닫으려면 `Ctrl + c` 를 입력하면 된다.
9. 이후 가상환경을 비활성화 시키려면 `deactivate` 을 입력하면 된다.

### 맥 사용시
1. 파이썬이 설치 안되있을 경우 https://www.python.org/downloads/ 에 접속해서 파이썬 3.0 이상 버전을 다운받아 설치한다.
2. `python<버전> -V` 를 통해서 정상적으로 `Python <버전>` 이 뜨는지 확인한다 (예. 만약 파이썬 3.11 버전을 다운 받았을 경우, `python3.11 -V` 라고 쳐야 한다.)
3. 현재 이 API 폴더 경로를 찾아서 `cd <경로>` 로 들어온다.
4. 해당 위치에서 `python<버전> -m venv api` 를 쳐서 가상환경을 구축해준다.
5. 곧바로 `source api/bin/activate` 를 쳐서 가상환경을 활성화 시켜준다.
6. 그리고 `pip install -r requirements.txt` 를 쳐서 실행에 필요한 모듈들을 전부 다운받아 준다. (MariaDB 셋업이 안되있다면 설치 실패할수도 있다. MariaDB 를 먼저 셋업한후 다시 시도해보자.)
7. 이 후 서버를 열어놓으려면 가상환경이 활성화된 상태에서 `python<버전> app.py` 를 치면 된다.
8. 서버를 닫으려면 `Ctrl + c` 를 입력하면 된다.
9. 이후 가상환경을 비활성화 시키려면 `deactivate` 을 입력하면 된다.

#### 편의를 위한 복붙용 명령어들 (윈도우):
`api\Scripts\activate.bat` : 가상환경 활성화\
`python app.py` : 서버 실행\
`deactivate` : 가상환경 비활성화

#### 편의를 위한 복붙용 명령어들 (맥):
`source api/bin/activate` : 가상환경 활성화\
`python3.11 app.py` : 서버 실행 (파이썬 3.11 기준)\
`deactivate` : 가상환경 비활성화