/*
author: gamingdy

You must set user_nb, with a number between 2 and infinity as argument 
*/
#include <iostream>

bool isPrime(int number){
	for (int a =2; a<number;a++){
		if (!(number%a)){
			return false;
		}
	}
	return true;
}

int find_factor(int number){
	int highest_prime_factor {0};
	for (int i = 2; i < number+1; i++)
	{
		if( !(number%i))
		{
			if (isPrime(i))
			{
				highest_prime_factor = i;
			}
		}
	}
	return highest_prime_factor;
}


int main(){
	int user_nb{100};
	int result {find_factor(user_nb)};
	std::cout << result;
	return 0;
}