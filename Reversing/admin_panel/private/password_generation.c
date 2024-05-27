#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <openssl/sha.h>
#include <string.h>

void print_hash(unsigned char hash[SHA256_DIGEST_LENGTH]) {
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");
}

int main() {
    // Seed the random number generator
    srand(time(NULL));

    // Generate a random number
    int random_number = rand();

    // Print the random number
    printf("Random number: %d\n", random_number);

    // Convert the random number to a string
    char random_number_str[8]; // enough to hold an integer in string form
    
    snprintf(random_number_str, sizeof(random_number_str), "%d", random_number);

    // Compute the SHA-256 hash
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char*)random_number_str, strlen(random_number_str), hash);

    // Print the SHA-256 hash
    printf("SHA-256 hash: ");
    print_hash(hash);

    return 0;
}

