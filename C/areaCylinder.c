#include <stdio.h>
#include <math.h>

int main(){
	
	//Variables//
	float r = 0;
	float h = 0;
	float area = 0;

	//Getting data//
	printf("Radius of the cylinder? ");
	scanf("%f",&r);
	printf("The height of the cylinder? ");
	scanf("%f",&r);
	printf("\n");

	//Area//
	area = 2 * 3.1415 * r * r + 2 * 3.1415 * h *r * h;

	//Result//
	printf("The area is %f \n", area);
	
	return 0;
}
