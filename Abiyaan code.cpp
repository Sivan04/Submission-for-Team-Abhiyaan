# include <iostream>
using namespace std;

int main()
{
	int* matrix;
	int m, n, k;
	cout << "Enter the size of matrix:";
	cin >> m >> n;
	cout << "Enter the integer to be checked:";
	cin >> k;
	matrix = (int*)malloc(m * n);// allocating the matrix size dynamically
	int row=0,column=0;
	int count = 0; // to check the number of times the element k is repeating
	for ( row = 1;row <= m ;row++)
	{
		for (int column = 1;column <= n;column++)
		{
			cout << "Enter the value for " << row << " and " << column << " th element:" ;
			cin >> *(matrix + row * n + column);
			
		}
	}
	for (row = 1;row <= m;row++)
	{
		for (int column = 1;column <= n;column++)
		{
			if (*(matrix + row * n + column) == k)
			{
				count++;
				if (count == 1)
				{
					cout << "True" << endl;
				}
				cout << "The given element " << k << " is present at " << row << ' ' << column << " position" << endl;
			}
			

		}
	}

	if (count == 0)
	{
		cout << "False" << endl;
	}
}

