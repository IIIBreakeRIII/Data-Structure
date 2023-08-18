// Binary Search
// 이진 탐색

#include <stdio.h>
#include <time.h>

#define MAX_ELEMENTS 10000000L

int list[MAX_ELEMENTS];
int count = 0;

// make list
int make_list(int first, int last) {

	int index = 0;
	
	for (int i = first; i <= last; i++) {
		list[index] = i;
		index++;
	}

	return 0;
}

// binary search algo
int search_binary(int key, int low, int high) {

	int middle;

	if (low <= high) {
		middle = (low + high) / 2;

		if (key == list[middle]) {
			count++;
			printf("Search Count = %d", count);
			return middle;

		} else if (key < list[middle]) {
			count++;
			return search_binary(key, low, middle - 1);

		} else {
			count++;
			return search_binary(key, middle + 1, high);

		}
	}

	return -1;
}

int main() {
	make_list(0, 10);
	search_binary(4, 0, 10);
}
