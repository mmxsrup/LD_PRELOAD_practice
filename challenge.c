#include <stdio.h>
#include <stdlib.h>
#include <time.h>


// secret flag
char flag[256] = "FLAG{HACK}";

int main() {
	srand(time(NULL));
	int key = rand();

	int input;
	printf("Input Password > ");
	scanf("%d", &input);

	if (key == input) {
		printf("Pass! flag is %s\n", flag);
	} else {
		printf("Wrong, Key is %d\n", key);
	}
	return 0;
}
