#include <iostream>
#include <math.h>
using namespace std;

class Solution {
public:
  int atoi(string str) {
    int result = 0;
    int len = str.length();
    int postive_tag = 1;
    int start_index = 0;
    while(str[start_index] == ' '){
      start_index ++;
    }
    while(str[len-1] == ' '){
      len --;
    }
    if(str[start_index] == '-'){
      postive_tag = -1;
      start_index++;
    }
    else if(str[start_index] == '+'){
      start_index++;
    }
    else
    {
      ;
    }
    for (int i = (len-1), j = 0; i >= start_index; i--, j++) {
      if(str[i] >= '0' && str[i] <= '9')
      {
        int s = str[i] - '0';
        result += (s * pow(10, j) * postive_tag);
      }
      else{
        result = 0;
        j = -1;
      }
    }
    if(postive_tag >= 0 and result < 0){
      result = INT_MAX;
    }
    else if(postive_tag <= 0 and result > 0)
    {
      result = INT_MIN;
    }
    else
    {
      ;
    }
    return result;
  }
};


int main(int argc, char *argv[])
{
  string str = "12a34";
  Solution *test_class = new Solution();
  int result = test_class->atoi(str);
  cout << result << endl;
  str = "0000";
  result = test_class->atoi(str);
  cout << result << endl;
  str = " -456";
  result = test_class->atoi(str);
  cout << result << endl;
  str = "-2147483648";
  result = test_class->atoi(str);
  cout << result << endl;
  return 0;
}
