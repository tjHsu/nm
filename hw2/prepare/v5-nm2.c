#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv){

////set up grid
	int Nin = atoi(argv[1]);
	double T=0.2;
	int N = Nin-1;
	double h=1./Nin;
	double lambda= Nin*1.0;
	double tau = 1./Nin;
	int i =0;
	int j=0;
	double u[N];
	double e[N];
	double garr[N][2*N];
	double ginv[N][N];
	double Barr[N][N];
	double r[N];
	
////set u[N] and r[N];
	for(i=0;i<N;i++){
		u[i]=0.0;
		}
	for (i=0;i<N;i++){
		u[i]=sin((i+1)*h*M_PI);
		printf("u[%d]=%f,beforeloop%f\n",i,u[i],(i+1)*h*M_PI);
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
////solve GJ
	/*
	for (i=0;i!=N;i++){
		for (j=0;j!=2*N;j++){

			printf("garr[%d][%d]=%1.2f  ",i,j,garr[i][j]);
		}
		printf("\n");	
	}	
	*/	
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
	*/
	for (i=0;i!=N;i++){
		for(j=0;j!=N;j++){
			ginv[i][j]=garr[i][j+N];
		}
	}
	/*
	for (i=0;i!=N;i++){
		for (j=0;j!=N;j++){

			printf("ginv[%d][%d]=%1.2f  ",i,j,ginv[i][j]);
		}
		printf("\n");	
	}	
	*/
	
////loop for the tau	
	int Tmax=T/tau;
	int l =0;
	for (l=0;l<Tmax;l+=1){
		printf ("for the %dth loop , when t=%f\n",l+1,tau*(l+1));
////reset r[i]
		for (i=0;i!=N;i++){
			r[i]=0;
		}
////B.u[]
		for (i=0;i!=N;i++){
			for (j=0;j!=N;j++){
				r[i]+=Barr[i][j]*u[j];
			}
		}
	
	
////reset u[i]
		for (i=0;i!=N;i++){
			u[i]=0;
		}
	
////A^-1.r[]
		for (i=0;i!=N;i++){
			for (j=0;j!=N;j++){
				u[i]+=ginv[i][j]*r[j];
			}
		}
////compute the exact solution	
		for (i=0;i!=N;i++){
			e[i]=sin(M_PI*(i+1)*h)*exp((-1.)*M_PI*M_PI*(l+1)*tau);		
		}
		
////print and compare
		for (i=0;i!=N;i++){
			printf("u[%d]=%f,when t=%f\n",i+1,u[i],tau*(l+1));
			printf("e[%d]=%f,when t=%f\n",i+1,e[i],tau*(l+1));
		}

	}

	double c=0.;
	for (i=0;i!=N;i++){
		printf("%f\n",(u[i]-e[i]));
		if ((u[i]-e[i])<c){
			c=(u[i]-e[i]);
		}
	}
	printf("the max error (i.e.CrNiM-ExactSol.)when N=%d is %f\n",Nin,c);

		
		
return 0;
}
