@echo off
python -m PyInstaller -F ./vspBench.py

pause
start explorer /select,"%CD%\dist\vspBench.exe"