@ECHO OFF
pip install --upgrade pip
pip list | findstr /I /B /C:"Pillow"
if NOT %errorlevel% == 0 (
  pip install pillow
)
python memewarrior.py "%~1"
PAUSE
