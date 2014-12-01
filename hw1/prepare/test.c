#include <stdio.h>

int main(void){
int i,j,k,n;
double a[100][100]={0},m;

printf("n=");
scanf("%d",&n);

for(i=0;i<n;i++){
for(j=0;j<n;j++){
printf("(%d)X%d=",i+1,j+1);
scanf("%lf",&a[i][j]);
}
}

for(i=0;i<n;i++)
a[i][n+i]=1;

for(i=0;i<n-1;i++){
for(j=i+1;j<n;j++){
m=a[j][i]/a[i][i];
for(k=i;k<n*2;k++)
a[j][k]-=m*a[i][k];
}
}

for(i=n-1;i>0;i--){
for(j=i-1;j>=0;j--){
m=a[j][i]/a[i][i];
for(k=i;k<n*2;k++)
a[j][k]-=m*a[i][k];
}
}

for(i=0;i<n;i++){
m=a[i][i];
for(j=0;j<n*2;j++)
a[i][j]/=m;
}

for(i=0;i<n;i++){
for(j=n;j<n*2;j++)
printf("%.2f\t",a[i][j]);
printf("\n");
}

//getch();
return 0;
}

