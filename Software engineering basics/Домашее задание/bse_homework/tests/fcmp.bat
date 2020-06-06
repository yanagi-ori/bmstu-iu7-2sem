@echo off
main.exe < in_%1.txt
fc out_hex.txt out_file_%1.txt
pause