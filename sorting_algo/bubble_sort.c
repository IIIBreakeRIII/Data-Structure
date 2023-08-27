// Bubble Sort Algorithm
// 버블 정렬 알고리즘

#include <stdio.h>
#define ELEMENTS 5

void bubble_sort(int* list) {
	int i, j, temp;
	// index which I gonna compare
	for (i = 0; i < ELEMENTS; i++) {
		// index which I gonna change
		// j must be the next index of i
		for (j = i + 1; j < ELEMENTS; j++) {
			// if index_i is bigger than index_j
			if (list[i] > list[j]) {
				// save value of index_i in temp
				temp = list[i];
				// swap value index_i to index_j
				list[i] = list[j];
				// push temp to index_j
				list[j] = temp;
			}
		}
	}
}

int main() {
	int list[ELEMENTS] = {9, 6, 1, 3, 5};
	int i;
	
	bubble_sort(list);

	for (int i = 0; i < ELEMENTS; i++) {
		printf("%d ", list[i]);
	}
}
