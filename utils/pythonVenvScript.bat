ECHO OFF
:: This batch file creates a new Python 2.7 virtualenv for csweb on Windows.
:: It assumes:
::     Python 2.7 is installed in the default location
::     utils/pythonVenvRequirements.txt has a list of required packages
::         (except numpy and scipi, which must be installed from binary on Windows)
::     The appropriate numpy/scipy binaries are stored in c:\pythonvenv.
::         (downloaded from http://www.lfd.uci.edu/~gohlke/pythonlibs/)
:: Run it from the csweb/utils directory.
:: 
:: kvlinden, Summer, 2015

SET VENV_PATH=C:\PythonVenv
SET VENV_DIR=csweb
SET VENV=%VENV_PATH%\%VENV_DIR%

if exist %VENV% (
   ECHO Removing existing venv...
   RMDIR /S /Q %VENV%
   )

ECHO Building new venv...
C:\Python27\Scripts\virtualenv %VENV%

ECHO Loading packages...
%VENV%\Scripts\pip install %VENV_PATH%\numpy-1.10.0b1+mkl-cp27-none-win_amd64.whl
%VENV%\Scripts\pip install %VENV_PATH%\scipy-0.16.0-cp27-none-win_amd64.whl
%VENV%\Scripts\pip install -r pythonVenvRequirements.txt

ECHO Finished building new venv...
