// Insertion Sort Algorithm
// 삽입 정렬 알고리즘

#include <stdio.h>

#define MAX_SIZE 5

// insertion sort algo
void insertion_sort(int list[], int n) {
	// key = present value of list
	int i, j, key;
	// index start from 1, repeat whole list
	for (i = 1; i < n; i ++) {
		key = list[i];
		// j will repeat reversed
		// j must be positive number & if no.j value is bigger than key
		for (j = i - 1; j >= 0 && list[j] > key; j--) {
			// no.j + 1 move to right part
			list[j + 1] = list[j];
		}

		list[j + 1] = key;
	}
}

int main() {
	int i;
	int list[MAX_SIZE] = {9, 6, 1, 5, 3};
	// insertion sort execute
	insertion_sort(list, MAX_SIZE);
	// print result
	for (i = 0; i < MAX_SIZE; i++) {
		printf("%d ", list[i]);
	}
}
