#pragma warning(disable: 4786)
#include <iostream>
#include "Calculator.h"
using namespace std;

int main()
{
  Calculator calculator;
  try{
    calculator.add(10);
    calculator.printWithStars();
    calculator.multiply(5);
    calculator.printWithStars();
    cout << "Result: " << calculator.getResult() << endl;
    calculator.clear();
    cout << "After clearing: " << calculator.getResult() << endl;
    calculator.subtract(3);
    calculator.printWithStars();
    calculator.divide(2);
    calculator.printWithStars();
    cout << "Result: " << calculator.getResult() << endl;
  }
  catch (runtime_error& e) {
    cout << e.what() << endl;
  }
  try{
    calculator.divide(0);}
  catch (runtime_error& e) {
    cout << e.what() << endl;
  }
  
  return 0;
}
