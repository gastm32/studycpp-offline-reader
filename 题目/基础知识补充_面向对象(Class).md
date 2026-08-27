# 基础知识补充：面向对象编程 (Class 类) 核心指南

看到你在 `bankAccount.cpp` 里停下了脚步，完全能理解！从普通的“面条式”代码过渡到“面向对象（Class）”，是 C++ 学习中非常大的一个跨越。不要觉得没有自信，其实它的底层逻辑非常直观。

## 1. 什么是类 (Class)？
在前面的学习中，如果你想描述一个“账户”，你可能需要写好几个分散的变量：`string name; double money;`。这很散乱，且容易出错。
**类 (Class)** 就像是一个“模具”或“图纸”，它允许你把 **状态 (变量)** 和 **行为 (操作这些变量的函数)** 捆绑在一起，打包成一个全新的类型。

## 2. Public (公有) vs Private (私有) —— 为什么要“封装”？
这是面向对象最核心的灵魂：**保护数据，拒绝随意篡改**。
- `private`（私有）：写在这里的变量，外界（比如 `main` 函数里）绝对不允许直接访问或修改。这就像你银行卡里的“真实余额”，绝不能让任何外面的程序直接写 `balance = 9999999;`。
- `public`（公有）：写在这里的函数，是开放给外界使用的接口。外界只能通过这些合法的接口（比如存款、取款函数）来间接操作私有数据。

```cpp
class BankAccount {
private:
    // 核心数据藏起来，外界绝对碰不到
    double balance; 

public:
    // 开放合法的方法让外界操作
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount; // 内部自己改自己的私有数据是可以的
        }
    }
    
    // 只提供“看”的方法，不提供直接改的权限
    double getBalance() {
        return balance; 
    }
};
```

## 3. 构造函数 (Constructor) 与 初始化列表
模具 (Class) 设计好之后，我们需要在 `main` 函数里用它来真正产生一个具体的对象。在对象诞生的那一刻，我们需要给它一个初始状态（比如开户时要填名字和存点底油钱）。这就是**构造函数**的工作。

**构造函数的 3 个铁律：**
1. 名字必须和类名**一模一样**！
2. **没有任何返回值**（连 `void` 都不写）。
3. **初始化列表**：C++ 强烈推荐在参数后面加个冒号 `:` ，直接在这里给成员变量赋初值，而不是在大括号里用 `=` 赋值，这样运行效率最高。

```cpp
class BankAccount {
private:
    std::string accountName;
    double balance;

public:
    // 这就是构造函数，当有人开户时，必须提供名字和初始金额
    BankAccount(std::string name, double initialBalance) 
        : accountName(name), balance(initialBalance) // 这就是极其优雅的初始化列表！
    {
        // 因为初始化列表已经把活干完了，这里通常空着就行
    }
};
```

## 4. `const` 成员函数（只读函数）
如果你有一个函数，它的目的仅仅是“偷看一下”数据，发誓**绝对不会修改**类里面的任何私有变量（比如 `getBalance`），强烈建议在括号后面加上 `const`。
编译器会监督你，一旦你不小心在这个函数里改了变量，直接报错。这是一种极其良好的编程习惯。
```cpp
double getBalance() const {
    return balance;
}
```

---
## 🎯 回到你的任务
结合上面的知识，你再回头看你的 `bankAccount.cpp`：
1. 你已经很棒地写好了 `private` 里的 `account` 和 `balance`。
2. 接下来，你只需要在 `public` 下面，照猫画虎补上一个**构造函数**。
3. 最后再补上 `deposit` (存款) 和 `withdraw` (取款) 的方法，里面写一点简单的加减法 `if-else` 逻辑。

一切就大功告成了！Class 就是一个自带数据和专属技能的“小机器人”，试着把它造出来吧！
