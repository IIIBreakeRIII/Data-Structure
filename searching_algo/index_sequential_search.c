// Index Sequential Search
// 색인 순차 탐색

#include <stdio.h>

#define MAX_SIZE 1000
#define INDEX_SIZE 10

int n = 9;
int list[MAX_SIZE] = {3, 9, 15, 22, 31, 55, 67, 88, 91};

// making index table structure
typedef struct {
	int key;
	int index;
} indexTable;

// index table
indexTable index_list[INDEX_SIZE] = { {3, 0}, {15, 2}, {67, 6} };

// Search in list between two index : LOW & HIGH
int sequential_search(int key, int low, int high) {
	int i;
	for (i = low; i <= high; i++) {
		if (list[i] == key) {
			printf("Key is in index No.%d.\n", i);
			return i;
		}
	}
	return -1;
}

// Search index in INDEX TABLE
int index_search(int key) {
	int i, low, high;

	// if key is not in list, searching gone break
	if (key < list[0] || key > list[n - 1]) {
		return -1;
	}
	
	// search index table to find range of key
	for (i = 0; i < INDEX_SIZE; i++) {
		if (index_list[i].key <= key && index_list[i + 1].key > key) {
			break;
		}
	}
	
	// result of "i" after above loop
	if (i == INDEX_SIZE) {
		low = index_list[i - 1].index;
		high = n;
		printf("Key is located in between of No.%d INDEX and No.%d INDEX.\n", low, high);

	} else {
		low = index_list[i].index;
		high = index_list[i + 1].index;
		printf("Key is located in between of No.%d INDEX and No.%d INDEX.\n", low, high);
	}

	return sequential_search(key, low, high);
}

int main() {
	index_search(31);
}
