#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    char buffer[100];
    if (argc > 1) {
        strcpy(buffer, argv[1]);
        printf("Received: %s\n", buffer);
    } else {
        printf("No input.\n");
    }
    return 0;
}
