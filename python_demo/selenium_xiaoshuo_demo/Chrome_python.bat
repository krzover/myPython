@echo off
color 0a
title python
echo.
echo 直接拖入调用Chrome浏览器的python文件
echo 运行后会在当前文件夹生成log.txt文件记录输出信息
echo.
echo 拖入python文件,回车执行:
set /p file=$:
@echo ----------开始---------- >>log.txt
@echo %DATE:~0,4%-%DATE:~5,2%-%DATE:~8,2% %TIME:~0,2%:%TIME:~3,2%:%TIME:~6,2% >>log.txt
python %file% >>log.txt
@echo ----------结束---------- >>log.txt
@echo. >>log.txt
@echo 运行结束.按任意键退出
pause & exit