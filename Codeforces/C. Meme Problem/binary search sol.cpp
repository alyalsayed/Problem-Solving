//https://codeforces.com/problemset/problem/1076/C

#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int d;
        cin >> d;

        double l = 0, r = d, a, b;
        int iter = 100;
        while (iter--) {
            double mid = (l + r) / 2;
            a = mid;
            b = d - a;
            if (abs(a * b - d) < 1e-9) {
                break;
            }
            if (a * b > d) {
                r = mid;
            } else {
                l = mid;
            }
        }

        if (abs(a + b - d) < 1e-9 && abs(a * b - d) < 1e-9) {
            cout << std::fixed << std::setprecision(9);
            cout << "Y " << a << " " << b << "\n";
        } else {
            cout << "N\n";
        }
    }
    return 0;
}