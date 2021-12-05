#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include "board.h"

int main()
{
    std::ifstream input("input.txt");
	std::string line;
	int x;
    std::vector<int> nums;  // Nums to pick from
	std::vector<Board> boards;

	// First line of nums
	std::getline(input, line);
	std::replace(line.begin(), line.end(), ',', ' ');
	std::stringstream lineStream(line);
	while (lineStream >> x) {
		nums.push_back(x);
	}

	while (!input.eof()) {
		Board b;
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				input >> x;
				b.bingo[i][j] = x;
			}
		}
		boards.push_back(b);
	}

	int firstWinningNum = -1;
	int lastWinningNum = -1;
	int unmarkedSumF = -1;
	int unmarkedSumL = -1;
	for (int n : nums) {
		for (int i = 0; i < boards.size(); i++) {
			boards[i].mark(n);
			if (boards[i].checkBoard()) {
				if (firstWinningNum == -1) {
					firstWinningNum = n;
					unmarkedSumF = boards[i].sumUnmarked();
				}
				else if (boards.size() == 1) {
					lastWinningNum = n;
					unmarkedSumL = boards[i].sumUnmarked();
				}

				boards.erase(boards.begin() + i);  // remove the board that won so it doesn't get counted again
				i--;
				// Can't break here for part 2, the num has to be marked for all boards regardless
			}
		}
		if (lastWinningNum != -1) {
			break;
		}
	}

	std::cout << "Part 1: " << unmarkedSumF * firstWinningNum << std::endl;
	std::cout << "Part 2: " << unmarkedSumL * lastWinningNum << std::endl;
}
