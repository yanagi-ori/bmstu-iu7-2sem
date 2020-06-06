@echo off
cls
for %%i in (1 2 3 4 5) do call test.bat %%i
for %%i in (5) do call fcmp.bat %%i