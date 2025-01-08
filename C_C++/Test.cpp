#include <iostream>
using namespace std;
class Solution {
public:
    void res(int arr[],int size,int t) {
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                if (arr[i] + arr[j] == t) {
                    cout << "[" << i << ", " << j << "]";
                }
            }
        }
    }
};
int main() {
    Solution s;
    int size,target;
    cout<<"Enter size of array: ";
    cin>>size;
    int *arr = new int[size];
    for(int i=0;i<size;i++){
        cout<<"Enter the element at "<<i<<" index : ";
        cin>>arr[i];
    }
    cout<<"Enter Target Value : ";
    cin>>target;
    s.res(arr,size,target);
    cout << endl;
    return 0;
}