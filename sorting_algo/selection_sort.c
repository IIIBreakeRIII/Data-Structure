// Selection Sorting Algorithm
// 선택 정렬 알고리즘

#include <stdio.h>
#define ELEMENTS 5

int main(void) {

	int index, temp;
	// list define
	int list[ELEMENTS] = {9, 6, 1, 3, 5};
	// repeat all index
	for (int i = 0; i < ELEMENTS; i++) {
		// define min_value to save minimum value in list
		int min_value = 100;
		// repeat to find minimum value
		for (int j = i; j < ELEMENTS; j++) {
			// if no. j value is small than min_value
			if (list[j] < min_value) {
				// change min_value & index is j
				min_value = list[j];
				index = j;
			}
		}
		// save no.i value to temp value
		temp = list[i];
		// change the no.i value to index value
		list[i] = list[index];
		// change the existing index value to no.i value
		list[index] = temp;
	}
	// print list after sort finished
	for (int i = 0; i < ELEMENTS; i++) {
		printf("%d, ", list[i]);
	}
}
