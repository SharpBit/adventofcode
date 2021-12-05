#include "board.h"
#include <iostream>


bool Board::checkCols() {
	bool hasUnmarked;
	for (int j = 0; j < marked[0].size(); j++) {
		hasUnmarked = false;
		for (int i = 0; i < marked.size(); i++) {
			if (!marked[i][j]) {
				hasUnmarked = true;
				break;
			}
		}
		if (!hasUnmarked) {
			return true;
		}
	}
	return false;
}

bool Board::checkRows() {
	bool hasUnmarked;
	for (int i = 0; i < marked.size(); i++) {
		hasUnmarked = false;
		for (int j = 0; j < marked[0].size(); j++) {
			if (!marked[i][j]) {
				hasUnmarked = true;
				break;
			}
		}
		if (!hasUnmarked) {
			return true;
		}
	}
	return false;
}
bool Board::checkBoard() {
	return checkRows() || checkCols();
}
void Board::mark(int num) {
	bool numFound = false;
	for (int i = 0; i < bingo.size(); i++) {
		for (int j = 0; j < bingo[0].size(); j++) {
			if (bingo[i][j] == num) {
				marked[i][j] = true;
				numFound = true;
				break;
			}
		}
		if (numFound) break;
	}
}

int Board::sumUnmarked() {
	int sum = 0;
	for (int i = 0; i < marked.size(); i++) {
		for (int j = 0; j < marked[0].size(); j++) {
			if (!marked[i][j]) {
				sum += bingo[i][j];
			}
		}
	}
	return sum;
}

// Method for debugging purposes, not used
void Board::displayBoard() {
	for (int x = 0; x < bingo.size(); x++) {
		for (int y = 0; y < bingo[0].size(); y++) {
			std::cout << bingo[x][y] << " ";
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;

	for (int x = 0; x < marked.size(); x++) {
		for (int y = 0; y < marked[0].size(); y++) {
			std::cout << marked[x][y] << " ";
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
}
