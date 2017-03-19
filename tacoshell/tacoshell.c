#include<stdio.h>
#define size 4

int j=0,i=0;
int days,shell,meat,rice,bean;

void printtable(int (a [int] [int ]));
void main()
{
	int table[days][size];
	int x=0,y=0;
	printf("enter days:\n");
	scanf("%d",&days);
	while(j<days)
	{
		printf("enter:\n");
		scanf("%d%d%d%d",&table[j][0],&table[j][1],&table[j][2],&table[j][3]);
		j++;
	}
	printtable(table[x][y]);
	
}

void printtable(int (a [int row][int column])
{
	for (row;row<days;row++)
	{
		for(column;column<size;column++)
		printf("%d\n",(a[row][column]);
	}
}

