# 排错解析：`collect2.exe: error: ld returned 1 exit status`

放心，这**绝对不是** CLion 软件坏了，而是所有学 C/C++ 的人都会遇到的最经典报错之一：**链接器错误 (Linker Error)**。

## 1. 为什么会报这个错？
仔细看你截图里那一长串红色的报错，里面有一个非常核心的词：`ld`（有时候报错里会写完整：`undefined reference to main`）。

`ld` 是 C++ 编译系统中的“链接器”。当你点击 CLion 的运行按钮时，系统在尝试把你写的代码打包成一个可以运行的程序（.exe）。
但是，任何一个能运行的 C++ 程序，都必须有一个“大门”（也就是程序的唯一入口）。这个大门的名字，C++ 强行规定只能叫 `main`。

如果链接器在你的代码里翻了个底朝天，**没有找到 `main` 函数**，它就会直接罢工，并抛出 `ld returned 1 exit status`（链接器异常退出）的报错。

## 2. 破案了：看看你的代码
我之前帮你看过你的 `checkSecre.cpp`，你的代码是这样写的：
```cpp
class getNum {
    public:
     getNum() {
        // ...你写的验证密码的完美逻辑...
     }
};
```
你写了一个类，写了构造函数，逻辑非常棒。**但是，你忘记写 `main` 函数了！**

没有 `main` 函数，编译器就不知道你的程序该从哪里开始执行。

## 3. 怎样修复？
修复非常简单，只需要在你的文件的最下面，补上一个 `main` 函数，然后在里面调用你写的类，触发它即可。

请把你的 `checkSecre.cpp` 改成这样：

```cpp
#include "checkSecre.h"
#include <iostream>
#include <string>

using namespace std;

class getNum {
public:
    getNum() {
        string num;
        while (true) {
            cout << "Enter an integer: ";
            cin >> num;
            if (num.length() < 8) {
                cout << "Length must be greater than 8" << endl;
            } else {
                cout << "mima is ok" << endl;
                break;
            }
        }
    }
};

// 【修复核心】：必须要有 main 函数作为程序入口！
int main() {
    // 在这里创建你写的类的对象。
    // 一旦创建对象，就会自动触发上面那个 getNum() 构造函数，你的密码验证循环就开始跑了！
    getNum myPasswordChecker; 
    
    return 0;
}
```

把这个 `int main()` 补到你的文件最后面，再去 CLion 里点绿色的三角形运行，报错瞬间解决！
