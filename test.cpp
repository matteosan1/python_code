#include <iostream>
#include <functional>
#include <vector>

using namespace std::placeholders;

class A {};
class B {};
class C {
public:
  operator A() {};
  explicit operator B() {};
};

int main() {
  
  std::cout << "auto" << std::endl;
  int i1 = 10;
  auto i2 = i1;

  std::cout << "lambda" << std::endl;
  /*
    int vettore[10] ;
    std::vector<int> nums{3, 4, 2, 9, 15, 267};
    std::for_each(nums.begin(), nums.end(), [](int &n) { n++;}) ;
  */
  
  std::cout << "explicit" << std::endl;
  A a;
  B b;
  C c;
  a = c;
  //b = static_cast<B> (c);
  
  return 0;
}
