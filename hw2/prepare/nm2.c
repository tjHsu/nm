#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv){

	////set up grid
	int N = atoi(argv[1]);
	//const int N=20;
	float h=1./N;
	
	float lambda= N*1.0;
	float tau = 1./N;
	//printf("N=%d,h=%f,lambda =%f,tau=%f\n",N,h,lambda,tau);


	int i =0;
	int j=0;
	//float e[N];
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
		printf("u[%d]=%f,when%f\n",i,u[i],i*h*M_PI);		
		}


	for (i=0;i<N;i++){
		r[i]=0;
		}
	/*
	for(i=0;i<N;i++){
		printf("u[%d]=%f\n",i,u[i]);
		}	
	*/

	
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
	


	printf ("N=%d\n",N);
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


	/*
	for (i=0;i!=N;i++){
		for (j=0;j!=2*N;j++){

			printf("garr[%d][%d]=%1.2f  ",i,j,garr[i][j]);
		}
		printf("\n");	
	}
	printf("\n\n");
	*/
	
////

////B.u[]
	for (i=0;i!=N;i++){
		for (j=0;j!=N;j++){
			r[i]+=Barr[i][j]*u[j];
		}
	}

	/*
	for (i=0;i!=N;i++){
		printf("u[%d]=%f,since%f\n",i,u[i],i*h*M_PI);
		printf("r[%d]=%f,%f\n",i,r[i],i*h*M_PI);
	}
	*/
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
	/*	
	for (i=0;i!=N;i++){
		for (j=0;j!=2*N;j++){

			printf("garr[%d][%d]=%1.2f  ",i,j,garr[i][j]);
		}
		printf("\n");	
	}
	printf("\n\n");
	*/	
	
////A^-1.r[]
	for (i=0;i!=N;i++){
		for (j=N;j!=2*N;j++){
			u[i]+=garr[i][j]*r[j];
		}
	}
	
	for (i=0;i!=N;i++){
		printf("u[%d]=%f,since%f\n",i,u[i],i*h*M_PI);
		//printf("r[%d]=%f,%f\n",i,r[i],i*h*M_PI);
	}
	









/*
for (i=0;i<N;i++){

	e[i]=sin(i*h*M_PI)*exp(-1*M_PI*M_PI*0.2);
	}
	
for(i=0;i<N;i++){
	printf("e[%d]=%f\n",i,e[i]);
	printf("u[%d]=%f\n",i,u[i]);
	}	
*/
	





return 0;
}
