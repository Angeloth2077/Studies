#include <stdio.h>
#include <string.h>

int main(){
	char word[10] = "";
	printf("Enter a	word\n");
	scanf(" %s", word);
	printf("\n");
	
	int n = sizeof(word);
	for(int i = 0; i<=sizeof(word); i++){
		char temp = word[i];
        word[i] = word[n-i-1];
        word[n-i-1] = temp;
	}
	printf("%s \n", word);
	return 0;
}
