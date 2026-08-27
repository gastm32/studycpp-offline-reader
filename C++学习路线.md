# C++ 免费学习资源（全部公开合法，适合 Ubuntu‑Linux 环境）

> 不提供盗版压缩包、网盘破解资源，全部是官网、GitHub 开源项目，可以网页浏览 /git clone 下载源码、文档到本地离线看。

## 📖 文档 & 教程网站

### 1）权威参考手册（写代码必查）

1. **cppreference 中文（标准库文档）** https://zh.cppreference.com/

> C++ 官方级参考，C++11~C++26，查 STL 容器、函数、语法，支持离线 HTML 打包下载。

1. **[learncpp.com](https://learncpp.com)（零基础英文教程，业界公认最好免费入门）** https://www.learncpp.com/

> 循序渐进，每章带练习题，适配现代 C++，可以复制示例代码直接在 Ubuntu g++ 编译运行GitHub Gis...。社区有非官方中文翻译版。

1. **吴咏炜《现代 C++ 教程》【开源中文，重点 C++11/14/17/20】** 在线阅读：https://changkun.de/modern‑cpp/ GitHub 仓库（可下载全部 markdown 源码到本地）：https://github.com/changkun/modern‑cpp‑tutorial
2. **C++ Core Guidelines（C++ 之父编写，进阶最佳实践）**https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines

> 教怎么写安全、规范现代 C++，网络编程、多线程非常有用CSDN博...。

1. Awesome‑C++（GitHub 资源总目录，6 万 + star） https://github.com/fffaraz/awesome‑cpp

> 聚合教程、库、开源项目、视频、书籍清单，适合进阶拓展GitHub Gis...。

## 💻在线编译网站（Ubuntu 临时调试，不用本地建文件）

1. Godbolt（看 C++ 编译生成汇编，理解底层）：https://godbolt.org/
2. OnlineGDB（在线运行 C/C++）：https://www.onlinegdb.com/

## 🎬视频资源（B 站免费）

1. 侯捷 STL 源码剖析（经典）
2. freeCodeCamp C++20 完整教程（英文，B 站搬运）
3. 《现代 C++ 实战》、陈硕 Linux C++ 网络编程系列（适合你做 socket、UNIX 域套接字）

## 🧪刷题练习网站（C++ 提交）

1. LeetCode：https://leetcode.cn/ 算法练习
2. HackerRank C++ 专题：https://www.hackerrank.com/domains/cppCSDN博...
3. DotCpp（中文 OJ）：https://www.dotcpp.com/oj/

## 📂GitHub 开源仓库（可以 git clone 下载整套资料到本地，相当于压缩包）

### ① 现代 C++ 教程（吴咏炜）

```
git clone https://github.com/changkun/modern-cpp-tutorial.git
```

克隆后本地打开 html/markdown 文档离线阅读。

### ② 小彭老师 C++ 大典（中文开源大部头）

```
git clone https://github.com/ccwanggl/cppguidebook.git
```

https://github.com/ccwanggl/cppguidebookGitHub

### ③ awesome‑modern‑cpp（专注 C++11 以后新特性）

```
git clone https://github.com/rigtorp/awesome-modern-cpp.git
```

### ④ Linux 下 C++ 完整学习案例项目（Ubuntu 环境）

```
git clone https://github.com/NDXDeveloper/formation-cpp-moderne-ubuntu.git
```

> 专门面向 Ubuntu g++，从环境安装、基础语法到网络编程、CMake，大量可编译示例代码GitHub。

## 🛠 Ubuntu 环境快速安装 C++ 编译工具

```
sudo apt update
sudo apt install build-essential g++ gdb cmake git
# build‑essential包含g++编译器、make工具
g++ --version
```

编译命令示例：

```
g++ main.cpp -o app -std=c++17 -pthread
./app
```

## 📚经典正版书籍清单（购买渠道：微信读书、京东读书）

1. 《C++ Primer》第 5 版（入门）
2. 《Effective C++》（进阶）
3. 《现代 C++ 教程：高速上手 C++11/14/17/20》吴咏炜（开源免费网页版）
4. 《C++ 程序设计语言》Bjarne Stroustrup（C++ 之父，权威）

## 📝学习路线建议（你有 C、Linux socket 基础）

1. learncpp 过一遍面向对象、类、引用、智能指针、STL 容器（vector string map）
2. 阅读吴咏炜现代 C++ 教程，掌握 auto、lambda、移动语义
3. 在 Ubuntu 写代码，把你之前 UNIX‑UDP 聊天程序改成 C++ 版本
4. 学习 CMake 构建工具，代替手写 g++ 编译命令
5. 看 C++ Core Guidelines，学习多线程、网络编程最佳实践