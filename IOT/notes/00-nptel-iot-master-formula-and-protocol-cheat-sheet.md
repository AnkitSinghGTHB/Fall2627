# 📑 NPTEL IoT: Master Formulas, Protocols & Hardware Cheat Sheet (1-Page)

> **Course**: Introduction to Internet of Things (IIT Kharagpur — Prof. Sudip Misra)  
> **Exam Date**: Tuesday, October 27, 2026 (08:00 AM)  
> **Format**: Computer-Based Test (MCQ / MSQ) | **Marks**: 100 Marks  
> **Keep this sheet open for instant protocol lookup, pinouts, formulas, and high-frequency exam traps!**

---

## 1. IoT Communication Protocols Master Matrix

| Protocol | Transport | Port | Architecture | Message Header | Key Characteristics & Exam Triggers |
|:---|:---:|:---:|:---:|:---:|:---|
| **MQTT** | **TCP** | **1883** (no SSL)<br>**8883** (TLS) | **Pub / Sub** (Broker-based) | **2 Bytes** (Fixed) | • Best for constrained networks with intermittent connectivity.<br>• Topic routing with wildcards: `+` (single-level), `#` (multi-level).<br>• **QoS 0**: At most once (no ack).<br>• **QoS 1**: At least once (PUBACK, may duplicate).<br>• **QoS 2**: Exactly once (4-way handshake: PUBLISH $\to$ PUBREC $\to$ PUBREL $\to$ PUBCOMP).<br>• **SMQTT**: Secure MQTT using lightweight encryption. |
| **CoAP** | **UDP** | **5683** (no DTLS)<br>**5684** (DTLS) | **Client / Server** (RESTful) | **4 Bytes** (Fixed) | • Binary web transfer protocol for constrained nodes.<br>• 4 Message types: **CON** (Confirmable), **NON** (Non-confirmable), **ACK** (Acknowledgement), **RST** (Reset).<br>• REST methods: `GET`, `POST`, `PUT`, `DELETE`.<br>• Supports **Resource Observation** (`Observe` option) and Block-wise transfers. |
| **XMPP** | **TCP** | **5222** | **Client / Server** (Decentralized) | XML Stream | • Extensible Messaging and Presence Protocol; human-to-human & M2M instant messaging; XML text-based (high overhead). |
| **AMQP** | **TCP** | **5672** | **Pub / Sub & Queuing** | Binary | • Advanced Message Queuing Protocol; enterprise-grade reliability, wire-level format, Exchanges, Queues, and Bindings. |
| **6LoWPAN** | **IPv6 over 802.15.4** | — | **Mesh / Star** | Compressed | • Adapts IPv6 (1280-byte MTU) to IEEE 802.15.4 (127-byte PHY frame).<br>• Employs header compression (stateless/stateful), fragmentation, and mesh routing (**RPL**). |
| **Zigbee** | **IEEE 802.15.4** | — | **Star, Tree, Mesh** | MAC frame | • Operates at **2.4 GHz** (global, 250 kbps), **868 MHz** (EU, 20 kbps), **915 MHz** (US, 40 kbps).<br>• Roles: **ZC** (Coordinator - exactly one), **ZR** (Router), **ZED** (End Device - sleeping/battery). |
| **Z-Wave** | **Proprietary RF** | — | **Mesh** | RF frame | • Smart home automation.<br>• Frequencies: **908.42 MHz (US)**, **868.42 MHz (Europe)**.<br>• Supports up to 232 nodes. |
| **WirelessHART** | **IEEE 802.15.4** | — | **Time-Synchronized Mesh** | Industrial | • Industrial process automation at 2.4 GHz.<br>• Uses **TDMA** and frequency hopping.<br>• ⚠️ **Exam Trap**: **Wired HART has NO Network Layer**! |
| **LoRaWAN** | **Chirp Spread Spectrum** | — | **Star-of-Stars** | RF packet | • Sub-GHz ISM bands (868 MHz EU, 915 MHz US, 865–867 MHz India).<br>• **Class A**: Lowest power, uplink-driven, 2 short downlink windows.<br>• **Class B**: Scheduled downlink receive slots via gateway beacons.<br>• **Class C**: Continuously listening, highest power, lowest downlink latency. |

---

## 2. Essential Mathematical & Geometric Formulas

### 1. Sensing Coverage vs Network Connectivity
$$\text{Condition: } r_c \ge 2 r_s$$
* If the communication radius $r_c$ of every sensor is at least **twice** the sensing radius $r_s$, then **complete sensing coverage mathematically guarantees complete network connectivity**!

### 2. ADC Resolution & Voltage Step Size
$$\text{Step Size (Resolution)} = \frac{V_{\text{ref}}}{2^n - 1} \quad \text{or} \quad \frac{V_{\text{ref}}}{2^n}$$
* For an **Arduino Uno** (10-bit ADC, $V_{\text{ref}} = 5.0\text{ V}$):
  $$\text{Resolution} = \frac{5.0}{1023} \approx 4.887\text{ mV per unit}$$
* An `analogRead()` value of $512$ corresponds to:
  $$\text{Voltage} = 512 \times \frac{5.0}{1023} \approx 2.50\text{ V}$$

### 3. Ultrasonic Distance Measurement (HC-SR04)
$$\text{Distance} = \frac{\text{Echo Time Pulse } (\mu\text{s}) \times \text{Speed of Sound}}{2} = \frac{\text{Time } (\mu\text{s}) \times 0.034\text{ cm}/\mu\text{s}}{2} = \frac{\text{Time } (\mu\text{s})}{58.2}\text{ cm}$$

---

## 3. Hardware Architecture & Programming Blueprints

### 🔌 Arduino Uno (ATmega328P) Specifications
* **Operating Voltage**: **5 V** | **Input Voltage (recommended)**: **7–12 V**
* **Clock Speed**: **16 MHz** | **Flash Memory**: 32 KB (0.5 KB bootloader) | **SRAM**: 2 KB | **EEPROM**: 1 KB
* **Digital Pins**: 14 (Pins 0 to 13)
* **PWM Pins**: **6 pins** marked with `~` $\implies$ **Pins 3, 5, 6, 9, 10, 11** (8-bit output: values $0 - 255$ via `analogWrite()`).
* **Analog Input Pins**: **6 pins** $\implies$ **A0 to A5** (10-bit resolution: values $0 - 1023$ via `analogRead()`).
* **Hardware Communication Pins**:
  * **Serial UART**: Pin 0 (`RX`), Pin 1 (`TX`)
  * **I2C**: Pin **A4 (SDA)**, Pin **A5 (SCL)**
  * **SPI**: Pin 10 (`SS`), Pin 11 (`MOSI`), Pin 12 (`MISO`), Pin 13 (`SCK`)
* **Standard Code Skeleton**:
  ```cpp
  void setup() {
    pinMode(13, OUTPUT);      // Set pin mode: INPUT, OUTPUT, INPUT_PULLUP
    Serial.begin(9600);       // Initialize UART baud rate
  }
  void loop() {
    digitalWrite(13, HIGH);   // Set 5V
    delay(1000);              // Milliseconds
    digitalWrite(13, LOW);    // Set 0V
    delay(1000);
  }
  ```

---

### 🍓 Raspberry Pi Architecture & Python Sockets
* **GPIO Header**: **40 pins** | **Logic Level**: **3.3 V** (⚠️ **NOT 5V tolerant!** Applying 5V destroys the SoC).
* **Pin Numbering Schemes**:
  * `GPIO.setmode(GPIO.BOARD)` $\implies$ Uses physical pin numbers (1 to 40).
  * `GPIO.setmode(GPIO.BCM)` $\implies$ Uses Broadcom chip channel numbers (e.g., GPIO17, GPIO27).
* **Python Network Sockets for IoT**:
  * **TCP Client/Server**: `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  * **UDP Client/Server**: `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`
* **DHT Sensor Reading**: `humidity, temperature = Adafruit_DHT.read_retry(sensor_type, pin)`

---

## 4. Architectural Paradigms & Core Concepts

### 1. Cloud vs Fog vs Edge Computing
* **Cloud Computing**: Centralized, remote mega-data centers, virtually unlimited compute/storage, **high latency**, high bandwidth demand.
* **Fog Computing**: Extends the cloud to local network edge; hierarchical; local servers, routers, and gateways compute close to nodes; **lowers latency and conserves backbone bandwidth**.
* **Edge Computing**: Directly on terminal devices or local micro-controllers; sub-millisecond reaction, preserves data privacy.

### 2. Sensor-Cloud Architecture
* **Sensor Virtualization**: Decouples physical sensor hardware from applications by creating **Virtual Sensors (VS)**.
* **Multi-Tenancy**: Allows multiple users and concurrent applications to share physical sensing infrastructure dynamically on-demand.

### 3. Software Defined Networking (SDN) in IoT
* **Separation of Concerns**: Decouples the **Control Plane** (centralized intelligence/controller) from the **Data Plane** (forwarding switches).
* **ODIN Architecture**: Light-weight SDN framework for wireless networks. The **Odin Agent** runs directly on physical Access Points (APs).
* **Mobi-Flow**: Proactive flow-rule placement mechanism to reduce handoff latency in mobile IoT networks.

### 4. Smart City Human Body Analogy
* **Sensors & Tags** $\longleftrightarrow$ **Sensory Organs** (eyes, ears, skin)
* **Digital Communication Network** $\longleftrightarrow$ **Nerves**
* **Embedded Intelligence & Analytics** $\longleftrightarrow$ **Brain**
* **Buildings, Facilities & Infrastructure** $\longleftrightarrow$ **Skeleton & Body**

### 5. Smart Grid & Metering
* **Traditional Grid vs Smart Grid**: Traditional is one-way electricity flow; Smart Grid has **bidirectional electricity AND bidirectional information flow**.
* **AMI vs AMR**:
  * **AMR (Automated Meter Reading)**: One-way meter-to-utility consumption reporting.
  * **AMI (Advanced Metering Infrastructure)**: Two-way communication between customer and utility supporting real-time pricing and remote control.
* **Demand-Side Management (DSM) Techniques**:
  * **Peak Clipping**: Reducing consumption during peak hours.
  * **Valley Filling**: Stimulating power usage during off-peak night hours.
  * **Load Shifting**: Moving heavy appliances from peak to off-peak periods.
  * **Time-of-Use (TOU) Pricing**: Charging higher rates during peak hours and lower rates off-peak.

### 6. Data Analytics & Statistical Modeling
* **Qualitative vs Quantitative Data**: Categorical data (labels, categories) is analyzed using **Qualitative analysis**; numerical measurements use Quantitative analysis.
* **Complete Statistical Model**: Occurs when the number of parameters/variables equals the maximum available degrees of freedom, fitting the training set completely.
* **ANOVA (Analysis of Variance)**: Applied to compare differences between the means of **3 or more groups** simultaneously.

---

## 5. Top 10 High-Frequency Exam Trap Questions

1. **Wired HART Network Layer?**  
   👉 **False!** Wired HART has **no network layer** (Physical, Data Link, Application only).
2. **Does complete sensing coverage always imply network connectivity?**  
   👉 **Only if $r_c \ge 2 r_s$!** If communication radius is less than $2 \times$ sensing radius, coverage does NOT guarantee connectivity.
3. **Z-Wave operating frequencies?**  
   👉 **908.42 MHz in US**, **868.42 MHz in Europe**.
4. **MQTT Topic Wildcards?**  
   👉 `+` matches **exactly one level** (e.g., `home/+/temperature`). `#` matches **all remaining levels** and must be at the end (e.g., `home/#`).
5. **Which socket type is used for fast, connectionless UDP sensor logging?**  
   👉 `socket.SOCK_DGRAM` (TCP is `socket.SOCK_STREAM`).
6. **Smart Dust concept?**  
   👉 Tiny, microelectromechanical (MEMS) computing devices that can be dispersed/sprayed into an environment for ubiquitous sensing.
7. **Is M2M the same as IoT?**  
   👉 **No!** M2M is machine-to-machine hardware communication; **M2M is a subset of IoT**, while IoT encompasses people, cloud services, and broad business systems.
8. **Raspberry Pi GPIO Voltage?**  
   👉 **3.3 V** (Connecting 5V inputs directly will burn the GPIO pin!).
9. **Which Arduino Uno pins are PWM?**  
   👉 **Pins 3, 5, 6, 9, 10, 11** (Total 6 PWM pins).
10. **In smart cities, what do digital telecommunication networks correspond to?**  
    👉 The **Nerves** (Sensors = Sensory Organs, Buildings = Skeleton, Intelligence = Brain).
