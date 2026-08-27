//
// Created by hal on 2026/8/4.
//

#include "checkSecre.h"
#include<iostream>
using namespace std;
class getNum {
    public:
     getNum() {
        string num;
         while (true) {
             cout<<"Enter an integer: ";
             cin>>num;
             if (num.length() <8){
                 cout<<"Length must be greater than 8"<<endl;}
             else
             {cout<<"mima is ok"<<endl;break;}
         }
    }

};

