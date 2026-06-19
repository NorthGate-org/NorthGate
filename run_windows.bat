@ECHO OFF
IF "%ENVIRONMENT%"=="" (
    SET "ENVIRONMENT=env"
) ELSE (
    ECHO ENVIRONMENT IS defined as %ENVIRONMENT%
)

IF "%LOGGING_LEVEL%"=="" (
    SET "LOGGING_LEVEL=INFO"
) ELSE (
    ECHO LOGGING_LEVEL IS defined as %LOGGING_LEVEL%
)

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