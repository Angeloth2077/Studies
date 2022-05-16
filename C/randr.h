#define RANDR_DOT_H
#ifndef RANDR_DOT_H
#include <stdlib.h>
#include <stdio.h>

int randr(int lower, int upper,	int count){
    for (int i = 0; i < count; i++) {
        int num = (rand() % (upper - lower + 1)) + lower;

		return num;
    }
}
#endif /*RANDR_DOT_H*/
