#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define adminMode 0

void sendTimesheet(){
    char name[20];
    fgets(&name, 20, stdin);
    //Send the timesheet of person with name
}

void manualEntry(char timesheet_m[4][5]) {
    printf("Select a week of the current month (1 - 4):\n");
    for (int i = 0; i < 4; ++i) {
        printf("You have selected week %d\n", i + 1);
        printf("Fill in your timesheet by entering:\n H (Home), O (Office), C (Course), V (Vacation)\n");
        printf("Example: HHOOC --> Mon: Home, Tue: Home, Wed: Office, Thu: Office, Fri: Course\n\n");

        // Clear the input buffer
        int c;
        while ((c = getchar()) != '\n' && c != EOF);

        // Read input into a temporary buffer
        char timesheet_w[6];
        fgets(timesheet_w, sizeof(timesheet_w), stdin);

        // Copy the contents of timesheet_w into timesheet_m[i]
        strncpy(timesheet_m[i], timesheet_w, sizeof(timesheet_m[i]) - 1);
        timesheet_m[i][sizeof(timesheet_m[i]) - 1] = '\0'; // Ensure null termination
    }

    printf("Thank you for filling in your timesheet\n");
}


void printMenu(){
    printf("Welcome to the Timesheet portal\n");
    printf("Chose your option:\n\n");
    printf("1. Manual entry\n2. Random entry\n3. Send timesheet\n4. Exit\n> ");
}

void printAdminMenu(){
    printf("Welcome to the Timesheet portal\n");
    printf("Chose your option:\n\n");
    printf("1. Manual entry\n2. Random entry\n3. Send timesheet\n4. Admin mode\n5. Exit\n> ");
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
	while (true){

        int adminCode = 0;
        char choice;

        if(adminMode){
            printAdminMenu();
            scanf("%d", &adminCode);
        }else{
            printMenu();
        }

        scanf("%s", &choice);

        char timesheet_m[4][5];

        switch (choice) {
            case '1':
                manualEntry(timesheet_m);
                break;
            case '2':
                printf("You chose %c", choice);
                break;
            case '3':
                sendTimesheet();
                break;
            case '5':
                if(adminCode == 123456){
                    printf("ctf{buff3r_0v3r_fl0w1ng_th3_c0ntr0l_v4ri4bl3}\n");
                } else{
                    return 0;
                }
                break;
            case '4':
                return 0;
        }
    }

}

