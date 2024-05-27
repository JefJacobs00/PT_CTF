#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>


int generate_seeded_random(long seed){
    // Seed the random number generator with the current time
    srand(seed);

    int random_number = rand();

    if (random_number == 1926729754){
        printf("Congrats you found it: %d", random_number);
        exit(1);
    }
    return random_number;
}

int main() {

    int now = time(NULL);
    int yesterday = 1651418955;

    for (int i = yesterday; i < now; ++i) {
        generate_seeded_random(i);
    }
}
