// #include <iostream>
// using namespace std;

// int main(){
//     cout<< "Hello";
// }


// #include<iostream>
// using namespace std;

// int main(){
//     int a=12;
//     cout<<a;
// }


// int main(){
//     cout<<"dgfgf" << endl;
//     cout<<"sdgfddf";
// }



/*int main(){
    cout<<"dgfdh\n\n";
    cout<<"dhgfdhf";
}*/

// int main(){
//     int n=12;
//     int *k = &n;
//     n=10;
//     cout<< n<<k;
// }


// int main(){
//     char n='r';
//     int a=5;
//     string st="madhu";
//     bool d=true;

//     cout<< n<<a <<st<<d;
// }

// int main(){
//     int  a=45,b=56,c=67;
//     cout<<a<<b<<c;

// }


// int main(){
//     const int a=10;
//     // a=8;
//     cout<< a;
// }

// #include <iostream>
// using namespace std;

// int main(){
//     int length;
//     int breath;
//     int area;

//     cout << "Enter the length:";
//     cin >>length;
//     cout <<"Enter the breath:";
//     cin >>breath;
//     area=length*breath;
//     cout<<area;

// }


// int 
// char

// string
// float
// double

// bool

// #include <iostream>
// using namespace std;

// int main(){
//     char a=10,b=20,c=30;
//     cout<< a << b << c ;
// }

// #include<iostream>
// using namespace std;

// int main(){
    
//     string name="Mad";
//     string &name1=name;
//     cout<<name;
//     cout<<name1;
// }


// #include <iostream>
// #include<vector>
// using namespace std;

// void fun(int vars[4]){
    
//      for(int ch=0 ; ch<4;ch++){
//         cout<<vars[ch]<<endl;
//     }
// }

// int main(){
//     int a[4]={1,2,3,4};
//     fun(a);
    
 
// }


// void myFunction(int myNumbers[5]) 
//   for (int i = 0; i < 5; i++) {
//     cout<< myNumbers[i] << "\n";
//   }
// }

// int main() {
//   int myNumbers[5] = {10, 20, 30, 40, 50};
//   myFunction(myNumbers);
//   return 0;
// }


#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    vector<vector<int>> res;
    sort(nums.begin(), nums.end());
    
    for (int i = 0; i < nums.size(); i++) {
        if (i > 0 && nums[i] == nums[i-1]) continue; // skip duplicates
        int left = i + 1, right = nums.size() - 1;
        
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];
            
            if (sum == 0) {
                res.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left+1]) left++;  // skip duplicates
                while (left < right && nums[right] == nums[right-1]) right--; // skip duplicates
                left++;
                right--;
            } 
            else if (sum < 0) left++;
            else right--;
        }
    }
    return res;
}

int main() {
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> result = threeSum(nums);

    for (auto triplet : result) {
        cout << "[";
        for (int x : triplet) cout << x << " ";
        cout << "] ";
    }
}
















