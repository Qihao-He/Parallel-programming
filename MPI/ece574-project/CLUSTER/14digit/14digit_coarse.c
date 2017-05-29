/* Auther: Qihao He <qi.he@maine.edu> */

#include <stdio.h>
int main(){
  double p = 3;
  int i;
  for (i = 2 ; i <= 100000 ; i+=4){
    p += 4 / (double(i)*(i+1)*(i+2));
    p -= 4 / (double(i+2)*(i+3)*(i+4));
  }

  printf("pi=%.14f\n", p);
  return 0;
}
