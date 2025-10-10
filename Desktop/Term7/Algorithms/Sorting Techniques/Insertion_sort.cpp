#include <iostream>
using namespace std;

int main() {
    
    int arr[5] = {5,4,3,2,1};
    int key = 0;
    int j = 0;
    for (int i = 1;i<arr.size();i++)
    {
        key = arr[i];
        j = i-1;
        while(key<arr[j]&&j>=0)
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }

    return 0;
}
wewewewe
weewewewe
