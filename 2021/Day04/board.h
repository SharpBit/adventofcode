#pragma once
#include <array>

class Board {
	
public:
	std::array<std::array<int, 5>, 5> bingo;
	std::array<std::array<bool, 5>, 5> marked;
	Board();
	bool checkCols();
	bool checkRows();
	bool checkBoard();
	void mark(int i);
	int sumUnmarked();
	void displayBoard();
};