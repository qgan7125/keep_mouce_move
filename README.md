# Automatic Move Mouce
A simple python application to randomly move your mouce.

## Generate exe file
```
pip install -r requirements.txt
pyinstaller --onefile move.py
```
The exe file is `dist/move`. Because of the the limitation of pyinstaller, the generated exe file is not cross-compiler. In order to generate windows verions, please run the above command under windows environment. or Mac OS version in mac environment.