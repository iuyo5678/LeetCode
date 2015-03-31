#include <string>
#include <algorithm>
#include <iostream>
#include <stdlib.h>
using namespace std;

string custom_reverse(string str){
  int len = str.length();

  for (int i = 0; i<len/2; i++)
  {
    //前后交换
    char temp = str[i];
    str[i] = str[len-i-1];
    str[len-i-1] = temp;
  }
  return str;
}

class Solution {
public:
  int reverse(int x) {
    int abs_value = abs(x);
    std::string s = std::to_string(abs_value);
    int reverse_value;
    s = custom_reverse(s);
    try {
      reverse_value = std::stoi(s);
    }
    catch (const std::out_of_range& oor) {
      reverse_value = 0;
    }
    if(reverse_value <= 0)
      reverse_value =0;
    if(x<=0)
      reverse_value = 0-reverse_value;
    return reverse_value;
  }
};

int main(int argc, char *argv[])
{
  Solution *test_class = new Solution();
  int s = 1234;
  s = test_class->reverse(s);
  cout << s << endl;
  s = 0;
  s = test_class->reverse(s);
  cout << s << endl;
  s = -1234;
  s = test_class->reverse(s);
  cout << s << endl;
  s = -1;
  s = test_class->reverse(s);
  cout << s << endl;
  s = 1000000003;
  s = test_class->reverse(s);
  cout << s << endl;
  return 0;
}

