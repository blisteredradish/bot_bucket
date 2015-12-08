#include <fix_fft.h>

int led[]={3,6,9};
int x=0;
char im[128],data[128];
char data_avgs[14];
int i=0,val;

#define AUDIOPIN A0


void setup(){
  for(int i=0;i<3;i++){
  pinMode(led[i],OUTPUT);
  }
  Serial.begin(9600);  
}

void loop(){
  for(i=0;i<128;i++){
    val=analogRead(AUDIOPIN);
    data[i]=val;
    im[i]=0;
  }
  
  fix_fft(data,im,5,0);
  for (i=0;i<64;i++){
    data[i]=sqrt(data[i]*data[i]+im[i]*im[i]);
  }
  
  for (i=0;i<14;i++){
    data_avgs[i]=data[i*4]+data[i*4+1]+data[i*4+2]+data[i*4+3];
    data_avgs[i]=map(data_avgs[i],0,30,0,6);
  }
  int value = data_avgs[0];
 ledArray(value); 
  
}

void ledArray(int input){
  if (input >5){
    for (int i=0; i<3;i++)
    {
      digitalWrite(led[i],HIGH);
    }
    for (int i=3; i<3;i++)
    {
      digitalWrite(led[i],LOW);
    } 
  }
  else if (input > 3)
  {
    for (int i=0;i<3;i++)
    {
      digitalWrite(led[i],HIGH);
    }
    for (int i=2;i<3;i++)
    {
      digitalWrite(led[i],LOW);
    }
  }
  else if (input >1)
  {
    for (int i=0;i<3;i++)
    {
      digitalWrite(led[i],HIGH);
    }
    for (int i=1;i<3;i++)
    {
      digitalWrite(led[i],LOW);
    }
  }
      
  else
  {
    for (int i=0;i<3;i++)
    {
      digitalWrite(led[i],LOW);
    }
  }
}
