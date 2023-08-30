// Quick Sorting Algorithm
// 퀵 정렬 알고리즘

#include <stdio.h>
#define ELEMENTS 10

void quick_sort(int list[], int left, int right) {
	// L = 0, R = 9
	int L = left, R = right;
	int temp;
	// pivot = list[4] => 1(In Initital List)
	int pivot = list[(L + R) / 2];
	printf("pivot = %d\n", pivot);
	// L & R is pointer of comparing value of list
	while (L <= R) {
		// if list[L] is smaller than pivot, it is correct position
		// so, pointer L is +1
		// if it is bigger than pivot, loop is stop and go for change
		while (list[L] < pivot) {
			printf("L = %d\n", L);
			L++;
		}
		// also if list[R] is bigger than pivot, it is also correct position
		// so, pointer R is -1
		// also if it is samller than pivot, loop is stop and go for change
		while (list[R] > pivot) {
			printf("R = %d\n", R);
			R--;
		}
		// changing position of 2 pointer
		if (L <= R) {
			if (L != R) {
				printf("temp = %d\n", temp);
				temp = list[L];
				list[L] = list[R];
				list[R] = temp;
			}
			// after change, it is finished so pointer get next index
			L++;
			R--;
			printf("%d, %d\n", L, R);
		}
	}
	// To check how list is changing
	printf("now list = ");
	for (int i = 0; i < 10; i++) {
		printf("%d ", list[i]);
	}
	printf("\n");
	// if first cycle completed, compared L and right
	// if L is smaller than right, list which finished first cycle and L and right be the new parameter of quick sort algo
	if (left < R) {
		printf("Pass Quick Sort No. 1(list, %d, %d)\n", left, R);
		quick_sort(list, left, R);
	}
	// also if first cycle completed, compared R and left
	// if R is bigger than L, list which finished first cycle and R and lieft be the new parameter of quick sort algo
	if (L < right) {
		printf("Pass Quick Sort No. 2(list, %d, %d)\n", L, right);
		quick_sort(list, L, right);
	}
}

int main() {
	int list[ELEMENTS] = {5, 2, 3, 6, 1, 9, 0, 7, 8, 4};
	quick_sort(list, 0, 9);
	for (int i = 0; i < 10; i++) {
		printf("%d ", list[i]);
	}
}
