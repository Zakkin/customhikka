@echo off
echo Restarting...
taskkill /im python.exe /f
start python bot.py
