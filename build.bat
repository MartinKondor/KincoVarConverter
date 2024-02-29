@echo off
pyinstaller gui.spec
xcopy /s .\dist_src\* .\dist\script\
