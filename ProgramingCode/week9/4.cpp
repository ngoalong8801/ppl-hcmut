
#include <iostream>
using namespace std;

// Tạo một hàm tìm chu vi đường tròn:
template <class T>
T maxValue(T a, T b)
{
    return max(a, b);
}

// Tuy nhiên do không sử dụng hàm ở trên trong hàm main,
// nên hàm tìm chu vi ở trên đã không được chạy trong chương trình.
int main
{
    cout << maxValue(4.6, 6.7);
    return 0;
}