//https://codeforces.com/problemset/problem/1076/C

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
   int t;
   cin>>t;
   while(t--){
       int d;
       cin>>d;
       double a,b;
       //a=(d+√(d^2−4d))/2 and b=d−a.
       a = (d + sqrt(d*d - 4 * d) )/2 ;
       b=d-a;
       if( abs((a+b)- a*b) <=1e-6  &&  abs((a+b)-d) <= 1e-6 ){
            cout << std::fixed << std::setprecision(9);
            cout << "Y " << a << " " << b << "\n";
       }
       else
           cout<<"N" <<"\n";
       }
   
   
    
    return 0;
}
