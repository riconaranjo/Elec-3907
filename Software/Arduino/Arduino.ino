/* This code allows for synchronized reading from ultrasound sensors.
 * There is an artifical delay of 20 ms between each sensor reading to
 * avoid interference, with each 20 reading per sensor being averaged.
 * This means each average result of three sensors takes about 1.2 s
 * (3*20*20 = 1200 ms).
 * 
 * Any data spikes are automatically removed if they are x2 bigger
 * than the largest value before it.
 */

#define trigPin_A1 -1
#define echoPin_A1 2
#define trigPin_A2 4
#define echoPin_A2 3
#define trigPin_A3 9
#define echoPin_A3 7

#define trigPin_B1 13
#define echoPin_B1 12
#define trigPin_B2 6
#define echoPin_B2 5
#define trigPin_B3 11
#define echoPin_B3 10

// total delay per sensor should be about 60 milliseconds
// as more sensors are added, this delay can be reduced
// cycle time = sample_size * sensor_delay * {number of sensors}
const long sensor_delay = 15;       // in milliseconds [delay between sensors, avoids interference] = 60 / [# of sensors]
const long conversion_factor = 58;  // converts to centimetres
const int sample_size = 10;         // how many values are averaged per cycle

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
  // pinMode(trigPin_A1, OUTPUT);
  pinMode(trigPin_A2, OUTPUT);
  pinMode(trigPin_A3, OUTPUT);
  pinMode(trigPin_B1, OUTPUT);
  pinMode(trigPin_B2, OUTPUT);
  pinMode(trigPin_B3, OUTPUT);
  pinMode(A0, OUTPUT);
  
  pinMode(echoPin_A1, INPUT);
  pinMode(echoPin_A2, INPUT);
  pinMode(echoPin_A3, INPUT);
  pinMode(echoPin_B1, INPUT);
  pinMode(echoPin_B2, INPUT);
  pinMode(echoPin_B3, INPUT);
 
  Serial.begin(9600);
  // Serial.println("---Setup Complete---");
}

void loop() {
  // Serial.println("~ ~ ~ loop ~ ~ ~");
  listen_sensors();

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

void triggerPulse(int trigPin) {
  if(trigPin == -1) {
    digitalWrite(A0, LOW);
    delayMicroseconds(20);
    digitalWrite(A0, HIGH);
    delayMicroseconds(50);
    digitalWrite(A0, LOW);
    return;
  }
  digitalWrite(trigPin, LOW);
  delayMicroseconds(20);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(50);
  digitalWrite(trigPin, LOW);
}

long echo(int echoPin) {
  long duration = pulseIn(echoPin, HIGH);
  long distance = duration / conversion_factor;  // convert to cm
  return distance;
}

void listen_sensors() {
  distances_A1[count] = listen_sensor(trigPin_A1, echoPin_A1);
  distances_A2[count] = listen_sensor(trigPin_A2, echoPin_A2);
  distances_A3[count] = listen_sensor(trigPin_A3, echoPin_A3);
  distances_B1[count] = listen_sensor(trigPin_B1, echoPin_B1);
  distances_B2[count] = listen_sensor(trigPin_B2, echoPin_B2);
  distances_B3[count] = listen_sensor(trigPin_B3, echoPin_B3);
}

long listen_sensor(int trigPin, int echoPin) {
  triggerPulse(trigPin);
  long distance = echo(echoPin);
  delay(sensor_delay);
  return distance;
}

// void listen_sensor_1() {
//   triggerPulse(trigPin_A1);
//   distances_1[count] = echo(1);
//   delay(sensor_delay);
// }

// void listen_sensor_2() {
//   triggerPulse(trigPin_A2);
//   distances_2[count] = echo(2);
//   delay(sensor_delay);
// }

// void listen_sensor_3() {
//   triggerPulse(trigPin_A3);
//   distances_3[count] = echo(3);
//   delay(sensor_delay);
// }

void average_distances() {
  long avgSensor_A1 = avgSensorValues("A1");
  long avgSensor_A2 = avgSensorValues("A2");
  long avgSensor_A3 = avgSensorValues("A3");
  long avgSensor_B1 = avgSensorValues("B1");
  long avgSensor_B2 = avgSensorValues("B2");
  long avgSensor_B3 = avgSensorValues("B3");

  //Serial.print("average sensor A1: ");
  Serial.print(avgSensor_A1);
  Serial.print(" ");
  //Serial.print("average sensor A2: ");
  Serial.print(avgSensor_A2);
  Serial.print(" ");  
  //Serial.print("average sensor A3: ");
  Serial.print(avgSensor_A3);
  Serial.print(" ");
  //Serial.print("average sensor B1: ");
  Serial.print(avgSensor_B1);
  Serial.print(" ");
  //Serial.print("average sensor B2: ");
  Serial.print(avgSensor_B2);
  Serial.print(" ");  
  //Serial.print("average sensor B3: ");
  Serial.print(avgSensor_B3);
  Serial.print("\n");
}

long avgSensorValues(String sensor) {
  long *arr;

  if(sensor == "A1") {
    arr = distances_A1;
  }
  else if(sensor == "A2") {
    arr = distances_A2;
  }
  else if(sensor == "A3") {
    arr = distances_A3;
  }
  else if(sensor == "B1") {
    arr = distances_B1;
  }
  else if(sensor == "B2") {
    arr = distances_B2;
  }
  else if(sensor == "B3") {
    arr = distances_B3;
  }
  else {
    Serial.println("invalid index in avgSensorValues function");
  }  
  
  // sort distances array
  qsort(arr, sample_size, sizeof(arr[0]), sort_asc);

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
int sort_asc(const void *x, const void *y) {
  // Need to cast the (void pointer) to (int pointer)
  int a = *((int *)x);
  int b = *((int *)y);
  // return a > b ? 1 : (a < b ? -1 : 0);
  // A simpler, probably faster way:
  return a - b;
}
