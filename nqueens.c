#include <stdio.h>  
#include <stdlib.h>  
  
// every row must be a queen, array value is some queen's column
void printBoard(int rowQueen[], int n)  
{  
	int i,j;  
	for(i = 0; i < n; i++)        //行  
	{                  
		for(j = 0; j < n; j++)    //列  
		{  
			if(rowQueen[i] != j)  
				printf("0 ");  
			else   
				printf("1 ");   
		}  
		printf("\n");  
	}  
 
}  
 
// checking for row and col
int is_attacked(int rowQueen[], int row, int col)    
{  
	int row1 = 0;  
	while (row1 < row)
	{  
		if(rowQueen[row1] == col 
				|| abs(row1 - row) == abs(rowQueen[row1] - col))
		{
			return 1;  
		}
 
		row1++;  
	}  
 
	return 0;  
 
}  
 
void nqueens(int rowQueens[], int row, int n)    
{  
	if( row < n )  
	{  
		for(int col = 0; col < n; col++)
		{  
			if (rowQueens[n - 1] > -1)
			{
				break;
			}
 
			if(!is_attacked(rowQueens, row, col))  
			{  
				rowQueens[row] = col;  
				nqueens(rowQueens, row + 1, n);
 
			}  
		}  
 
	}  
	else
	{
	}
 
}  
  
int main(void)  
{  
	int n;  
	scanf("%d",&n);  
 
	if (n > 0)
	{
		int* pRowQueens = (int*)malloc(n * sizeof(int));
		for (int idx = 0; idx < n; idx++)
		{
			pRowQueens[idx] = -1;
		}
 
		nqueens(pRowQueens, 0, n);
 
		if (pRowQueens[n - 1] == -1)
		{
			printf("Not possible");
		}
		else
		{
			printBoard(pRowQueens, n);
		}
 
		free(pRowQueens);
	}
	return 0;  
 
}