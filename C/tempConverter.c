#include <stdio.h>
#include <string.h>

int main(){
	//variables//
	float c = 0;
	float f = 0;
	char choose[1] = "";	
	float result = 0;


	//Choose the mode and solving//
	printf("What do you want to convert it to? F° or C°\n");
	scanf(" %c", choose);	

	if(strcmp(choose, "F") == 0){
		printf("Temperature in celsius: ");
		scanf("%f", &c);	
		result = c * 9/5 + 32;
		printf("\nThe result is %f", result);
	}
	else if(strcmp(choose, "C") == 0){
		printf("Temperature in fahrenheit: ");
		scanf("%f", &f);
		result = (f - 32) * 5/9;
		printf("\nThe result is %f", result);
	}
	else{
		printf("Please select either F or C");
	}

	return 0;
}
