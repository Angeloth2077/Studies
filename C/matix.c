#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "randr.h"

int randr(int lower, int upper,	int count){
    for (int i = 0; i < count; i++) {
        int num = (rand() % (upper - lower + 1)) + lower;

		return num;
    }
}


int main(){
	extern int randr();
	int avr_row[5];
	int avr;
	int grades[6][7];
	
	/* Setting random numbers each position */
	for(int i = 0; i <= 5; i++){
		for(int j = 0; j <= 5; j++){
			grades[i][j] = randr(6, 10, 1);
		}
	}
	
	/* Taking the avarage of each row */
	for(int i = 0; i <= 5; i++){
		for(int j = 0; j <=5; j++){
			avr = avr + grades[i][j];
			avr_row[i] = avr;
		}
	}
	
	/* Adding to the last position of each row */
	for(int i = 0; i <=5; i++){
		grades[i][6] = avr_row[i];
	}
	
	/* Print time */
	for(int i = 0; i <= 5; i++){
		printf("%d\n", grades);
	}
}
