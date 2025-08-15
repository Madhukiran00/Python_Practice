#include<iostream>
using namespace std;




class poly{
public:
    void fun(int x){
        cout<< "Called fun() int:" << x << endl;
    }


void fun(double y){
    cout<< "Called fun() with float:" << y << endl;
}

};

int main(){
  poly obj;
  obj.fun(5);
  obj.fun(4.56);
  return 0;

}