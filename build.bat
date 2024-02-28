@echo off
pyinstaller script.spec
xcopy /s .\dist_src\* .\dist\script\
