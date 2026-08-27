//
// Created by hal on 2026/8/4.
//

#include "vectorReference.h"

#include <iostream>
#include <ostream>
#include <vector>

using namespace std;
class VectorReference {
private:
    int num=0;
    double avg=0;
    public:
    void calculateAverage(const vector<int>& v) {
        for (int i=0; i<v.size(); i++) {
            if (v[i]>60) {
                num+=v[i];
            }
        }
        avg=num/(double)v.size();
        cout<<"Average: "<<avg<<endl;
    }
};

