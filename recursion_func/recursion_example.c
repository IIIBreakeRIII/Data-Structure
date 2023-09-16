// Recursion Function Example

#include <stdio.h>

void recursion(int num) {

	if (num == 0) {
		return;
	}
	
	printf("%d | Recursion \n", num);
	num -= 1;
	recursion(num);
}

int main() {
	recursion(5);
}
