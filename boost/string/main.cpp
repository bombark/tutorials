/*================================  HEADER  ==================================*/

#include <iostream>
#include <boost/algorithm/string.hpp>

typedef std::string String;

using namespace std;

/*----------------------------------------------------------------------------*/



/*=================================  MAIN  ===================================*/

int main(){
	String text = "    ana comeu uma    banana";

	boost::trim(text);
	cout << text << endl;

	boost::to_lower(text);
	cout << text << endl;

	boost::to_upper(text);
	cout << text << endl;

	String tmp = boost::to_lower_copy(text);
	cout << tmp << endl;

	return 0;
}

/*----------------------------------------------------------------------------*/
