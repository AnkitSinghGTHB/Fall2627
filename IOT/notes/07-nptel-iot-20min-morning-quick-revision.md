# ⚡ NPTEL IoT: 20-Minute Morning Exam-Hall Quick Revision Sheet

> **Course**: Introduction to Internet of Things (IIT Kharagpur — Prof. Sudip Misra)  
> **Exam Date**: Tuesday, October 27, 2026 (08:00 AM)  
> **Target Audience**: Read this in the **last 20 minutes** before walking into the examination center!  
> **Format**: Direct Question $\to$ Direct Answer (No options, zero fluff, highest-yield repeats across 2022–2026).

---

## 🎯 Part 1: Top 50 Most Frequently Repeated Questions (Cross-Matched 2022–2026)

**Q: Who coined the term Fog computing?**  
**A:** CISCO

**Q: How many layers does Zigbee consist of?**  
**A:** 4 (Physical, MAC, Network, Application)

**Q: State whether there is a network layer in Wired HART.**  
**A:** False (Wired HART has NO network layer; Physical, Data Link, Application only)

**Q: Which among the following is the principal feature of sensor clouds?**  
**A:** Sensor virtualization

**Q: In human to smart city analogy, what do Sensors and Tags correspond to?**  
**A:** Sensory Organs (Telecommunication Network = Nerves, Embedded Intelligence = Brain, Buildings/People = Skeleton)

**Q: How many digital I/O pins are there in Arduino Uno?**  
**A:** 14 (Pins 0 to 13; 6 are PWM pins: 3, 5, 6, 9, 10, 11)

**Q: What does 'CIA' in cloud data security stand for?**  
**A:** Confidentiality, Integrity, Availability

**Q: Which of the following is NOT a component of OpenStack?**  
**A:** Plasma / Suse / Stellar (Valid OpenStack components are Nova, Swift, Horizon, Neutron, Cinder)

**Q: Which component of OpenStack do you use to access all other components via web GUI?**  
**A:** Horizon

**Q: What are the operating frequencies of Z-Wave?**  
**A:** 908.42 MHz in US and 868.42 MHz in Europe

**Q: What allows automatic identification of objects and data extraction via electromagnetic fields?**  
**A:** RFID

**Q: Which of the following converts electrical energy to mechanical motion?**  
**A:** Actuator

**Q: In Socket programming, what does the parameter AF_INET stand for?**  
**A:** Internet Protocol (IPv4 addressing)

**Q: Which socket type is used for fast, connectionless UDP sensor logging?**  
**A:** SOCK_DGRAM (SOCK_STREAM is used for connection-oriented TCP)

**Q: During remote server access using socket programming, what is the utility of the listen() method?**  
**A:** To wait for clients to connect

**Q: What is the delay provided by the sketch command delay(3000); in Arduino?**  
**A:** Provides a delay of 3 seconds (parameter is in milliseconds)

**Q: What is the output of the Python code: x='17'; y='23'; z=x+y; print(z)?**  
**A:** 1723 (String concatenation, not integer addition)

**Q: An organization wants to put sensitive data on a private cloud and non-sensitive data on a public cloud. What cloud architecture is this?**  
**A:** Hybrid Cloud

**Q: When does sensing coverage guarantee 100% network connectivity in a sensor network?**  
**A:** When communication radius is at least twice the sensing radius ($r_c \ge 2 r_s$)

**Q: Which distance measuring sensor module operates on ultrasonic sound waves?**  
**A:** HC-SR04

**Q: NFC is designed for use by devices within what distance to each other?**  
**A:** Close proximity (typically less than 4 cm)

**Q: What is the solution for mobility-aware flow rule placement in Software-Defined IoT?**  
**A:** Mobi-Flow

**Q: In the ODIN architecture for software-defined wireless networks, where is the 'Odin agent' placed?**  
**A:** Within the physical Access Point (AP)

**Q: Which among the following is the correct direction for PACKET_IN type messages in SDN?**  
**A:** From switch to controller

**Q: Which UMB interoperability component converts physical device messages into universal messages?**  
**A:** UMB Adaptor (Universal Middleware Bridge Adaptor)

**Q: What does UMB stand for in IoT interoperability?**  
**A:** Universal Middleware Bridge

**Q: Which kind of conflict occurs when different systems apply different processing logics to the same data?**  
**A:** Semantic conflict

**Q: What type of client requires constant network communication/connection with the server?**  
**A:** Thin client

**Q: In MQTT, what is used by the broker as routing information?**  
**A:** Topic

**Q: Which MQTT wildcard matches exactly one level in the topic hierarchy?**  
**A:** `+` (Single-level wildcard; `#` matches all remaining multi-levels)

**Q: What is the fixed header size of an MQTT packet?**  
**A:** 2 Bytes (CoAP fixed header is 4 Bytes)

**Q: What are the four fundamental message types in CoAP?**  
**A:** CON (Confirmable), NON (Non-Confirmable), ACK (Acknowledgement), RST (Reset)

**Q: What is the operating logic voltage level of Raspberry Pi GPIO pins?**  
**A:** 3.3 V (Applying 5V directly destroys the Broadcom SoC!)

**Q: What distinguishes a smart grid from a traditional electrical grid?**  
**A:** Bidirectional flow of electricity and bidirectional flow of information

**Q: Smart grid is also known as what?**  
**A:** Energy Internet

**Q: Under Time-of-Use (TOU) pricing, when are consumers encouraged to operate high-power appliances?**  
**A:** Off-peak hours (to reduce peak load and lower bills)

**Q: What is the correct flow of data in the IoT lifecycle?**  
**A:** Generation $\to$ Acquisition $\to$ Storage $\to$ Analysis

**Q: The two most relevant sensors directly used in smart agriculture are?**  
**A:** Soil moisture and water level sensors

**Q: How many caching mechanisms exist in Sensor-Cloud?**  
**A:** 2 (Internal Cache and External Cache)

**Q: The managerial role in sensor-cloud architecture is played by?**  
**A:** Sensor-Cloud Service Provider (SCSP)

**Q: What statistical analysis is used for data that is categorical in nature?**  
**A:** Qualitative analysis

**Q: Analysis of Variance (ANOVA) is best applied when which of the following are to be compared?**  
**A:** Means of 3 or more groups

**Q: What is the effect size parameter used for determining statistical significance?**  
**A:** Mean

**Q: In IoT, what are tiny, microelectromechanical (MEMS) devices that can be sprayed or injected for sensing?**  
**A:** Smart Dust

**Q: What is the relationship between IoT and M2M?**  
**A:** M2M is a part/subset of IoT; IoT has a much broader scope (including people and cloud applications)

**Q: Does dumb behavior of sensor nodes depend on environmental effects over time?**  
**A:** Yes, it is Temporal in nature

**Q: What does ISA stand for in the ISA 100.11A wireless standard?**  
**A:** International Society of Automation

**Q: Which Adafruit Python function reads humidity and temperature from a DHT sensor?**  
**A:** Adafruit_DHT.read_retry()

**Q: What does OpenStack use as virtualized compute resources that you can define and boot?**  
**A:** Instances

**Q: In IoT healthcare, processing handheld activity device accelerometer data with AI is primarily used for?**  
**A:** Fall detection

---

## ⚡ Part 2: High-Speed Numerical & Formula Flashcards

* **Sensing Coverage vs Connectivity**: $r_c \ge 2 r_s \implies$ Sensing coverage guarantees network connectivity.
* **Arduino 10-Bit ADC Step Size ($V_{\text{ref}} = 5\text{V}$)**:
  $$\text{Resolution} = \frac{5.0}{1023} \approx 4.887\text{ mV}$$
  Reading of $512 \implies 512 \times 4.887\text{ mV} \approx \mathbf{2.50\text{ V}}$.
* **HC-SR04 Ultrasonic Distance Formula**:
  $$\text{Distance (cm)} = \frac{\text{Time } (\mu\text{s})}{58.2} \quad \text{or} \quad \frac{\text{Time } (\mu\text{s}) \times 0.034}{2}$$
* **Network Latency / Transfer Delay Formula**:
  $$\text{Delay} = \frac{\text{Packet Size}}{\text{Bandwidth}} + \text{Propagation Time}$$
  *(For standard NPTEL 5MB / 1MBps question $\implies$ **5s**)*.

---

## 🔌 Part 3: Hardware Pinout Rapid Snapshot

| Platform | Key Specification | Crucial Exam Detail |
|:---|:---|:---|
| **Arduino Uno** | ATmega328P, 16 MHz, 5V | **14 Digital pins** (6 PWM: `3, 5, 6, 9, 10, 11`), **6 Analog pins** (`A0-A5`), 10-bit ADC ($0-1023$). |
| **Arduino I2C** | Two-wire serial | **A4 (SDA)**, **A5 (SCL)** |
| **Arduino SPI** | 4-wire high speed | **Pin 10 (SS)**, **Pin 11 (MOSI)**, **Pin 12 (MISO)**, **Pin 13 (SCK)** |
| **Raspberry Pi** | 40-pin header | **3.3V Logic level ONLY** (NOT 5V tolerant!). `BOARD` mode = physical pins 1-40; `BCM` mode = Broadcom GPIO channels. |

---

## 🌐 Part 4: Protocol Port Numbers & Transports Rapid Drill

* **MQTT**: Port **1883** (8883 SSL) | **TCP** | Pub/Sub | 2-byte header | QoS 0, 1, 2
* **CoAP**: Port **5683** (5684 DTLS) | **UDP** | Client/Server REST | 4-byte header | CON, NON, ACK, RST
* **XMPP**: Port **5222** | **TCP** | XML streams
* **AMQP**: Port **5672** | **TCP** | Message queues & exchanges
* **Zigbee**: IEEE **802.15.4** | 2.4 GHz global (250 kbps), 868 MHz EU, 915 MHz US | 4 Layers
* **Z-Wave**: 908.42 MHz (US), 868.42 MHz (EU) | Home automation mesh | Up to 232 nodes
* **Wired HART**: Industrial field communication | **NO Network Layer**
* **LoRaWAN Class A**: Lowest power, uplink initiated | **Class C**: Continuous listening, lowest downlink latency

---

## 🧠 Part 5: Last-Minute Mental Checklist
1. **MSQ Questions**: Read whether multiple options can be correct. If multiple characteristics fit, select all!
2. **Negative Traps**: Check for *"NOT"* (e.g. Wired HART has *no* network layer; Plasma/Suse are *not* OpenStack components).
3. **Pacing**: 100 Marks $\implies$ Finish the direct repeats in the first 40 minutes, leave time to verify numericals.

**Take a deep breath. You are 100% prepared. Go claim your Elite Certificate! 🏆**
