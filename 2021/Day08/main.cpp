#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>

// Checks to see if two strings have the same chars
bool hasSameChars(std::string a, std::string b) {
	std::unordered_map<char, bool> charArr1(a.length());
	for (int i = 0; i < a.length(); i++) {
		charArr1[a[i]] = true;
	}
	std::unordered_map<char, bool> charArr2(b.length());
	for (int i = 0; i < b.length(); i++) {
		charArr2[b[i]] = true;
	}
	return charArr1 == charArr2;
}

// Checks to see if a string contains all the characters of the substring
bool containsChars(std::string str, std::string sub) {
	for (int i = 0; i < sub.length(); i++) {
		if (str.find(sub[i]) == std::string::npos) {  // If the character is not found
			return false;
		}
	}
	return true;
}


int main() {
	std::ifstream input("input.txt");
	std::string line;
	std::string signal;
	std::vector<std::vector<std::string>> signals, outputs;

	int uniqueDigits = 0;
	while (std::getline(input, line)) {
		std::stringstream signalstream(line);
		std::vector<std::string> linesignals, lineoutputs;
		bool passedPipe = true;
		while (signalstream >> signal) {
			if (signal == "|") {
				passedPipe = false;
			}
			else if (passedPipe) {
				linesignals.push_back(signal);
			}
			else {
				lineoutputs.push_back(signal);
				if (signal.length() <= 4 || signal.length() == 7) {
					uniqueDigits++;
				}
			}
		}
		signals.push_back(linesignals);
		outputs.push_back(lineoutputs);

	}

	std::cout << "Part 1: " << uniqueDigits << std::endl;

	int sum = 0;
	for (int i = 0; i < signals.size(); i++) {
		std::unordered_map<std::string, int> signalMap;
		std::string one;
		std::string four;
		for (const std::string& s : signals.at(i)) {
			if (s.length() == 2) {
				signalMap[s] = 1;
				one = s;
			}
			else if (s.length() == 3) {
				signalMap[s] = 7;
			}
			else if (s.length() == 4) {
				signalMap[s] = 4;
				four = s;
			}
			else if (s.length() == 7) {
				signalMap[s] = 8;
			}
			else {
				signalMap[s] = -1;  // We don't know yet
			}
		}

		std::string fourArm(four);  // the arm of the four not part of the one

		// Remove from four the 2 letters of one
		fourArm.erase(std::remove(fourArm.begin(), fourArm.end(), one[0]), fourArm.end());
		fourArm.erase(std::remove(fourArm.begin(), fourArm.end(), one[1]), fourArm.end());

		// Fill in the rest of the signals
		for (auto& pair : signalMap) {
			if (pair.second != -1) continue;
			if (pair.first.length() == 5) {
				if (containsChars(pair.first, one)) {
					pair.second = 3;
				}
				else if (containsChars(pair.first, fourArm)) {
					pair.second = 5;
				}
				else {
					pair.second = 2;
				}
			}
			else {  // length is 6
				if (containsChars(pair.first, four)) {
					pair.second = 9;
				}
				else if (containsChars(pair.first, one)) {  // This has to go after checking for four otherwise it will always skip the four check
					pair.second = 0;
				}
				else {
					pair.second = 6;
				}
			}
		}

		for (int x = 0; x < outputs.at(i).size(); x++) {
			int digit = -1;
			for (const auto& pair : signalMap) {
				if (pair.first.length() != outputs.at(i).at(x).length()) continue;
				if (hasSameChars(outputs.at(i).at(x), pair.first)) {
					digit = pair.second;
					break;
				}
			}

			// First digit worth 10 ^ 3, then 10 ^ 2, etc.
			sum += digit * std::pow(10, 3 - x);
		}
	}

	std::cout << "Part 2: " << sum << std::endl;

	return 0;
}