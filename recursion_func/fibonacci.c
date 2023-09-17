// Fibonacci Algorithm

#include <stdio.h>

int fibonacci_for(int num) {

	int fib1 = 0;
	int fib2 = 1;
	int fib3 = 0;
	
	for (int i = 2; i < num; i++) {
		fib3 = fib1 + fib2;
		fib1 = fib2;
		fib2 = fib3;
	}

	return fib3;
}

int fibonacci_recursion(int num) {
	
	if (num == 1) {
		return 0;
	} else if (num == 2) {
		return 1;
	}

	return fibonacci_recursion(num - 1) + fibonacci_recursion(num - 2);
}

int main() {
	printf("Fibonacci Using for = %d \n", fibonacci_for(10));
	printf("Fibonacci Using Recursion = %d \n", fibonacci_recursion(10));
}
