#include<iostream>
#include "Point.h"
#include "Line.h"
using namespace std;


int main() {
    Point p1(0, 0);
    Point p2(3, 4);
    Point p3 = p1 + p2;

    cout << "p1: " << p1 << endl;
    cout << "p2: " << p2 << endl;
    cout << "p3: " << p3 << endl;

    Line line(p1, p2);
    Line line2(line);

    cout << "Line length: " << line.length() << endl;
    cout << "Line2 length: " << line2.length() << endl;

    system("pause");
    return 0;
}
