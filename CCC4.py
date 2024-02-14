#include <iostream>
using namespace std;

int main(){
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	
	string inp;
	int l;
	cin >> inp;
	while(inp != "quit!"){
			l = inp.length();
			if(l > 4 && inp[l - 1] == 'r' && inp[l - 2] == 'o' && !(inp[l - 3] == 'a' || inp[l - 3] == 'e' || inp[l - 3] == 'i' || inp[l - 3] == 'o' || inp[l - 3] == 'u' || inp[l - 3] == 'y')){
				
				cout << inp.substr(0, l - 2) << "our\n";
			}else{
				cout << inp << "\n";
			}
			
		cin >> inp;
	}
		
	return 0;
}