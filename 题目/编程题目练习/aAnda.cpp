//
// Created by hal on 2026/8/22.
//

#include "aAnda.h"

#include <thread>

int v=0;

void func(int a) {
    static std::mutex m;
    std::lock_guard<std::mutex> lk(m);
    v=a;
}

int  main(void) {
    std::thread t1(func,2),t2(func,3);
    t1.join();
    t2.join();
    printf("%d\n",v);
    return 0;
}
