# 🌐 NPTEL IoT Module 3: Weeks 7 to 9 Remote Logging, SDN, Cloud & Fog Computing
> **Course**: Introduction to Internet of Things (IIT Kharagpur — Prof. Sudip Misra)  
> **Exam Date**: Tuesday, October 27, 2026 (08:00 AM)  
> **Scope**: Weeks 7, 8, and 9 Official & Synthesized High-Yield Assignment Questions with Verified Solutions & Explanations.

---

## 📘 Week 7: Remote Data Logging, Sockets (TCP/UDP) & Sensor Interfacing

### Q1. In the remote data logging system, which socket type is used to send sensor data from the client to the server?

* a. SOCK_STREAM
* b. SOCK_DGRAM
* c. SOCK_RAW
* d. SOCK_SEQPACKET

> **✅ Correct Answer**: `b. SOCK_DGRAM`  
> **💡 Explanation**: The client creates a UDP socket using socket.socket(socket.AF_INET, socket.SOCK_DGRAM) to send the sensor readings to the server. See Lecture 31 (Implementation of IoT with Raspberry Pi – Part 2) @ 07:10

---

### Q2. Which Adafruit function is used in the client code to read humidity and temperature values from the DHT sensor?

* a. Adafruit_DHT.read_retry()
* b. Adafruit_DHT.get_data()
* c. Adafruit_DHT.sense()
* d. Adafruit_DHT.capture()
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur

> **✅ Correct Answer**: `a. Adafruit_DHT.read_retry()`  
> **💡 Explanation**: The sensordata() function calls Adafruit_DHT.read_retry(sensor,17), which returns the humidity and temperature values from the DHT sensor. See Lecture 31 (Implementation of IoT with Raspberry Pi – Part 2) @ 04:50

---

### Q3. Where does the server in the remote data logging example save the data received from the client as mentioned in the lecture?

* a. In a MySQL database
* b. In a text file named Datalog.txt
* c. On a cloud dashboard
* d. In an Excel spreadsheet

> **✅ Correct Answer**: `b. In a text file named Datalog.txt`  
> **💡 Explanation**: The server code opens 'Datalog.txt' in append mode and writes the received message from the client into this text file. See Lecture 31 (Implementation of IoT with Raspberry Pi – Part 2) @ 15:40

---

### Q4. Which Python string function is used to split the comma-separated sensor data into separate values on the server?

* a. split()
* b. divide()
* c. partition()
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur
* d. separate()

> **✅ Correct Answer**: `a. split()`  
> **💡 Explanation**: The split() function splits a string into multiple strings based on a specified separator/delimiter, e.g. Data.split(",") splits data wherever a comma is found. See Lecture 32 (Implementation of IoT with Raspberry Pi – Part 3) @ 08:40

---

### Q5. State whether the following statement is True or False. Statement: Matplotlib Python library is used to plot the temperature and humidity data received at the server in the lecture.

* a. False
* b. True

> **✅ Correct Answer**: `b. True`  
> **💡 Explanation**: MATPLOTLIB is a Python library used to create 2D plots; functions such as plot(), xlabel(), ylabel(), and title() are used to plot and label the sensor data. See Lecture 32 (Implementation of IoT with Raspberry Pi – Part 3) @ 12:15

---

### Q6. Which matplotlib function turns on interactive mode so that the plot updates in real time as new data arrives?

* a. ion()
* b. grid()
* c. subplot()
* d. figure()
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur

> **✅ Correct Answer**: `a. ion()`  
> **💡 Explanation**: ion() turns on the interactive mode in matplotlib. Other common plotting functions mentioned include figure(), grid(), subplot(), close(), and scatter(). See Lecture 32 (Implementation of IoT with Raspberry Pi – Part 3) @ 23:25

---

### Q7. In a traditional (non-SDN) network, where does the routing protocol logic (e.g., OSPF) mainly execute?

* a. In a centralized controller
* b. At the individual switches
* c. On the end-user device
* d. In the cloud

> **✅ Correct Answer**: `b. At the individual switches`  
> **💡 Explanation**: In the current network, protocols like OSPF execute at the switches, which forward traffic in a distributed manner with no centralized control. See Lecture 33 (Software-Defined Networking – Part I) @ 04:10

---

### Q8. In which year was the OpenFlow project — from which the idea of software-defined networking originated — presented at ACM SIGCOMM?

* a. 2006
* b. 2008
* c. 2009
* d. 2011
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur

> **✅ Correct Answer**: `b. 2008`  
> **💡 Explanation**: The idea of software-defined networking originated from the OpenFlow project, presented at ACM SIGCOMM in 2008. Stanford published the OpenFlow V1.0.0 specification the following year. See Lecture 33 (Software-Defined Networking – Part I) @ 10:50

---

### Q9. What message does a switch send to the SDN controller when it receives a packet for which no matching flow-rule exists?

* a. PACKET-IN message
* b. FLOW-REQUEST message
* c. RULE-MISS alert
* d. CONTROL-SYNC message

> **✅ Correct Answer**: `a. PACKET-IN message`  
> **💡 Explanation**: When no flow-rule is present for an incoming request, the switch sends a PACKET-IN message to the controller, which then decides a suitable flow-rule and inserts it at the switch. See Lecture 33 (Software-Defined Networking – Part I) @ 22:33

---

### Q10. Which SDN API is used for communication between the control layer and the infrastructure layer?

* a. Northbound API
* b. Southbound API
* c. East-Westbound API
* d. North-Southbound API
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur

> **✅ Correct Answer**: `b. Southbound API`  
> **💡 Explanation**: The Southbound API is used to communicate between the control layer and the infrastructure layer using the OpenFlow protocol. The Northbound API communicates between the control and application layers. See Lecture 34 (Software-Defined Networking – Part II) @ 02:00

---

### Q11. According to the lecture, approximately how many requests per second can a typical SDN controller handle through a single thread?

* a. 50
* b. 100
* c. 200
* d. 500

> **✅ Correct Answer**: `c. 200`  
> **💡 Explanation**: The lecture states that a controller can typically handle around 200 requests in a second through a single thread. See Lecture 34 (Software-Defined Networking – Part II) @ 04:10

---

### Q12. Which control mechanism is described where the entire network's control decisions are taken by a single controller?

* a. Distributed control
* b. Centralized control
* c. Hierarchical control
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur
* d. Federated control

> **✅ Correct Answer**: `b. Centralized control`  
> **💡 Explanation**: In centralized control, control decisions are taken in a centralized manner by a single controller, unlike distributed control where each subnetwork is controlled by a different controller. See Lecture 34 (Software-Defined Networking – Part II) @ 08:15

---

### Q13. Which of the following is listed as a benefit of integrating SDN with IoT?

* a. Increased hardware cost
* b. Visibility of network resources
* c. Reduced sensor accuracy
* d. Elimination of all controllers

> **✅ Correct Answer**: `b. Visibility of network resources`  
> **💡 Explanation**: Benefits of integrating SDN in IoT include intelligent routing decisions, simplified information collection/analysis/decision-making, visibility of network resources, and intelligent traffic pattern analysis. See Lecture 35 (Software-Defined IoT Networking – Part I) @ 02:50

---

### Q14. According to the lecture, what is a key resource-constraint challenge in wireless sensor networks that motivates software-defined WSN?

* a. Excess bandwidth
* b. Limited memory for control programs
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur
* c. Too many controllers
* d. Unlimited computation power

> **✅ Correct Answer**: `b. Limited memory for control programs`  
> **💡 Explanation**: Wireless sensor network challenges include real-time programming of sensor nodes, vendor-specific architecture, resource-constrained (heavy computation cannot be performed) devices, and limited memory, meaning too many control programs cannot be inserted. See Lecture 35 (Software-Defined IoT Networking – Part I) @ 08:10

---

### Q15. In the SDN-WISE protocol stack for sensor nodes, what does "INPP" stand for?

* a. Integrated Node Path Protocol
* b. Internal Node Power Processing
* c. In Network Packet Processing
* d. IoT Network Priority Protocol

> **✅ Correct Answer**: `c. In Network Packet Processing`  
> **💡 Explanation**: In the SDN-WISE protocol stack, the forwarding layer above IEEE 802.15.4 consists of flow-rules, and INPP stands for In Network Packet Processing. See Lecture 35 (Software-Defined IoT Networking – Part I) @ 15:35 ************END************

---

## 📘 Week 8: Software Defined Networking (SDN) in IoT, ODIN & Mobi-Flow

### Q1. Which of the following is listed as a problem in traditional (non-SDN) mobile networks?

* a. Too flexible hardware architecture
* b. Excess centralized control
* c. Very low operational cost
* d. Difficult to scale due to static, over-provisioned networks

> **✅ Correct Answer**: `d. Difficult to scale due to static, over-provisioned networks`  
> **💡 Explanation**: Traditional mobile networks are difficult to scale because static, over-provisioned networks are inflexible to manage high-demand mobile traffic; they are also difficult to manage, inflexible, and cost-expensive. See Lecture 36 (Software-Defined IoT Networking – Part II, slide 3)

---

### Q2. In the ODIN architecture for software-defined wireless networks, what does the 'Odin agent' do?

* a. It is placed at the controller end to manage policies
* b. It replaces the OpenFlow protocol entirely
* c. It is placed with the physical devices to communicate with the controller
* d. It performs billing for cloud resources

> **✅ Correct Answer**: `c. It is placed with the physical devices to communicate with the controller`  
> **💡 Explanation**: In ODIN, an agent is placed at access points (with the physical devices) to communicate with the controller, while the Odin master resides at the controller end. NPTEL Online Certification Courses Indian Institute of Technology Kharagpur See Lecture 36 (Software-Defined IoT Networking – Part II, slide 11)

---

### Q3. What is the primary goal of Mobi-Flow's proactive rule placement approach in Software-Defined IoT?

* a. To place flow-rules randomly across all access points
* b. To predict users' future location and place flow-rules at APs accordingly
* c. To eliminate the need for a controller
* d. To increase the number of PACKET-IN messages

> **✅ Correct Answer**: `b. To predict users' future location and place flow-rules at APs accordingly`  
> **💡 Explanation**: Mobi-Flow predicts the location of end-users at time (t+1) while they are at time (t), and places flow-rules at the access points that can be associated with the users based on their predicted locations, using an order-K Markov predictor. See Lecture 36 (Software-Defined IoT Networking – Part II, slides 15–16)

---

### Q4. Which simulation tool is mentioned in the lecture for experimenting with wireless software-defined networks, supporting both wired and wireless (IEEE 802.11) protocols?

* a. CloudSim
* b. NS2
* c. GreenCloud
* d. Mininet-WiFi

> **✅ Correct Answer**: `d. Mininet-WiFi`  
> **💡 Explanation**: Mininet-WiFi can be used to deploy a network supporting both wired (Ethernet) and wireless (WiFi, IEEE 802.11) protocols, while ONOS can be used to place the controllers. See Lecture 36 (Software-Defined IoT Networking – Part II, slide 21) NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q5. According to the NIST definition quoted in the lecture, cloud computing enables on-demand network access to a shared pool of what?

* a. Fixed, dedicated hardware resources
* b. Configurable computing resources
* c. Only storage resources
* d. Only networking resources

> **✅ Correct Answer**: `b. Configurable computing resources`  
> **💡 Explanation**: NIST defines cloud computing as a model for enabling convenient, on-demand network access to a shared pool of configurable computing resources such as networks, servers, storage, and applications. See Lecture 37 (Cloud Computing – Fundamentals, slide 4)

---

### Q6. Which of the following is one of the essential characteristics of cloud computing as defined by NIST?

* a. Rapid elasticity
* b. Manual resource allocation
* c. Single-tenant only access
* d. Fixed billing regardless of usage

> **✅ Correct Answer**: `a. Rapid elasticity`  
> **💡 Explanation**: NIST lists rapid elasticity as an essential characteristic, meaning cloud resource allocation and release should be rapid, elastic, and automatic, giving consumers the impression of infinite resources. See Lecture 37 (Cloud Computing – Fundamentals, slide 9) NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q7. Which cloud deployment model is set up for the exclusive use of a single organization, typically managed on-premises or by a third party off-premises?

* a. Public cloud
* b. Private cloud
* c. Community cloud
* d. Multi-cloud

> **✅ Correct Answer**: `b. Private cloud`  
> **💡 Explanation**: A private cloud is a cloud set-up functioned only for a single organization, typically managed by the organization itself (on-premises) or by a third party (off-premises). See Lecture 37 (Cloud Computing – Fundamentals, slide 20)

---

### Q8. Which of the following is given as an example of a public cloud provider in the lecture?

* a. Amazon Web Services (AWS)
* b. A company's internal private data center
* c. A single organization's dedicated server room
* d. A community-only cloud shared by hospitals

> **✅ Correct Answer**: `a. Amazon Web Services (AWS)`  
> **💡 Explanation**: Public cloud examples given include Amazon Web Services (AWS), Google Compute Engine, and Microsoft Azure — cloud set-ups available for the use of any person or industry. See Lecture 37 (Cloud Computing – Fundamentals, slide 19)

---

### Q9. Which cloud service model provides on-demand delivery of computing infrastructure such as servers, storage, network, and operating system? NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

* a. SaaS
* b. PaaS
* c. IaaS
* d. DBaaS

> **✅ Correct Answer**: `c. IaaS`  
> **💡 Explanation**: Infrastructure-as-a-Service (IaaS) contains the basic building blocks for cloud IT, providing access to networking features, computers (virtual or dedicated hardware), storage, and operating systems. See Lecture 38 (Cloud Computing – Service Models, slide 4)

---

### Q10. In the IaaS working methodology, which component allows multiple virtual machines to share the same physical hardware?

* a. DNS server
* b. Load balancer
* c. Firewall
* d. Hypervisor

> **✅ Correct Answer**: `d. Hypervisor`  
> **💡 Explanation**: In IaaS, the hypervisor sits above the physical hardware and manages multiple virtual machines (VMs), each running its own operating system, on a virtualized server. See Lecture 38 (Cloud Computing – Service Models, slide 5)

---

### Q11. Which cloud service model is described as 'application middleware offered as a service to developers', removing the need to manage underlying hardware and operating systems?

* a. IaaS
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur
* b. SaaS
* c. PaaS
* d. Community Cloud

> **✅ Correct Answer**: `c. PaaS`  
> **💡 Explanation**: Platform-as-a-Service (PaaS) removes the need for organizations to manage underlying infrastructure (hardware and OS) and lets developers focus on deploying and managing their applications; it is described as application middleware offered as a service. See Lecture 38 (Cloud Computing – Service Models, slide 15)

---

### Q12. What is the primary purpose of a Service Level Agreement (SLA) in cloud service management?

* a. To define the physical location of the data center
* b. To define the non-functional requirements expected from the service provider
* c. To specify the programming language used by the cloud provider
* d. To list the hardware vendors used by the provider

> **✅ Correct Answer**: `b. To define the non-functional requirements expected from the service provider`  
> **💡 Explanation**: An SLA defines the non-functional requirements expected from the service provider and provides a roadmap with clearly defined deliverables, describing the quality, utility, and warranty of services expected by the customer. See Lecture 39 (Cloud Computing – Service Management and Security, slide 4)

---

### Q13. In cloud service accounting and billing, what does 'service accounting' primarily aim to obtain?

* a. Resource usage information, typically in the form of records
* b. The physical address of end-users
* c. The source code of hosted applications
* d. The marketing budget of the provider
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur

> **✅ Correct Answer**: `a. Resource usage information, typically in the form of records`  
> **💡 Explanation**: Service accounting aims to obtain resource usage information, typically in the form of records, depending on infrastructure and service monitoring where usage information is obtained from metric measurements. See Lecture 39 (Cloud Computing – Service Management and Security, slide 5)

---

### Q14. What is the main purpose of using cloud simulators such as CloudSim before actual deployment?

* a. To permanently replace the need for real cloud infrastructure
* b. To physically manufacture cloud hardware
* c. To increase the billing cost of cloud services
* d. To provide a reliable, scalable, and repeatable environment for pre-deployment performance evaluation

> **✅ Correct Answer**: `d. To provide a reliable, scalable, and repeatable environment for pre-deployment performance evaluation`  
> **💡 Explanation**: Simulation tools provide a reliable, scalable, and repeatable environment for performance evaluation, facilitating pre-deployment tests of services at no cost and enabling repeatable evaluation. See Lecture 40 (Cloud Computing – Case Studies, slides 2–3)

---

### Q15. CloudSim, a widely used cloud simulation framework, was developed at which institution and is based on which programming language?

* a. Stanford University, based on Python
* b. CLOUDS Lab, University of Melbourne, based on Java
* c. MIT, based on C++
* d. IIT Kharagpur, based on JavaScript

> **✅ Correct Answer**: `b. CLOUDS Lab, University of Melbourne, based on Java`  
> **💡 Explanation**: CloudSim is a simulation framework that models cloud computing environments (data centers, VMs, applications, users, and network topology), written in a Java-based environment, and developed at the CLOUDS Lab of the University of Melbourne. See Lecture 40 (Cloud Computing – Case Studies, slide 5) NPTEL Online Certification Courses Indian Institute of Technology Kharagpur ************END************

---

## 📘 Week 9: Cloud & Fog Computing, Sensor-Cloud & OpenStack (Official Solutions)

### Q1. Which of the following is/are the advantages of cloud computing?

* a.  Elasticity
* b. Pay-per-use
* c.  Self Service
* d. All of the above

> **✅ Correct Answer**: `d. All of the above`  
> **💡 Explanation**: The advantages of cloud computinginclude Elasticity, Pay-per-use and Self-Service. (Please refer Lecture 42@6:45)

---

### Q2. Fill in the blanks. Fog computing is an intermediate layer between __________ and _________.

* a.      Dew and devices
* b.      Cloud and devices
* c.      Cloud and server
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur
* d.      None of these

> **✅ Correct Answer**: `b. Cloud and devices`  
> **💡 Explanation**: Fog computing is an intermediatelayer between Cloud and devices. (Please refer Lecture 44@6:40)

---

### Q3. The managerial role is played by __________ in sensor-cloud architecture.

* a.      End-users
* b.     Sensor-Cloud Service Provider
* c.      Neither a nor b
* d.      Both a and b

> **✅ Correct Answer**: `b. Sensor-Cloud Service Provider`  
> **💡 Explanation**: Sensor-Cloud Service Provider plays the managerial role in sensor-cloud architecture. (Please refer Lecture 42@14:29)

---

### Q4. Which of the following is not a component of OpenStack?

* a. Suse
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur
* b. Nova
* c. Swift
* d. All of these

> **✅ Correct Answer**: `a. Suse`  
> **💡 Explanation**: Nova and Swift are two of themany components of OpenStack (Please refer Lecture 41@3:18)

---

### Q5. Who coined the term Fog computing?

* a. IBM
* b. CISCO
* c. All of these
* d. None of these

> **✅ Correct Answer**: `b. CISCO`  
> **💡 Explanation**: CISCO coined the term Fog computing.(Please refer Lecture 44@4:18)

---

### Q6. Fill in the blank. The concept of ________ enables physical hardware to be shared among multiple entities. NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

* a. Hardware virtualization
* b. Software virtualization
* c. Module virtualization
* d. All of these

> **✅ Correct Answer**: `a. Hardware virtualization`  
> **💡 Explanation**: The concept of hardware virtualizationenables physical hardware to be shared among multiple entities. (Please refer to Page 262, Chapter 11, Introduction to IoT. S. Misra, A. Mukherjee, and A. Roy, 2020. Cambridge University Press.)

---

### Q7. Openstack is a free open source software for cloud framework simulation and experimentation with various cloud applications.

* a. True
* b. False

> **✅ Correct Answer**: `a. True`  
> **💡 Explanation**: Openstack is a free open sourcesoftware for cloud framework simulation and experimentation with various cloud applications. It can be downloaded and installed for free. Refer Lecture 41.

---

### Q8. In IoT, temporal sensitivity of data DOES NOT playan important role a. True b. False NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

> **✅ Correct Answer**: `b. False`  
> **💡 Explanation**: IoT data can be classified in totime sensitive data, less time sensitive data and data not sensitive to time. Hence time sensitivity plays a big role in IOT data classification. Refer lecture 44 on Fog Computing

---

### Q9. Which among the following is NOT a component of OpenStack.

* a. Horizon
* b. Heat
* c. Stellar
* d. Neutron

> **✅ Correct Answer**: `c. Stellar`  
> **💡 Explanation**: Stellar is not a component of OpenStack.The rest are various components, including Nova, Glance, Swift etc. Refer lecture 41, ppt No. 4

---

### Q10. Which among the following is the principal feature of sensor clouds, with respect to sensor nodes?

* a. Sensor monitoring
* b. Sensor instantiation
* c. Sensor virtualization
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur
* d. Sensor collection

> **✅ Correct Answer**: `c. Sensor virtualization`  
> **💡 Explanation**: Sesnorvirtualizationistheprincipalfeatureofsensorcloudsandtheir utility. Refer lecture 42 and 43 on Sensor cloud

---

### Q11. The optimal composition of __________ is a management issue in sensor-cloud.

* a. Logistics
* b. Pricing
* c. Caching
* d. Virtual sensor nodes

> **✅ Correct Answer**: `d. Virtual sensor nodes`  
> **💡 Explanation**: The optimal composition of Virtualsensor nodes is a management issue in sensor-cloud. (Please refer Lecture 43@4:39)

---

### Q12. How many different types of caching mechanism are there in sensor cloud?

* a. 1
* b. 4
* c. 2
* d. 3

> **✅ Correct Answer**: `c. 2 Detailed Answer:Internal Cache (IC) and ExternalCache (EC) are two different types of caching NPTEL Online Certification Courses Indian Institute of Technology Kharagpur mechanisms used in sensor cloud. Refer lecture 43, ppt No. 13`  


---

### Q13. Data from an IoT device is transferred to cloud via a network, which is then processed at the cloud and then a response is sent back to the IoT device from the cloud after processing. The time it takes for one- way data transfer between the node and cloud is 10s and the data processing time at the cloud is ‘x’ seconds. It takes a total of 25s for the entire to and fro transfer of data between the sensor and cloud along with processing at the cloud. What is the value of x?

* a. 10s
* b. 5s
* c. 15s
* d. 20s

> **✅ Correct Answer**: `b. 5s`  
> **💡 Explanation**: Time taken for one-way data transferbetween the node and cloud is 10s. Total time taken for the data transfer is 25s. So 25=10+x+10 (transfer from node to cloud+processing at cloud+transfer from cloud to node). Thus x=5s. NPTEL Online Certification Courses Indian Institute of Technology Kharagpur

---

### Q14. Which among the following is true?

* a. Fog computing acts as a complement to cloud computing.
* b. Fog computing is a replacement for cloud computing.
* c. Fog computing and cloud computing are the same.
* d. Fog computing is more powerful than cloud computing (with respect to resources).

> **✅ Correct Answer**: `a. Fog computing acts as a complement to cloud computing.`  
> **💡 Explanation**: Fog computing and cloud computingare complementary technologies. Fog helps in bringing the cloud closer to the IoT devices. (Please refer Lecture 45@1:06)

---

### Q15. Which component of OpenStack do you use to access all the other components?

* a. Horizon
* b. Glance
* c. Neutron
* d. None of these
* NPTEL Online Certification Courses
* Indian Institute of Technology Kharagpur

> **✅ Correct Answer**: `a. Horizon`  
> **💡 Explanation**: Horizon is the dashboard of OpenStackwhich provides the GUI and from where you can access other components. Please refer Lecture 41@3:54 ************END***********

---
