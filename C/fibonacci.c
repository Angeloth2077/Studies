#include <stdio.h>
#include <string.h>

int main(){
	int a = 1;
	int b = 0;
	int result = 0;

	for(int i = 0; i <= 8; i++){
		printf("%d \n", result);	
		result = a + b;	
		a = b;
		b = result;
	}
	return 0;
}
