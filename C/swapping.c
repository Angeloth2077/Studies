#include <stdio.h>

int main(){

	//variables//
	int x = 0;
	int y = 0;
	int swap = 0;

	//getting data//
	printf("The x number? ");
	scanf("%d", &x);
	printf("The y number? ");
	scanf("%d", &y);

	printf("\n");

	//swapping//
	swap = y;
	y = x;
	x = swap;

	//printing//
	printf("The x numeber is: %d\n", x);
	printf("The y number is: %d\n", y);	

	return 0;
}
