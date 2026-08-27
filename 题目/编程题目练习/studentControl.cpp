//
// Created by hal on 2026/8/4.
//

#include "studentControl.h"

#include <string>
#include <vector>

class Student {
private:
    std::string name;
    int score;
    public:
    Student(std::string name, int score) {
        this->name = name;
        this->score = score;

    }
};
class Classtoom {
    private:
    std::vector <Student> students;
    public:
    Classtoom() {}
    void addStudent(Student student) {
        push_back
    }
};
