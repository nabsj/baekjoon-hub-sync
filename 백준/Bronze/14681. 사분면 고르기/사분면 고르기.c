#include <stdio.h>

int main(void) {
  int x,y;

  scanf("%d",&x);
  scanf("%d",&y);
  
  if(x>0){
    if(y>0){
      printf("1");
    }
    if(y<0){
      printf("4");
    }
  }
  if(x<0){
    if(y>0){
      printf("2");
    }
    if(y<0){
      printf("3");
    }
  }
  return 0;
}