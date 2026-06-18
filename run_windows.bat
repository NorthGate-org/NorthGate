@ECHO OFF
SET "ENVIRONMENT=env"
SET "LOGGING_LEVEL=DEBUG"

IF NOT EXIST "%ENVIRONMENT%\" (
    ECHO [INFO] The environment directory is missing. Creating...
    python -m venv "%ENVIRONMENT%"
    %ENVIRONMENT%\Scripts\activate
    pip install -r requirements.txt & python -m northgate.main --logging-level %LOGGING_LEVEL%
) ELSE (
    ECHO [INFO] Activating the existing environment...
    %ENVIRONMENT%\Scripts\activate
    python -m northgate.main --logging-level %LOGGING_LEVEL%
)