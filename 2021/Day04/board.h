#pragma once
#include <array>

class Board {
	
public:
	std::array<std::array<int, 5>, 5> bingo;
	std::array<std::array<bool, 5>, 5> marked = { {
		{false, false, false, false, false},
		{false, false, false, false, false},
		{false, false, false, false, false},
		{false, false, false, false, false},
		{false, false, false, false, false}
	} };
	bool checkCols();
	bool checkRows();
	bool checkBoard();
	void mark(int i);
	int sumUnmarked();
	void displayBoard();
};