// Linear Search
// 순차 탐색

#include <stdio.h>
#define MAX_SIZE 100

int list[MAX_SIZE];		// List 선언

// fuction for making list
int make_list(int first, int last) {

	int index = 0;
	
	for (int i = first; i <= last; i++) {
		list[index] = i;
		index++;
	}
	
	return 0;
}

// function for linear search
int linear_search(int key) {

	int index;

	for (index = 0; index <= MAX_SIZE; index++) {
		if (list[index] == key) {

			printf("Index of %d : No.%d\n", key, index);

			break;
		}
	}
	
	return 0;
}

int main() {

	make_list(1, 10);
	linear_search(4);

	make_list(50, 128);
	linear_search(88);

}
