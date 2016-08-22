e#include<stdio.h>
#include<stdlib.h>

#define N 200
#define BRANCO 0
#define PRETO 1
#define iC 100
#define jC 50
#define jC2 150
#define R 75

int main(){
	int m[N][N], i, j;
	FILE *f;

	for(i=0;i<N;i++){
		for(j=0;j<N;j++){

			if(((i-iC)*(i-iC)+(j-jC2)*(j-jC2) <= R*R)||((i-iC)*(i-iC)+(j-jC)*(j-jC) <= R*R)){
				m[i][j]=BRANCO;
				if(((i-iC)*(i-iC)+(j-jC2)*(j-jC2) <= R*R)&&((i-iC)*(i-iC)+(j-jC)*(j-jC) <= R*R)){
					m[i][j]=PRETO;
				}
			}
			else m[i][j]=PRETO;
		}
	}

	f = fopen("test.pbm", "w");
	fprintf(f,"P1\n");
	fprintf(f,"%d %d\n",N,N);

	for(i=N-1;i>=0;i--){
		for(j=0;j<N;j++){
			fprintf(f,"%d",m[i][j]);
		}
		fprintf(f,"\n");
	}

	fclose(f);

	return 0;
}
