#include <stdio.h>

int main(void) {
  int tcase;
  double a, b;
  double ares, bres;
  double abres, allres;
  scanf("%d", &tcase);

  for(int i = 0; i < tcase; i++){
    scanf("%lf %lf", &a, &b);
    allres = b/a;

    if( a > 1){
      for(int u = 1; u < a; u++){
        bres = b-u;
        ares = a-u;
        abres = bres/ares;
        allres = allres * (bres/ares);
      }
    }
  printf("%.0lf\n", allres);
  }
}