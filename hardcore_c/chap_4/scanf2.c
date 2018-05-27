#include <stdio.h>

int main()
{
  int n = 0;

  printf("정수 n을 입력해주세요. n = ");
  scanf ("%d", &n);
  printf("entered n = %d\n", n);
  printf("double of n = %d\n", n+n);
  printf("triple of n = %d\n", n+n+n);

  return 0;
}
