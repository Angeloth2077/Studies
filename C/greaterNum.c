#include <stdio.h>

int main(){
	
	int num[4];
	int greater = 0;
	printf("Please enter 5 numbers \n \n");

	for(int i=0; i <=4; i++){
		printf("Number %d: ", i + 1);
		scanf("%d",&num[i]);

		if(greater < num[i]){
			greater = num[i];
		}
	}
	printf("The greaater number is %d \n", greater);

	return 0;
}
