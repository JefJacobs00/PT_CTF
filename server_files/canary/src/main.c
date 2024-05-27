#include <stdio.h>
#include <stdlib.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    printf("Kill the canary\n");
    char a = 0;
    char input[20];
    gets(input);
    if(a != 0){
        printf("ctf{0mg_th3y_k1ll3d_th3_canary_y0u_b4st4rds}");
        exit(0);
    }
    return 0;
}
