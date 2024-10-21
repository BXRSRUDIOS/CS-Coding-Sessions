#include <iostream>
#include <cmath>

using namespace std;

int factorial(int n, int count) {
    if (count == 1) {
        return n;
    } else {
        return factorial(n*count, count-1);
    }
}

int main() {
    int num;
    int factAns = 1;
    cin >> num;
    cout << (factorial(factAns, num)) << endl;
}