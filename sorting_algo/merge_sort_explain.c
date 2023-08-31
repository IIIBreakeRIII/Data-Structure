// Merge Sort Algorithm
// 합병 정렬 알고리즘

#include <stdio.h>
#define ELEMENTS 10

// merge divided list
void merge(int list[], int left, int mid, int right) {
	printf("merge_mid = %d\n", mid);
	printf("merge_left = %d\n", left);
	printf("merge_right = %d\n", right);
	int temp_list[ELEMENTS] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	int L = left;
	int R = mid + 1;
	int n = left;
	
	printf("Merge start\n");
	printf("L = %d \n", L);
	printf("R = %d\n", R);
	printf("n = %d\n", n);
	// compare value L and value R
	// we want the smaller than mid_value goes to left side of list
	// and bigger than mid_value goes to right side of list
	while (L <= mid && R <= right) {
		// if L is smaller than R,
		if (list[L] <= list[R]) {
			// it goes left side
			temp_list[n++] = list[L++];
			printf("while_if_temp_list = [%d, %d, %d, %d, %d, %d, %d, %d, %d, %d]\n", temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9]);
		} else {
			// else, it goes right side
			temp_list[n++] = list[R++];
			printf("while_else_temp_list = [%d, %d, %d, %d, %d, %d, %d, %d, %d, %d]\n", temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9]);
		}
	}
	// if value L is bigger than mid
	if (L > mid) {
		// start point is R(bigger than mid_value) and loop until right
		for (int i = R; i <= right; i++) {
			temp_list[n++] = list[i];
		}
		printf("if_temp_list = [%d, %d, %d, %d, %d, %d, %d, %d, %d, %d]\n", temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9]);
	} else {
		// else, start point is L(smaller than mid_value) and loop until mid
		for (int i = L; i <= mid; i++) {
			temp_list[n++] = list[i];
		}
		printf("else_temp_list = [%d, %d, %d, %d, %d, %d, %d, %d, %d, %d]\n", temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4], temp_list[5], temp_list[6], temp_list[7], temp_list[8], temp_list[9]);
	}
	// re-sort list
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
	printf("mid = %d\n", mid);
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
