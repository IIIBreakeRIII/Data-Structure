// Merge Sort Algorithm
// 합병 정렬 알고리즘

#include <stdio.h>
#define ELEMENTS 10

// merge divided list
void merge(int list[], int left, int mid, int right) {
	int temp_list[ELEMENTS];
	int L = left;
	int R = mid + 1;
	int n = left;

	while (L <= mid && R <= right) {
		if (list[L] <= list[R]) {
			temp_list[n++] = list[L++];
		} else {
			temp_list[n++] = list[R++];
		}
	}

	if (L > mid) {
		for (int i = R; i <= right; i++) {
			temp_list[n++] = list[i];
		}
	} else {
		for (int i = L; i <= mid; i++) {
			temp_list[n++] = list[i];
		}
	}

	for (int i = left; i <= right; i++) {
		list[i] = temp_list[i];
	}
}

// this for divide list in half until left >= right
// after finished dividing, starting merge
void merge_sort(int list[], int left, int right) {
	if (left >= right) {
		return;
	}
	
	int mid = (left + right) / 2;
	merge_sort(list, left, mid);
	merge_sort(list, mid + 1, right);
	merge(list, left, mid, right);
}

int main() {
	int list[ELEMENTS] = {5, 3, 2, 7, 8, 1, 9, 0, 6, 4};
	merge_sort(list, 0, 9);
	for (int i = 0; i < 10; i++) {
		printf("%d ", list[i]);
	}
	return 0;
}
