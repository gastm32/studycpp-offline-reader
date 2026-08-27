#include <iostream>
#include <string>

class BankAccount {
private:
    std::string account;
    double balance;

public:
    // 【修复1】：加上构造函数，使用优雅的初始化列表！
    BankAccount(std::string accountName, double initialBalance) 
        : account(accountName), balance(initialBalance) {
    }

    void deposit(double amount) {
        balance += amount;
    }

    void withdraw(double amount) {
        if (amount > balance) {
            // 【修复2】：补上 std::endl
            std::cout << "no money" << std::endl;
        }
        else {
            balance -= amount;
        }
    }

    // 【修复3和4】：不要参数，且 const 写在最后面
    double getBalance() const {
        return balance;
    }
};

int main() {
    // 【修改】：创建对象时，必须按照构造函数的要求，给入名字和初始金额
    BankAccount account("张三", 100.0); 

    account.deposit(10);
    account.withdraw(10);
    
    // 这次代码完全合法，且一定能正确返回 100
    double dooler = account.getBalance(); 
    std::cout << dooler << std::endl;
    
    return 0;
}