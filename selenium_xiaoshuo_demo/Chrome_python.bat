@echo off
color 0a
title python
echo.
echo ֱ���������Chrome�������python�ļ�
echo ���к���ڵ�ǰ�ļ�������log.txt�ļ���¼�����Ϣ
echo.
echo ����python�ļ�,�س�ִ��:
set /p file=$:
@echo ----------��ʼ---------- >>log.txt
@echo %DATE:~0,4%-%DATE:~5,2%-%DATE:~8,2% %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2% >>log.txt
python %file% >>log.txt
@echo ----------����---------- >>log.txt
@echo. >>log.txt
@echo ���н���.��������˳�
pause & exit