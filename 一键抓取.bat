@echo off
echo ========================================
echo       C++学习网 - 自动抓取脚本
echo ========================================
echo.

:: 检查是否安装了 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Python 环境！
    echo 本脚本需要 Python 才能运行。
    echo 请先前往 https://www.python.org/ 下载并安装 Python。
    echo (注意：安装时请务必勾选 "Add Python to PATH" 选项)
    echo.
    pause
    exit /b
)

echo [1/2] 正在检查并自动安装所需的依赖环境...
pip install requests beautifulsoup4 markdownify -q

echo.
echo [2/2] 正在启动爬虫脚本，请耐心等待抓取...
echo.
python scrape.py
echo.
echo ========================================
echo 抓取完毕！所有 Markdown 均已保存至当前目录。
echo ========================================
pause
