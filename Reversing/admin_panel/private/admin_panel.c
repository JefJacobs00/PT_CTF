#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

#define HASH_LENGTH SHA256_DIGEST_LENGTH

void print_hash(unsigned char hash[HASH_LENGTH]) {
    for (int i = 0; i < HASH_LENGTH; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");
}

int read_hash_from_file(const char *filename, unsigned char hash[HASH_LENGTH]) {
    FILE *file = fopen(filename, "rb");
    if (!file) {
        perror("Error opening file");
        return -1;
    }
    
    for (int i = 0; i < HASH_LENGTH; i++) {
        if (fscanf(file, "%02hhx", &hash[i]) != 1) {
            fclose(file);
            fprintf(stderr, "Error reading hash from file\n");
            return -1;
        }
    }
    
    fclose(file);
    return 0;
}

void compute_sha256(const char *str, unsigned char hash[HASH_LENGTH]) {
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, str, strlen(str));
    SHA256_Final(hash, &sha256);
}

int main() {
    const char *filename = "hash.txt";
    unsigned char file_hash[HASH_LENGTH];
    
    if (read_hash_from_file(filename, file_hash) != 0) {
        return EXIT_FAILURE;
    }

    char password[256];
    printf("Enter password: ");
    if (fgets(password, sizeof(password), stdin) == NULL) {
        fprintf(stderr, "Error reading password\n");
        return EXIT_FAILURE;
    }

    // Remove newline character from password input if present
    size_t len = strlen(password);
    if (len > 0 && password[len - 1] == '\n') {
        password[len - 1] = '\0';
    }

    unsigned char password_hash[HASH_LENGTH];
    compute_sha256(password, password_hash);
    print_hash(file_hash);
    print_hash(password_hash);
    if (memcmp(file_hash, password_hash, HASH_LENGTH) == 0) {
        printf("Authentication successful\n");
    } else {
        printf("Authentication failed\n");
    }

    return EXIT_SUCCESS;
}
