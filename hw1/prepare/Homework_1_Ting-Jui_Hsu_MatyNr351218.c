#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc, char **argv){

	int i = 0;
	int j = 0;
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
//check argument
	if (argc!=4  ){
		fprintf(stderr,"please enter the order of derivative,p, and q\n");
		return 0;
	}
	else if (atoi(argv[2])<0 || atoi(argv[3])<0){
		fprintf(stderr,"please insert only positive p and q\n");
		return 0;
	}
	else if  (atoi(argv[2])+atoi(argv[3])<atoi(argv[1])){
		fprintf(stderr,"please insert enough p and q for this order of derivative\n");
		return 0;
	}
	
	/*
	printf("argc = %d\n",argc);
	for (i=0; i!=argc;i++){
		printf("argv[%d]=%s\n",i,argv[i]);
	}
	*/
////////////////////////////////////////////////////////////	
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
//fill in the Taylor Series Coefficient	
	int n = atoi(argv[1]);
	int p = atoi(argv[2]);
	int q =	atoi(argv[3]);
	int L = p+q+1;
	float iarr[L][L+L];
	
	//printf("L=%d\n",L);
	while (i!=L){
		if (i<L-q-2){
			//printf("i=%d\n",i);
			
			while (j<L+L){
				//printf("mod2[%d]=%d\n",j,j%2);
				if (j%2 != 0){
					float r = -1.*power(i-L+q+1,j);
					//printf("%f\n",-r);
					iarr[i][j] =(-r)*(1./factorial(j));//*power(i-L+q+1,j);
					//printf("iarr[%d][%d]=[%f]\n",i,j,iarr[i][j]);
					j++;
				}
				else {
					iarr[i][j] = power(i-L+q+1,j) *(1./factorial(j));
					//printf("iarr[%d][%d]=[%f]\n",i,j,iarr[i][j]);
					j++;
				
				}	
			}
			
			j=0;
			i++;
		}
		else if (i == L-q){
			while(j<L+L){
				iarr[i][j]=1./factorial(j);				
				//printf("iarr[%d][%d]=[%f]\n",i,j,iarr[i][j]);
				j++;
			}
			j=0;
			i++;
		}
		else if (i==L-q-2 ){
			while(j<L+L){
				iarr[i][j]=power(-1,j)*1./factorial(j);				
				//printf("iarr[%d][%d]=[%f]\n",i,j,iarr[i][j]);
				j++;
			}
			j=0;
			i++;
		}
		else if (i == L-q-1){
			while(j<L+L){
				if (j==0){
					iarr[i][j]=1;
					//printf("iarr[%d][%d]=[%f]\n",i,j,iarr[i][j]);
					j++;
				}
				else {
			    	iarr[i][j]=0;
					//printf("iarr[%d][%d]=[%f]\n",i,j,iarr[i][j]);
					j++;				
				}
			}
			j=0;
			i++;
		}
		
		else if (i>L-q){
			//printf("i=%d\n",i);
			while (j<L+L){
				
				iarr[i][j] = power(i-L+q+1,j) *(1./factorial(j));
				//printf("iarr[%d][%d]=[%f]\n",i,j,iarr[i][j]);
				j++;
			}
			j=0;
			i++;
		}
			
	}	
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
//Soving it!


	
	float garr[L][2*L];
//chang iarr into right format for GJ array,garr
	//printf("\n\n");
	for (i=0;i!=L;i++){
		for (j=0;j!=L;j++){
			garr[i][j]=iarr[j][i];
			//printf("garr[%d][%d]=%f  ",i,j,garr[i][j]);
		}
		//printf("\n");	
	}
	//printf("\n\n");	
//expand 0
	for (i=0;i!=L;i++){
		for (j=0;j!=L;j++){
			garr[i][j+L]=0;
			//printf("garr[%d][%d]=%f  ",i,j+L,garr[i][j+L]);
		}
		//printf("\n");	
	}
	//printf("\n\n");
//add 1 	
	for (i=0;i!=L;i++){
		for (j=0;j!=L;j++){
			if (i+L==j+L){
				garr[i][j+L]=1;
			}
			//printf("garr[%d][%d]=%f  ",i,j+L,garr[i][j+L]);
		}
		//printf("\n");	
	}
	//printf("\n\n");
//print to check garr[L][2L]	
	for (i=0;i!=L;i++){
		for (j=0;j!=2*L;j++){

			//printf("garr[%d][%d]=%1.2f  ",i,j,garr[i][j]);
		}
		//printf("\n");	
	}
	//printf("\n\n");	
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
//solve GJ

double m;
int k;
for(i=0;i<L-1;i++){
	for(j=i+1;j<L;j++){
		m=garr[j][i]/garr[i][i];
		for(k=i;k<L*2;k++)
			garr[j][k]-=m*garr[i][k];
	}
}

for(i=L-1;i>0;i--){
	for(j=i-1;j>=0;j--){
		m=garr[j][i]/garr[i][i];
		for(k=i;k<L*2;k++)
			garr[j][k]-=m*garr[i][k];
	}
}

for(i=0;i<L;i++){
	m=garr[i][i];
	for(j=0;j<L*2;j++)
		garr[i][j]/=m;
}

//printf("inverse array as below\n");

for(i=0;i<L;i++){
	//for(j=L;j<L*2;j++)
		//printf("garr[%d][%d]=%.2f  ",i,j,garr[i][j]);
	//printf("\n");
	
}
//GJ solved
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////	

////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////	
//solve the coefficient
	float rvec[L];
	for (i=0;i!=L;i++){
		rvec[i]=0;
	}
	rvec[n]=1;
	float svec[L];
	
	for (i=0;i!=L;i++){
		svec[i]=0;
	}
	
	for (i=0;i!=L;i++){
		for (j=0;j!=L;j++){
			svec[i]=svec[i]+garr[i][j+L]*rvec[j];
		}
	}	
	printf("\n"); 
	printf("The coefficient a is %f\n", svec[0]);
	printf(",and the coefficient b is %f\n", svec[1]);
	printf(",and the coefficient c is %f\n", svec[2]);
	printf(",and the coefficient d is %f\n", svec[3]);
	printf(",and the coefficient e is %f\n", svec[4]);
	if (L>5){
		printf("and the following are ");
		for (i=5;i!=L-1;i++){
			printf(",the %dth coefficient, %f\n",i ,svec[i]);
		}
		printf(",the %dth coefficient, %f.\n",L-1, svec[L-1]);
	}

	printf("\n");
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////	

////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////	
//calculate leading error
	float evec[L+L];
	for (i=0;i!=L+L;i++){
		evec[i]=0;
	}	
	for (j=0;j!=L+3;j++){
		for (i=0;i!=L;i++){
			evec[j]+=svec[i]*iarr[i][j];
		}
		//printf("the %dth power error=%f\n",j,evec[j]);
	}
	for (i=L;i!=L+L;i++){
		if (evec[i]!=0){
			if (evec[i]<-(1)*(10e-8) || evec[i]>10e-8){
				//printf ("the leading error term is %dth power and the coefficient is %f.\n\n\n",i,evec[i]);
				printf ("The value r in (3) is %d.\n\n",i-n);
				return 0;
			}
		}
	}	

//	
	return 0;
}



////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////
//my function
 
int factorial(int n)
{
    if (n == 0 || n == 1) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}

int power(int a, int b)
{
	int i=0;
	int n=1;
	for (i=0;i!=b;i++){
		n=n*a;
	}
	return n;
}
////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////