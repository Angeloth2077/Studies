#include <stdio.h>

int main(){
	int values[5];
	int result;	
	/*Asking the data*/
	printf("Please enter 5 numbers \n");
	printf("\n");

	for(int i = 0; i <= 4; i++){
		printf("Value [%d]: ", i);
		scanf("%d", &values[i]);
	}
	result = values[0] * values[1] * values[2] * values[3] * values[4];
	
	printf("Multiplying all values we get: %d \n", result);

	return 0;
}
