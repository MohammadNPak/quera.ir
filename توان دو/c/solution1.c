#include <stdio.h>
int main()
{
  int n, x;
  scanf("%d", &n);
  x = 2;
  while (x < n)
  {
    x = x * 2;
  }
  printf("%d", x);
  return 0;
}