// author : gamingdy

#include <iostream>
#include <algorithm>

int main(){
	std::string user_string {"This is an string exemple"}; // Put your string here

	char user_char {'a'}; // Put the char you want to count the occurence in the given string


	auto occurence_char {std::count(std::begin(user_string), std::end(user_string), user_char)};

	std::cout << "There are " << occurence_char << " "<<user_char << " in given string: " << user_string;

	return 0;
}