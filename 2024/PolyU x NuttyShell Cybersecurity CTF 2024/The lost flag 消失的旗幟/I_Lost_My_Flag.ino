#include <LiquidCrystal.h>

// LCD1602 HD44780 Datasheet: https://www.sparkfun.com/datasheets/LCD/HD44780.pdf
// ESP32-WROOM-32 Module Pinout: https://www.upesy.com/cdn/shop/products/upesy-esp32-wroom-low-power-devkit-pinout.png?v=1679563719&width=1100
const int LCDPin_RS = 19; // ESP32 GPIO 19 -> Register Select Pin
const int LCDPin_EN = 18; // ESP32 GPIO 18 -> HD44780 Enable Pin
const int LCDPin_D4 = 33; // ESP32 GPIO 33 -> HD44780 DB4
const int LCDPin_D5 = 25; // ESP32 GPIO 33 -> HD44780 DB5
const int LCDPin_D6 = 26; // ESP32 GPIO 33 -> HD44780 DB6
const int LCDPin_D7 = 27; // ESP32 GPIO 33 -> HD44780 DB7

char flag[] = "PUCTF24{SecretD4???????????????????????}"; // OMG Parts of my flag were lost!
// For the LOLs, I am not using Ardunio's LCD Library, but create one myself
// :)
// The HD44780 DDRAM can hold 40 x 2 lines of data.
// For a 1602 Display, only the first 16 bytes are displayed for each line.
// But data are still data, right? Can you recover the flag?

// Write 4-bits to data pin
void writeDataPin(uint8_t byte) {
  // Write lower 4 bits of `byte` to DB4-DB7
  // Very dumb way to do this, but I just want to make sure it's easy to understand
  if((byte & 0x08) == 0x08) { digitalWrite(LCDPin_D7, HIGH); }else{ digitalWrite(LCDPin_D7, LOW); }
  if((byte & 0x04) == 0x04) { digitalWrite(LCDPin_D6, HIGH); }else{ digitalWrite(LCDPin_D6, LOW); }
  if((byte & 0x02) == 0x02) { digitalWrite(LCDPin_D5, HIGH); }else{ digitalWrite(LCDPin_D5, LOW); }
  if((byte & 0x01) == 0x01) { digitalWrite(LCDPin_D4, HIGH); }else{ digitalWrite(LCDPin_D4, LOW); }
}

// Sends command to the LCD
void lcdCmd(uint8_t cmd) {
  // We are in 4-bits data mode
  // So the first 4-bits (higher nibble) will be sent
  // Then the low 4-bits (lower nibble) will be sent

  writeDataPin(((cmd & 0xF0) >> 4)); // First 4-bits
  digitalWrite(LCDPin_RS, LOW); // Selecting "Command" Register
  delay(1);
  // Generate High-to-low pulse at EN to latch data into the HD44780
  digitalWrite(LCDPin_EN, HIGH);
  delay(3);
  digitalWrite(LCDPin_EN, LOW); // Generate High-to-low pulse at EN to latch data into the HD44780
  delay(3);

  writeDataPin((cmd & 0x0F)); // Remaining 4-bits
  delay(1);
  // Generate High-to-low pulse at EN to latch data into the HD44780
  digitalWrite(LCDPin_EN, HIGH);
  delay(3);
  digitalWrite(LCDPin_EN, LOW); // Generate High-to-low pulse at EN to latch data into the HD44780
  delay(3);
}

// Sends data to the LCD
void lcdData(uint8_t data) {
  // We are in 4-bits data mode
  // So the first 4-bits (higher nibble) will be sent
  // Then the low 4-bits (lower nibble) will be sent

  writeDataPin(((data & 0xF0) >> 4)); // First 4-bits
  digitalWrite(LCDPin_RS, HIGH); // Selecting "Data" Register
  delay(1);
  // Generate High-to-low pulse at EN to latch data into the HD44780
  digitalWrite(LCDPin_EN, HIGH);
  delay(3);
  digitalWrite(LCDPin_EN, LOW); // Generate High-to-low pulse at EN to latch data into the HD44780
  delay(3);

  writeDataPin((data & 0x0F)); // Remaining 4-bits
  delay(1);
  // Generate High-to-low pulse at EN to latch data into the HD44780
  digitalWrite(LCDPin_EN, HIGH);
  delay(3);
  digitalWrite(LCDPin_EN, LOW); // Generate High-to-low pulse at EN to latch data into the HD44780
  delay(3);
}

// Sends string data to LCD
void lcdWriteString(char *str) {
  char *ptr = str;
  while(*ptr != 0x00) lcdData(*ptr++);
}

void setup() {
  pinMode(LCDPin_RS, OUTPUT);
  pinMode(LCDPin_EN, OUTPUT);
  pinMode(LCDPin_D4, OUTPUT);
  pinMode(LCDPin_D5, OUTPUT);
  pinMode(LCDPin_D6, OUTPUT);
  pinMode(LCDPin_D7, OUTPUT);
  digitalWrite(LCDPin_EN, LOW);
  digitalWrite(LCDPin_RS, LOW);

  lcdCmd(0x02); // HD44780 Datasheet Figure 11, "Function Set", DL=0 for 4-bits interface mode
  lcdCmd(0x28); // "Function Set", DL=0, N=1, F=0
  lcdCmd(0x0C); // "Display on/off control", D=1, C=0, B=0 
  lcdCmd(0x06); // "Entry Mode Set", I/D=1, S=0
  lcdCmd(0x01); // "Clear display"
  lcdCmd(0x80); // "Set DDRAM address" to 0x00
  
  delay(50);

  lcdWriteString("THE LOST FLAG \xEF");
  lcdCmd(0x80 | 0x40); // "Set DDRAM address" to 0x40 (second line). See "Set DDRAM Address" section in the datasheet.
  lcdWriteString(flag);

  while(1);
}

void loop() {
  ;
}
