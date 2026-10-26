# 📡 NPTEL IoT Module 1: Weeks 1 to 3 Master Question Bank & Solutions
> **Course**: Introduction to Internet of Things (IIT Kharagpur — Prof. Sudip Misra)  
> **Exam Date**: Tuesday, October 27, 2026 (08:00 AM)  
> **Scope**: Weeks 1, 2, and 3 Official Assignment Questions with Verified Solutions & Explanations.

---

## 📘 Week 1: Introduction to IoT, Sensing, Actuation & IoT Networking Basics

### Q1. According to the ITU Internet Report 2005 discussed in the lecture, the future Internet is expected to become wider and more complex mainly because:

* a. Humans will completely stop using the Internet
* b. Most Internet traffic may flow between devices and different kinds of things
* c. Only desktop computers will remain connected
* d. Internet communication will be restricted to email services

> **✅ Correct Answer**: `b. Most Internet traffic may flow between devices and different kinds of things`  
> **💡 Explanation**: The ITU report describes a future where humans may become a minority as generators and receivers of traffic. Instead, communication will increasingly happen between devices and “things,” forming the Internet of Things. See lecture 1 Introduction to IoT — Part-I @ 03:10 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q2. Which of the following are characteristics of IoT systems?

* a. Efficient and scalable architecture
* b. Unambiguous naming and addressing
* c. Presence of sleeping nodes, mobile nodes, and non-IP devices
* d. Guaranteed continuous connectivity for every device at all times

> **✅ Correct Answer**: `a, b, c`  
> **💡 Explanation**: IoT systems require scalable architecture, clear naming and addressing, and must support heterogeneous devices such as sleeping nodes, mobile nodes, and non-IP devices. However, IoT systems may have intermittent connectivity, so option d is incorrect. See lecture 1: Introduction to IoT — Part-I @ 06:05

---

### Q3. In the lecture, “Smart Dust” refers to:

* a. A cloud storage model for IoT data
* b. A large-scale wireless router used in smart cities
* c. Very tiny computing devices that can be sprayed or injected for sensing purposes
* d. A type of IPv6 address used in IoT networks

> **✅ Correct Answer**: `c. Very tiny computing devices that can be sprayed or injected for sensing purposes`  
> **💡 Explanation**: Smart Dust refers to extremely small computing devices, smaller than a grain of sand, that can be used to measure chemicals in soil or diagnose problems in the human body. See lecture 1 Introduction to IoT — Part-I @ 10:40 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q4. Which statement best explains the relation between IoT and M2M communication?

* a. IoT and M2M are exactly the same
* b. M2M is broader than IoT because it includes people and applications
* c. M2M is a part of IoT, while IoT has a broader scope of interactions
* d. IoT does not include machine-to-machine interaction

> **✅ Correct Answer**: `c. M2M is a part of IoT, while IoT has a broader scope of interactions`  
> **💡 Explanation**: M2M focuses mainly on communication among machines and devices. IoT is broader because it includes interactions between things, people, applications, and systems. See lecture 1 Introduction to IoT — Part-I @ 19:30

---

### Q5. State whether the following statement is True or False. Statement: In the Web of Things, IoT sensors are replaced completely by cloud databases.

* a.   True
* b.   False

> **✅ Correct Answer**: `b. False`  
> **💡 Explanation**: The Web of Things does not replace sensors. Sensors remain responsible for collecting physical-world data, while web technologies help expose and access IoT resources. See lecture 1 Introduction to IoT — Part-I @ 22:50 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q6. In an IoT network configuration, local addresses may be valid only within a gateway’s domain. The same local address may even appear under another gateway. The main advantage of this strategy is:

* a. It increases unnecessary address consumption
* b. It helps conserve address space
* c. It removes the requirement of a gateway
* d. It prevents any device from communicating with the Internet

> **✅ Correct Answer**: `b. It helps conserve address space`  
> **💡 Explanation**: Using locally valid addresses within a gateway’s domain allows address reuse across different gateway domains. This helps avoid unnecessary wastage of global addresses. See lecture 2 Introduction to IoT — Part-II @ 05:30

---

### Q7. Which of the following functions are associated with IoT gateways in the addressing strategy discussed in the lecture?

* a. Providing Internet connectivity
* b. Supporting IoT LAN intra-connectivity
* c. Obtaining upstream address prefixes using mechanisms such as DHCPv6
* d. Delegating addresses to nodes using SLAAC

> **✅ Correct Answer**: `a, b, c, d`  
> **💡 Explanation**: IoT gateways can provide Internet connectivity and IoT LAN intra-connectivity. They may obtain upstream prefixes through DHCPv6 and delegate them to nodes using SLAAC. See lecture 2 Introduction to IoT — Part-II @ 09:40 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q8. Which of the following is true about IPv6 compared to IPv4?

* a. IPv6 uses dotted decimal notation
* b. IPv6 has a smaller address space than IPv4
* c. IPv6 uses hexadecimal notation and supports a much larger address space
* d. IPv6 requires broadcast addresses in the same way as IPv4

> **✅ Correct Answer**: `c. IPv6 uses hexadecimal notation and supports a much larger address space`  
> **💡 Explanation**: IPv4 uses 32-bit addresses and dotted decimal notation, whereas IPv6 uses 128- bit addresses and hexadecimal notation. This makes IPv6 more suitable for large-scale IoT addressing. See lecture 2 Introduction to IoT — Part-II @ 16:50

---

### Q9. Which statement correctly represents the design expectation from a good sensor?

* a. It should influence the measured property significantly
* b. It should respond strongly to unrelated physical properties
* c. It should be sensitive to the measured property and should not disturb it
* d. It should always produce random output

> **✅ Correct Answer**: `c. It should be sensitive to the measured property and should not disturb it`  
> **💡 Explanation**: A good sensor should measure the desired property, remain insensitive to unrelated properties, and should not influence or alter the measured quantity. See lecture 3 Sensing @ 13:00 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q10. Which of the following statements about sensor resolution are correct?

* a. Sensor resolution is the smallest change that the sensor can detect
* b. For a digital sensor, resolution is related to the smallest digital output change it can process
* c. Sensor resolution and sensor accuracy always refer to exactly the same property
* d. Sensor accuracy does not depend only on resolution

> **✅ Correct Answer**: `a, b, d`  
> **💡 Explanation**: Resolution refers to the smallest detectable change in the measured quantity. In digital sensors, it is related to the smallest digital output step. However, accuracy and resolution are not the same; a high-resolution sensor may still be inaccurate if it has bias or calibration errors. See lecture 3 Sensing @ 14:10

---

### Q11. State True or False. An accelerometer that measures acceleration along the x, y, and z coordinate axes is classified as a vector sensor.

* a. True
* b. False

> **✅ Correct Answer**: `a. True`  
> **💡 Explanation**: A vector sensor measures quantities that have both magnitude and direction or orientation. Since an accelerometer measures acceleration components along different coordinate axes, such as x, y, and z, it is classified as a vector sensor. See lecture 3 Sensing @ 18:40 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q12. A sensor gives different output for the same input value depending on whether that input was reached by increasing or decreasing the measured quantity. This error is called:

* a. Quantization error
* b. Hysteresis error
* c. IPv6 translation error
* d. Gateway prefix error

> **✅ Correct Answer**: `b. Hysteresis error`  
> **💡 Explanation**: Hysteresis error occurs when the sensor output depends on the previous input history. The same present input may give different readings depending on whether the input was approached from a lower or higher value. See lecture 3 Sensing @ 22:40

---

### Q13. State True or False A hydraulic actuator can produce considerable force because liquids are nearly incompressible.

* a. False
* b. True

> **✅ Correct Answer**: `b. True`  
> **💡 Explanation**: A hydraulic actuator uses hydraulic fluid to generate mechanical motion. Since liquids are nearly incompressible, hydraulic actuators can exert large forces. See lecture 4 Actuation @ 06:20 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q14. Which of the following statements are correct about Shape Memory Polymer actuators?

* a. They may respond to stimuli such as light, heat, electrical, magnetic, pH, or moisture changes
* b. They can show high strain recovery
* c. They may have properties such as low density and biocompatibility
* d. They are used only as passive temperature sensors

> **✅ Correct Answer**: `a, b, c`  
> **💡 Explanation**: Shape Memory Polymer actuators can respond to different stimuli and are known for features such as low density, high strain recovery, biocompatibility, and biodegradability. They are actuator materials, not merely passive temperature sensors. See lecture 4 Actuation @ 18:20

---

### Q15. State whether the following statement is True or False. Statement: According to the IoT implementation example discussed in the lecture, data gathered by a sensor travels through a gateway and a proxy server before arriving at the cloud server.

* a. True
* b. False

> **✅ Correct Answer**: `a. True`  
> **💡 Explanation**: In the example IoT implementation, the sensor first collects the data. The data then passes through the gateway and proxy server before reaching the cloud server for further processing and analytics. See Lecture 5: Basics of IoT Networking — Part-I @ 07:30 ************END*********** NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

## 📘 Week 2: IoT Communication Protocols: MQTT, CoAP, XMPP, AMQP & SMQTT

### Q1. In MQTT, which field of a published message is used by the broker as routing information?

* a.  Topic
* b.  Client identifier
* c.  Payload length
* d.  Session timer

> **✅ Correct Answer**: `a. Topic`  
> **💡 Explanation**: The MQTT broker dispatches messages between senders and receivers. The topic included in a published message provides the routing information that the broker uses to deliver the message to clients subscribed to the matching topic. Answer Location: Week 2, Module 6 (Basics of IoT Networking - Part II) @ 08:27

---

### Q2. Which of the following statements about MQTT topic wildcards are correct?

* a.  The plus sign (+) matches an arbitrary value at exactly one hierarchy level.
* b.  The hash sign (#) can be used to subscribe to all underlying hierarchy levels.
* c.  The subscription house/# matches only the exact topic house.
* d.  The subscription house/+/temperature can match house/kitchen/temperature.

> **✅ Correct Answer**: `a, b, and d`  
> **💡 Explanation**: The plus sign (+) is a single-level wildcard, whereas the hash sign (#) is a multilevel wildcard. Thus, house/+/temperature can match house/kitchen/temperature, and house/# matches all topics whose hierarchy begins with house, not only the exact topic house. Answer Location: Week 2, Module 6 (Basics of IoT Networking - Part II) @ 12:01 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q3. Which of the following are main stages of Secure MQTT (SMQTT)?

* a.  Setup
* b.  Publish
* c.  Decryption
* d.  Route discovery

> **✅ Correct Answer**: `a, b, and c`  
> **💡 Explanation**: SMQTT consists of four main stages: setup, encryption, publish, and decryption. Route discovery is not one of the SMQTT stages. Answer Location: Week 2, Module 6 (Basics of IoT Networking - Part II) @ 13:45

---

### Q4. At the transport layer, CoAP (Constrained Application Protocol) operates over which protocol?

* a.  TCP
* b.  UDP
* c.  SCTP
* d.  FTP

> **✅ Correct Answer**: `b. UDP`  
> **💡 Explanation**: CoAP is designed for constrained environments and operates over UDP at the transport layer. Its lightweight design helps reduce communication overhead for resource-constrained IoT devices. Answer Location: Week 2, Module 7 (Basics of IoT Networking - Part III) @ 05:41 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q5. State True or False. In CoAP, a piggyback response is carried with the acknowledgment, whereas in the separate mode, the server response is sent in a message separate from the acknowledgment.

* a.  True
* b.  False

> **✅ Correct Answer**: `a. True`  
> **💡 Explanation**: In the piggyback mode, the server places its response in the acknowledgment message. In the separate mode, the acknowledgment is sent first and the response is transmitted later as a separate message. Answer Location: Week 2, Module 7 (Basics of IoT Networking - Part III) @ 07:48

---

### Q6. Which of the following CoAP request-method mappings are correct?

* a.  GET - retrieve data
* b.  PUT - create data
* c.  PUSH - update data
* d.  DELETE - delete data

> **✅ Correct Answer**: `a, b, c, and d`  
> **💡 Explanation**: As presented in the lecture, CoAP uses GET, PUT, PUSH, and DELETE requests to retrieve, create, update, and delete data, respectively. Answer Location: Week 2, Module 7 (Basics of IoT Networking - Part III) @ 07:48 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q7. Which AMQP frame type is used to control the message-flow rate?

* a.  Transfer
* b.  Detach
* c.  Disposition
* d.  Flow

> **✅ Correct Answer**: `d. Flow`  
> **💡 Explanation**: The Flow frame controls the rate of message flow between AMQP peers. By comparison, Transfer carries messages, Disposition communicates a change in transfer state, and Detach terminates a link. Answer Location: Week 2, Module 8 (Basics of IoT Networking - Part IV) @ 06:21

---

### Q8. Which of the following statements about AMQP components are correct?

* a.  An exchange receives messages and routes them to queues.
* b.  A queue stores messages for business processes or consumers.
* c.  A binding specifies message-distribution rules between an exchange and queues.
* d.  A consumer must route every producer message before it reaches an exchange.

> **✅ Correct Answer**: `a, b, and c`  
> **💡 Explanation**: The main AMQP components discussed in the lecture are exchanges, queues, and bindings. An exchange receives and routes messages, a queue stores messages for consumers or business processes, and a binding defines the distribution rules connecting exchanges to queues. Answer Location: Week 2, Module 8 (Basics of IoT Networking - Part IV) @ 08:03 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q9. Which of the following IEEE 802.15.4 variant-application pairs are correct?

* a.  IEEE 802.15.4c - China
* b.  IEEE 802.15.4e - Industrial applications
* c.  IEEE 802.15.4f - Active RFID
* d.  IEEE 802.15.4g - Smart utility networks

> **✅ Correct Answer**: `a, b, c, and d`  
> **💡 Explanation**: The lecture associates IEEE 802.15.4c with China, 802.15.4d with Japan, 802.15.4e with industrial applications, 802.15.4f with active RFID, and 802.15.4g with smart utility networks. Answer Location: Week 2, Module 9 (Connectivity Technologies - Part I) @ 09:03

---

### Q10. In a non-beacon-enabled IEEE 802.15.4 network, data frames are transmitted using:

* a.  Slotted CSMA/CA
* b.  Unslotted CSMA/CA
* c.  Token passing
* d.  Pure TDMA only

> **✅ Correct Answer**: `b. Unslotted CSMA/CA`  
> **💡 Explanation**: Non-beacon-enabled IEEE 802.15.4 networks transmit data frames using unslotted CSMA/CA. In contrast, beacon-enabled networks use slotted CSMA/CA with a superframe structure managed by the PAN coordinator. Answer Location: Week 2, Module 9 (Connectivity Technologies - Part I) @ 14:11 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q11. Which statement correctly describes the relationship between IEEE 802.15.4 and ZigBee?

* a.  IEEE 802.15.4 provides layers 1 and 2, while ZigBee extends the functionality to layer 3 and above.
* b.  ZigBee provides only the physical layer, while IEEE 802.15.4 provides all higher layers.
* c.  Both standards operate only at the application layer.
* d.  ZigBee and IEEE 802.15.4 are identical standards with no functional distinction.

> **✅ Correct Answer**: `a. IEEE 802.15.4 provides layers 1 and 2, while ZigBee extends the functionality to layer 3 and above.`  
> **💡 Explanation**: IEEE 802.15.4 primarily specifies the physical and MAC layers. ZigBee operates on top of these layers and adds higher-layer functions, including authentication, encryption, routing, forwarding, and support for mesh networking. Answer Location: Week 2, Module 9 (Connectivity Technologies - Part I) @ 16:08

---

### Q12. Which of the following statements characterizes a ZigBee end device?

* a.  It communicates with its parent node.
* b.  It cannot relay data for other devices.
* c.  It is a reduced-functionality device.
* d.  It forms the network root and acts as the trust center.

> **✅ Correct Answer**: `a, b, and c`  
> **💡 Explanation**: A ZigBee end device has sufficient functionality to communicate with its parent, but it cannot relay data for other devices. It is therefore a reduced-functionality device. The coordinator, not an end device, forms the network root and may act as the trust center. Answer Location: Week 2, Module 9 (Connectivity Technologies - Part I) @ 23:54 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q13. Which option correctly describes addressing in 6LoWPAN?

* a.  A 16-bit address is globally unique, while a 64-bit address is PAN-specific.
* b.  A 16-bit short address is PAN-specific and assigned by the PAN coordinator, while a 64-bit
* extended address is globally unique.
* c.  Both 16-bit and 64-bit addresses are globally unique and assigned by an Internet router.
* d.  Both address types are used only for multicast communication.

> **✅ Correct Answer**: `b. A 16-bit short address is PAN-specific and assigned by the PAN coordinator, while a 64-bit extended address is globally unique.`  
> **💡 Explanation**: 6LoWPAN supports 16-bit short addresses for PAN-specific communication; these are assigned by the PAN coordinator. It also supports 64-bit extended addresses, which are globally unique. Answer Location: Week 2, Module 10 (Connectivity Technologies - Part II) @ 04:58

---

### Q14. State True or False. In LOADng routing, an intermediate router may respond to a Route Request (RREQ) whenever it already has an active route to the requested destination.

* a.  True
* b.  False

> **✅ Correct Answer**: `b. False`  
> **💡 Explanation**: In LOADng, only the destination is permitted to respond to an RREQ. Intermediate LOADng routers are explicitly prohibited from responding, even when they have an active route to the requested destination. Answer Location: Week 2, Module 10 (Connectivity Technologies - Part II) @ 12:48 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q15. How does a passive RFID tag obtain the power required to transmit information?

* a.  It uses its own internal battery.
* b.  It is powered inductively by an RFID reader.
* c.  It receives power through a wired AIDC connection.
* d.  It does not require any source of power.

> **✅ Correct Answer**: `b. It is powered inductively by an RFID reader.`  
> **💡 Explanation**: Passive RFID tags do not have their own power supply. They must first be powered inductively by an RFID reader before they can transmit information. Active RFID tags, in contrast, have their own power supply. Answer Location: Week 2, Module 10 (Connectivity Technologies - Part II) @ 19:30 ************END***********

---

## 📘 Week 3: Industrial Protocols, Wired/Wireless HART, Z-Wave & Zigbee

### Q1. State whether the following statement is true or false. Statement: There is no network layer in Wired HART

* a. True
* b. False

> **✅ Correct Answer**: `a. True`  
> **💡 Explanation**: There is no network layer in Wired HART. See lecture 11 @ 05:22

---

### Q2. Zwave operates at ________ MHz in the US and ________ MHz in Europe.

* a. 1008,989
* b. 908.42, 868.42
* c. 767.56,855.28
* d. None of these

> **✅ Correct Answer**: `b. 908.42, 868.42`  
> **💡 Explanation**: Zwave operates at 908.42 MHz in the US and 868.42 MHz in Europe. See lecture 13 @ 3:40 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q3. Dumb behavior of sensor nodes is _______________ in nature (as it is dependent on the effects of the environmental conditions).

* a. Temporal
* b. Spatial
* c. Both (a) and (b)
* d. None of these

> **✅ Correct Answer**: `a. Temporal`  
> **💡 Explanation**: Dumb behavior of sensor nodes is Temporal in nature (as it is dependent on the effects of the environmental conditions). See lecture 15 @ 05:40

---

### Q4. The process of identifying channels consistently affected by interference and removing them from use is known as _________________.

* a. Channel Trimming
* b. Channel Flushing
* c. Both (a) and (b)
* d. None of these

> **✅ Correct Answer**: `d. None of these`  
> **💡 Explanation**: Channel Blacklisting identifies channels consistently affected by interference and removes them from use. See lecture 11 @ 07:30 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q5. The full form of NFC is

* a. Near Field Contact
* b. Near Field Communication
* c. Both (a) and (b)
* d. Neither (a) nor (b)

> **✅ Correct Answer**: `b. Near field communication`  
> **💡 Explanation**: The full form of NFC is Near Field Communication. See lecture 11 @ 17:44

---

### Q6. State true or false. NFC works on the principle of magnetic induction.

* a. True
* b. False

> **✅ Correct Answer**: `a. True`  
> **💡 Explanation**: NFC works on the principle of magnetic induction. See lecture 11 @ 21:00

---

### Q7. State whether the following statement is true or false. Statement: NFC tags found in supermarket products are examples of active NFC.

* a. True
* b. False

> **✅ Correct Answer**: `b. False NPTEL Online Certification Courses Indian Institute of Technology Kharagpur`  
> **💡 Explanation**: Passive NFC tags found in supermarket products are examples of passive NFC. See lecture 11 @ 18:47

---

### Q8. Bluetooth is based on ___________.

* a. Nanonets
* b. Binarynets
* c. Both (a) and (b)
* d. None of these

> **✅ Correct Answer**: `d. None of these`  
> **💡 Explanation**: Bluetooth is based on Piconets. See lecture 12 @ 01:55

---

### Q9. A __________ in NFC emits a small electric current which creates a magnetic field that in turn bridges the physical space between the devices.

* a. reader
* b. writer
* c. destroyer
* d. None of these

> **✅ Correct Answer**: `a. reader`  
> **💡 Explanation**: A reader in NFC emits a small electric current which creates a magnetic field that in turn bridges the physical space between the devices NPTEL Online Certification Courses Indian Institute of Technology Kharagpur See lecture 11 @ 20:31

---

### Q10. State true of false. Bluetooth technology is based on Ad-hoc network technology.

* a. False
* b. True

> **✅ Correct Answer**: `b. True`  
> **💡 Explanation**: Bluetooth technology is based on Ad-hoc network technology. See lecture 12 @ 02:30

---

### Q11. State true or false. Zwave utilizes GFSK modulation and Hongkong channel encoding.

* a. True
* b. False

> **✅ Correct Answer**: `b. False`  
> **💡 Explanation**: Zwave utilizes GFSK modulation and Manchester channel encoding. See lecture 13 @ 07:36 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q12. The process of bypassing radio dead-spots is done using a message called ________ in Zwave.

* a. Ping
* b. Healing
* c. Frame
* d. None of these

> **✅ Correct Answer**: `b. Healing`  
> **💡 Explanation**: The process of bypassing radio dead-spots is done using a message called Healing in Zwave. See lecture 13 @ 11:34

---

### Q13. State whether the following statement is true or false. Statement: Sensor nodes have unlimited battery life.

* a. True
* b. False

> **✅ Correct Answer**: `b. False`  
> **💡 Explanation**: Sensors nodes have limited battery life. See lecture 14 @ 13:15 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q14. State whether the following statement is true or false. Statement: The Link Manager Protocol in Bluetooth manages the establishment, authentication, link configuration.

* a. True
* b. False

> **✅ Correct Answer**: `a. True`  
> **💡 Explanation**: The Link Manager Protocol in Bluetooth manages the establishment, authentication, link configuration. See Page number – 157, Chapter - 7, Book - Introduction to IoT, Authors – Sudip Misra, Anandarup Mukherjee, and Arijit Roy, Publisher – Cambridge University Press, Edition – 1 (2021)

---

### Q15. Zigbee commonly uses __________data rate.

* a. 250 kbps
* b. 250 Mbps
* c. 260 kbps
* d. 260 Mbps

> **✅ Correct Answer**: `a. 250 kbps`  
> **💡 Explanation**: Zigbee commonly uses 250 kbps data rate. See Page number – 131, Chapter - 7, Book - Introduction to IoT, Authors – Sudip Misra, Anandarup Mukherjee, and Arijit Roy, Publisher – Cambridge University Press, Edition – 1 NPTEL Online Certification Courses Indian Institute of Technology Kharagpur (2021) ************END***********

---
