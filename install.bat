@echo off
cls

set "arch="

REM PowerShell kullanarak sistem mimarisini belirle
for /f %%a in ('powershell -command "(Get-WmiObject -Class Win32_Processor | Select-Object -ExpandProperty AddressWidth)"') do set arch=%%a

REM Eğer mimari 64 bit ise
if "%arch%"=="64" (
    echo sisteminiz x64 mimarisinde.
    curl -o python.exe https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe
    cls
    start python.exe
    del install.bat
) else (
    echo Sistem x32 mimarisinde.
    curl -o python.exe https://www.python.org/ftp/python/3.12.4/python-3.12.4.exe
    cls
    start python.exe
    del install.bat
)

pause
