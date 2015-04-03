const int m1=9;
const int d1=8;
const int m2=10;
const int d2=12;
const int TIME=500;
void setup(){
  
  pinMode(d1,OUTPUT);
  pinMode(m1,OUTPUT);
  pinMode(d2,OUTPUT);
  pinMode(m2,OUTPUT);

  
}
void loop(){
  
  turnleft();
  delay(10);
}

void fwd(){
  digitalWrite(d1,HIGH);
  digitalWrite(d2,HIGH);
  analogWrite(m1,255);
  analogWrite(m2,255);
  delay(250);
}

void bwd(){
  digitalWrite(d1,LOW);
  digitalWrite(d2,LOW);
  analogWrite(m1,75);
  analogWrite(m2,75);
  delay(250);
  }
  
  void stp(){
   digitalWrite(m1,0);
   digitalWrite(m2,0);
   delay(250);
  }
  
  void rotleft(){
  digitalWrite(d1,LOW);
  digitalWrite(d2,HIGH);
  analogWrite(m1,200);
  analogWrite(m2,200);
  delay(250);
  }
  
  void rotright(){
  digitalWrite(d1,HIGH);
  digitalWrite(d2,LOW);
  analogWrite(m1,200);
  analogWrite(m2,200);
  }
  
  void turnleft(){
  digitalWrite(d1,HIGH);
  digitalWrite(d2,HIGH);
  analogWrite(m1,75);
  analogWrite(m2,255);
  delay(250);
  }
  
