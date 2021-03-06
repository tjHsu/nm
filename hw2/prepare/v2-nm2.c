#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv){

////set up grid
	int N = atoi(argv[1]);
	float h=1./N;
	float lambda= N*1.0;
	float tau = 1./N;
	int i =0;
	int j=0;
	float u[N];
	float garr[N][2*N];
	float Barr[N][N];
	float r[N];
	
////set u[N] and r[N];
	for(i=0;i<N;i++){
		u[i]=0.0;
		}
	for (i=0;i<N;i++){
		u[i]=sin(i*h*M_PI);
		printf("u[%d]=%f,beforeloop\n",i,u[i]);
		}
	for (i=0;i<N;i++){
		r[i]=0;
		}
	
////set Barr and garr
	for (i=0;i!=N;i++){
		for (j=0;j!=N;j++){
			Barr[i][j]=0;
			if (i==j){
			Barr[i][j]=1.0-lambda;
			}
			if (i==j-1){
			Barr[i][j]=lambda/2.0;
			}
			if (i-1==j){
			Barr[i][j]=lambda/2.0;
			}		
		}
	}
	for (i=0;i!=N;i++){
		for (j=0;j!=2*N;j++){
			garr[i][j]=0;
			if (i==j-N){
				garr[i][j]=1.0;
			}
			if (i==j   && j<N){
				garr[i][j]=1.0+lambda;
			}
			if (i==j-1 && j<N){
				garr[i][j]=(-1)*lambda/2.0;
			}
			if (i-1==j && j<N){
				garr[i][j]=(-1)*lambda/2.0;
			}		
		}
	}
int l=0;
/*
for (l=0;l<=4;l=l+1){
printf ("%d",l);
}
*/

for (l=0;l<4;l+=1){
printf ("%d\n",l);
////B.u[]
	for (i=0;i!=N;i++){
		for (j=0;j!=N;j++){
			r[i]+=Barr[i][j]*u[j];
		}
	}

////GJ
	double m;
	int k;
	for(i=0;i<N-1;i++){
		for(j=i+1;j<N;j++){
			m=garr[j][i]/garr[i][i];
			for(k=i;k<N*2;k++)
				garr[j][k]-=m*garr[i][k];
		}
	}
	for(i=N-1;i>0;i--){
		for(j=i-1;j>=0;j--){
			m=garr[j][i]/garr[i][i];
			for(k=i;k<N*2;k++)
				garr[j][k]-=m*garr[i][k];
		}
	}	
	for(i=0;i<N;i++){
		m=garr[i][i];
		for(j=0;j<N*2;j++)
			garr[i][j]/=m;
	}

////A^-1.r[]
	for (i=0;i!=N;i++){
		for (j=N;j!=2*N;j++){
			u[i]+=garr[i][j]*r[j];
		}
	}
	for (i=0;i!=N;i++){
		printf("u[%d]=%f,after%dloop\n",i,u[i],l);
	}
	
}
		
		
return 0;
}
