#include <bits/stdc++.h>
using namespace std; 

int main() 
{ 
	vector<int> g1,g2;
	for (int i = 1; i <= 10; i++) 
		g1.push_back(i * 10); 

	cout << "\nat : g1.at(4) = " << g1[1]; 

	cout << "\nfront() : g1.front() = " << g1.front(); 

	cout << "\nback() : g1.back() = " << g1.back(); 

	sort(g1.begin(), g1.end());
  cout << "Sorted \n"; 
  for (int i=0; i<g1.size(); i++) 
    cout << g1.at(i) << " ";
  g2 = g1;
  reverse(g1.begin(), g1.end()); 
  
    // Print the reversed vector 
  cout << "Reversed Vector: "; 
  for (int i = 0; i < g1.size(); i++) 
      cout << g1[i] << " "; 
  cout << endl; 
  for (int i = 0; i < g2.size(); i++) 
      cout << g2[i] << " "; 
  cout << endl; 

  g2.insert(g2.end(), g1.begin(), g1.end());
  for (int i = 0; i < g2.size(); i++) 
      cout << g2[i] << " "; 
  cout << endl; 

  if (find(g2.begin(), g2.end(), 1) != g2.end() )
  	cout << "Yes";
  else
  	cout << "No";
  cout<<endl;

  //counting
  cout << "Number of times 10 appears : "<<count(g2.begin(), g2.end(), 10)<<endl;
  
  string str="asdfgh";
  cout<<str;
  cout << endl; 
  str.push_back('s'); 
  cout<<str;
  cout << endl; 
  reverse(str.begin(), str.end()); 
  cout<<str;
  cout << endl; 
  string str1=str, str2;
  cout<<str1;
  cout << endl; 
  str2.insert(str2.end(), str1.begin(), str1.end());
  cout<<str2;
  cout << endl; 

  //dictionary
	map<int, int> aNiceMap;
	aNiceMap.insert ( pair<int,int>(1,0));
	aNiceMap.insert ( pair<int,int>(2,0));
	cout << aNiceMap.find(12)->second << '\n';
	aNiceMap.find(12)->second++;
	cout << aNiceMap.find(12)->second << '\n';
	if (find(g2.begin(), g2.end(), 1) != g2.end() )
  	cout << "Yes";
  else
  	cout << "No";
  cout<<endl;

	return 0; 
} 
