#include <stdio.h>
#include <stdlib.h>


int main(void) {
    long p = 0;
    long q = 0;
    long n = 239867394157913;
    for (long i=0; i<100000000; i++) {
        for (long j=0; i<100000000; j++) {
            if (i * j == n) {
                p = i;
                q = j;
            }
        }
    }
    printf("P = %d", p);
    printf("q = %d", q);
    return 0;
}