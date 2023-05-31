#include <iostream>
using namespace std;

const int MAXX = 1000000;
int d[MAXX + 1];

void sieve() {
    for (int i = 1; i <= MAXX; i++) {
        for (int j = i; j <= MAXX; j += i) {
            d[j]++;
        }
    }
}

int main() {
    sieve();
    int n;
    cin >> n;
    while (n--) {
        int x;
        cin >> x;
        cout << d[x] << endl;
    }
    return 0;
}
