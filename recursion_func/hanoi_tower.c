// Hanoi Tower Algorithm

#include <stdio.h>

void hanoi_tower(int n, char from, char temp, char to) {

	if (n == 1) {
		printf("No.1 disk moves from %c to %c\n", from, to);
	} else {
		hanoi_tower(n - 1, from, to, temp);
		printf("No.%d disk moves from %c to %c\n", n, from, to);
		hanoi_tower(n - 1, temp, from, to);
	}
}

int main() {
	hanoi_tower(3, 'A', 'B', 'C');
	return 0;
}
