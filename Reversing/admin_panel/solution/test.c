#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <openssl/sha.h>

#define HASH_LENGTH SHA256_DIGEST_LENGTH

void print_hash(unsigned char hash[HASH_LENGTH]) {
    for (int i = 0; i < HASH_LENGTH; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");
}

int hex_to_bytes(const char *hex_str, unsigned char *byte_array) {
    for (int i = 0; i < HASH_LENGTH; i++) {
        if (sscanf(&hex_str[i * 2], "%2hhx", &byte_array[i]) != 1) {
            return -1;  // Error in conversion
        }
    }
    return 0;
}

void find_hash_value(int random_number){
    char *file_hash_str = "da569ed43f5265cbc2a3aeb765496ff2a00bc8c75b9b2dd81ac1c62b2f01b97e";
    unsigned char stored_hash[HASH_LENGTH];

    // Convert the stored hash string to a binary format
    if (hex_to_bytes(file_hash_str, stored_hash) != 0) {
        fprintf(stderr, "Error converting hex string to bytes\n");
        return EXIT_FAILURE;
    }

    char random_number_str[8]; // enough to hold an integer in string form
    
    snprintf(random_number_str, sizeof(random_number_str), "%d", random_number);

    // Compute the SHA-256 hash
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char*)random_number_str, strlen(random_number_str), hash);

    if(memcmp(stored_hash, hash, HASH_LENGTH) == 0){
        printf("WE FOUND THE VALUE!!! %d\n", random_number);
        exit(1);
    }


}


int generate_seeded_random(long seed){
    srand(seed);

    int random_number = rand();

    char random_number_str[12]; 
    snprintf(random_number_str, sizeof(random_number_str), "%d", random_number);
    printf("Random number: %s\n", random_number_str);


    return random_number;
}

int main() {

    int now = time(NULL);
    int yesterday = 1716478155;

    for (int i = yesterday; i < now; ++i) {
        int r = generate_seeded_random(i);
        find_hash_value(r);
    }
}

