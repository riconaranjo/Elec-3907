/* This code allows for synchronized reading from ultrasound sensors.
 * There is an artifical delay of 20 ms between each sensor reading to
 * avoid interference, with each 20 reading per sensor being averaged.
 * This means each average result of three sensors takes about 1.2 s
 * (3*20*20 = 1200 ms).
 * 
 * Any data spikes are automatically removed if they are x2 bigger
 * than the largest value before it.
 */

#define trigPin_A1 13
#define trigPin_A2 12
#define trigPin_A3 11
#define trigPin_B1 10
#define trigPin_B2 9
#define trigPin_B3 8
#define echoPin_A1 7
#define echoPin_A2 6
#define echoPin_A3 5
#define echoPin_B1 4
#define echoPin_B2 3
#define echoPin_B3 2

// total delay per sensor should be about 60 milliseconds
// as more sensors are added, this dealy can be reduced
const long sensor_delay = 10; // in milliseonds [delay between sensors, avoids interference]
const long conversion_factor = 58;
const int sample_size = 20;     // how many values are averaged per cycle
// cycle time = sample_size * sensor_delay * {number of sensors}

// store values in arrays of <sample_size> to be averaged
long distances_A1[sample_size];
long distances_A2[sample_size];
long distances_A3[sample_size];
long distances_B1[sample_size];
long distances_B2[sample_size];
long distances_B3[sample_size];

// this is used to see which is the current index in the distances arrays
int count = 0;

void setup() {
  Serial.println("---Setup Start---");
  pinMode(trigPin_A1, OUTPUT);
  pinMode(trigPin_A2, OUTPUT);
  pinMode(trigPin_A3, OUTPUT);
  pinMode(trigPin_B1, OUTPUT);
  pinMode(trigPin_B2, OUTPUT);
  pinMode(trigPin_B3, OUTPUT);
  
  pinMode(echoPin_A1, INPUT);
  pinMode(echoPin_A2, INPUT);
  pinMode(echoPin_A3, INPUT);
  pinMode(echoPin_B1, INPUT);
  pinMode(echoPin_B2, INPUT);
  pinMode(echoPin_B3, INPUT);
 
  Serial.begin(9600);
  Serial.println("---Setup Complete---");
}

void loop() {
  // Serial.println("---loop---");
  listen_sensor_A1();
  listen_sensor_A2();
  listen_sensor_A3();
  listen_sensor_B1();
  listen_sensor_B2();
  listen_sensor_B3();

  // print_sensor_A1();
  // print_sensor_A2();
  // print_sensor_A3();
  // print_sensor_B1();
  // print_sensor_B2();
  // print_sensor_B3();

  // increment count from 0 to sample_size-1
  // will reset to 0 on roll-over
  // get averages when arrays are full [i.e. right at roll-over]
  count = (count+1)%sample_size;
  if(count == 0) {
     average_distances();
  }
}

void print_sensor_A1() {
  Serial.print("print A1: ");
  Serial.println(distances_A1[count]);
}

void print_sensor_A2() {
  Serial.print("print A2: ");
  Serial.println(distances_A2[count]);
}

void print_sensor_A3() {
  Serial.print("print A3: ");
  Serial.println(distances_A3[count]);
}

void print_sensor_B1() {
  Serial.print("print B1: ");
  Serial.println(distances_B1[count]);
}

void print_sensor_B2() {
  Serial.print("print B2: ");
  Serial.println(distances_B2[count]);
}

void print_sensor_B3() {
  Serial.print("print B3: ");
  Serial.println(distances_B3[count]);
}

void triggerPulse(int index) {
  int pin;

  if(index == 1) {
    pin = trigPin_A1;
  }
  else if(index == 2) {
    pin = trigPin_A2;
  }
  else if(index == 3) {
    pin = trigPin_A3;
  }
  else if(index == 4) {
    pin = trigPin_B1;
  }
  else if(index == 5) {
    pin = trigPin_B2;
  }
  else if(index == 6) {
    pin = trigPin_B3;
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
     duration = pulseIn(echoPin_A1, HIGH);
  }
  else if(index == 2) {
     duration = pulseIn(echoPin_A2, HIGH);
  }
  else if(index == 3) {
     duration = pulseIn(echoPin_A3, HIGH);
  }
  else if(index == 4) {
     duration = pulseIn(echoPin_B1, HIGH);
  }
  else if(index == 5) {
     duration = pulseIn(echoPin_B2, HIGH);
  }
  else if(index == 6) {
     duration = pulseIn(echoPin_B3, HIGH);
  }
  else {
      Serial.println("Invalid echo index");  
  }

  long distance = duration/conversion_factor;  // convert to cm
  return distance;
}

void listen_sensor_A1() {
  triggerPulse(1);
  distances_A1[count] = echo(1);
  delay(sensor_delay);
}

void listen_sensor_A2() {
  triggerPulse(2);
  distances_A2[count] = echo(2);
  delay(sensor_delay);
}

void listen_sensor_A3() {
  triggerPulse(3);
  distances_A3[count] = echo(3);
  delay(sensor_delay);
}
void listen_sensor_B1() {
  triggerPulse(4);
  distances_B1[count] = echo(4);
  delay(sensor_delay);
}

void listen_sensor_B2() {
  triggerPulse(5);
  distances_B2[count] = echo(5);
  delay(sensor_delay);
}

void listen_sensor_B3() {
  triggerPulse(6);
  distances_B3[count] = echo(6);
  delay(sensor_delay);
}


void average_distances() {
  long avg_sensor_A1 = avgSensorValues(0);
  long avg_sensor_A2 = avgSensorValues(1);
  long avg_sensor_A3 = avgSensorValues(2);
  long avg_sensor_B1 = avgSensorValues(3);
  long avg_sensor_B2 = avgSensorValues(4);
  long avg_sensor_B3 = avgSensorValues(5);

  //Serial.print("average sensor A1: ");
  Serial.print(avg_sensor_A1);
  Serial.print(" ");
  //Serial.print("average sensor A2: ");
  Serial.print(avg_sensor_A2);
  Serial.print(" ");  
  //Serial.print("average sensor A3: ");
  Serial.print(avg_sensor_A3);
  Serial.print(" ");
  //Serial.print("average sensor B1: ");
  Serial.print(avg_sensor_B1);
  Serial.print(" ");
  //Serial.print("average sensor B2: ");
  Serial.print(avg_sensor_B2);
  Serial.print(" ");  
  //Serial.print("average sensor B3: ");
  Serial.print(avg_sensor_B3);
  Serial.print("\n");
}

long avgSensorValues(int sensor) {
  long *arr;

  if(sensor == 0) {
    arr = distances_A1;
  }
  else if(sensor == 1) {
    arr = distances_A2;
  }
  else if(sensor == 2) {
    arr = distances_A3;
  }
  else if(sensor == 3) {
    arr = distances_B1;
  }
  else if(sensor == 4) {
    arr = distances_B2;
  }
  else if(sensor == 5) {
    arr = distances_B3;
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