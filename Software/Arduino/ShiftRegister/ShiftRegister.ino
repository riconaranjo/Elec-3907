/* This code allows for synchronized reading from ultrasound sensors.
 * There is an artifical delay of 20 ms between each sensor reading to
 * avoid interference, with each 20 reading per sensor being averaged.
 * This means each average result of three sensors takes about 1.2 s
 * (3*20*20 = 1200 ms).
 * 
 * Any data spikes are automatically removed if they are x2 bigger
 * than the largest value before it.
 */

// shift register pins
#define latchPin = 5;
#define clockPin = 6;
#define dataPin = 4;

// #define trigPin_1 12
// #define trigPin_2 11
// #define trigPin_3 10
// #define echoPin_1 9
// #define echoPin_2 8
// #define echoPin_3 7

// total delay per sensor should be about 60 milliseconds
// as more sensors are added, this dealy can be reduced
const long sensor_delay = 20; // in milliseonds [delay between sensors, avoids interference]
const long conversion_factor = 58;
const int sample_size = 20;     // how many values are averaged per cycle
// cycle time = sample_size * sensor_delay * {number of sensors}

// store values in arrays of <sample_size> to be averaged
long distances_1[sample_size];
long distances_2[sample_size];
long distances_3[sample_size];

// this is used to see which is the current index in the distances arrays
int count = 0;

void setup() {
  Serial.println("---Setup Start---");
  
  pintMode(latchPin,OUTPUT);
  pintMode(clockPin,OUTPUT);
  pintMode(dataPin,OUTPUT);

  // pinMode(trigPin_1, OUTPUT);
  // pinMode(trigPin_2, OUTPUT);
  // pinMode(trigPin_3, OUTPUT);
  
  // pinMode(echoPin_1, INPUT);
  // pinMode(echoPin_2, INPUT);
  // pinMode(echoPin_3, INPUT);
 
  Serial.begin(9600);
  Serial.println("---Setup Complete---");
}

void loop() {
  listen_sensor_1();
  listen_sensor_2();
  listen_sensor_3();

  // print_sensor_1();
  // print_sensor_2();
  // print_sensor_3();

  // increment count from 0 to sample_size-1
  // will reset to 0 on roll-over
  // get averages when arrays are full [i.e. right at roll-over]
  count = (count+1)%sample_size;
  if(count == 0) {
    average_distances();
  }
}

void print_sensor_1() {
  Serial.print("print 1: ");
  Serial.println(distances_1[count]);
}

void print_sensor_2() {
  Serial.print("print 2: ");
  Serial.println(distances_2[count]);
}

void print_sensor_3() {
  Serial.print("print 3: ");
  Serial.println(distances_3[count]);
}

void triggerPulse(int index) {
  int pin;

  if(index == 1) {
    pin = trigPin_1;
  }
  else if(index == 2) {
    pin = trigPin_2;
  }
  else if(index == 3) {
    pin = trigPin_3;
  }
  else {
    Serial.println("Invalid trigger index");
  }
  
  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  digitalWrite(pin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pin, LOW);
}

long echo(int index) {
  long duration;
  if(index == 1) {
     duration = pulseIn(echoPin_1, HIGH);
  }
  else if(index == 2) {
     duration = pulseIn(echoPin_2, HIGH);
  }
  else if(index == 3) {
     duration = pulseIn(echoPin_3, HIGH);
  }
  else {
      Serial.println("Invalid echo index");  
  }

  long distance = duration/conversion_factor;  // convert to cm
  return distance;
}

void listen_sensor_1() {
  triggerPulse(1);
  distances_1[count] = echo(1);
  delay(sensor_delay);
}

void listen_sensor_2() {
  triggerPulse(2);
  distances_2[count] = echo(2);
  delay(sensor_delay);
}

void listen_sensor_3() {
  triggerPulse(3);
  distances_3[count] = echo(3);
  delay(sensor_delay);
}

void average_distances() {
  long avg_sensor_1 = avgSensorValues(0);
  long avg_sensor_2 = avgSensorValues(1);
  long avg_sensor_3 = avgSensorValues(2);

  //Serial.print("average sensor 1: ");
  Serial.print(avg_sensor_1);
  Serial.print(" ");
  //Serial.print("average sensor 2: ");
  Serial.print(avg_sensor_2);
  Serial.print(" ");  
  //Serial.print("average sensor 3: ");
  Serial.print(avg_sensor_3);
  Serial.print("\n");
}

long avgSensorValues(int sensor) {
  long *arr;

  if(sensor == 0) {
    arr = distances_1;
  }
  else if(sensor == 1) {
    arr = distances_2;
  }
  else if(sensor == 2) {
    arr = distances_3;
  }
  else {
    Serial.println("invalid index in avgSensorValues");
  }  
  
  // sort distances array
  qsort(arr, sample_size, sizeof(arr[0]), sort_desc);

  // print array
  // Serial.print("after { ");
  // for(int i = 0; i < sample_size; i++) {
  //   Serial.print(arr[i]);
  //   Serial.print(" ");
  // }
  // Serial.print("}\n");

  // find average of sorted sample array
  long sum = 0;
  long last_value = arr[0];
  int c = 0;
  for(int i = 0; i < sample_size; i++) {
    // exit loop if the numbers jump by a factor of 2
    if(arr[i] > 2*last_value && last_value > 0){
      break;
    }
    last_value = arr[i];
    sum += arr[i];
    c++;
  }
  long avg = sum / c;
  return avg;
}

// qsort requires you to create a sort function
int sort_desc(const void *x, const void *y) {
  // Need to cast the (void pointer) to (int pointer)
  int a = *((int*)x);
  int b = *((int *)y);
  // return a > b ? 1 : (a < b ? -1 : 0);
  // A simpler, probably faster way:
  return a - b;
}

void updateShiftRegister(int triggerPin)
{

  
  digitalWrite(latchPin, LOW);


  digitalWrite(pin, LOW);
  delayMicroseconds(2);
  digitalWrite(pin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pin, LOW);


   
  shiftOut(dataPin, clockPin, LSBFIRST, triggerPin);
  digitalWrite(latchPin, HIGH);
}