@echo on
if exist __pycache__ (rd /S /Q __pycache__)
if exist build (rd /S /Q build)
if exist dist (rd /S /Q dist)
del /Q /F *.spec
pause