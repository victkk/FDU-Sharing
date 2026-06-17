#include <iostream>
#include <list>
#include <vector>
using namespace std;

//TODO: implement a template function: inner_product



int main(){
    vector<double> a;
    list<double> b;
    int i,n=5;
    double x,y;
    for(i=0;i<n;i++){
        cin>> x >> y;
        a.push_back(x);
        b.push_back(y);
    }
    cout<<"int result:"<<inner_product(a.begin(),a.end(),b.begin(),0)<<endl;
    cout<<"double result:"<<inner_product(a.begin(),a.end(),b.begin(),0.0)<<endl;
}

