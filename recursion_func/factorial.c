// Factorial Algorithm

#include <stdio.h>

// using for - repeat
int factorial_repeat(int num) {

	int result = 1;

	for(int i = num; i > 0; --i) {
		result = result * i;
	}

	return result;
}

// using recursion function
int factorial_recursion(int num) {

	if(num == 1) {
		return 1;
	}

	return num * factorial_recursion(num - 1);
}

int main() {
	printf("Factorial using for-repeat = %d \n", factorial_repeat(5));
	printf("Factorial using recursion = %d \n", factorial_recursion(5));
}
