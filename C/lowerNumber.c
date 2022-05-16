#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
	/*Variables*/
	int x = 0;
	int y = 0;
	int sum = x - y;
	/*Taking data*/
	printf("Enter 2 numbers, I'll give you the lower one \n");
	printf("x: ");
	scanf("%d",&x);
	printf("y: ");
	scanf("%d", &y);
	printf("\n");
	/*Operationg*/
	if(sum <= 0){
		printf("The lower number is %d", x);
	}
	else if(sum >= 0){
		printf("The lower number is %d", y);	
	}
	else if(sum == 0){
		printf("They are the same");
	}	

	return 0;
}

