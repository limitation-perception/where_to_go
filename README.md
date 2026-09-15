## Як запустити 

### 1. Клонувати репозиторій

```bash
git clone https://github.com/limitation-perception/where_to_go.git
cd where_to_go
```

### 2. Створити й активувати віртуальне оточення

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Встановити залежності

```bash
pip install -r requirements.txt
```

### 4. Застосувати міграції

```bash
python manage.py migrate
```

### 5. Запустити сервер

```bash
python manage.py runserver
```

Відкрийте в браузері: <http://127.0.0.1:8000/>
Ця інструкція зроблена не без допомоги нейронки!