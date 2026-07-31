#!/bin/bash
cd "$(dirname "$0")"

echo "========================================"
echo "      C++学习网 - 自动抓取脚本"
echo "========================================"
echo ""

if ! command -v python3 &> /dev/null; then
    echo "[错误] 未检测到 Python3 环境！"
    echo "本脚本需要 Python3 才能运行。"
    echo "请前往 https://www.python.org/ 下载并安装 Python。"
    echo ""
    read -p "按回车键退出..."
    exit 1
fi

echo "[1/2] 正在检查并自动安装所需的依赖环境..."
pip3 install requests beautifulsoup4 markdownify -q

echo ""
echo "[2/2] 正在启动爬虫脚本，请耐心等待抓取..."
echo ""
python3 scrape.py
echo ""
echo "========================================"
echo "抓取完毕！所有 Markdown 均已保存至当前目录。"
echo "========================================"
read -p "按回车键退出..."
