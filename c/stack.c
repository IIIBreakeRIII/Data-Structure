// 스택 알고리즘 구현

#include <stdio.h>
#define STACK_SIZE 10		// 스택의 전체 사이즈 정의

int stack[STACK_SIZE];	// stack 배열 정의
int top = -1;						// 가장 위에 있는 원소

// 스택이 모두 찼는지 확인
int isFull() {
	if (top >= STACK_SIZE - 1) {
		printf("Error: Stack Is Full\n");
		return 1;
	}
	return 0;
}

// 스택이 모두 비었는지 확인
int isEmpty() {
	if (top == -1) {
		printf("Error: Stack Is Empty\n");
		return 1;
	}
	return 0;
}

// 스택 프린트
void printStack() {
	int i;
	for (i = 0; i <= top; i++) {
		printf("%d ", stack[i]);
	}
	printf("\n");
}

// push 구현 -> 스택에 원소 넣기
void push(int data) {
	if (!isFull()) {				// 스택이 꽉 차지 않았다면
		top++;								// 한 칸 위로 올리기
		stack[top] = data;		// 해당 스택 인덱스에 데이터 삽입
		printStack();
	}
}

// pop 구현 -> 스택에 원소 빼기
void pop() {
	if (!isEmpty()) {
		stack[top--];
		printStack();
	}
}

int main() {
	push(5);
	push(4);
	push(3);
	push(2);
	push(1);
	pop();
	pop();
	push(0);

	return 0;
}

