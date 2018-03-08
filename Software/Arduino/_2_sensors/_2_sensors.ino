

#define trigPin 7
#define trigPin2 4
#define echoPin2 5
#define echoPin 6
#define led 13
#define led2 12
#define led3 11
#define led4 10
#define led5 9
#define led6 8





void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(echoPin2, INPUT);
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  
 
}

void firstsensor(){ // This function is for first sensor.
  long duration, distance;
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  digitalWrite (trigPin, HIGH);
  delayMicroseconds (10);
  digitalWrite (trigPin, LOW);
  duration = pulseIn (echoPin, HIGH);
  distance = (duration/2) / 29.1;

      Serial.print("1st Sensor: ");
      Serial.print(distance);  
      Serial.print("cm    ");
  
  
  
  if (distance < 30) {  // Change the number for long or short distances.
    digitalWrite (led, HIGH);
  } else {
    digitalWrite (led, LOW);
  }    

 /* if (distance <= 30) {
    digitalWrite(led, HIGH);
}
  else {
    digitalWrite(led,LOW);
  }
  if (distance < 25) {
      digitalWrite(led2, HIGH);
     
}
  else {
      digitalWrite(led2, LOW);
  }
  if (distance < 20) {
      digitalWrite(led3, HIGH);
      
} 
  else {
    digitalWrite(led3, LOW);
  }
  if (distance < 15) {
    digitalWrite(led4, HIGH);
    
}
  else {
    digitalWrite(led4,LOW);
  }
  if (distance < 10) {
    digitalWrite(led5, HIGH);
    
}
  else {
    digitalWrite(led5,LOW);
  }
  if (distance < 5) {
    digitalWrite(led6, HIGH);
    
}
  else {
    digitalWrite(led6,LOW);
  }*/
}
 void secondsensor(){ // This function is for second sensor.
    int duration2, distance2;
    digitalWrite(trigPin2, LOW); 
    delayMicroseconds(2);
    digitalWrite (trigPin2, HIGH);
    delayMicroseconds (10);
    digitalWrite (trigPin2, LOW);
    duration2 = pulseIn (echoPin2, HIGH);
    distance2 = (duration2/2) / 29.1;
  
      Serial.print("2nd Sensor: "); 
      Serial.print(distance2);  
      Serial.print("cm    ");
       if (distance2 <30) {  // Change the number for long or short distances.
      digitalWrite (led2, HIGH);
    }
 else {
      digitalWrite (led2, LOW);
    }
     
 /*if (distance2 <= 30) {
    digitalWrite(led6, HIGH);
}
  else {
    digitalWrite(led,LOW);
  }
  if (distance2 < 25) {
      digitalWrite(led5, HIGH);
     
}
  else {
      digitalWrite(led5, LOW);
  }
  if (distance2 < 20) {
      digitalWrite(led4, HIGH);
      
} 
  else {
    digitalWrite(led4, LOW);
  }
  if (distance2 < 15) {
    digitalWrite(led3, HIGH);
    
}
  else {
    digitalWrite(led3,LOW);
  }
  if (distance2 < 10) {
    digitalWrite(led2, HIGH);
    
}
  else {
    digitalWrite(led2,LOW);
  }
  if (distance2 < 5) {
    digitalWrite(led, HIGH);
    
}
  else {
    digitalWrite(led,LOW);
  }
  */
 }
void loop() {
  Serial.println("\n");
  firstsensor();
  secondsensor();
  delay(500);
}



