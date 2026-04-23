# INTERNATIONAL STANDARD

colour inside

Maritime navigation and radiocommunication equipment and systems – Class B shipborne equipment of the automatic identification system (AIS) – Part 2: Self-organising time division multiple access (SOTDMA) techniques

![](images/a0385f82cf17ea3cc71e89d6e61d0a4fe0beb0eee26734b80222443d81fd92c5.jpg)

![](images/a08182b65f6852af8251fe06c203e3f34a15c6f70acc43132decf6de6b877274.jpg)

# THIS PUBLICATION IS COPYRIGHT PROTECTED Copyright $\circledcirc$ 2017 IEC, Geneva, Switzerland

All rights reserved. Unless otherwise specified, no part of this publication may be reproduced or utilized in any form or by any means, electronic or mechanical, including photocopying and microfilm, without permission in writing from either IEC or IEC's member National Committee in the country of the requester. If you have any questions about IEC copyright or have an enquiry about obtaining additional rights to this publication, please contact the address below or your local IEC member National Committee for further information.

IEC Central Office

3, rue de Varembé

CH-1211 Geneva 20

Switzerland

Tel.: +41 22 919 02 11

Fax: +41 22 919 03 00

info@iec.ch

www.iec.ch

# About the IEC

The International Electrotechnical Commission (IEC) is the leading global organization that prepares and publishes International Standards for all electrical, electronic and related technologies.

# About IEC publications

The technical content of IEC publications is kept under constant review by the IEC. Please make sure that you have the latest edition, a corrigenda or an amendment might have been published.

# IEC Catalogue - webstore.iec.ch/catalogue

The stand-alone application for consulting the entire bibliographical information on IEC International Standards, Technical Specifications, Technical Reports and other documents. Available for PC, Mac OS, Android Tablets and iPad.

# IEC publications search - www.iec.ch/searchpub

The advanced search enables to find IEC publications by a variety of criteria (reference number, text, technical committee,…). It also gives information on projects, replaced and withdrawn publications.

# IEC Just Published - webstore.iec.ch/justpublished

Stay up to date on all new IEC publications. Just Published details all new publications released. Available online and also once a month by email.

# Electropedia - www.electropedia.org

The world's leading online dictionary of electronic and electrical terms containing 20 000 terms and definitions in English and French, with equivalent terms in 16 additional languages. Also known as the International Electrotechnical Vocabulary (IEV) online.

# IEC Glossary - std.iec.ch/glossary

65 000 electrotechnical terminology entries in English and French extracted from the Terms and Definitions clause of IEC publications issued since 2002. Some entries have been collected from earlier publications of IEC TC 37, 77, 86 and CISPR.

# IEC Customer Service Centre - webstore.iec.ch/csc

If you wish to give us your feedback on this publication or need further assistance, please contact the Customer Service Centre: csc@iec.ch.

# INTERNATIONAL STANDARD

![](images/e8b2e12452bf97ad8733c0740b3d10c2e22af87bc3b170c3499dcde5375698f9.jpg)

Maritime navigation and radiocommunication equipment and systems – Class B shipborne equipment of the automatic identification system (AIS) – Part 2: Self-organising time division multiple access (SOTDMA) techniques

INTERNATIONAL ELECTROTECHNICAL COMMISSION

ICS 47.020.70

ISBN 978-2-8322-3906-3

Warning! Make sure that you obtained this publication from an authorized distributor.

# CONTENTS

# FOREWORD. .. 8

1 Scope .. . 10   
2 Normative references . .. 10   
3 Terms, definitions and abbreviated terms .11

3.1 Terms and definitions.. . 11   
3.2 Abbreviated terms. . 11

4 General requirements . . 12   
4.1 General.. . 12

4.1.1 Capabilities of the Class B "SO" AIS. .12   
4.1.2 Quality assurance .. . 12   
4.1.3 Safety of operation . . 13   
4.1.4 Additional features. .13   
4.1.5 Functionality . .13

4.2 Manuals . .13   
4.3 Marking and identification . 13

5 Environmental, power supply, interference and safety requirements .13   
6 Performance requirements. .. 14

6.1 Internal processes .14   
6.2 Operating frequency channels. .15

6.3 Internal GNSS receiver for position reporting . . 15   
6.4 Identification . . 15

6.5 AIS Information . 15

6.5.1 Information content. .15   
6.5.2 Information reporting intervals .16   
6.5.3 Short safety-related messages .17   
6.5.4 Permissible initialisation period. .17

6.6 Alarms and indications, fall-back arrangements . 17

6.6.1 Built-in integrity tests (BIIT) . .17   
6.6.2 Transmitter shutdown procedure. .18   
6.6.3 Position sensor fallback conditions .19

6.7 User interface . . 19

6.7.1 Indication and display . .19   
6.7.2 Static data input . .20   
6.7.3 External interfaces. .20

6.8 Protection from invalid control commands . 20

7 Technical requirements . 20

7.1 General.. .20   
7.2 Physical layer . .21

7.2.1 General . .21   
7.2.2 Receiver characteristics.. .21   
7.2.3 Other characteristics.. .22   
7.2.4 Transmitter requirements .23

7.3 Link layer .. .24

7.3.1 General . .24   
7.3.2 Link sub-layer 1: medium access control (MAC).. .24   
7.3.3 Link sub-layer 2: data link service (DLS).. .26

7.3.4 Link sub-layer 3: link management entity (LME) . . 26

7.4 Network layer.. . 30

7.4.1 General . . 30   
7.4.2 Management of regional operating settings. . 30   
7.4.3 Multi-channel operation . ... 31

7.5 Transport layer ...... .. 31   
7.6 Presentation interface . . 32   
7.7 DSC receive capability .. . 32   
7.8 Long-range application by broadcast. . 32

8 Test conditions ....... .32

8.1 General.. .32   
8.2 Normal test conditions . 32

8.2.1 Temperature and humidity .32   
8.2.2 Power supply . . 33

8.3 Extreme test conditions. .33   
8.4 Test signals ..... .. 33

8.4.1 Standard test signal number 1 ... . 33   
8.4.2 Standard test signal number 2 . .33   
8.4.3 Standard test signal number 3 . .33   
8.4.4 Standard test signal number 4 . .33

8.5 Standard test environment . .34

8.5.1 Test setup ...... . 34   
8.5.2 Sensor test input . .35   
8.5.3 Synchronisation .. . 35   
8.5.4 Test signals applied to the receiver input . .35   
8.5.5 Waiver for receivers. .35   
8.5.6 Artificial antenna (dummy load) . 35   
8.5.7 Modes of operation of the transmitter. .35   
8.5.8 Common test conditions for protection from invalid controls . . 35   
8.5.9 Measurement uncertainties. .35

9 Power supply, environmental and EMC tests . . 36

9.1 Test summary ........ .. 36   
9.2 Vibration . . 37

9.2.1 Purpose ..... .37   
9.2.2 Method of measurement . 37   
9.2.3 Required results .38

9.3 Shock .. .38

9.3.1 Purpose.. .38   
9.3.2 Method of measurement .38   
9.3.3 Required result . .38

9.4 Performance tests/checks . 38   
9.5 Under voltage test (brown out) ...... .. 38

9.5.1 Purpose.. .38   
9.5.2 Method of test.. .38   
9.5.3 Required result . .39

9.6 Under voltage test (short term) ..... .. 39

9.6.1 Purpose ..... ... 39   
9.6.2 Method of test.. .39   
9.6.3 Required result . .39

10 Operational tests . . 39

10.1 General.. .39

10.1.1 Tests by inspection. . 39   
10.1.2 Safety of operation .39   
10.1.3 Additional features. .. 40

10.2 Modes of operation .. 40

10.2.1 Autonomous mode. .. 40   
10.2.2 Single messages . .42   
10.2.3 Polled mode and interrogation response . .. 45

10.3 Channel selection . . 45

10.3.1 Valid channels . .. 46   
10.3.2 Invalid channels. . 46

10.4 Internal GNSS receiver . . 46   
10.5 AIS information . .. 46

10.5.1 Information content. .. 46   
10.5.2 Information update intervals .47

10.6 Initialisation period . . 49

10.6.1 Purpose.. .. 49   
10.6.2 Method of measurement . .49   
10.6.3 Required results .. 49

10.7 Alarms and indications, fall-back arrangements . 49

10.7.1 Built in integrity test . .. 49   
10.7.2 Transceiver protection . . 50   
10.7.3 Transmitter shutdown procedure.. . 50   
10.7.4 Position sensor fallback conditions . 50

10.8 User interface .51

10.8.1 Status indication . . 51   
10.8.2 Message display ....... .. 51   
10.8.3 Static data input . . 52

11 Physical tests . ... 53

11.1 TDMA transmitter. .53

11.1.1 Frequency error ..... ... 53   
11.1.2 Carrier power...... ... 53   
11.1.3 Transmission spectrum ..... .54   
11.1.4 Modulation accuracy. . 55   
11.1.5 Transmitter output power versus time function . .56

11.2 TDMA receivers . .57

11.2.1 Sensitivity .. .57   
11.2.2 Error behaviour at high input levels. .58   
11.2.3 Co-channel rejection. .58   
11.2.4 Adjacent channel selectivity.. .59   
11.2.5 Spurious response rejection . .... 60   
11.2.6 Intermodulation response rejection .62   
11.2.7 Blocking or desensitisation .63

11.3 Conducted spurious emissions. .64

11.3.1 Spurious emissions from the receiver . .64   
11.3.2 Spurious emissions from the transmitter .... ... 64

12 Specific tests of link layer . .65

12.1 TDMA synchronisation . .65

12.1.1 Synchronisation test using UTC direct and indirect . . 65   
12.1.2 Synchronisation test without UTC, EUT receiving semaphore . .66

12.2 Time division (frame format) . ... 66

12.2.1 Purpose.. .. 66   
12.2.2 Method of measurement . .66   
12.2.3 Required results .. .. 66

12.3 Synchronisation jitter ...... .... 66

12.3.1 Definition . .66   
12.3.2 Purpose... .67   
12.3.3 Method of measurement . .67   
12.3.4 Required results . 67

12.4 Data encoding (bit stuffing) ....... .. 67

12.4.1 Purpose ..... .67   
12.4.2 Method of measurement . .67   
12.4.3 Required results . 67

12.5 Frame check sequence . .67

12.5.1 Purpose.. .. 67   
12.5.2 Method of measurement . .67   
12.5.3 Required results .. . 67

12.6 Slot allocation (channel access protocols).. .68

12.6.1 Network entry . .68   
12.6.2 Autonomous scheduled transmissions (SOTDMA) . .68   
12.6.3 Autonomous scheduled transmissions (ITDMA) ...... .... 68   
12.6.4 Transmission of Messages 24A and 24B (ITDMA) .68   
12.6.5 Assigned operation . . 69   
12.6.6 Group assignment .. .71   
12.6.7 Base station reservations .75

12.7 Message formats .75

12.7.1 Received messages. . 75   
12.7.2 Transmitted messages.. .75

13 Specific tests of network layer ........ ... 76

13.1 Regional area designation by VDL Message . . 76

13.1.1 Purpose.. . 76   
13.1.2 Method of measurement . .76   
13.1.3 Required results . .77

13.2 Channel management by addressed Message 22 . .. 78

13.2.1 Purpose.. . 78   
13.2.2 Method of measurement . .78   
13.2.3 Required results .78

13.3 Invalid regional operating areas . .78

13.3.1 Purpose.. . 78   
13.3.2 Method of measurement .78   
13.3.3 Required results .78

13.4 Continuation of autonomous mode reporting interval. .78

13.4.1 Purpose.. .78   
13.4.2 Method of test.. .79   
13.4.3 Required result . .79

13.5 Slot reuse and FATDMA reservations . ... .. 79

13.5.1 Method of measurement .79

13.5.2 Required results .. 79   
13.6 Long-range application by broadcast.. .79   
13.6.1 Long-range broadcast. . 79   
13.6.2 Multiple assignment operation .80

13.7 Other features.. . 81

Annex A (normative) DSC channel management ... .82

A.1 DSC functionality . . 82   
A.2 DSC time sharing ......... .82   
A.3 DSC test signals . 83

A.3.1 DSC test signal number 1 . .83   
A.3.2 DSC test signal number 2 . . 83   
A.3.3 DSC test signal number 3 . .83   
A.3.4 DSC test signal number 4 . .83

A.4 DSC functionality tests. .83

A.4.1 General . .83   
A.4.2 Method of measurement .83   
A.4.3 Required results . .84   
A.4.4 Regional area designation .84   
A.4.5 Scheduling . .84   
A.4.6 DSC flag in Message 18 . .84   
A.4.7 DSC monitoring time plan ...... .... 85   
A.4.8 Replacement or erasure of dated or remote regional operating settings .........85   
A.4.9 Test of addressed telecommand . .86   
A.4.10 Invalid regional operating areas ..... ... 86

A.5 DSC receiver tests . .86

A.5.1 General . .86   
A.5.2 Maximum sensitivity. . 87   
A.5.3 Error behaviour at high input levels .87   
A.5.4 Co-channel rejection...... . 87   
A.5.5 Adjacent channel selectivity....... .. 88   
A.5.6 Spurious response rejection .88   
A.5.7 Inter-modulation response rejection . .88   
A.5.8 Blocking or desensitisation . .89

Annex B (normative) Calculation of area size . .. 90

B.1 Importance of a common method for area size . .90   
B.2 Calculation of area sizes . .90

Annex C (informative) Digital interface sentence to parameter group number equivalence . .91

Bibliography... .92

Figure 1 – OSI layer model . .. 21   
Figure 2 – Power versus time mask . .25   
Figure 3 – Format for repeating four-packet cluster. .. 33   
Figure 4 – Measurement arrangement for carrier power .......... .. 53   
Figure 5 – Emission mask . . 55   
Figure 6 – Measurement arrangement for modulation accuracy .......... .. 55   
Figure 7 – Measurement arrangement . .. 57   
Figure 8 – Measurement arrangement with two generators .58

Figure 9 – SINAD or PER/BER measuring equipment . . 61   
Figure 10 – Measurement arrangement for intermodulation.. . 62   
Figure 11 – Regional transitional zones ........ ... 77   
Table 1 – Dynamic information autonomous reporting intervals for Class B "SO" AIS........ .... 16   
Table 2 – BIIT and reaction to malfunctions . .18   
Table 3 – Position sensor fallback conditions . .19   
Table 4 – Required receiver performance . 22   
Table 5 – Transceiver characteristics. . 22   
Table 6 – Transmitter characteristics .24   
Table 7 – Definitions of timing for Figure 2 . . 26   
Table 8 – Use of VDL Messages by a Class B "SO" AIS .. 29   
Table 9 – Content of first two packets . 34   
Table 10 – Fixed PRS data derived from ITU-T O.153. . 34   
Table 11 – Test.. .37   
Table 12 – Peak frequency deviation versus time. .56   
Table 13 – Frequencies for intermodulation test. .63   
Table 14 – Regional area scenario. .77   
Table 15 – Required channels in use . .77   
Table A.1 – DSC monitoring times . . 83   
Table B.1 – Coordinate points. .90   
Table C.1 – Digital sentence to PGN equivalence . . 91

# INTERNATIONAL ELECTROTECHNICAL COMMISSION

# MARITIME NAVIGATION AND RADIOCOMMUNICATION EQUIPMENT AND SYSTEMS – CLASS B SHIPBORNE EQUIPMENT OF THE AUTOMATIC IDENTIFICATION SYSTEM (AIS) –

# Part 2: Self-organising time division multiple access (SOTDMA) techniques

# FOREWORD

1) The International Electrotechnical Commission (IEC) is a worldwide organization for standardization comprising all national electrotechnical committees (IEC National Committees). The object of IEC is to promote international co-operation on all questions concerning standardization in the electrical and electronic fields. To this end and in addition to other activities, IEC publishes International Standards, Technical Specifications, Technical Reports, Publicly Available Specifications (PAS) and Guides (hereafter referred to as “IEC Publication(s)”). Their preparation is entrusted to technical committees; any IEC National Committee interested in the subject dealt with may participate in this preparatory work. International, governmental and nongovernmental organizations liaising with the IEC also participate in this preparation. IEC collaborates closely with the International Organization for Standardization (ISO) in accordance with conditions determined by agreement between the two organizations.   
2) The formal decisions or agreements of IEC on technical matters express, as nearly as possible, an international consensus of opinion on the relevant subjects since each technical committee has representation from all interested IEC National Committees.   
3) IEC Publications have the form of recommendations for international use and are accepted by IEC National Committees in that sense. While all reasonable efforts are made to ensure that the technical content of IEC Publications is accurate, IEC cannot be held responsible for the way in which they are used or for any misinterpretation by any end user.   
4) In order to promote international uniformity, IEC National Committees undertake to apply IEC Publications transparently to the maximum extent possible in their national and regional publications. Any divergence between any IEC Publication and the corresponding national or regional publication shall be clearly indicated in the latter.   
5) IEC itself does not provide any attestation of conformity. Independent certification bodies provide conformity assessment services and, in some areas, access to IEC marks of conformity. IEC is not responsible for any services carried out by independent certification bodies.   
6) All users should ensure that they have the latest edition of this publication.   
7) No liability shall attach to IEC or its directors, employees, servants or agents including individual experts and members of its technical committees and IEC National Committees for any personal injury, property damage or other damage of any nature whatsoever, whether direct or indirect, or for costs (including legal fees) and expenses arising out of the publication, use of, or reliance upon, this IEC Publication or any other IEC Publications.   
8) Attention is drawn to the Normative references cited in this publication. Use of the referenced publications is indispensable for the correct application of this publication.   
9) Attention is drawn to the possibility that some of the elements of this IEC Publication may be the subject of patent rights. IEC shall not be held responsible for identifying any or all such patent rights.

International Standard IEC 62287-2 has been prepared by IEC technical committee 80: Maritime navigation and radiocommunication equipment and systems.

This second edition cancels and replaces the first edition published in 2013. It constitutes a technical revision.

This edition includes the following significant technical change with respect to the previous edition: the introduction of transmission of Message 27 on channels 75 and 76 for the long range application by broadcast.

The text of this document is based on the following documents:

<table><tr><td>FDIS</td><td>Report on voting</td></tr><tr><td>80/827/FDIS</td><td>80/836/RVD</td></tr></table>

Full information on the voting for the approval of this document can be found in the report on voting indicated in the above table.

This publication has been drafted in accordance with the ISO/IEC Directives, Part 2.

A list of all parts in the IEC 62287 series, published under the general title Maritime navigation and radiocommunication and systems – Class B shipborne equipment of the automatic identification system (AIS), can be found on the IEC website.

The committee has decided that the contents of this publication will remain unchanged until the stability date indicated on the IEC web site under "http://webstore.iec.ch" in the data related to the specific publication. At this date, the publication will be

reconfirmed,   
withdrawn,   
• replaced by a revised edition, or   
amended.

A bilingual version of this publication may be issued at a later date.

IMPORTANT – The 'colour inside' logo on the cover page of this publication indicates that it contains colours which are considered to be useful for the correct understanding of its contents. Users should therefore print this document using a colour printer.

# MARITIME NAVIGATION AND RADIOCOMMUNICATION EQUIPMENT AND SYSTEMS – CLASS B SHIPBORNE EQUIPMENT OF THE AUTOMATIC IDENTIFICATION SYSTEM (AIS) –

# Part 2: Self-organising time division multiple access (SOTDMA) techniques

# 1 Scope

This part of IEC 62287 specifies operational and performance requirements, methods of testing and required test results for Class B "SO" shipborne automatic identifications system (AIS) equipment using self-organising time division multiple access (SOTDMA) techniques as described in Recommendation ITU-R M.1371. This document takes into account other associated IEC International Standards and existing national standards, as applicable.

The main differences between Class B "CS" (IEC 62287-1) and Class B "SO" units are that the Class B "SO"

• covers all 25 kHz channels listed in Recommendation ITU-R M.1084-5,   
• only uses the internal GNSS – no position sensor input is allowed,   
• requires use of VDL Message 17 for correction of the internal GNSS,   
• requires a presentation interface,   
• has additional reporting intervals, down to 5 s,   
• has two power settings, with a high level of 5 W, and   
• has the capability to transmit binary messages.

This document is applicable for AIS equipment used on craft that are not covered by a mandatory carriage requirement of AIS under SOLAS Chapter V.

# 2 Normative references

The following documents are referred to in the text in such a way that some or all of their content constitutes requirements of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.

IEC 60945:2002, Maritime navigation and radiocommunication equipment and systems – General requirements – Methods of testing and required test results

IEC 61108 (all parts), Maritime navigation and radiocommunication equipment and systems – Global navigation satellite systems (GNSS)

IEC 61108-4, Maritime navigation and radiocommunication equipment and systems – Global navigation satellite systems (GNSS) – Part 4: Shipborne DGPS and DGLONASS maritime radio beacon receiver equipment – Performance requirements, methods of testing and required test results

IEC 61162-1, Maritime navigation and radiocommunication equipment and systems – Digital interfaces – Part 1: Single talker and multiple listeners

IEC 61993-2, Maritime navigation and radio communication equipment and systems – Automatic identification systems (AIS) – Part 2: Class A shipborne equipment of the automatic identification system (AIS) – Operational and performance requirements, methods of test and required test results

ITU Radio regulations:2012

ITU-R Recommendation M.825-3:1998, Characteristics of a transponder system using digital selective calling techniques for use with vessel traffic services and ship-to-ship identification

ITU-R Recommendation M.1084-5:2012, Interim solutions for improved efficiency in the use of the band 156-174 MHz by stations in the maritime mobile service

ITU-R Recommendation M.1371-5:2014, Technical characteristics for an automatic identification system using time division multiple access in the VHF maritime mobile band

# 3 Terms, definitions and abbreviated terms

# 3.1 Terms and definitions

No terms and definitions are listed in this document.

ISO and IEC maintain terminological databases for use in standardization at the following addresses:

• IEC Electropedia: available at http://www.electropedia.org/   
• ISO Online browsing platform: available at http://www.iso.org/obp

# 3.2 Abbreviated terms

AIS automatic identification system

BER bit error rate

BIIT built-in integrity tests

BT bandwidth time

COG course over ground

CRC cyclic redundancy check

CSD compass safe distance

DGNSS differential global navigation satellite service

DLS data link service

DSC digital selective calling

EUT equipment under test

FM frequency modulation

GMSK gaussian minimum shift keying

GNSS global navigation satellite service

IMO International Maritime Organization

ITDMA incremental time division multiple access

ITU International Telecommunication Union

LME link management entity

MAC medium access control

MMSI maritime mobile service identity

NM nautical mile $( 1 ~ \mathsf { N M } = 1 ~ 8 5 2 ~ \mathsf { m } )$ )

<table><tr><td>NRZI</td><td>non return to zero inverted</td></tr><tr><td>OSI</td><td>open systems interconnection model</td></tr><tr><td>PER</td><td>packet error rate</td></tr><tr><td>PI</td><td>presentation interface</td></tr><tr><td>RAIM</td><td>receiver autonomous integrity monitoring</td></tr><tr><td>RATDMA</td><td>random access time division multiple access</td></tr><tr><td>RF</td><td>radio frequency</td></tr><tr><td>RR</td><td>Radio Regulations</td></tr><tr><td>Rx</td><td>Receive</td></tr><tr><td>SAR</td><td>Search and rescue</td></tr><tr><td>SINAD</td><td>signal interference noise and distortion ratio</td></tr><tr><td>SOG</td><td>speed over ground</td></tr><tr><td>SOTDMA</td><td>self organised time division multiple access</td></tr><tr><td>TDMA</td><td>dime division multiple access</td></tr><tr><td>Tx</td><td>Transmit</td></tr><tr><td>UTC</td><td>universal time co-ordinated</td></tr><tr><td>VDL</td><td>VHF data link</td></tr><tr><td>VHF</td><td>very high frequency</td></tr><tr><td>VSWR</td><td>voltage standing wave ratio</td></tr><tr><td>VTS</td><td>vessel traffic services</td></tr></table>

# 4 General requirements

# 4.1 General

# 4.1.1 Capabilities of the Class B "SO" AIS

The Class B "SO" AIS shall improve the safety of navigation by assisting in the efficient navigation of ships and small craft, protection of the environment, and operation of vessel traffic services (VTS).

The Class B "SO" AIS station shall be inter-operable and compatible with all AIS stations operating on the AIS VHF Data Link. In particular, Class B "SO" AIS stations shall not degrade the integrity of the AIS VHF data link.

The Class B "SO" AIS shall be capable of providing information from the craft, automatically, continuously and with the required accuracy and update rate

• in a ship-to-ship mode for collision avoidance,   
• as a means for littoral States to obtain information about the craft, and   
• as a VTS tool, i.e. ship-to-shore (traffic management).

# 4.1.2 Quality assurance

(See 10.1.1)

Manufacturers shall have a quality control system audited by a competent authority to ensure continuous compliance with the requirements of this document. Alternatively, the manufacturer may use final product verification procedures where a competent authority verifies compliance with the requirements of this document before the product is put to the market.

NOTE ISO 9000 (all parts), as applicable, meets the requirements of a quality control system.

# 4.1.3 Safety of operation

(See 10.1.2)

It shall not be possible for the operator to augment, amend or erase any program software required for operation in accordance with this document. The manufacturer may provide means to install software updates.

Data used during operation and stored in the system shall be protected in such a way that necessary modifications and amendments by the user cannot endanger its integrity and correctness.

# 4.1.4 Additional features

(See 10.1.3, 13.7)

Where equipment provides a feature that is additional to the minimum requirements and options of this document, the operation and, as far as is reasonably practicable, the malfunction of such additional features shall not degrade the performance of the equipment.

# 4.1.5 Functionality

The equipment shall operate in three modes (see 7.3.4.3):

autonomous (default mode);   
assigned;   
• interrogation.

# 4.2 Manuals

(See 10.1.1)

The manuals shall include

• the type of external connectors, if applicable,   
• the information for correct installation and positioning of the antennas, and   
• the information for compass safe distance.

# 4.3 Marking and identification

(See 10.1.1)

In addition to the requirements of IEC 60945:2002, 4.9, the markings shall include

• details of the power supply from which the equipment is intended to be operated, and   
• if applicable, the date by which batteries need to be replaced.

# 5 Environmental, power supply, interference and safety requirements

(See Clause 9)

In addition to the specific requirements of this document, the Class B "SO" AIS shall fulfil the following general requirements as detailed in IEC 60945:

inter-unit connection (electrical interfaces other than IEC 61162-1, for instance IEC 61162-450, are permissible);   
• power supply;   
• extreme power supply;

• excessive conditions;   
• power supply short-term variation and power supply failure;   
• durability and resistance to environmental conditions;   
interference;   
• electromagnetic compatibility;   
• compass safe distance;   
• safety precautions;   
• protection against accidental access to dangerous voltages;   
• electromagnetic radiofrequency radiation.

The Class B "SO" AIS shall not enter an undefined or unstable state in case of under voltage.

The manufacturer shall declare the category of the equipment as follows:

a) portable;   
b) protected from the weather;   
c) exposed to the weather;   
d) submerged or in continuous contact with sea water.

The Class B "SO" AIS shall be tested for compliance with the environmental, power supply, special purpose and safety requirements of IEC 60945:

AIS equipment declared for protected installation shall meet the requirements described in Table 3, column "Protected", of IEC 60945:2002;   
exposed AIS equipment shall meet the requirements described in Table 3, column "Exposed", of IEC 60945:2002;   
portable AIS equipment shall meet the requirements of Table 3, colums "Protected" or "Exposed", as appropriate, of IEC 60945:2002.

In addition, the AIS installation, when operating, shall not be damaged by the effects of open circuited or short circuited antenna terminals.

# 6 Performance requirements

# 6.1 Internal processes

(See 10.1.1)

The Class B "SO" AIS shall comprise

• a communication processor, capable of operating in the VHF maritime mobile service band,   
• at least one transmitter and two receiving processes for TDMA operation,   
• a third receiving process for DSC channel management,   
a means for automatic channel switching in the maritime mobile band (by Message 22 and by DSC) – manual channel switching shall not be provided –, and   
an internal GNSS position sensor, which provides a resolution of one ten thousandth of a minute of arc and uses the WGS-84 datum only.

# 6.2 Operating frequency channels

(See 10.3)

The Class B "SO" AIS shall be designed to operate with $2 5 ~ \mathsf { k H z }$ bandwidth (see 7.2.3.3) in the range from 156,025 MHz to 162,025 MHz of the ITU Radio Regulations:2012, Appendix 18, and in accordance with Recommendation ITU-R M.1084-5:2012, Annex 4.

The Class B "SO" AIS shall indicate its capabilities of channel operation in the VHF maritime mobile band with the flag settings of Message 18 (see 6.5.1.3).

The DSC receiving process shall be tuned to VHF Channel 70 (see 7.2.3.7).

# 6.3 Internal GNSS receiver for position reporting

(See 10.4)

The Class B "SO" AIS shall have an internal GNSS receiver as the only source for position, COG and SOG except for test purposes.

The internal GNSS receiver shall meet the following requirements of a receiver as specified in IEC 61108 (all parts):

• position accuracy; static and dynamic;   
• COG/SOG accuracy;   
• position update;   
• interference susceptibility;   
• status indications (RAIM optional);   
• WGS-84 datum positions.

The internal GNSS receiver shall be capable of being differentially corrected by Message 17.

Optionally, in addition to Message 17, the Class B "SO" AIS may be differentially corrected by a radio beacon. If the radio beacon option is implemented, it shall be tested in accordance with IEC 61108-4.

# 6.4 Identification

(See 10.8.3)

For the purpose of ship and message identification, the appropriate maritime mobile service identity (MMSI) number shall be used.

The unit shall be supplied with a default MMSI of "000000000" that is not a valid MMSI.

The unit shall check that any programmed MMSI is between 200000000 and 799999999 or between 982000000 and 987999999, otherwise the unit shall reject the programming and not be capable of transmitting.

# 6.5 AIS Information

# 6.5.1 Information content

(See 10.5.1)

# 6.5.1.1 Static and voyage related (Messages 19, 24A and 24B)

The list of static information shall include the following:

• identification (MMSI);   
name of ship;   
• type of ship;   
• vendor ID (unit should respond to interrogation for Message 24B);   
• call sign;   
• dimensions of ship and reference for position.

The default value for type of ship shall be 37 (pleasure craft). Defaults for other static data shall be chosen such that it is obvious that the equipment has been properly initialised, in particular, the default MMSI shall be set to 000000000 and the equipment shall be designed such that transmissions are inhibited with this default setting.

# 6.5.1.2 Dynamic (Message 18)

The list of dynamic information shall include the following:

• ship's position with accuracy indication and integrity status;   
• UTC second when position fix was generated;   
• course over ground (COG) from internal GNSS;   
• speed over ground (SOG) from internal GNSS;   
• true heading (optional).

# 6.5.1.3 Configuration information (Message 18)

The following information about configuration and options active in the specific unit shall be provided by flag settings in Message 18:

• type of AIS Class B unit;   
• availability of minimum keyboard/display facility;   
• availability of DSC Channel 70 receiver;   
• ability to operate in the marine VHF band;   
• ability to process channel management Message 22.

# 6.5.2 Information reporting intervals

(See 10.5.2, 10.6)

The reporting interval for Static and Voyage related information shall be every 6 min, when data has been amended, or upon interrogation.

The reporting interval for dynamic information shall be as stated in Table 1.

Table 1 – Dynamic information autonomous reporting intervals for Class B "SO" AIS   

<table><tr><td>Condition</td><td>Nominal reporting interval</td><td>Increased reporting interval</td></tr><tr><td>Class B &quot;SO&quot; AIS Mobile Equipment moving &lt; 2 kn</td><td>3 min</td><td>3 min</td></tr><tr><td>Class B &quot;SO&quot; AIS Mobile Equipment moving at 2 kn to 14 kn</td><td>30 s</td><td>30 s</td></tr><tr><td>Class B &quot;SO&quot; AIS Mobile Equipment moving at 14 kn to 23 kn</td><td>15 s</td><td>30 s</td></tr><tr><td>Class B &quot;SO&quot; AIS Mobile Equipment moving &gt; 23 kn</td><td>5 s</td><td>15 s</td></tr></table>

The Class B "SO" AIS shall follow the rules set by Recommendation ITU-R M.1371, and shall increase the reporting interval to "increased reporting interval" in accordance with Table 1 when less than $50 \%$ of the slots of each of the last four consecutive frames are free. When more than $65 \%$ of the slots of each of the last four consecutive frames are free, the Class B "SO" AIS shall report at the "nominal reporting interval".

An assignment command, received by Message 16 or Message 23, may decrease or increase the reporting interval defined by Table 1 (see 4.1.5).

A reporting interval of less than 5 s shall not be required.

An assignment using Message 16 has priority over an assignment using Message 23.

When the BIIT determines that the position sensor is unavailable, the Class B "SO" AIS shall maintain a reporting interval of 3 min (see 6.6.1).

# 6.5.3 Short safety-related messages

(See 10.2.2.5)

Short safety-related messages as described in Recommendation ITU-R M.1371 (Message 14) shall not be provided.

NOTE IMO COMSAR.1/Circ.46:2009-02 advises that "short safety-related messages should not be incorporated in AIS equipment because there is no SAR infrastructure in place to accommodate them".

# 6.5.4 Permissible initialisation period

(See 10.6)

The AIS unit shall be operational within 2 min of switching on.

# 6.6 Alarms and indications, fall-back arrangements

(See 10.7)

# 6.6.1 Built-in integrity tests (BIIT)

The Class B "SO" AIS shall have BIIT which monitor the processes listed in Table 2.

Any BIIT failure shall set the error indicator as defined in 6.7.1.

The Class B "SO" AIS reacts to BIIT malfunctions as indicated in Table 2.

Table 2 – BIIT and reaction to malfunctions   

<table><tr><td>Test</td><td>Reaction to malfunction</td></tr><tr><td>AIS: Tx malfunction</td><td>Stop transmission</td></tr><tr><td>AIS: Antenna VSWR exceeds limit</td><td>Continue operation</td></tr><tr><td>AIS: Rx channel 1 malfunction</td><td>Stop transmission on affected channel</td></tr><tr><td>AIS: Rx channel 2 malfunction</td><td>Stop transmission on affected channel</td></tr><tr><td>AIS: Rx channel 70 malfunction</td><td>Continue operationa</td></tr><tr><td>AIS: general failure</td><td>Stop transmission</td></tr><tr><td>AIS: UTC sync invalid</td><td>Continue operation using indirect or semaphore synchronisation</td></tr><tr><td>AIS: display connection lost</td><td>Continue operation with &quot;Class B Display Flag&quot; of message 18 set to &quot;0&quot; a</td></tr><tr><td>AIS: no sensor position in use</td><td>Continue operation at 3 minute reporting interval</td></tr><tr><td>AIS: no valid SOG information</td><td>Continue operation using SOG = 1 023</td></tr><tr><td>AIS: no valid COG information</td><td>Continue operation using COG = 3 600</td></tr><tr><td>AIS: Heading lost/invalid</td><td>Continue operation using Heading = 511a</td></tr><tr><td colspan="2">a Alarm may be enabled/disabled depending on system configuration.</td></tr></table>

Alarm messages shall be output via a presentation interface:

• alarm codes and descriptive text shall be compliant with IEC 61993-2;   
• the alarm message protocol shall be compliant with IEC 61162-1;   
active alarms shall be output via the presentation interface upon occurrence and repeated every 30 s;   
• non-active alarm messages shall be repeated every 60 s;   
• upon a relevant system status change, an appropriate alarm message shall be output.

# 6.6.2 Transmitter shutdown procedure

An automatic transmitter hardware shutdown procedure and indication should be provided in case a transmitter continues to transmit for more than 2 s. This shutdown procedure should be independent of software control.

# 6.6.3 Position sensor fallback conditions

Priorities and affected position report data (refer to Recommendation ITU-R M.1371-5) shall be as in Table 3.

Table 3 – Position sensor fallback conditions   

<table><tr><td rowspan="2">Priority</td><td rowspan="2" colspan="2">Position sensor status</td><td colspan="4">Affected data in Message 18</td></tr><tr><td>Position accuracy flag</td><td>Time stamp</td><td>RAIM-flag</td><td>Position Latitude/Longitude</td></tr><tr><td>1.</td><td colspan="2">internal DGNSS in use (corrected; Message 17)c</td><td>1b</td><td>UTC-s</td><td>1 / 0a</td><td>Lat/Lon (internal)</td></tr><tr><td>2.</td><td colspan="2">internal DGNSS in use (corrected; e.g. beacon)d</td><td>1a</td><td>UTC-s</td><td>1 / 0a</td><td>Lat/Lon (internal)</td></tr><tr><td>3.</td><td colspan="2">internal GNSS in use (uncorrected)c</td><td>0b</td><td>UTC-s</td><td>1 / 0a</td><td>Lat/Lon (internal)</td></tr><tr><td>4.</td><td rowspan="2">no sensor position in use</td><td>dead reckoning position</td><td rowspan="2">0</td><td>62</td><td rowspan="2">0</td><td rowspan="2">Default to +91/+181</td></tr><tr><td></td><td>no position</td><td>63</td></tr><tr><td colspan="7">aIf RAIM available &quot;1&quot;; if not, default &quot;0&quot;.bThe position accuracy flag shall be set as defined in ITU-R M.1371-5:2014, Annex 8, 3.16 Message 18.cApplicable in all configurations (minimum requirement).dApplicable only if (optionally) a beacon receiver is provided.</td></tr></table>

The AIS shall automatically select the position sensor status with the highest priority available. If data availability changes, the AIS shall automatically switch to the position sensor status with the highest priority available after 5 s when switching downwards, or 30 s when switching upwards. During this period, the latest valid position sensor status shall be used for reporting.

# 6.7 User interface

# 6.7.1 Indication and display

(See 10.8.1)

The Class B "SO" AIS shall be provided with the following indicators:

Power: power on

No transmission: the unit is not transmitting

Error: detection of an error as a result of the BIIT (see 6.6.1).

If an integrated display is provided, it shall

display received Messages 12 and 14 and the position report from AIS-SART in active mode,   
provide means to enable or disable the AIS-SART test mode – all messages from AIS-SART under test should only be displayed when the test mode is enabled – ,   
• not display messages addressed to other stations, and   
• display active alarm conditions.

# 6.7.2 Static data input

(See 10.8.3)

Means shall be provided to input and verify the static data prior to use.

It shall not be possible for the user to alter the MMSI once programmed.

# 6.7.3 External interfaces

(See 10.2.1.2)

To enable a user to access, select and display the information on a separate system, the Class B "SO" AIS shall be provided with at least one interface.

The formats and protocol for this data stream shall be as defined by IEC 61162-1. Additional interfaces may be implemented such as IEC 61162-450. The electrical and physical parameters shall be as specified by the manufacturer.

NOTE Additional optional digital interface network IEC 61162-3 parameter group numbers equivalent to the specified network IEC 61162-1 sentences are described for information in Annex C.

The Class B "SO" AIS may be provided with an interface to input heading sensor data. If provided, the input interface for sensor data shall be compliant with IEC 61162-1.

# 6.8 Protection from invalid control commands

(See 8.5.8)

The Class B "SO" AIS shall not accept control commands sent from stations with invalid base station MMSI. Before accepting and processing the Messages 4, 16, 17, 20, 22 and 23, the unit shall check the MMSI of the sender station. When the MMSI is "00xyyyyyy" where x is between 2 and 7, the unit shall accept and process the received command, otherwise the unit shall ignore it.

# 7 Technical requirements

# 7.1 General

Clause 7 covers layers 1 to 4 (physical layer, link layer, network layer, transport layer) of the open systems interconnection (OSI) model.

Figure 1 illustrates the layer model of an AIS station (physical layer to transport layer) and the layers of the applications (session layer to application layer):

![](images/6f6899cf4190e6425e5eb11066888254843075c9ed183baa9b3f9ec1f73a6b5a.jpg)  
Figure 1 – OSI layer model

# 7.2 Physical layer

# 7.2.1 General

The physical layer is responsible for the transfer of a bit-stream from an originator out, on to the data link. In addition to the specific requirements of 7.2, the physical layer shall be designed in accordance with Recommendation ITU-R M.1371.

# 7.2.2 Receiver characteristics

(See 11.2, 11.3.1)

The technical characteristics as specified in Table 4 shall apply to the TDMA receivers.

Table 4 – Required receiver performance   

<table><tr><td rowspan="2">Receiver parameters</td><td colspan="3">Values</td></tr><tr><td>Results</td><td>Wanted signal</td><td>Unwanted signal(s)</td></tr><tr><td rowspan="3">Sensitivity</td><td rowspan="3">20 % per</td><td>-107 dBm normal</td><td rowspan="3">-</td></tr><tr><td>-101 dBm extreme</td></tr><tr><td>-104 dBm at ± 500 Hz offset</td></tr><tr><td rowspan="2">Error at high input levels</td><td>2 % per</td><td>-77 dBm</td><td>-</td></tr><tr><td>10 % per</td><td>-7 dBm</td><td>-</td></tr><tr><td rowspan="3">Co-channel rejection</td><td rowspan="3">20 % per</td><td rowspan="3">-101 dBm</td><td>-111 dBm</td></tr><tr><td>-111 dBm at</td></tr><tr><td>±1 kHz offset</td></tr><tr><td>Adjacent channel selectivity</td><td>20 % per</td><td>-101 dBm</td><td>-31 dBm</td></tr><tr><td>Spurious response rejection</td><td>20 % per</td><td>-101 dBm</td><td>-31 dBm</td></tr><tr><td>Intermodulation response rejection</td><td>20 % per</td><td>-101 dBm</td><td>-36 dBm</td></tr><tr><td rowspan="2">Blocking and desensitization</td><td rowspan="2">20 % per</td><td rowspan="2">-101 dBm</td><td>-23 dBm (&lt; 5 MHz)</td></tr><tr><td>-15 dBm (&gt; 5 MHz)</td></tr><tr><td rowspan="2">Spurious emissions</td><td>-57 dBm</td><td colspan="2">9 kHz to 1 GHz</td></tr><tr><td>-47 dBm</td><td colspan="2">1 GHz to 4 GHz</td></tr></table>

# 7.2.3 Other characteristics

# 7.2.3.1 General transceiver characteristics

(See Clause 11)

General transceiver characteristics shall be as specified in Table 5.

Table 5 – Transceiver characteristics   

<table><tr><td>Symbol</td><td>Parameter name</td><td>Low setting</td><td>High setting</td></tr><tr><td>PH.RFR</td><td>Regional frequencies (range of frequencies within RR:2012, Appendix 18)</td><td>156,025 MHz</td><td>162,025 MHz</td></tr><tr><td>PH.CHS</td><td>Channel spacing (coded according to RR:2012, Appendix 18 with footnotes)</td><td>25 kHz</td><td>25 kHz</td></tr><tr><td>PH.AIS1</td><td>AIS 1 (default channel 1) (2 087)a</td><td>161,975 MHz</td><td>161,975 MHz</td></tr><tr><td>PH.AIS2</td><td>AIS 2 (default channel 2) (2 088)a</td><td>162,025 MHz</td><td>162,025 MHz</td></tr><tr><td>PH.BR</td><td>Bit rate</td><td>9 600 bit/s</td><td>9 600 bit/s</td></tr><tr><td>PH.TS</td><td>Training sequence</td><td>24 bits</td><td>24 bits</td></tr><tr><td>PH.TxBT</td><td>Transmit BT product</td><td>~0,4</td><td>~0,4</td></tr><tr><td>PH.RxBT</td><td>Receive BT product</td><td>~0,5</td><td>~0,5</td></tr><tr><td>PH.MI</td><td>Modulation index</td><td>~0,5</td><td>~0,5</td></tr><tr><td>PH.TxP</td><td>Transmit output power</td><td>1 W</td><td>5 W</td></tr><tr><td colspan="4">a See Recommendation ITU-R M.1084-5:2012, Annex 4.</td></tr></table>

# 7.2.3.2 Channel operation

(See 10.2.1.1)

The AIS shall be capable of receiving on two parallel channels and transmitting on two separate channels. Two separate TDMA receive channels or processes shall be used to receive simultaneously information on two independent frequency channels. One TDMA

transmitter shall be used to alternate TDMA transmissions on two independent frequency channels.

Data transmissions and receptions shall default to AIS 1 and AIS 2 unless otherwise specified (see 7.4.3 and Annex A).

# 7.2.3.3 Bandwidth

(See 11.1.3)

The Class B "SO" AIS shall operate on 25 kHz channels according to Recommendation ITU R M.1084-5 and ITU Radio Regulations:2012, Appendix 18.

# 7.2.3.4 Modulation scheme

(See 11.1.4)

The modulation scheme is bandwidth adapted frequency modulated Gaussian filtered minimum shift keying (GMSK/FM). The NRZI encoded data shall be GMSK coded before frequency modulating the transmitter.

# 7.2.3.5 Training sequence

(See 11.1.4)

Data transmission shall begin with a 24-bit demodulator training sequence (preamble) consisting of one segment synchronisation. This segment shall consist of alternating zeros and ones (0101....). This sequence always starts with a 0.

# 7.2.3.6 Data encoding

(See 12.4)

The NRZI waveform is used for data encoding. The waveform is specified as giving a change in the level when a zero (0) is encountered in the bit stream.

Forward error correction, interleaving or bit scrambling is not used.

# 7.2.3.7 DSC operation

(See Annex A)

The Class B "SO" AIS shall be capable of receiving DSC channel management commands (see Annex A).

DSC receive function shall be provided at least in accordance with the time schedule specified in ITU-R M.1371-5:2014, Table 45.

DSC channel (channel 70) shall be monitored by a dedicated receiver or by switching one of the TDMA receivers from the AIS channels to the DSC channel. In order to avoid a new entry phase when switching back the time out, values should be selected so that there is no time out 0 during the DSC receiving period.

# 7.2.4 Transmitter requirements

(See 11.1, 11.3.2)

Transmitter parameters shall be as given in Table 6.

Table 6 – Transmitter characteristics   

<table><tr><td>Transmitter parameters</td><td>Requirement</td><td>Condition</td></tr><tr><td>Frequency error</td><td>±500 Hz normal ±1 000 Hz extreme</td><td></td></tr><tr><td>Carrier power, high setting</td><td>Nominal high transmit power shall be 5 W. ±1,5 dB normal test conditions ±3 dB extreme test conditions</td><td>Conducted</td></tr><tr><td>Carrier power, low setting</td><td>Nominal low transmit power shall be 1 W. ±1,5 dB normal test conditions ±3 dB extreme test conditions</td><td>Conducted</td></tr><tr><td>Modulation spectrum</td><td>-25 dBc -70 dBc</td><td>Δfc&gt;±10 kHz ±25 kHz &lt; Δfc&lt; ±62,5 kHz slotted transmissions</td></tr><tr><td>Modulation accuracy</td><td>&lt; 3 400 Hz normal and extreme 2 400 Hz ± 480 Hz normal and extreme 2 400 Hz ± 240 Hz normal ±480 Hz extreme 1 740 Hz ± 175 Hz normal ±350 Hz extreme 2 400 Hz ± 240 Hz normal ±480 Hz extreme</td><td>Bit 0, 1 Bit 2, 3 Bit 4 ... 31 Bit 32 ... 199 0101 Bit 32 ... 199 00001111</td></tr><tr><td>Transmitter attack behaviour</td><td>attack time ≤ 1 ms Pout ≤ Pnom + 1,5 dB (Fnom - 3,4 kHz) &lt; fc &lt; (Fnom + 3,4 kHz)</td><td>Pc-1 dB Pout &gt; (Pc-30 dB)</td></tr><tr><td>Transmitter release behaviour</td><td>Release time ≤ 1 ms (Fnom - 3,4 kHz) &lt; fc &lt; (Fnom + 3,4 kHz)</td><td>Pc to -50 dB Pout &gt; (Pc-30 dB)</td></tr><tr><td>Spurious emissions</td><td>-36 dBm -30 dBm</td><td>9 kHz ... 1 GHz 1 GHz ... 4 GHz</td></tr></table>

# 7.3 Link layer

(See Clause 12)

# 7.3.1 General

The link layer specifies how data shall be packaged in order to apply error detection to the data transfer. The link layer is divided into three (3) sub-layers.

• Link sub-layer 1: medium access control (MAC)   
• Link sub-layer 2: data link service (DLS)   
• Link sub-layer 3: link management entity (LME)

# 7.3.2 Link sub-layer 1: medium access control (MAC)

# 7.3.2.1 General

The MAC sub-layer provides a method for granting access to the data transfer medium, i.e. the VHF data link. The method used shall be a time division multiple access (TDMA) scheme

using a common time reference. The medium access control sub-layer shall be designed in accordance with Recommendation ITU-R M.1371.

# 7.3.2.2 Synchronisation

Synchronisation is used to determine the TDMA frames and individual time slots so that the transmission of the AIS message is performed within the desired slot. The synchronisation for Class B "SO" AIS shall be UTC direct or UTC indirect mode. Class B "SO" is not allowed to act as Semaphore.

The Class B "SO" AIS shall meet the timing requirements set out in Recommendation ITU-R M.1371 for UTC direct and indirect.

# 7.3.2.3 VDL access

(See 11.1.5)

The transmitter shall begin transmission by turning on the RF power immediately after slot start $( T _ { 0 } )$ .

The transmitter shall be turned off after the last bit of the transmission packet has left the transmitting unit; nominal transmission end is $T _ { \mathsf { E } }$ (assuming 1 stuffing bit).

![](images/8888d0bad56b1fdefcbe44b3badc426f4567761e4a88f73a663ddca1f4ca52de.jpg)  
Figure 2 – Power versus time mask

The access to the medium is performed as shown in Figure 2 and Table 7.

Table 7 – Definitions of timing for Figure 2   

<table><tr><td colspan="2">Reference</td><td>bits</td><td>Time ms</td><td>Definition</td></tr><tr><td colspan="2">T0</td><td>0</td><td>0</td><td>Start of transmission slot. Power shall NOT exceed -50 dB of Pss before T0</td></tr><tr><td colspan="2">TA</td><td>0 to 6</td><td>0 to 0,625</td><td>Power exceeds -50 dB of Pss</td></tr><tr><td rowspan="2">TB</td><td>TB1</td><td>6</td><td>0,625</td><td>Power shall be within +1,5 or -3 dB of Pss</td></tr><tr><td>TB2</td><td>8</td><td>0,833</td><td>Power shall be within +1,5 or -1 dB of Pss (start of training sequence)</td></tr><tr><td colspan="2">TE(includes 1 stuffing bit)</td><td>233</td><td>24,271</td><td>Power shall remain within +1,5 or -1 dB of Pss during the period TB2 to TE</td></tr><tr><td colspan="2">TF(includes 1 stuffing bit)</td><td>241</td><td>25,104</td><td>Power shall be -50 dB of Pss and stay below this</td></tr><tr><td colspan="2">TG</td><td>256</td><td>26,667</td><td>Start of next transmission time period</td></tr></table>

# 7.3.2.4 VDL state

(See 13.5)```

Each slot can be in one of the following states., `,, `

Free: meaning that the slot is unused within the receiving range of the own station. An externally allocated slot that has not been used during the preceding 3 frames is also a free slot. This slot may be considered as a candidate slot for use by own station (refer to ITU-R M.1371-5:2014, Annex 2, 3.3.1.2);   
Internal allocation: meaning that the slot is allocated by own station and can be used for transmission;   
• External allocation: meaning that the slot is allocated for transmission by another station;   
Available: meaning that the slot is externally allocated by a station and is a possible candidate for slot reuse (refer to ITU-R M.1371-5:2014, Annex 2, 4.4.1);   
Unavailable: meaning that the slot is externally allocated by a station. An unavailable slot cannot be a candidate for slot reuse (refer to ITU-R M.1371-5:2014, Annex 2, 4.4.1).

# 7.3.3 Link sub-layer 2: data link service (DLS)

The DLS sub-layer provides methods for

• data link activation and release,   
data transfer, or   
• error detection and control.

The data link service sub-layer shall be designed in accordance with Recommendation ITU-R M.1371.

# 7.3.4 Link sub-layer 3: link management entity (LME)

# 7.3.4.1 General

The LME controls the operation of the DLS, MAC and the physical layer.

The link management entity sub-layer shall be designed in accordance with Recommendation ITU-R M.1371.

# 7.3.4.2 Access algorithm for transmissions

(See 10.2.2.6)

Class B "SO" shall respond to interrogations in the slots allocated when the slot "off set" is provided in the Message 15 where the minimum slot offset is 10 slots.

Class B "SO" shall select slots using ITDMA to respond to interrogations that do not provide a slot "off set". The response shall be transmitted within 30 s. In the event that ITDMA cannot allocate slots within $\mathfrak { Z 0 ~ s }$ , RATDMA shall be used.

The total number of slots for Class B "SO" transmissions of Messages 6, 8, 25 and 26 shall not exceed 3 slots in any frame. The maximum length of Messages 6, 8 and 26 is 2 slots per Message.

Class B "SO" shall transmit Messages 6, 8, 25 and 26 within 30 s and Message 7 and 13 within 4 s, in response to addressed Message 6 and 12.

Class B "SO" shall pre-announce Messages 6, 7, 8, 13, 25 and 26 by using the ITDMA communications state in a scheduled Message 18 if a Message 18 is available in the required transmission interval. Otherwise, RATDMA should be used.

Class B "SO" shall not retransmit Message 6 if no acknowledgement by Message 7 is received.

# 7.3.4.3 Modes of operation

# 7.3.4.3.1 Three modes

There shall be three modes of operation:

autonomous (default mode);   
assigned;   
• interrogation.

# 7.3.4.3.2 Autonomous

(See 10.2.1)

In the "autonomous and continuous" mode of operation, the Class B "SO" AIS shall transmit Message 18 for scheduled position reporting and Message 24A and 24B for static data reporting. Message 24B shall be transmitted within 1 min of Message 24A transmission.

The Class B "SO" AIS shall be able to receive and process Messages at any time except when affected by its own transmission.

# 7.3.4.3.3 Assigned

(See 12.6.5)

A Class B "SO" AIS station operating in the assigned mode shall use a transmission schedule assigned by Messages 16 or 23. The assigned mode command may assign a new reporting interval or time slots to be used for Message 18. The minimum reporting interval is 5 s.

The assigned mode shall affect only the reporting interval of Message 18, and no other behavior shall be affected. Class B "SO" AIS shall maintain a reporting interval of 6 min for Message 24A and 24B, regardless of any assignment command.

Class B "SO" AIS shall be put in the assigned mode when all of the following criteria apply:

• it is in the geographic area specified in Message 23;   
• the "type of ship and cargo type" parameter is as specified in Message 23;   
• the "station type" parameter is as specified in Message 23.

The Mode Flag in Message 18 is set to "1" when in assigned mode. Class B "SO" AIS shall apply a random time-out of between 4 min and 8 min to the assigned mode. This time-out is refreshed every time an assigned mode command is received. After the time-out has elapsed, Class B "SO" AIS shall return to autonomous mode.

A Message 16 assignment takes precedence over a Message 23 assignment. When in a Message 16 assigned mode, Message 23 shall be ignored.

Any individual assignment command received shall take precedence over any group assignment command received, i.e. the following cases shall be applied:

if Message 22 is individually addressed, the Tx/Rx mode field setting of Message 22 shall take precedence over the Tx/Rx mode field setting of Message 23;   
a Message 23 assignment of the "Tx/Rx mode" field setting takes precedence over a Message 22 geographic "Tx/Rx mode" field setting. When the Message 23 assignments time-out, the Class B "SO" reverts to the geographic "Tx/Rx mode" defined by Message 22.

# 7.3.4.3.4 Interrogation

(See 10.2.3)

Class B "SO" AIS shall respond to interrogations for Messages 18, 19, 24A and 24B.

A Class B "SO" AIS shall not have the capability to interrogate other stations.

An autonomous interrogation has no offset and the Class B "SO" AIS selects the slots for response by applying the access algorithm as described in 7.3.4.2. The response shall be transmitted within 30 s of the interrogation.

An assigned interrogation has an offset that determines the slots for the response.

The response shall be transmitted on the channel where the interrogation message was received.

Interrogations for the same message received before own response has been transmitted shall be ignored.

# 7.3.4.4 VDL Message use

(See 10.2.2)

The Messages defined in ITU-R M.1371 shall be used by Class B "SO" AIS as detailed in Table 8.

Table 8 – Use of VDL Messages by a Class B "SO" AIS   

<table><tr><td>Message No.</td><td>Name of message</td><td>ITU-R M.1371-5:2014 Annex 8 ref.</td><td>R/P</td><td>O</td><td>T</td><td>Remark</td></tr><tr><td>0</td><td>Undefined</td><td>None</td><td>Yes</td><td>Yes</td><td>No</td><td>Reserved for future use. If CRC checksum is correct, output on PI.</td></tr><tr><td>1</td><td>Position Report (Scheduled)</td><td>3.1</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>2</td><td>Position Report (Assigned)</td><td>3.1</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>3</td><td>Position Report (When interrogated)</td><td>3.1</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>4</td><td>Base Station Report</td><td>3.2</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>5</td><td>Static and Voyage Related Data</td><td>3.3</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>6</td><td>Addressed Binary Message</td><td>3.4</td><td>Yes</td><td>Yes (1)</td><td>Yes</td><td>(1) Only if addressed to own station.</td></tr><tr><td>7</td><td>Binary Acknowledge</td><td>3.5</td><td>Yes</td><td>INF (1) (2)</td><td>Yes</td><td>(2) An ABK PI Message shall be sent to the PI even if no Message 7 has been received</td></tr><tr><td>8</td><td>Binary Broadcast Message</td><td>3.6</td><td>Yes</td><td>Yes</td><td>Yes</td><td></td></tr><tr><td>9</td><td>Standard SAR Aircraft Position Report</td><td>3.7</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>10</td><td>UTC and Date Inquiry</td><td>3.8</td><td>No</td><td>No</td><td>No</td><td>Operational process not defined by ITU-R M.1371.</td></tr><tr><td>11</td><td>UTC/Date Response</td><td>3.9</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>12</td><td>Addressed Safety Related Message</td><td>3.10</td><td>Yes</td><td>Yes (3)</td><td>No</td><td>(3) Only if addressed to own station.</td></tr><tr><td>13</td><td>Safety Related Acknowledge</td><td>3.11</td><td>Yes</td><td>INF (3)</td><td>Yes</td><td></td></tr><tr><td>14</td><td>Safety Related Broadcast Message</td><td>3.12</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>15</td><td>Interrogation</td><td>3.13</td><td>Yes (4)</td><td>INF</td><td>No</td><td>(4) A Class B "SO" AIS unit shall respond to interrogation for Messages 18, 19, 24 A and 24 B but shall not interrogate other units.</td></tr><tr><td>16</td><td>Assigned Mode Command</td><td>3.14</td><td>Yes (5)</td><td>INF</td><td>No</td><td>(5) Class-B SO AIS shall receive and process only if the message is sent from a station with a valid base station MMSI</td></tr><tr><td>17</td><td>DGNSS</td><td>3.15</td><td>Yes (5)</td><td>INF (6)</td><td>No</td><td>(6) May be provided on other ports of the PI: INF</td></tr><tr><td>18</td><td>Standard Class B Equipment Position Report</td><td>3.16</td><td>Yes</td><td>Yes</td><td>Yes</td><td></td></tr><tr><td>19</td><td>Extended Class B Equipment Position Report</td><td>3.17</td><td>Yes</td><td>Yes</td><td>Yes (7)</td><td>(7) Only when interrogated</td></tr><tr><td>20</td><td>Data Link Management Message</td><td>3.18</td><td>Yes (5)</td><td>INF</td><td>No</td><td></td></tr><tr><td>21</td><td>Aids-to-Navigation Report</td><td>3.19</td><td>Yes</td><td>Yes</td><td>No</td><td></td></tr><tr><td>22</td><td>Channel Management Message</td><td>3.20</td><td>Yes (5)</td><td>INF</td><td>No</td><td></td></tr><tr><td>23</td><td>Group Assignment Command</td><td>3.21</td><td>Yes (5)</td><td>INF</td><td>No</td><td></td></tr><tr><td>24A/24B</td><td>Static Data Report</td><td>3.22</td><td>Yes</td><td>Yes</td><td>Yes</td><td></td></tr><tr><td>25</td><td>Single slot binary message</td><td>3.23</td><td>Yes</td><td>Yes (8)</td><td>Yes (9)</td><td>(8) Only if broadcast or addressed to own station (9) Use ABM or BBM sentence indicating Message 25/70 in message ID field to initiate</td></tr><tr><td>26</td><td>Multiple slot binary message with Communications State</td><td>3.24</td><td>Yes</td><td>Yes (10)</td><td>Yes (11)</td><td>(10) Only if broadcast or addressed to own station (11) Use ABM or BBM sentence indicating Message 26/71 in message ID field to initiate</td></tr><tr><td>27</td><td>Position report for long-range applications</td><td>3.25</td><td>No</td><td>No</td><td>Yes (12)</td><td>(12) When long-range broadcast enabled</td></tr><tr><td>28-63</td><td>Undefined</td><td>None</td><td>Yes</td><td>Yes</td><td>No</td><td>Reserved for future use. If CRC checksum is correct output on PI.</td></tr><tr><td colspan="7">Key</td></tr><tr><td>R/P</td><td colspan="6">Receive and process internally, e.g. prepare for output via PI, act upon the received information, and use the received information internally.</td></tr><tr><td>O</td><td colspan="6">Output Message content via PI using PI VDM Messages</td></tr><tr><td>T</td><td colspan="6">Transmission by own station: "Yes" = either allowed or required; "No" = shall not be transmitted</td></tr><tr><td>INF</td><td colspan="6">VDL Message may be output via PI using a PI VDM Message for information only. This function may be suppressed by configuration setting.</td></tr><tr><td>(x)</td><td colspan="6">Numbers in parenthesis refer to the comment in column Remark.</td></tr></table>

For Messages 6, 8, 25 and 26, the Class B "SO" AIS transmissions shall not exceed 3 slots in a frame. If either case is exceeded, the Class B "SO" AIS shall generate an ABK warning sentence.

# 7.4 Network layer

(See Clause 13)

# 7.4.1 General

The network layer shall be used for

• establishing and maintaining channel connections,   
• managing priority assignments of Messages,   
• distributing transmission packets between channels, and   
• resolving data link congestion.

The network layer shall be designed in accordance with Recommendation ITU-R M.1371.

# 7.4.2 Management of regional operating settings

All stored regional operating settings shall be time/date-tagged. The operating settings shall be tagged to indicate the method by which the information was received (TDMA Message 22 or DSC telecommand).

The Class B "SO" AIS shall continuously verify regional settings to determine if

the nearest boundary of the regional operating area of any stored regional operating setting is more than 500 NM away from the current position, or   
• any stored regional operating setting was older than $^ { 2 4 \mathrm { ~ h ~ } }$

If either of the above conditions is met, the stored regional operating setting shall be erased from the memory.

The regional operating settings set shall be handled as a whole, i.e. a change requested for any parameter of the regional operating settings shall be interpreted as a new regional operating setting. However, in case that the narrow bandwidth $( 1 2 , 5 \ \mathsf { k H z } )$ operation is requested, the AIS shall continue the wide bandwidth operation (25 kHz) while accepting other parameter changes.

The Class B "SO" AIS shall not accept any new regional operating setting which includes a region that does not conform to the rules for regional operating areas laid out in ITU-R M.1371.

When a new regional operating setting overlaps or matches an existing setting, the new setting shall be adopted and the existing setting shall be erased from memory.

A new regional operating setting may be adjacent to an existing regional operating setting and share a common boundary. This shall not lead to the erasure of the existing regional operating setting.

Subsequently, the AIS shall store a new, accepted regional operating setting in one free memory location of the eight memories for regional operating settings. If there is no free memory location, the most distant regional operating setting shall be replaced by the new, accepted one.

NOTE The distance to a regional operating setting is the distance to the nearest boundary.

It shall not be possible to erase any stored regional operating setting by manual input.

# 7.4.3 Multi-channel operation

(See 10.2.1.1)

The two TDMA receiving processes shall work independently and concurrently on channels A and B.

For periodic repeated Messages, the transmissions shall alternate between channels A and B. The Class B "SO" AIS shall transmit Messages 24A and 24B every 6 min. The transmission of Messages 24A and 24B shall not affect the scheduled transmissions of Message 18. The transmission of Messages 24A and 24B shall, if possible, be pre-announced by the ITDMA CommState in previous Messages 18 for reporting intervals other than 3 min. Transmission of the set of Messages 24A and 24B shall alternate between the channels.

# 7.5 Transport layer

(See 10.2.2)

The transport layer shall be responsible for

• converting data into transmission packets of correct size,   
sequencing data packets, and   
• interfacing protocol to upper layers.

The transport layer shall be designed in accordance with Recommendation ITU-R M.1371.

# 7.6 Presentation interface

(See 10.2.2.6, 10.7.2, 12.7.1)

The interface between the transport layer and higher layers shall be performed by the presentation interface (PI).

Data which is to be transmitted by the AIS device shall be input via the PI. Data which is received by the AIS device shall be output through the PI. The formats and protocol used for this data stream shall be in accordance with referenced IEC 61162-1.

If other formats and protocols are used, they should be on a separate logical port.

# 7.7 DSC receive capability

(See Annex A)

The Class B "SO" AIS shall be capable of accepting DSC channel management commands conforming to the provisions of Recommendation ITU-R M.1371.

# 7.8 Long-range application by broadcast

(See 13.6)

Long-range application by broadcast is described in Recommendation ITU-R M.1371-5:2014, Annex 4.

Long-range AIS receiving systems (for example a satellite based receiver) will receive long-range AIS broadcast messages, provided these messages are appropriately structured and transmitted to suit the receiving systems.

The long-range AIS broadcast Message 27 shall be transmitted only on the channel 75 and channel 76. The transmissions should alternate between these two channels such that each channel is used once every 6 min. The broadcast of Message 27 in coastal areas is subject to base station control through the combined use of Message 4 and Message 23 with station type 10.

The Navigational Status of Message 27 shall be set to 15.

The long-range application broadcast shall be disabled by default. The Class B "SO" AIS shall have the capability of enabling this function during normal operation.

# 8 Test conditions

# 8.1 General

When a requirement in this document is different from IEC 60945, the requirement in this--``` document shall take precedence.

# 8.2 Normal test conditions``,,, `,

# 8 . 2 . 1 `- `,, ` Temperature and humidity

Temperature and humidity shall be within the following range:`---

Temperature $+ 1 5 ^ { \circ } C$ to $+ 3 5 ~ ^ { \circ } \mathrm { C }$

Humidity $20 \%$ to $75 \%$

# 8.2.2 Power supply

The normal power supply for the tests shall be the nominal voltage as defined by the manufacturer $\pm 3 \%$ .

# 8.3 Extreme test conditions

Tests under extreme test conditions shall be a combination of high temperature (dry heat) and upper limit of supply voltage applied simultaneously and low temperature and lower limit of supply voltage applied simultaneously (see Clause 9).

During type testing of battery operated equipment, the power source to the equipment may be replaced by a test power source, capable of producing normal and extreme test voltages.

# 8.4 Test signals

NOTE Transmitters can have limitations concerning their maximum continuous transmit time and/or their transmission duty cycle. It is intended that such limitations are respected during testing.

# 8.4.1 Standard test signal number 1

A series of 010101 as the data within an AIS Message frame, with header, start flag, end flag and CRC. NRZI is not applied to the 010101 bit stream or CRC (i.e. unaltered "On Air" data). The RF should be ramped up and down on either end of the AIS message frame.

# 8.4.2 Standard test signal number 2

A series of 00001111 as the data within an AIS Message frame, with header, start flag, end flag and CRC. NRZI is not applied to the 00001111 bit stream or CRC. The RF should be ramped up and down on either end of the AIS message frame.

# 8.4.3 Standard test signal number 3

A pseudo-random sequence (PRS) as specified in Recommendation ITU-T O.153 as the data within an AIS Message frame with header, start flag, end flag and CRC. NRZI is not applied to the PRS stream or CRC. The RF should be ramped up and down on either end of the AIS message frame.

# 8.4.4 Standard test signal number 4

This test signal consists of 200 packets grouped into clusters of 4 as described in Figure 3. Each cluster consists of 2 consecutive transmissions of the packets described in Table 9.

NRZI shall be applied to every packet. After sending packet 1 and 2, the notional initial state of the NRZI process shall be inverted and then packet 1 and 2 repeated.

Between every transmitted packet, there shall be at least 2 free slots. The RF carrier shall be switched off between packets to simulate normal operation.

![](images/bb0767e0acd0943990ed1e8d32d5c3b6d35a0bed70b8143dd4efea17abb7108b.jpg)  
Figure 3 – Format for repeating four-packet cluster

Table 9 – Content of first two packets   

<table><tr><td>Packet</td><td>Parameter</td><td>Bits</td><td>Contents</td><td>Comment</td></tr><tr><td rowspan="5">1</td><td>Training</td><td>24</td><td>0101....0101</td><td></td></tr><tr><td>Start flag</td><td>8</td><td>01111110</td><td></td></tr><tr><td>Data</td><td>168</td><td>Pseudo Random</td><td>As per Table 10</td></tr><tr><td>CRC</td><td>16</td><td>Calculated</td><td></td></tr><tr><td>End flag</td><td>8</td><td>01111110</td><td></td></tr><tr><td rowspan="5">2</td><td>Training</td><td>24</td><td>1010....1010</td><td></td></tr><tr><td>Start flag</td><td>8</td><td>01111110</td><td></td></tr><tr><td>Data</td><td>168</td><td>Pseudo Random</td><td>As per Table 10</td></tr><tr><td>CRC</td><td>16</td><td>Calculated</td><td></td></tr><tr><td>End flag</td><td>8</td><td>01111110</td><td></td></tr></table>

Table 10 – Fixed PRS data derived from ITU-T O.153   

<table><tr><td>Address</td><td colspan="8">Contents (HEX)</td></tr><tr><td rowspan="2">0 to 7</td><td>0x04</td><td>0xF6</td><td>0xD5</td><td>0x8E</td><td>0xFB</td><td>0x01</td><td>0x4C</td><td>0xC7</td></tr><tr><td>0000.0100</td><td>1111.0110</td><td>1101.0101</td><td>1000.1110</td><td>1111.1011</td><td>0000.0001</td><td>0100.1100</td><td>1100.0111</td></tr><tr><td rowspan="2">8 to 15</td><td>0x76</td><td>0x1E</td><td>0xBC</td><td>0x5B</td><td>0xE5</td><td>0x92</td><td>0xA6</td><td>0x2F</td></tr><tr><td>0111.0110</td><td>0001.1110</td><td>1011.1100</td><td>0101.1011</td><td>1110.0101</td><td>1001.0010</td><td>1010.0110</td><td>0010.1111</td></tr><tr><td rowspan="2">16 to 20</td><td>0x53</td><td>0xF9</td><td>0xD6</td><td>0xE7</td><td>0xE0</td><td rowspan="2" colspan="3">21 bytes = 168 bits (+ 4 stuffed bits), CRC = 0x3B85</td></tr><tr><td>0101.0011</td><td>1111.1001</td><td>1101.0110</td><td>1110.0111</td><td>1110.0000</td></tr></table>

# 8.5 Standard test environment

# 8.5.1 Test setup

The EUT is tested in an environment using test equipment to simulate and to log VDL messages (see Table 8). Standard environment consists of at least 1 simulated target. The simulated targets may include, as appropriate, the following:

• Class A Mobile;   
• Class B "CS" Mobile;   
• Class B "SO" Mobile;   
Base Station;   
• AtoN Station;   
• SAR Aircraft;   
• AIS-SART.

The signal input level at the RF input port of the EUT for any simulated target shall be at least –100 dBm. Own ship test sensor inputs to EUT will be simulated by the test system or other means. Operation is checked on channels in the maritime mobile band.

Channels in use shall be selected by channel assignment messages before starting tests.

# 8.5.2 Sensor test input

An appropriate test input shall be provided for simulated position and speed information in IEC 61162-1 format.

# 8.5.3 Synchronisation

The standard test input messages shall be synchronised to slot boundaries unless otherwise specified.

The EUT shall be synchronised to its normal synchronised mode unless the test specifies otherwise.

# 8.5.4 Test signals applied to the receiver input

Sources of test signals for application to the receiver input shall be connected in such a way that the source impedance presented to the receiver input is $5 0 ~ \Omega$ irrespective of whether one or more signals using a combining network are applied to the receiver simultaneously.

The levels of the test signals at the receiver input terminals (RF socket) shall be expressed in terms of dBm.

# 8.5.5 Waiver for receivers

If the manufacturer declares that both TDMA receivers are identical, the test shall be limited to one receiver and the test for the second receiver shall be waived. The test report shall indicate this.

# 8.5.6 Artificial antenna (dummy load)

Tests shall be carried out using an artificial antenna, which shall be a non-reactive nonradiating load of $5 0 ~ \Omega$ connected to the antenna connector.

NOTE Some of the methods of measurement described in this document for the transmitters allow for two or more different test setups. The figures illustrate a specific test setup, and are provided as examples. In many of the figures, power attenuators are shown. These attenuators are not "artificial antennas" as defined above.

The method of measurement used shall be stated in the test report.

# 8.5.7 Modes of operation of the transmitter

There should be a means to operate the transmitter unmodulated. Alternatively, special types of modulation patterns may be agreed by the manufacturer and test laboratory. The alternative methods may involve suitable temporary internal modifications to the EUT. The alternative method shall be described in the test report.

# 8.5.8 Common test conditions for protection from invalid controls

(See 6.8)

In all functional tests using Messages 4, 16, 17, 20, 22, 23 and DSC channel management telecommands, the messages or telecommands sender station shall use a valid base station MMSI format to verify that the EUT operates as described in the required results. The tests shall be repeated using an invalid base station MMSI format for the messages or DSC telecommands sender station to verify that the EUT ignores these messages or telecommands.

# 8.5.9 Measurement uncertainties

Maximum values of absolute measurement uncertainties shall be as follows:

RF frequency . . $\pm 1 \times 1 0 ^ { - 7 }$

RF power ...... ..... $\pm 0 { , } 7 5$ dB

Adjacent channel power $\pm 5$ dB

Conducted spurious emission of transmitter ...... ..... $\pm 4$ dB

Conducted spurious emission of receiver . ±3 dB

Two-signal measurement ..... $\pm 4$ dB

Three-signal measurement $\pm 3$ dB

Radiated emission of transmitter $\pm 6$ dB

Radiated emission of receiver $\pm 6$ dB

Transmitter timing characteristics $\pm 1$ bit $( 1 0 4 ~ \mu \mathsf { s } )$

For the test methods according to this document, these uncertainty figures are valid to a confidence level of $9 5 \ \%$ .

The interpretation of the results recorded in a test report for the measurements described in this document shall be as follows:

a) the measured value related to the corresponding limit shall be used to decide whether an equipment meets the requirements of this document;

b) the actual measurement uncertainty of the test laboratory carrying out the measurements, for each particular measurement, shall be included in the test report; and

c) the values of the actual measurement uncertainty shall be, for each measurement, equal to or lower than the figures given in 8.5.9 (absolute measurement uncertainties).

# 9 Power supply, environmental and EMC tests

(See Clause 5)

# 9.1 Test summary

Tests shall be in accordance with IEC 60945, as specified in Table 11.

Table 11 – Test   

<table><tr><td>Test title</td><td>Clause/subclause of IEC 60945:2002</td><td>Comment</td></tr><tr><td>Power supply</td><td>4.3</td><td></td></tr><tr><td>Extreme power supply</td><td>4.3.1 (7.1)</td><td>Lower limit of extreme DC power supply shall be -20 % of nominal voltage; waivera</td></tr><tr><td>Excessive conditions</td><td>4.3.2 (7.2)</td><td>Waivera</td></tr><tr><td>Power supply short-term variation and power supply failure</td><td>4.3.3 (7.3, 7.4)</td><td>Waivera</td></tr><tr><td>Undervoltage (brown out) test</td><td></td><td>See 9.5; waivera</td></tr><tr><td>Durability and resistance to environmental conditions</td><td>4.4 (8)</td><td></td></tr><tr><td>Dry heat storage test</td><td>8.2.1</td><td>reduce time to 5 h; waivera</td></tr><tr><td>Dry heat functional test</td><td>8.2.2</td><td>This test is covered by Clause 11</td></tr><tr><td>Damp heat</td><td>8.3</td><td>Waivera</td></tr><tr><td>Low temperature storage test</td><td>8.4.1</td><td>Waivera</td></tr><tr><td>Low temperature functional test</td><td>8.4.2</td><td>This test is covered by Clause 11</td></tr><tr><td>Thermal shock</td><td></td><td>No</td></tr><tr><td>Drop</td><td></td><td>No</td></tr><tr><td>Vibration/shock</td><td></td><td>See 9.2, 9.3</td></tr><tr><td>Rain and spray</td><td>8.8</td><td>Waivera</td></tr><tr><td>Immersion</td><td></td><td>No</td></tr><tr><td>Solar radiation</td><td>Yes</td><td>Waivera</td></tr><tr><td>Oil resistance</td><td>Yes</td><td>Waivera</td></tr><tr><td>Corrosion</td><td>Yes</td><td>Waivera</td></tr><tr><td>Interference</td><td>4.5</td><td></td></tr><tr><td>Electromagnetic emission</td><td>9</td><td></td></tr><tr><td>Immunity to electromagnetic environment</td><td>10</td><td></td></tr><tr><td>Compass safe distance (CSD)</td><td>4.5.3; (11.2)</td><td>Waivera: the manufacturer may take liability for the figures given for CSD.</td></tr><tr><td>Safety precautions</td><td>4.6</td><td></td></tr><tr><td>Protection against dangerous voltages</td><td>4.6.1 (12.1)</td><td>Waivera</td></tr><tr><td>Electromagnetic radiofrequency radiation</td><td>4.6.2 (12.2, 12.3)</td><td></td></tr><tr><td>X-radiation</td><td>4.6.3 (12.4)</td><td></td></tr><tr><td colspan="3">a This test may be waived if the manufacturer is able to produce evidence that the requirement is fulfilled.</td></tr></table>

# 9.2 Vibration

# 9.2.1 Purpose

This test shall ensure the EUT can withstand vibrations in the normal operational environment.

# 9.2.2 Method of measurement

The vibration test shall use sweep range and amplitude as defined in IEC 60945 at a sweep rate of 0,2 octaves per minute.

One sweep up (2 Hz to $1 0 0 ~ \mathsf { H } z$ ) shall be followed by a sweep down ( $1 0 0 ~ \mathsf { H z }$ to 2 Hz) for each axis keeping the EUT operational throughout.

# 9.2.3 Required results

Verify that the EUT stays operational throughout the test. A successful performance check shall be carried out at the end of the test period.

# 9.3 Shock

# 9.3.1 Purpose

The test provides a method by which responses of components and equipment comparable with those likely to be experienced in the operational environment can be produced in the test laboratory.

This test only applies to exposed equipment.

# 9.3.2 Method of measurement

The EUT shall be mounted in the normal operating orientation and shall be kept operational during the shocks. The EUT shall be mechanically connected to the shock machine by its normal means of attachment. The peak acceleration shall be $1 0 0 ~ \mathsf { m } / \mathsf { s } ^ { 2 }$ ; pulse shape shall be half sine and duration $^ { 2 5 } { \mathsf { m s } }$ .

The shock pulse shall be measured by an accelerometer placed at the EUT fixing point nearest to the centre of the table surface.

a) Carry out a performance check.   
b) Apply three successive upward shocks with the EUT operative.   
c) Check for external indications of damage.   
d) Carry out a second performance check.

# 9.3.3 Required result

There shall be no external indications of damage or detectable degradation in performance during the performance check.

# 9.4 Performance tests/checks

When testing Class B "SO" AIS, a performance check shall be carried out.

The performance check shall repeat tests 10.2.1.1 (transmit position reports) and 10.2.1.2 (receive position reports).

# 9.5 Under voltage test (brown out)

# 9.5.1 Purpose

This test simulates the situation where the nominal supply voltage drops to below acceptable levels and then recovers over a medium time-period.

# 9.5.2 Method of test

Operate the EUT at the nominal supply voltage as indicated by the manufacturer.

a) Gradually reduce the supply voltage to $40 \%$ of the nominal supply voltage over 30 s.   
b) Gradually increase the supply voltage back to $80 \%$ of the nominal supply voltage over 30 s.

# 9.5.3 Required result

Confirm that:

a) the unit shall not enter into any undefined or undesirable state as verified by a performance check, and   
b) the EUT shall recover and be fully operational as verified by a performance check.

# 9.6 Under voltage test (short term)

# 9.6.1 Purpose

This test simulates the situation where the nominal supply voltage drops to below acceptable levels for a short period and then recovers.

# 9.6.2 Method of test

Operate the EUT at the nominal supply voltage as indicated by the manufacturer.

a) Reduce the supply voltage to $40 \%$ of the nominal supply voltage over 1 s.   
b) Increase the supply voltage back to $80 \%$ of the nominal supply voltage over 1 s.

# 9.6.3 Required result

The following results are required.

a) The unit shall not enter into any undefined or undesirable state as verified by a performance check.   
b) The EUT shall recover and be fully operational as verified by a performance check.

# 10 Operational tests

# 10.1 General

# 10.1.1 Tests by inspection

(See 4.1.2, 4.2, 4.3, 6.1)

# 10.1.1.1 Method of measurement

By inspection of documentation.

# 10.1.1.2 Required results

The relevant requirements shall be met.

# 10.1.2 Safety of operation

(See 4.1.3)

# 10.1.2.1 Purpose

To ensure the safety of operation.

# 10.1.2.2 Method of measurement

By inspection.

# 10.1.2.3 Required result

The requirements of 4.1.3 shall be met.

# 10.1.3 Additional features

(See 4.1.4)

# 10.1.3.1 Purpose

To ensure that any additional or optional features do not adversely affect operation of the EUT.

# 10.1.3.2 Method of measurement

Operate the EUT in standard test environment and enable any additional features provided. Repeat tests that might be affected by the additional feature.

# 10.1.3.3 Required results

The requirements of 4.1.4 shall be met.

# 10.2 Modes of operation

# 10.2.1 Autonomous mode

(See 4.1.5).

# 10.2.1.1 Transmit position reports

(See 7.2.3.2, 7.3.4.3.2, 7.4.3)

# 10.2.1.1.1 Purpose

The purpose of this test is to ensure that the EUT transmits in the autonomous mode.

# 10.2.1.1.2 Method of measurement

Set up standard test environment. Record the VDL communication and check for messages transmitted by the EUT.

# 10.2.1.1.3 Required result

Confirm that the EUT transmits Messages 18 and 24 part A and B following the autonomous continuous schedules, alternating between channels A and B and that Message 27 is not transmitted on the long-range channels when the default setting is used.

# 10.2.1.2 Receive AIS Class A position reports

(See 6.7.3)

# 10.2.1.2.1 Purpose

The purpose of this test is to ensure that the EUT receives AIS Class A position reports in the autonomous mode.

# 10.2.1.2.2 Method of measurement

Set up standard test environment. Perform the tests below and validate the required result for each test.

• Switch on test targets, and then start operation of the EUT.   
• Start operation of the EUT, and then switch on test targets.   
• Transmit test targets using same time slots on channels A and B.

• Transmit test targets that are not synchronised to time slot boundaries on channels A and B.

Check the VDL communication and external interface of the EUT and, where provided, display.

# 10.2.1.2.3 Required result

Confirm that the EUT receives continuously under the conditions above and outputs the received messages on the external interface in accordance with IEC 61162-1 and, where provided, on the display.

# 10.2.1.3 Receive AIS Class B "SO" position reports

# 10.2.1.3.1 Purpose

The purpose of this test is to ensure that the EUT receives AIS Class B "SO" position reports in the autonomous mode.

# 10.2.1.3.2 Method of measurement

Set up standard test environment. Simulate at least one additional Class B "SO" test target (bit stuffing shall not exceed 4 bits). Perform the tests below and validate the required result for each test.

• Switch on test targets, and then start operation of the EUT.   
• Start operation of the EUT, and then switch on test targets.   
• Transmit test targets using same time slots on channels A and B.   
• Transmit test targets that are not synchronised to time slot boundaries on channels A and B.

Check the VDL communication and external interface of the EUT and, where provided, display.

# 10.2.1.3.3 Required result

Confirm that the EUT receives continuously under the conditions above and outputs the received messages on the external interface and, where provided, on the display.

# 10.2.1.4 Receive Class B "CS" position reports

# 10.2.1.4.1 Purpose

The purpose of this test is to ensure that the EUT receives AIS Class B "CS" position reports in the autonomous mode.

# 10.2.1.4.2 Method of measurement

Set up standard test environment. Simulate at least one additional Class B "CS" test target (bit stuffing shall not exceed 4 bits). Perform the four tests below and validate the required result for each test.

• Switch on test targets, and then start operation of the EUT.   
• Start operation of the EUT, and then switch on test targets.   
• Transmit test targets using same time slots on channels A and B.   
Transmit test targets that are not synchronised to time slots boundaries on channels A and B.

Check the VDL communication and external interface of the EUT and, where provided, display.

# 10.2.1.4.3 Required results

Confirm that the EUT receives continuously under the conditions above and outputs the received messages on the external interface and, where provided, on the display.

# 10.2.1.5 Receive in time slot adjacent to own transmission

# 10.2.1.5.1 Purpose

The purpose of this test is to ensure that the EUT receives position reports in the slot adjacent to own transmission in the autonomous mode.

# 10.2.1.5.2 Method of measurement

Set up standard test environment. Simulate $80 \%$ VDL loading. The reporting interval of the EUT may be decreased for the purpose of this test.

Check the external interface of the EUT.

# 10.2.1.5.3 Required result

Confirm that the EUT continuously receives messages in the slots before and after own transmission with an acceptable loss of $5 \%$ .

# 10.2.1.6 High VDL loading reception test

# 10.2.1.6.1 Purpose

The purpose of this test is to ensure that the EUT receives position reports under high VDL loading in the autonomous mode.

# 10.2.1.6.2 Method of measurement

Set up standard test environment. Simulate $90 \%$ VDL loading.

Check the external interface of the EUT.

# 10.2.1.6.3 Required result

Confirm that the EUT continuously receives messages and outputs the received messages on the external interface with a loss of not more than $2 \%$ .

# 10.2.2 Single messages

(See 7.3.4.4, 7.5)

# 10.2.2.1 Transmit an addressed binary message

# 10.2.2.1.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode.

a) Initiate the transmission of an addressed binary Message 6 by the EUT using an ABM sentence input. An acknowledgement Message 7 shall be applied. Record the transmitted messages.   
b) Repeat the test without acknowledgement.   
c) Repeat test with a Message 6 exceeding 2 slots.

d) Apply more than 3 ABM sentences with 1 slot Message 6 to the EUT.   
e) Repeat test a) with the addressed unstructured binary Message 25.   
f) Repeat tests a), b) and d) with the addressed structured binary Message 25.   
g) Repeat test a) with a single addressed unstructured binary Message 26.   
h) Repeat tests a), b), c) and d) with a single addressed structured binary Message 26.

# 10.2.2.1.2 Required results

Check that:

a) the EUT transmits Message 6 as appropriate within 30 s. Check the content of Message 6. Check that the EUT outputs the appropriate ABK sentence;   
b) the EUT transmits Message 6 as appropriate. Check that the EUT outputs the appropriate ABK sentence indicating that no acknowledgment has been received. Check that the EUT does not retransmit Message 6;   
c) the EUT does not transmit Message 6. Check that the EUT outputs the appropriate ABK sentence indicating that the message could not be sent;   
d) the EUT transmits the first 3 Message 6s and does not transmit all following Message 6s within one frame. Check that the EUT outputs the appropriate ABK sentence indicating that the message could not be sent;   
e) the EUT transmits Message 25 as appropriate;   
f) the EUT transmits Message 25 as appropriate;   
g) the EUT transmits Message 26 as appropriate;   
h) the EUT transmits Message 26 as appropriate.

# 10.2.2.2 Transmit an addressed safety related Message 12

# 10.2.2.2.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode.

Initiate the transmission of an addressed binary Message 12 by the EUT using an ABM sentence input.

# 10.2.2.2.2 Required results

Check that the EUT does not transmit Message 12.

# 10.2.2.3 Acknowledgement of addressed Messages

# 10.2.2.3.1 Purpose

The purpose of this test is to ensure that the EUT acknowledges addressed messages in the autonomous mode.

# 10.2.2.3.2 Method of measurement

Operate standard test environment and the EUT in autonomous mode.

a) Apply an addressed binary Message 6 with the EUT as destination to the VDL on Channel A. Record transmitted messages on both channels.   
b) Repeat for Message 12.   
c) Repeat the test a) on channel B.

# 10.2.2.3.3 Required results

Confirm that:

a) the EUT transmits a binary acknowledge Message 7, with the appropriate sequence numbers within 4 s on the channel where the Message 6 was received;   
b) the EUT transmits a binary acknowledge Message 13, with the appropriate sequence numbers within 4 s on the channel where the Message 12 was received;   
c) the EUT transmits a binary acknowledge Message 7 on channel B.

# 10.2.2.4 Transmit a broadcast binary Message 8

# 10.2.2.4.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode.

a) Initiate the transmission of a broadcast binary Message 8 by the EUT using a BBM sentence input. Record the transmitted messages.   
b) Repeat test with a Message 8 exceeding 2 slots.   
c) Apply more than 3 BBM sentences with 1 slot Message 8 to the EUT.   
d) Repeat test a) with the broadcast unstructured binary Message 25.   
e) Repeat tests a) and c) with the broadcast structured binary Message 25.   
f) Repeat test a) with a single broadcast unstructured binary Message 26.   
g) Repeat tests a), b) and c) with a single broadcast structured binary Message 26.

# 10.2.2.4.2 Required results

Check that:

a) the EUT transmits Message 8 as appropriate within 30 s. Check the content of Message 8. Check that the EUT outputs the appropriate ABK sentence;   
b) the EUT does not transmit Message 8. Check that the EUT outputs the appropriate ABK sentence indicating that the message could not be sent;   
c) the EUT transmits the first 3 Message 8s and does not transmit all following Message 8s. Check that the EUT outputs the appropriate ABK sentence indicating that the message could not be sent;   
d) the EUT transmits Message 25 as appropriate;   
e) the EUT transmits Message 25 as appropriate;   
f) the EUT transmits Message 26 as appropriate;   
g) the EUT transmits Message 26 as appropriate.

# 10.2.2.5 Transmit a broadcast safety related Message 14

(See 6.5.3)

# 10.2.2.5.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode.

Initiate the transmission of a broadcast binary Message 14 by the EUT using an BBM sentence input.

# 10.2.2.5.2 Required results

Check that the EUT does not transmit the Message 14.

# 10.2.2.6 ITDMA and RATDMA transmission

(See 7.3.4.2, 7.6)

# 10.2.2.6.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode.

a) Apply a 1 slot binary broadcast message (Message 8) to the PI of the EUT less than 30 s before the next scheduled transmission. Record transmitted messages.   
b) Apply a 1 slot binary broadcast message (Message 8) to the PI of the EUT more than 30 s before the next scheduled transmission. Record transmitted messages.

# 10.2.2.6.2 Required results

Confirm that:

a) the EUT transmits the Message 8 within 30 s using ITDMA;   
b) the EUT transmits the Message 8 within 30 s using RATDMA.

# 10.2.3 Polled mode and interrogation response

(See 4.1.5, 7.3.4.3.4)

# 10.2.3.1 Purpose

The purpose of this test is to ensure that the EUT responds to interrogations.

# 10.2.3.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode. Apply interrogation Message 15 with the EUT as destination:

a) interrogation for Message 19 with transmission offset $= 0$ ;   
b) interrogation for Message 19 with transmission offset $= 1 0$ ;   
c) interrogation for Message 18 with transmission offset $= 0$   
d) interrogation for Message 24 with transmission offset $= 0$

Record transmitted messages and frame structure.

# 10.2.3.3 Required results

Confirm that:

a) the EUT transmits the appropriate interrogation response message within 30 s;   
b) the EUT transmits the appropriate interrogation response message as requested after defined transmission offset;   
c) the EUT transmits the appropriate interrogation response Message 18 within $\mathfrak { z o s }$ ;   
d) the EUT transmits the appropriate interrogation response Messages 24A within 30 s and 24B within 1 min of Message 24A.

Confirm that the EUT transmits the response on the same channel as the interrogation was,,,,,, received., `,, `

# 10.3 Channel selection,, ```-

(See 6.2),, `, `

# 10.3.1 Valid channels

# 10.3.1.1 Purpose

The purpose of this test is to ensure that the EUT responds appropriately when given instructions to change to valid channels.

# 10.3.1.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode. Switch the EUT to different channels within the operating band as specified in 6.2 by transmission of channel management Message 22, broadcast and addressed to the EUT.

Record the VDL Messages on the designated channels and check "band flag" and "Message 22 flag" in Message 18.

# 10.3.1.3 Required results

Confirm that the EUT switches to the correct channel and uses the correct "band flag" and "Message 22 flag".

# 10.3.2 Invalid channels

# 10.3.2.1 Purpose

The purpose of this test is to ensure that the EUT responds appropriately when given instructions to change to invalid channels.

# 10.3.2.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode. Apply a Message 22 with 25 kHz channels not specified in Recommendation ITU-R M. 1084-5.

Record the VDL messages on the designated channels.

# 10.3.2.3 Required results

Confirm that the EUT disregards Message 22.

# 10.4 Internal GNSS receiver

(See 6.3)

The following relevant tests according to IEC 61108 (all parts) shall be performed:

• position accuracy, static;   
• position accuracy, dynamic;   
• COG/SOG accuracy;   
• position update;   
• status indications (including RAIM, when implemented);   
differential mode.

# 10.5 AIS information

# 10.5.1 Information content

(See 6.5.1)

# 10.5.1.1 Purpose

The purpose of this test is to ensure that the EUT transmits all parameters in static and dynamic Class B AIS Messages.

# 10.5.1.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode. Apply all static data to the EUT.

Record all Messages on VDL and check the content of position report Message 18 and static data reports, Messages 24A and 24B.

# 10.5.1.3 Required results

Confirm that data transmitted by the EUT complies with static data and position sensor data.

# 10.5.2 Information update intervals

(See 6.5.2)

# 10.5.2.1 Autonomous reporting interval

# 10.5.2.1.1 Purpose

The purpose of this test is to ensure that the EUT adopts the correct reporting interval for its SOG.

# 10.5.2.1.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode.

a) Start with own SOG of 1 kn; record all Messages on VDL for at least 30 min and evaluate reporting interval for position report of the EUT by calculating average transmission offset over test period.   
b) Increase speed to 3 kn.   
c) Increase speed to 15 kn.   
d) Increase speed to 24 kn.   
e) Reduce speed to 22 kn.   
f) Reduce speed to 13 kn.   
g) Reduce speed to 1 kn.

Record all messages on VDL and check transmission offset between two consecutive transmissions.

# 10.5.2.1.3 Required results

Confirm that:

a) the reporting interval is 3 min $( \pm 1 0 \mathsf { s } )$ ;   
b) the reporting interval is 30 s $( \pm 3 \thinspace \mathsf { s } )$ ) ;   
c) the reporting interval is 15 s (±1,5 s);   
d) the reporting interval is 5 s (±0,5 s);   
e) the reporting interval is $1 5 \thinspace \thinspace \thinspace \thinspace \thinspace \thinspace \thinspace$   
f) the reporting interval is $\mathfrak { 3 0 ~ \mathfrak { s } }$   
g) the reporting interval is 3 min.

# 10.5.2.2 Polite behaviour

# 10.5.2.2.1 Purpose

The purpose of this test is to ensure that the EUT adopts the correct reporting interval dependent on VDL loading and SOG.

# 10.5.2.2.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode. Simulate a VDL loading of $55 \%$ . Record all messages.

a) Start with own SOG of 1 kn.   
b) Increase speed to ${ } ^ { 2 0 \ \mathsf { k n } }$ .   
c) Reduce VDL loading to $40 \%$   
d) Reduce VDL loading to $30 \%$ .   
e) Increase VDL loading to $45 \%$ .   
f) Increase VDL loading to $55 \%$ .   
g) Increase speed to $3 0 ~ \mathsf { k } \mathsf { n }$ .   
h) Reduce VDL loading to $40 \%$ .   
i) Reduce VDL loading to $30 \%$ .   
j) Increase VDL loading to $45 \%$ .   
k) Increase VDL loading to $55 \%$ .   
l) Reduce speed to $1 0 \ \mathsf { k n }$   
m) Reduce VDL loading to $30 \%$ .

Record all messages on the VDL.

# 10.5.2.2.3 Required results

Confirm that:

a) the reporting interval is 3 min;   
b) the reporting interval of 30 s has been established;   
c) the reporting interval of 30 s is maintained;   
d) the reporting interval decreases to 15 s within 4 min to 5 min;   
e) the reporting interval of 15 s is maintained;   
f) the reporting interval increases to 30 s within 4 min to 5 min;   
g) the reporting interval decreases to $1 5 \thinspace \thinspace \thinspace \thinspace \thinspace \thinspace \thinspace$   
h) the reporting interval of 15 s is maintained;   
i) the reporting interval decreases to 5 s within 4 min to 5 min;   
j) the reporting interval of 5 s is maintained;   
k) the reporting interval increases to 15 s within 4 min to 5 min;```,,,   
l) the reporting interval increases to, `,, `` $\mathfrak { 3 0 ~ \mathfrak { s } }$ ;   
m) the reporting interval of`,,, `, $\mathfrak { z o s }$ is maintained.

# 10.5.2.3 Static data reporting interval`-`,, `,,

# 10.5.2.3.1 `--- Purpose

The purpose of this test is to ensure that the EUT maintains the static data-reporting interval.

# 10.5.2.3.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode. Record the transmitted messages and check for static data Messages 24A and 24B.

Repeat the test at an assigned reporting interval of 5 s for Message 18.

# 10.5.2.3.3 Required results

Confirm that the EUT transmits Messages 24A and 24B every 6 min. Confirm that Message 24B is transmitted within 1 min of transmission of Message 24A, and on the same channel. Transmissions shall alternate between channels A and B, and shall be independent of the Message 18 reporting interval.

# 10.6 Initialisation period

(See 6.5.2, 6.5.4)

# 10.6.1 Purpose

The purpose of this test is to ensure that the EUT starts to transmit within the permissible initialisation period.

# 10.6.2 Method of measurement

Set up standard test environment with $\mathsf { S O G } > 2$ kn.

a) Switch on the EUT from cold (off-time minimum 1 h) with the EUT operating in autonomous mode.   
b) Switch off the EUT for between 15 min to 60 min and switch on again.   
c) Make the GNSS sensor position unavailable.

Record transmitted messages.

# 10.6.3 Required results

Confirm that the EUT:

a) starts regular transmission of Message 18 within 2 min and valid position within 30 min after switch on;   
b) starts regular transmission of Message 18 within 2 min and valid position within 5 min after switch on;   
c) continues transmission with last known position and time stamp "63" (positioning system inoperative) with a reporting interval of 3 min. Change to default position values (91, 181) after $3 0 ~ \mathsf { m i n }$ .

# 10.7 Alarms and indications, fall-back arrangements

(See 6.6)

# 10.7.1 Built in integrity test

# 10.7.1.1 Purpose

The purpose of this test is to ensure that the EUT has a BIIT.

# 10.7.1.2 Method of measurement

Check manufacturer’s documentation on BIIT.

# 10.7.1.3 Required result

Verify that an indication is provided if a malfunction is detected and the appropriate ALR sentence is output on the PI.

# 10.7.2 Transceiver protection

(See 7.6)

# 10.7.2.1 Purpose

The purpose of this test is to ensure that the EUT is capable of withstanding open and short circuit to the VHF-antenna terminals.

# 10.7.2.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode with SOG $> 2 3 ~ \mathsf { k n }$ .

a) Open circuit VHF-antenna terminals of the EUT for at least 5 min.   
b) Short circuit VHF-antenna terminals of the EUT for at least 5 min.   
c) Reconnect the VHF-antenna.

# 10.7.2.3 Required results

Check that:

a) an alarm sentence ALR with alarm ID 002 is sent to the PI;   
b) an alarm sentence ALR with alarm ID 002 is sent to the PI;   
c) the EUT shall be operative again after refitting the antenna, without damage to the transceiver and check that an alarm sentence ALR with a deactivated alarm ID 002 is sent to the PI.

# 10.7.3 Transmitter shutdown procedure

# 10.7.3.1 Purpose

The purpose of this test is to ensure that the EUT has a shutdown procedure that is independent of the operating system software.

# 10.7.3.2 Method of measurement

Check manufacturer’s documentation on transmitter shutdown procedure.

# 10.7.3.3 Required result

Verify that a transmitter shutdown procedure, independent of the operating software, is provided (see 6.6.2).

# 10.7.4 Position sensor fallback conditions

# 10.7.4.1 Purpose

The purpose of this test is to ensure that the EUT uses position source, position accuracy flag, RAIM flag and position information in accordance with Table 3.

# 10.7.4.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode.

Apply position sensor data such that the EUT operates as follows:

internal DGNSS in use (corrected by Message 17);   
• internal DGNSS in use (corrected by a beacon), if implemented;   
• internal GNSS in use;   
no sensor position in use.

Check the position accuracy and RAIM flag in the VDL Message 18 and, where provided, the ALR sentence.

# 10.7.4.3 Required result

Verify that the use of position source, position accuracy flag, RAIM flag and position information complies with Table 3.

Verify that the position sensor status is maintained for the next scheduled report and changed for subsequent reports.

Verify that the EUT does not accept Message 17 from a station using a non-base station MMSI.

# 10.8 User interface

# 10.8.1 Status indication

(See 6.7.1)

# 10.8.1.1 Purpose

The purpose of this test is to ensure that the status indicators provided on the EUT function correctly.

# 10.8.1.2 Method of measurement

Perform the following.

a) Set up standard test environment and operate the EUT in autonomous mode.   
b) Send Message 23 with a quiet time to EUT.   
c) Disable GNSS reception.

Check status indications.

# 10.8.1.3 Required results

Check that:

a) power indicator is on and the no transmission indicator is off;   
b) no transmission indicator is on and reverts to off after quiet time elapse;   
c) the error indicator is on.

# 10.8.2 Message display

(See 6.7.1)

This test is only applicable if a message display is provided.

# 10.8.2.1 Purpose

The purpose of this test is to ensure that, if a display is provided, the EUT displays the required information.

# 10.8.2.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode.

a) Apply to the VDL Message 12 addressed to EUT.   
b) Apply to the VDL Message 12 not addressed to EUT.   
c) Apply to the VDL Message 14 to EUT.   
d) Apply an active AIS- SART position report to EUT.   
e) Apply a test mode AIS-SART position report to EUT.   
f) Disable VHF antenna.

# 10.8.2.3 Required results

Verify that:

a) the EUT displays Message 12;   
b) the EUT does not display Message 12;   
c) the EUT displays Message 14;   
d) the EUT displays the AIS- SART position report Message 1, at least ID and position;   
e) the EUT displays the AIS-SART position report Message 1, at least ID and position only if unit set to AIS-SART test mode;   
f) the EUT displays the alarm status and that the error indicator is on.

# 10.8.3 Static data input

(See 6.4, 6.7.2)

# 10.8.3.1 Purpose

The purpose of this test is to ensure that static data can be input to the EUT according to the manufacturer’s documentation and the MMSI cannot be changed once input.

# 10.8.3.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode.

a) Enter all static data except MMSI.   
b) Enter an MMSI outside the valid range.   
c) Enter an MMSI according to the manufacturer’s initialisation procedure.   
d) Enter a new MMSI.   
e) Enter all other static data.

# 10.8.3.3 Required results

Verify that:

a) the static data is correctly stored according to the manufacturer’s initialisation procedure;   
b) the unit does not accept the MMSI;   
c) the unit accepts the MMSI as entered by the user;   
d) the unit does not accept the MMSI as entered by the user;

e) static data can be changed.

# 11 Physical tests

# 11.1 TDMA transmitter

(See 7.2.4)

# 11.1.1 Frequency error

# 11.1.1.1 Definition

The frequency error of the transmitter is the difference between the measured carrier frequency in the absence of modulation of the transmitter and its required frequency.

# 11.1.1.2 Method of measurement

The carrier frequency shall be measured in the absence of modulation.

Tests shall be performed on 156,025 MHz and 162,025 MHz.

The measurement shall be carried out under normal and extreme test conditions.

# 11.1.1.3 Required results

The frequency error shall not exceed $\pm 0 , 5 \ \mathsf { k H z }$ under normal and ±1 kHz under extreme test conditions.

# 11.1.2 Carrier power

# 11.1.2.1 Definition

The power of a radio frequency signal (conducted) is defined as the mean power delivered to $\textsf { a } 5 0 ~ \Omega$ load during a radio frequency cycle. The carrier power is defined as the average radio frequency power measured over the transmitter duration. The transmitter duration is defined in Table 7.

# 11.1.2.2 Method of measurement

Figure 4 shows the arrangement for carrier power.

![](images/b33a73c8b40ea73bfcf18b80f50c0d1e05e2b044a0b32868a05f4a03abd13db8.jpg)  
Figure 4 – Measurement arrangement for carrier power

The following measurement arrangement applies.

a) The transmitter shall generate test signal number 4.   
b) The average power shall be measured over the transmitter duration. This power shall be further averaged over measurements from 200 transmissions. This value shall be corrected according to the transmitter duty cycle to indicate the carrier power.   
c) Tests shall be performed on 156,025 MHz and 162,025 MHz.   
d) The measurement shall be carried out under normal and extreme test conditions.

# 11.1.2.3 Required results

At all test frequencies, the carrier power shall be for high power 37 dBm ± 1,5 dBm and $3 0 ~ \mathsf { d B m } \pm 1 , 5$ dBm for low power under normal test conditions.

At all test frequencies, the carrier power shall be for high power 37 dBm $\pm \nobreakspace 3 , 0 \nobreakspace$ dBm and $3 0 ~ \mathsf { d B m } \pm 3 , 0$ dBm for low power under extreme test conditions.

# 11.1.3 Transmission spectrum

(See 7.2.3.3)

# 11.1.3.1 Purpose

The purpose of this test is to ensure that the modulation and transient sidebands produced by the transmitter under normal operating conditions fall within the allowable mask.

# 11.1.3.2 Method of measurement

The test shall use test signal number 3.

The EUT shall be connected to a spectrum analyser. A resolution bandwidth of 1 kHz, video bandwidth of 3 kHz or greater and positive peak detection (maximum hold) shall be used for this measurement. A sufficient number of sweeps shall be used and sufficient transmission packets measured to ensure that the emission profile is developed.

Tests shall be performed on 156,025 MHz and 162,025 MHz.

# 11.1.3.3 Required result

The spectrum for slotted transmission shall be within the emission mask as follows:

in the region between the carrier and $\pm ~ 1 0 ~ \mathsf { k H z }$ removed from the carrier, the modulation and transient sidebands shall be below 0 dBc;   
• at $\pm 1 0 \mathsf { k H z }$ removed from the carrier, the modulation and transient sidebands shall be below –25 dBc;   
at $\pm 2 5 ~ { \mathsf { k H z } }$ to $\pm 6 2 , 5 \mathsf { k H z }$ removed from the carrier, the modulation and transient sidebands shall be below the lower value of –70 dBc;   
in the region between $\pm 1 0 \mathsf { k H z }$ and $\pm 2 5 ~ { \mathsf { k H z } }$ removed from the carrier, the modulation and transient sidebands shall be below a line specified between these two points.

The reference level for the measurement shall be the carrier power (conducted) recorded for the appropriate test frequency in 11.1.2.

For information, the emission mask specified above is shown in Figure 5.

![](images/5762b3c45b3d3a42984639a8c86feed2c407c4f5bed535571e9de274f92934c9.jpg)  
Figure 5 – Emission mask

# 11.1.4 Modulation accuracy

(See 7.2.3.4, 7.2.3.5)

# 11.1.4.1 Definition

The modulation accuracy is the measurement of the peak frequency deviation of the transmitter modulation and the correct implementation of the GMSK BT filtering.

# 11.1.4.2 Method of measurement

Figure 6 shows the arrangement for modulation accuracy.

![](images/6258d8b12888a8d37ccca9d835d7cb9c53548718f2b13a0ba411f021034e9845.jpg)  
Figure 6 – Measurement arrangement for modulation accuracy

The measurement procedure shall be as follows:

a) the equipment shall be connected in either configuration A or configuration B, as shown in Figure 6. The trigger device is optional if the equipment is capable of synchronising to the transmitted bursts;   
b) the transmitter shall be tuned to AIS 2 (162,025 MHz);   
c) the transmitter shall be modulated with test signal number 1;   
d) the deviation from the carrier frequency shall be measured as a function of time;   
e) the transmitter shall be modulated with test signal number 2;   
f) the deviation from the carrier frequency shall be measured as a function of time;   
g) measurements shall be repeated at 156,025 MHz;   
h) testing shall be repeated under extreme test conditions.

# 11.1.4.3 Required results

Peak frequency deviation at various points within the data frame shall comply with Table 12. These limits apply to both the positive and negative modulation peaks. Bit 0 is defined as the first bit of the training sequence.

Table 12 – Peak frequency deviation versus time   

<table><tr><td rowspan="2">Measurement period from centre to centre of each bit</td><td colspan="2">Test signal 1</td><td colspan="2">Test signal 2</td></tr><tr><td>Normal</td><td>Extreme</td><td>Normal</td><td>Extreme</td></tr><tr><td>Ramp up</td><td colspan="4">&lt; 3 400 Hz</td></tr><tr><td>Bit 0 to bit 1</td><td colspan="4">&lt; 3 400 Hz</td></tr><tr><td>Bit 2 to bit 3</td><td colspan="4">2 400 ± 480 Hz</td></tr><tr><td>Bit 4 to bit 31</td><td>2 400 ± 240 Hz</td><td>2 400 ± 480 Hz</td><td>2 400 ± 240 Hz</td><td>2 400 ± 480 Hz</td></tr><tr><td>Bit 32 to bit 199</td><td>1 740 ± 175 Hz</td><td>1 740 ± 350 Hz</td><td>2 400 ± 240 Hz</td><td>2 400 ± 480 Hz</td></tr></table>

# 11.1.5 Transmitter output power versus time function

(See 7.3.2.3)

# 11.1.5.1 Definition

Transmitter output power versus time function is a combination of the transmitter delay, attack time, release time and transmission duration (referring to Figure 2), where:

a) transmitter delay $( T _ { \mathsf { A } } )$ is the time between the start of the candidate transmission time period and the time when the transmission power exceeds –50 dBc,   
b) transmitter attack time $( T _ { \mathsf { B } } \ - \ T _ { \mathsf { A } } )$ is the time between the transmit power exceeding –50 dBc and the moment when the transmit power has reached a level 1 dB below the measured steady-state power $( P _ { \mathsf { s s } } )$ and maintains a level within $^ { + 1 , 5 }$ dB and –1 dB from $P _ { \mathsf { s s } }$ thereafter,   
c) transmitter release time the moment when the tr $( T _ { \mathsf { F } } - \tau _ { \mathsf { E } } )$ is the time between the end flag being transmitted  output power has reduced to a level 50 dB below $P _ { \mathsf { s s } }$ and remains below this level thereafter, and   
d) transmission duration $( T _ { \mathsf { F } } - T _ { \mathsf { A } } )$ is the time from when power exceeds –50 dBc to when the power returns to and stays below –50 dBc.

# 11.1.5.2 Method of measurement

The measurement shall be carried out by transmitting test signal number 1 (note that this test signal generates one additional stuffing bit within its CRC portion).

The EUT shall be connected to a spectrum analyser. A resolution bandwidth of 1 MHz, a video bandwidth of 1 MHz and a sample detector shall be used for this measurement. The analyser shall be in zero-span mode for this measurement.

For the purposes of this test, the EUT shall be equipped with a test signal (SYNC) indicating the start of each time period that it intends to transmit into. This will be used as a trigger source for the spectrum analyser. The SYNC signal shall be aligned to the nominal start time $( T _ { 0 } )$ of the transmission time period.

Tests shall be performed on 156,025 MHz and 162,025 MHz.

# 11.1.5.3 Required result

The transmitter power shall remain within the mask shown in Figure 2 and associated timings given in Table 7.

# 11.2 TDMA receivers

(See 7.2.2)

# 11.2.1 Sensitivity

# 11.2.1.1 Definition

The maximum usable sensitivity is the minimum level of signal (dBm) at the receiver input, produced by a carrier at the nominal frequency of the receiver, modulated with the typical test signal (test signal 4), which will, without interference, produce a data signal with a specified packet error rate (PER) after demodulation.

# 11.2.1.2 Method of measurement

![](images/b98c53673977129fb02b8a567df32000975d189e8677dd2420aa00ff48971b4c.jpg)  
Figure 7 shows the measurement arrangement.   
Figure 7 – Measurement arrangement

The measurement procedure shall be as follows:

a) the signal generator shall be at the nominal frequency of the receiver and shall be modulated to generate test signal number 4;   
b) the signal level at the input of the receiver shall be set to –107 dBm;   
c) the message measuring test set shall be monitored and the packet error rate observed; The PER shall be derived by the following formula:

$$
P E R = \left(P _ {\mathrm {T x}} - P _ {\mathrm {R x}}\right) / P _ {\mathrm {T x}} \times 100 (\%)
$$

where

$P _ { \mathsf { R } \mathsf { x } }$ is the number of packets received without errors;

$P _ { \mathsf { T x } }$ is the number of transmitted packets.

d) the test shall be repeated at the nominal carrier frequency $\pm 5 0 0 ~ \mathsf { H } z$ and the level at the input to the receiver adjusted to –104 dBm under normal conditions;

e) the test shall be carried out on 156,025 MHz and 162,025 MHz;   
f) repeat under extreme conditions, at the nominal carrier frequency only. The signal generator shall be adjusted so the level at the input to the receiver is –101 dBm.

# 11.2.1.3 Required results

The PER shall not exceed $20 \%$ .

# 11.2.2 Error behaviour at high input levels

# 11.2.2.1 Definition

The error behaviour (performance) at high input levels (noise free operation) is defined in the same manner as for the measurement of the maximum usable sensitivity when the level of the wanted signal is significantly above the maximum wanted sensitivity.

# 11.2.2.2 Method of measurement

The measurement configuration for receiver sensitivity (11.2.1) shall be used.

The signal generator shall be at the nominal frequency of the receiver and shall be modulated to generate test signal number 4. The test shall be carried out on 156,025 MHz and 162,025 MHz. The message measuring test set shall be monitored and the packet error rate observed.

a) The level of the input signal shall be adjusted to a level of –77 dBm;   
b) The level of the input signal shall be adjusted to a level of –7 dBm.

# 11.2.2.3 Required results

The PER shall not exceed $2 \%$ under 11.2.2.2 a) and $10 \%$ under 11.2.2.2 b).

# 11.2.3 Co-channel rejection

# 11.2.3.1 Definition

The co-channel rejection is a measure of the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of an unwanted modulated signal, both signals being at the nominal frequency of the receiver.

# 11.2.3.2 Method of measurement

![](images/523daf00a5dd03123b8b7d120b3e8c44330df2226669f3f37f399b9c7426f28b.jpg)  
Figure 8 shows the measurement arrangement with two generators.   
Figure 8 – Measurement arrangement with two generators

The measurement procedure shall be as follows:

a) two generators A and B, shall be connected to the receiver via a combining network;   
b) the wanted signal, provided by signal generator A, shall be at the nominal frequency of the receiver and shall be modulated to generate test signal number 4;   
c) the unwanted signal, provided by generator B, shall also be at the nominal frequency of the receiver. Generator B shall be modulated to generate test signal number 3, either continuously or in the same time period as that used by generator A for test signal number 4. The content of the wanted and unwanted signals shall not be synchronised;   
d) the level of the wanted signal from generator A shall be adjusted to –101 dBm;   
e) the level of the unwanted signal from generator B shall be adjusted to –111 dBm;   
f) the message measuring test set shall be monitored and the packet error rate (PER) observed;   
g) the measurement shall be repeated for displacements of the unwanted signal of ±1 kHz from the nominal frequency of the receiver and the PER again observed;

NOTE ±1 kHz is twice the allowable transmit frequency tolerance.

h) the test shall be carried out on 156,025 MHz and 162,025 MHz.

# 11.2.3.3 Required result

The PER shall not exceed $20 \%$ .

# 11.2.4 Adjacent channel selectivity

# 11.2.4.1 Definition

The adjacent channel selectivity is a measure of the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of an unwanted signal which differs in frequency from the wanted signal by an amount equal to the adjacent channel separation for which the equipment is intended.

# 11.2.4.2 Method of measurement

The measurement procedure shall be as follows:

a) the measurement configuration for co-channel rejection (11.2.3) shall be used;   
b) the wanted signal, provided by signal generator A, shall be at the nominal frequency of the receiver and shall be modulated to generate test signal number 4;   
c) the unwanted signal, provided by generator B, shall be frequency modulated with a $4 0 0 ~ \mathsf { H z }$ sine wave giving a deviation of $\pm 3$ kHz. Generator B shall be at a frequency 25 kHz above that of the wanted signal;   
d) the level of the wanted signal from generator A shall be adjusted to a level of –101 dBm;   
e) the level of the unwanted signal from generator B shall be adjusted to –31 dBm;   
f) the message measuring test set shall be monitored and the packet error rate observed;   
g) repeat the above measurement with the unwanted signal $2 5 ~ \mathsf { k H z }$ below the wanted signal;   
h) the test shall be carried out on 156,025 MHz and 162,025 MHz.

# 11.2.4.3 Required results

The PER shall not exceed $20 \%$ .

# 11.2.5 Spurious response rejection

# 11.2.5.1 Definition

The spurious response rejection is a measure of the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of an unwanted modulated signal at any other frequency, at which a response is obtained.

# 11.2.5.2 Manufacturers’ declarations

The manufacturer shall declare the following in order to calculate the "limited frequency range" over which the initial part of the test will be performed:

• list of intermediate frequencies: $( I F _ { 1 } , I F _ { 2 } , . . . I F _ { \mathsf N } )$ in Hz;   
• switching range of the receiver;

NOTE Switching range corresponds to the frequency range over which the receiver can be tuned.

• frequency of the local oscillator at 156,025 MHz and 162,025 MHz (fLOL, fLOH).

NOTE This can be a voltage controlled oscillator, crystal, sampling clock, beat frequency oscillator, numerically controlled oscillator depending on the design of the equipment.

# 11.2.5.3 Introduction to the method of measurement

The initial evaluation of the unit shall be performed over the "limited frequency range" and shall then be performed at the frequencies identified from this test and at "specific frequencies of interest" (as defined below).

If the EUT contains IF frequencies, the following procedure applies. Otherwise, the manufacturer shall provide an alternative procedure based on the design of the EUT that produces equivalent results.

To determine the frequencies at which spurious responses can occur, the following calculations shall be made.

a) Calculation of the "limited frequency range"

The limits of the limited frequency range $( L F R _ { \mathsf { H I } } \ L F R _ { \mathsf { L O } }$ ) are determined from the following calculations:

$$
L F R _ {\mathrm {H I}} = f _ {\mathrm {L O H}} + \left(I F _ {1} + I F _ {2} + \dots + I F _ {\mathrm {N}} + s r / 2\right)
$$

$$
L F R _ {\mathrm {L O}} = f _ {\mathrm {L O L}} - \left(I F _ {1} + I F _ {2} + \dots + I F _ {\mathrm {N}} + s r / 2\right)
$$

b) Calculation of specific frequencies of interest (SFI) outside the limited frequency range

These are determined by the following calculations:

$$
S F I _ {1} = (K \times f _ {\sf L O H}) \pm I F _ {1}
$$

$$
S F I _ {2} = (K \times f _ {\sf L O L}) \pm I F _ {1}
$$

where $K$ is an integer from 2 to 4.

# 11.2.5.4 Method of measurement over the limited frequency range

# 11.2.5.4.1 General

Two methods are available for the measurements over the limited frequency range, one based on SINAD measurements (A) and the other based on PER measurements (B), as shown in Figure 9. Either method may be used, but in each case shall be followed by the method of measurement at identified frequencies.

![](images/350e4472b25f5c594189d61b758102ec7d7ceeef3115b672b2dde8e2f28356bd.jpg)  
Figure 9 – SINAD or PER/BER measuring equipment

# 11.2.5.4.2 Method of search over the "limited frequency range" using SINAD measurement

For the SINAD measurement, proceed as follows.

a) Two generators A and B shall be connected to the receiver via a combining network.

The wanted signal, provided by generator A, shall be at AIS 2 and shall be modulated with 1 kHz sine wave at $\pm 2 , 4 \ k \mathsf { H } z$ deviation.

The unwanted signal, provided by generator B, shall be frequency modulated with a $4 0 0 ~ \mathsf { H z }$ sine wave giving a deviation of $\pm 3 \mathsf { k H z }$ .

b) Initially, generator B (unwanted) shall be switched off (maintaining the output impedance).

The signal level from generator A (wanted) shall be adjusted to –101 dBm at the receiver.

The SINAD value shall be noted (and should be greater than 14 dB).

c) Signal generator B shall be switched on and adjusted to –27 dBm at the receiver.   
d) The frequency of the unwanted signal shall be varied in steps of 5 kHz over the limited frequency range (from $L F R _ { \mathsf { L O } }$ to $L F R _ { \mathsf { H I } } )$ ) .   
e) The frequency of any spurious response detected (by an decrease in SINAD of 3 dB or more) during the search shall be recorded for use in the next measurements.   
f) Set the receiving frequency to 156,025 MHz and repeat the test.

# 11.2.5.4.3 Method of search over the "limited frequency range" using PER or BER measurement

For the PER or BER measurement, proceed as follows.

a) Two generators A and B shall be connected to the receiver via a combining network.

The wanted signal, provided by generator A, shall be at AIS 2 and shall be modulated to generate test signal number 4.

The unwanted signal, provided by generator B, shall be frequency modulated with a $4 0 0 ~ \mathsf { H z }$ sine wave giving a deviation of $\pm 3 \mathsf { k H z }$ .

b) Initially, generator B (unwanted) shall be switched off (maintaining the output impedance).

The signal level from generator A (wanted) shall be adjusted to –101 dBm at the receiver. The PER or BER shall be noted.

c) Signal generator B shall be switched on and adjusted to –27 dBm at the receiver.   
d) The frequency of the unwanted signal shall be varied in steps of 5 kHz over the limited frequency range (from $L F R _ { \mathsf { L O } }$ to $L F R _ { \mathsf { H I } } )$ ) .   
e) The frequency of any spurious response detected (by an increase in either PER or BER) during the search shall be recorded for use in the next measurements.

f) Set the frequency to 156,025 MHz and repeat the test.   
g) In the case where operation using a continuous packet stream is not possible, a similar method may be used.

# 11.2.5.5 Method of measurement (at identified frequencies)

Proceed as follows.

a) Two generators A and B shall be connected to the receiver via a combining network.

The wanted signal, provided by generator A, shall be at AIS 2 and shall be modulated to generate test signal number 4.

The unwanted signal, provided by generator B, shall be frequency modulated with a $4 0 0 ~ \mathsf { H z }$ sine wave giving a deviation of $\pm 3 \mathsf { k H z }$ . Generator B shall be at the frequency of that spurious response being considered.

b) Initially, generator B (unwanted) shall be switched off (maintaining the output impedance).   
The signal level from generator A (wanted) shall be adjusted –101 dBm at the receiver.   
c) Generator B shall be switched on, and the level of the unwanted signal set to –31 dBm.   
d) For each frequency noted during the tests over the limited frequency range and the specific frequencies of interest (SFI1), transmit 200 packets to the EUT and note the PER.   
e) Set the receiving frequency to 156,025 MHz and repeat the test for each frequency noted during the tests over the limited frequency range on the lowest frequency and the specific frequencies of interest (SFI2).

# 11.2.5.6 Required results

At any frequency separated from the nominal frequency of the receiver by two channels or more, the spurious responses shall not result in a PER of greater than $20 \%$ .

# 11.2.6 Intermodulation response rejection

# 11.2.6.1 Definition

The intermodulation response rejection is the capability of the receiver to receive a wanted modulated signal, without exceeding a given degradation due to the presence of two closespaced unwanted signals with a specific frequency relationship to the wanted signal frequency.

# 11.2.6.2 Method of measurement

Figure 10 shows the measurement arrangement for intermodulation.

![](images/c0d6e7a3c672182bdad169693946eaba7199290f7a62d5310910664752a974cb.jpg)  
Figure 10 – Measurement arrangement for intermodulation

The measurement procedure shall be as follows:

a) three signal generators shall be connected to the receiver via a combining network;   
b) the wanted signal, provided by signal generator A, shall be at the nominal frequency of the receiver and shall be modulated to generate test signal number 4;   
c) the unwanted signal from generator B shall be unmodulated;   
d) the unwanted signal from generator C shall be frequency modulated with a $4 0 0 ~ \mathsf { H z }$ sine wave giving a deviation of $\pm 3 \mathsf { k H z }$ ;   
e) the signal level from generator A (wanted) shall be set for –101 dBm at the receiver input;   
f) the signal level from generators B and C shall be set for –36 dBm at the receiver input;   
g) the frequencies of generators A, B, C shall be set as per test No.1 of Table 13;   
h) the message measuring test set shall be monitored and the packet error rate observed;   
i) repeat the measurement with frequencies set as per tests No.2, No.3 and No.4 of Table 13.

Table 13 – Frequencies for intermodulation test   

<table><tr><td></td><td>Generator A
Wanted AIS signal</td><td>Generator B
Unmodulated (±50 kHz)</td><td>Generator C
Modulated (±100 kHz)</td></tr><tr><td>Test
No.1</td><td>162,025 MHz</td><td>162,075 MHz</td><td>162,125 MHz</td></tr><tr><td>Test
No.2</td><td>162,025 MHz</td><td>161,975 MHz</td><td>161,925 MHz</td></tr><tr><td>Test
No.3</td><td>156,025 MHz</td><td>156,075 MHz</td><td>156,125 MHz</td></tr><tr><td>Test
No.4</td><td>156,025 MHz</td><td>155,975 MHz</td><td>155,925 MHz</td></tr></table>

# 11.2.6.3 Required results

The PER shall not exceed $20 \%$ .

# 11.2.7 Blocking or desensitisation

# 11.2.7.1 Definition

Blocking is a measure of the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of an unwanted input signal at any frequencies other than those of the spurious responses or the adjacent channels.

# 11.2.7.2 Method of measurement

The measurement procedure shall be as follows:

a) two generators A and B shall be connected to the receiver via a combining network (see Figure 9);   
b) the wanted signal, provided by signal generator A, shall be at the nominal frequency of the receiver and shall be modulated to generate test signal number 4;   
c) the unwanted signal from generator B shall be unmodulated and shall be at a frequency 0,5 MHz to 10 MHz away from the nominal frequency of the receiver. Measurements shall be carried out at frequencies of the unwanted signal at approximately ±500 kHz, $\pm 1$ MHz, $\pm 2$ MHz, $\pm 5$ MHz and $\pm 1 0$ MHz, avoiding those frequencies at which spurious responses could occur (see 11.2.5);

d) initially, signal generator B (unwanted signal) shall be switched off (maintaining the output impedance). The level of the wanted signal from generator A shall be adjusted to –101 dBm at the receiver input;   
e) the RF signal level for signal generator B (unwanted signal) shall be adjusted to –23 dBm when the frequency setting is less than $\pm 5$ MHz. For frequency settings of $\pm 5$ MHz or higher, the RF level shall be adjusted to –15 dBm;   
f) the test shall be repeated for all the frequencies defined in step c);   
g) the test shall be carried out on 156,025 MHz and 162,025 MHz.

# 11.2.7.3 Required results

The maximum packet error rate shall not exceed $20 \%$ .

# 11.3 Conducted spurious emissions

# 11.3.1 Spurious emissions from the receiver

(See 7.2.2)

# 11.3.1.1 Definition

Spurious emissions from the receiver are components at any frequency, conducted to the antenna. The level of spurious emissions shall be measured as their power level in a specified load.

# 11.3.1.2 Method of measurement

The receiver shall be connected to a $5 0 ~ \Omega$ attenuator. The output of the attenuator shall be connected to a spectrum analyser or selective voltmeter having an input impedance of $5 0 ~ \Omega$ . If the detecting device is not calibrated in terms of power input, the level of any detected components shall be determined by a substitution method using a signal generator. The measurement shall extend over the frequency range 9 kHz to 4 GHz.

The receiver shall be switched on, and the measuring receiver shall be tuned over the frequency range 9 kHz to 4 GHz.

At each frequency at which a spurious component is detected, the power level shall be recorded as the spurious level delivered into the specified load.

# 11.3.1.3 Required results

The power of any spurious emission in the specified range at the antenna terminal shall not exceed –57 dBm (2 nW) in the frequency range 9 kHz to 1 GHz and –47 dBm (20 nW) in the frequency range 1 GHz to 4 GHz.

# 11.3.2 Spurious emissions from the transmitter

(See 7.2.4)

# 11.3.2.1 Definition

Conducted spurious emissions are emissions on a frequency or frequencies, which are outside the necessary bandwidth and the level of which may be reduced without affecting the corresponding transmission of information. Spurious emissions include harmonic emissions, parasitic emissions, intermodulation products and frequency conversion products, but exclude out-of-band emissions.

# 11.3.2.2 Method of measurement

The transmitter shall be connected to a $5 0 \ \Omega$ power attenuator. The output of the power attenuator shall be connected to a measuring receiver.

If possible, the measurement shall be made with the transmitter unmodulated. If this is not possible, the transmitter shall be modulated by test signal number 3. If possible, the modulation should be continuous for the duration of the measurement.

The measurement shall be made over a frequency range from 9 kHz to 4 GHz, excluding the transmitting frequency $\pm 6 2 , 5 \mathsf { k H z }$ .

The resolution bandwidth of the measuring instrument shall be the smallest bandwidth available which is greater than the spectral width of the spurious component being measured. This shall be considered to be achieved when the next highest bandwidth causes less than 1 dB increase in amplitude. Positive peak detection (maximum hold) shall be selected on the spectrum analyser used for this measurement.

A sufficient number of sweeps shall be measured to ensure that the emission profile is developed.

At each frequency at which a spurious component is detected, the power level shall be recorded as the conducted spurious emission level delivered into the specified load, except for the transmitting frequency $\pm 6 2 , 5 \ \mathsf { k H z }$ . The conditions used in the relevant measurements shall be recorded in test reports.

# 11.3.2.3 Required results

The power of any spurious emission on any discrete frequency shall not exceed $0 , 2 5 \ \mu \mathsf { W }$ (–36 dBm) in the frequency range 9 kHz to 1 GHz and 1 $\mu \mathsf { W }$ (–30 dBm) in the frequency range 1 GHz to 4 GHz.

# 12 Specific tests of link layer

(See 7.3)

# 12.1 TDMA synchronisation

# 12.1.1 Synchronisation test using UTC direct and indirect

# 12.1.1.1 Purpose

The purpose of this test is to ensure that the EUT can operate UTC direct and indirect.

# 12.1.1.2 Method of measurement

Set up standard test environment; choose test conditions in a way that the EUT operates in the following synchronisation modes:

a) UTC direct;   
b) UTC indirect (internal synchronisation source disabled; at least one other station UTC direct synchronised);   
c) BASE direct (internal GNSS disabled; base station with UTC direct synchronisation within range);   
d) UTC indirect (internal GNSS receiver disabled; only Class B SO station UTC direct synchronised).

Check all CommState parameters in position report. Check reporting interval.

# 12.1.1.3 Required results

Confirm that:

a) the SynchState $= 0$ ,   
b) the SynchState $= 1$ ,   
c) the SynchState $= 1$ ,   
d) the SynchState $= 1$ .

# 12.1.2 Synchronisation test without UTC, EUT receiving semaphore

# 12.1.2.1 Purpose

The purpose of this test is to ensure that the EUT can synchronise to a semaphore.

# 12.1.2.2 Method of measurement

Set up standard test environment; choose test conditions such that the EUT operates with other units acting as follows.

a) The EUT is receiving a mobile station that is acting as semaphore with no Base Stations being received.   
b) Introduce a Base Station that is acting as a semaphore with different timing.   
c) Enable internal synchronisation source.

Check all CommState parameters in position report. Check reporting interval.

# 12.1.2.3 Required results

Confirm that:

a) transmitted SynchState $= 3$ ,   
b) the EUT shall change synchronisation source to the Base Station, and   
c) synchronisation mode shall revert to UTC direct, SynchState $= 0$ .

# 12.2 Time division (frame format)

# 12.2.1 Purpose

The purpose of this test is to ensure that the EUT uses SOTDMA correctly.

# 12.2.2 Method of measurement

Set the EUT to maximum reporting interval of 5 s by applying a speed of $> 2 3$ kn. Record VDL Messages and check for used slots. Check parameter slot number in CommState of position report. Check slot length (transmission time).

# 12.2.3 Required results

Slot number used and slot number indicated in CommState shall match. Slot number shall not exceed 2249. Slot length shall not exceed 26,67 ms.

# 12.3 Synchronisation jitter

# 12.3.1 Definition

Synchronisation jitter (transmission timing error) is the time between nominal slot start as determined by the UTC synchronisation source and the initiation of the "transmitter on" function.

# 12.3.2 Purpose

The purpose of this test is to ensure that the synchronisation jitter is within the allowable tolerances.

# 12.3.3 Method of measurement

Set up standard test environment. Set the EUT to 5 s reporting interval using

a) UTC direct synchronisation, and   
b) UTC indirect synchronisation by disconnecting the synchronisation source of the EUT.

Record VDL Messages and measure the time between the nominal beginning of the slot (Nominal $T _ { 0 }$ ) and the start flag, and calculate it back to $T _ { 0 }$ .

# 12.3.4 Required results

The synchronisation jitter shall not exceed

a) $\pm 1 0 4 \mu \mathsf { s }$ using UTC direct synchronisation, and   
b) $^ { \pm 3 1 2 } \mu \mathsf { s }$ using UTC indirect synchronisation.

# 12.4 Data encoding (bit stuffing)

(See 7.2.3.6)

# 12.4.1 Purpose

The purpose of this test is to ensure that the EUT conforms to the data encoding requirements.

# 12.4.2 Method of measurement

Set up standard test environment.

Set ship’s name to HEX-Values "7E 3B 3C 3E 7E" so that bit stuffing will be applied and check the VDL (note that this might require that the manufacturer provides means to input this data).

# 12.4.3 Required results

Confirm that transmitted VDL Messages 24A and 24B conform to data input.

# 12.5 Frame check sequence

# 12.5.1 Purpose

The purpose of this test is to ensure that the EUT rejects Messages with invalid CRC.

# 12.5.2 Method of measurement

Apply simulated position report Messages with wrong CRC bit sequence to the VDL.

a) Check test output; if a display interface is provided, check this.   
b) Repeat test 12.1.2 and check that a station transmitting Messages with wrong CRC is not used for synchronisation.

# 12.5.3 Required results

Confirm that Messages with invalid CRC are not accepted by the EUT in cases a) and b) of 12.5.2.

# 12.6 Slot allocation (channel access protocols)

# 12.6.1 Network entry

# 12.6.1.1 Method of measurement

Set up standard test environment; switch on EUT. Record transmitted scheduled position reports for the first 3 min of transmission after initialisation period. Check CommState for channel access mode.

# 12.6.1.2 Required results

EUT shall start autonomous transmissions of Message 18 (position report) with ITDMA CommState with KeepFlag set true for first minute of transmission and Message 18 with SOTDMA CommState thereafter.

# 12.6.2 Autonomous scheduled transmissions (SOTDMA)

# 12.6.2.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode.

a) Record transmitted scheduled position reports Message 18 and check frame structure. Check CommState of transmitted messages for channel access mode and parameters number of received stations, slot timeout, slot number and slot offset.   
b) Repeat the test with $50 \%$ channel loading ensuring there are at least 4 free slots in each SI.

# 12.6.2.2 Required results

Check that the following is achieved:

a) nominal reporting interval is achieved $120 \%$ (allocating slots in selection interval SI). Confirm that the EUT allocates new slots NTS within SI after 3 min to 8 min. Check that slot offset indicated in CommState matches slots used for transmission. Check that Class B "CS" are not included in the number of received stations. Check that during DSC monitoring periods there are no time out values of $" 0 "$ ;   
b) only free slots are used for transmission.

# 12.6.3 Autonomous scheduled transmissions (ITDMA)

# 12.6.3.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode. Set speed to less than 2 knots giving a reporting interval of 3 min. Record transmitted scheduled position reports.

# 12.6.3.2 Required results

Check that EUT transmits Message 18 with ITDMA CommState and allocates slots using ITDMA and that slot offset indicated in CommState matches slots used for transmission.

Check that nominal reporting interval is achieved $\pm 2 0 ~ \%$ .

# 12.6.4 Transmission of Messages 24A and 24B (ITDMA)

# 12.6.4.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode. Record transmitted messages.

# 12.6.4.2 Required results

Confirm that EUT transmits Messages 24A and 24B using the ITDMA access scheme. The SOTDMA CommState of Messages 18 shall, as far as possible, be changed to ITDMA CommState to allocate slots for Messages 24A and 24B.

# 12.6.5 Assigned operation

(See 4.1.5, 7.3.4.3.3)

# 12.6.5.1 Message 16 with slot assignment

# 12.6.5.1.1 Purpose

The purpose of this test is to ensure that the EUT can be assigned to use specific slots.

# 12.6.5.1.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode $\mathsf { P O G } < 2 \mathsf { k n }$ ) .

a) Transmit an assigned mode command Message 16 to the EUT with initial slot offset and increment.   
b) Increase speed to 25 kn while still assigned to a reporting interval of $\boldsymbol { 1 0 \ s }$ .   
c) Every 3 min, send further assignment Messages with the same slot assignment.   
d) Transmit an assigned mode command Message 16 with a non-base station MMSI to the EUT with initial slot offset and increment.   
e) Transmit an assigned mode command Message 16 to an MMSI different to the MMSI of the EUT with initial slot offset and increment.

Record transmitted Messages.

# 12.6.5.1.3 Required results

Confirm that the following is achieved:

a) the EUT transmits a Message 18 in the designated slots. Check that the assigned mode flag is set to 1;   
b) the EUT stays in assigned mode using the assigned slots;   
c) the EUT continues in assigned mode when it receives a further assignment commands by Message 16. Verify that the slot timeout value is updated for every received Message 16;   
d) the EUT ignores Message 16 and continues autonomous mode operation;   
e) the EUT ignores Message 16 and continues autonomous mode operation.

Confirm that the EUT reverts to autonomous mode with autonomous reporting interval 4 min to 8 min after the last Message 16.

# 12.6.5.2 Message 16 with rate assignment

# 12.6.5.2.1 Purpose

The purpose of this test is to ensure that the EUT can be assigned reporting intervals.

# 12.6.5.2.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode $\mathsf { P O G } < 2 \mathsf { k n }$ ) .

a) Transmit an assigned mode command Message 16 to the EUT with a designated reporting interval of 5 s.

b) Transmit an assigned mode command Message 16 to the EUT with the assigned reporting interval of $\boldsymbol { 1 0 \ s }$ .   
c) Increase speed to 25 kn while still assigned to a reporting interval of $\boldsymbol { 1 0 \ s }$ .   
d) Every 3 min, send further assignment Messages with a reporting interval of $\boldsymbol { 1 0 \ s }$   
e) Transmit an assigned mode command Message 16 to the EUT with a non-base station MMSI.

Record transmitted Messages.

# 12.6.5.2.3 Required results

Confirm that the following is achieved:

a) the EUT transmits with the designated reporting interval of 5 s. Check that the assigned mode flag is set to 1;   
b) the reporting interval is $1 0 \ \mathsf { s }$ ;   
c) the EUT stays in assigned mode with a reporting interval of $\boldsymbol { 1 0 \ \mathsf { s } }$ ;   
d) the EUT continues in assigned mode when it receives a further assignment commands by Message 16. Verify that the slot timeout value in the CommState is not updated by the received Message 16;   
e) confirm that the EUT ignores Message 16 and continues autonomous mode operation.

Confirm that the EUT reverts to autonomous mode with autonomous reporting interval 4 min to 8 min after the last Message 16.

# 12.6.5.3 Assigned mode using invalid reporting rates

# 12.6.5.3.1 Method of measurement

Operate standard test environment and EUT in autonomous mode. Transmit an assigned mode command Message 16 using a base station MMSI to the EUT with

a) the number of reports per 10 min which is not a multiple of 20, and   
b) the number of reports per 10 min which is higher than 120.

# 12.6.5.3.2 Required results

Confirm that:

a) the EUT transmits position reports Message 18 at a reporting rate that corresponds to the next highest multiple of 20 reports per 10 min, and   
b) the EUT transmits position reports Message 18 at a reporting interval of $\textsf { 5 s }$

# 12.6.5.4 Slot assignment to FATDMA reserved slots

# 12.6.5.4.1 Definition

This test checks the operation of Message 16 assignment of slots reserved by Message 20.

# 12.6.5.4.2 Method of measurement

Set up the standard test environment and operate EUT in autonomous mode. Transmit a Data Link Management message (Message 20) using a base station MMSI to the EUT with slot offset and increment. Transmit an Assigned Mode Command (Message 16) using a base station MMSI to the EUT and command it to use one or more of those FATDMA allocated slots. Record transmitted messages.

# 12.6.5.4.3 Required results

Confirm that the EUT uses the slots commanded by Message 16 for own transmissions.

# 12.6.6 Group assignment

NOTE In the tests of 12.6.6, a base station MMSI is used to transmit Message 23 with a geographic region so that the EUT is inside this region, unless mentioned otherwise.

# 12.6.6.1 Entering interval assignment

# 12.6.6.1.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode with a reporting interval of 15 s $\mathsf { S O G } = 1 5 \mathsf { k n }$ ). Perform the following tests after time-out of the previous test.

a) Transmit a Group Assignment command (Message 23) to the EUT with a reporting interval of 30 s assigned.   
b) Transmit a Group Assignment command (Message 23) to the EUT with a reporting interval of 5 s assigned.   
c) Using a non-base station MMSI, transmit a Group Assignment command (Message 23) to the EUT with a reporting interval of 5 s assigned.   
d) Transmit a Group Assignment command (Message 23) to the EUT with a reporting interval of 2 s assigned.   
e) Transmit a Group Assignment command (Message 23) to the EUT with a reporting interval field setting 9 (next shorter autonomous reporting interval).   
f) Transmit a Group Assignment command (Message 23) to the EUT with a reporting interval field setting 10 (next longer autonomous reporting interval).

Monitor the VDL.

# 12.6.6.1.2 Required result

# Verify that:

a) EUT enters assigned operation mode and transmits position report Message 18 with 30 s reporting interval. Verify that EUT builds up the assigned transmission scheduled according to the network entry procedure. Verify that unused slots of the previous reporting schedule are released. Verify that the EUT reverts to autonomous mode after a time out of 4 min to 8 min building up the autonomous transmission schedule according to the network entry procedure and releases unused slots from previous schedule;   
b) EUT enters assigned operation mode and transmits position report Message 18 with 5 s reporting interval. Verify that EUT builds up the assigned transmission scheduled according to network entry procedure. Verify that unused slots of the previous reporting schedule are released. Verify that the EUT reverts to autonomous mode after a time out of 4 min to 8 min building up the autonomous transmission schedule according to the network entry procedure and releases unused slots from the previous schedule;   
c) EUT does not react on Message 23;   
d) EUT does not react on Message 23;   
e) EUT enters assigned operation mode and transmits position report Message 18 with 5 s reporting interval;   
f) EUT enters assigned operation mode and transmits position report Message 18 with 30 s reporting interval.

# 12.6.6.2 Assignment by region

# 12.6.6.2.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode with a reporting interval of 15 s and use a base station MMSI to transmit Message 23.

a) Transmit a Group Assignment command (Message 23) to the EUT (define station type 0 and geographic region so that the EUT is inside this region). Set the reporting rate to 5 s and apply message to VDL.   
b) Transmit a Group Assignment command (Message 23) to the EUT (define station type 0 and geographic region so that the EUT is outside this region). Set the reporting rate to 5 s and apply message to VDL.

# 12.6.6.2.2 Required result

Verify that:

a) EUT switches to assigned mode and transmits position reports with 5 s interval. Verify that EUT reverts to normal operation mode after timeout period;   
b) EUT declines Message 23.

# 12.6.6.3 Assignment by station type

# 12.6.6.3.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode with a reporting interval of 15 s and transmit Message 23 with a reporting interval of 5 s.

a) Transmit a Group Assignment command with a station type to 0 (all stations).   
b) Transmit a Group Assignment command with a station type to 1 (Class A).   
c) Transmit a Group Assignment command with a station type to 2 (All Class B).   
d) Transmit a Group Assignment command with a station type to 3 (SAR aircraft).   
e) Transmit a Group Assignment command with a station type to 4 (Class B SO).   
f) Transmit a Group Assignment command with a station type to 5 (Class B CS).   
g) Transmit a Group Assignment command with a station type to 6 (Inland AIS).

# 12.6.6.3.2 Required result

Verify that:

a) EUT switches to assigned mode with 5 s reporting interval;   
b) EUT declines Message 23;   
c) EUT switches to assigned mode with 5 s reporting interval;   
d) EUT declines Message 23;   
e) EUT switches to assigned mode with 5 s reporting interval;   
f) EUT declines Message 23;   
g) EUT declines Message 23.

# 12.6.6.4 Addressing by ship and cargo type

# 12.6.6.4.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode with a reporting interval of 15 s and use a base station MMSI to transmit Message 23.

a) Transmit a Group Assignment command (Message 23) to the EUT. Set the reporting interval to 5 s and the ship and cargo value to the value which is configured in the EUT.

b) Transmit a Group Assignment command (Message 23) to the EUT. Set the reporting interval to 5 s and the ship and cargo value to a value different to the value which is configured in the EUT.   
c) Configure the ship and cargo type of the EUT to 72. Transmit a Group Assignment command (Message 23) to the EUT. Set the reporting interval to 5 s and the ship and cargo type value to 70.

# 12.6.6.4.2 Required result

Verify that:

a) EUT switches to assigned mode and transmits position reports with 5 s reporting interval;   
b) EUT declines Message 23;   
c) EUT switches to assigned mode and transmits position reports with 5 s reporting interval.

# 12.6.6.5 Quiet time command

# 12.6.6.5.1 Method of measurement

Set up the standard test environment and operate EUT in autonomous mode with 15 s reporting interval.

Transmit a Group Assignment message (Message 23) to the EUT with a quiet time command.

Record transmitted messages.

# 12.6.6.5.2 Required results

Confirm that the EUT continues transmission for one frame to release the allocated slots and then stops transmission. Confirm that the EUT starts transmission after the quiet time according to the network entry procedure. The quiet time period starts with the reception of Message 23.

# 12.6.6.6 Reverting from interval assignment

# 12.6.6.6.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode. Transmit a Group Assignment command (Message 23) to the EUT with a reporting interval of 5 s assigned. Monitor the VDL until at least 1 min after timeout occurred. Repeat 10 times (transmissions of Message 23 shall not be synchronised to the initial transmission schedule of the EUT).

Measure the time $T _ { \mathsf { r e v } }$ between the reception of Message 23 and the first transmission after timeout.

# 12.6.6.6.2 Required result

Verify that the time out is randomly distributed between 4 min and 8 min.

# 12.6.6.7 Assignment priority test – Message 16 and 23

# 12.6.6.7.1 Purpose

The purpose of this test is to ensure that the EUT selects the correct assignment Message when given both addressed and group assignments.

# 12.6.6.7.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode.

a) Transmit a Message 23, addressed to the EUT, to assign a reporting interval of $\boldsymbol { 1 5 \ s }$ . Check that the EUT reporting interval is 15 s. Transmit a Message 16, addressed to the EUT, assigning a reporting interval of 10 s while still assigned by Message 23.   
b) Transmit a Message 16, addressed to the EUT, to assign a reporting interval of $\boldsymbol { 1 5 \ s }$ . Check that the EUT reporting interval is 15 s. Transmit a Message 23, addressed to the EUT, assigning a reporting interval of 10 s while still assigned by Message 16.

# 12.6.6.7.3 Required result

Confirm that:

a) the EUT adopts the reporting interval of Message 16;   
b) the EUT continues with the reporting interval of Message 16.

# 12.6.6.8 Assignment priority test – Message 22 and 23

# 12.6.6.8.1 Purpose

The purpose of this test is to ensure that the EUT selects the correct assignment Message when given group assignments by Messages 22 and 23.

# 12.6.6.8.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode. Transmit a Message 22 defining a region with the EUT inside that region Tx/Rx mode $= 0$ .

a) Transmit an Assigned mode command (Message 23) to the EUT with Tx/Rx mode 1.   
b) Transmit Message 22 to the EUT with regional settings specifying Tx/Rx mode 2.   
c) Transmit an Assigned mode command (Message 23) to the EUT with Tx/Rx mode 1.   
d) During assigned mode, transmit a Message 22 to the EUT individually addressed and specifying Tx/Rx mode 2.   
e) W ithin $1 0 \mathrm { \ m i n }$ , transmit a Message 22 with regional area settings specifying Tx/Rx mode 0.   
f) Transmit an Assigned mode command (Message 23) to the EUT with Tx/Rx mode 1 every min for 15 min.   
g) After timeout of the last Message 23, transmit a Message 22 with regional settings specifying Tx/Rx mode 0.

Record transmitted messages.

# 12.6.6.8.3 Required result

The following results are required.

a) Check that Tx/Rx mode $= ~ 1$ . The Tx/Rx mode field setting of Message 23 takes precedence over the Tx/Rx mode field setting of Message 22.   
b) Check that Tx/Rx mode $= ~ 1$ . The EUT reverts to the Tx/Rx mode $= 2$ defined by Message 22 after the timeout of Message 23.   
c) Verify that Tx/Rx mode $= 1$ .   
d) Check that Tx/Rx mode $\qquad = \ 2$ . The Tx/Rx mode field setting of Message 22 takes precedence over the Tx/Rx mode field setting of Message 23.   
e) Check that Tx/Rx mode $= 2$ . The Tx/Rx mode setting of Message 22 is ignored.   
f) Check that the Tx/Rx mode remains at 2 min for 10 min after applying Message 22. Check that the Tx/Rx mode is changed to 1 when receiving Message 23 later than 10 min after Message 22. Check that after timeout of the last Message 23 the Tx/Rx mode reverts to 2 according to the individually addressed Message 22.

g) Check that Tx/Rx mode $= 0$ . The Tx/Rx mode setting of Message 22 is accepted.

# 12.6.7 Base station reservations

# 12.6.7.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode with 5 s reporting interval $( { \mathsf { S O G } } = 2 5 ~ { \mathsf { k n } }$ ). Apply a Message 4 to the VDL using a base station MMSI.

a) Transmit a Data Link Management message (Message 20) on Channel A from a Base Station within 120 NM to the EUT with slot offset $= ~ 5$ and increment = 10. Record transmitted messages.   
b) Repeat the test with a Base Station beyond 120 NM.   
c) Repeat the test without Base Station Report (Message 4).   
d) Repeat the test reserving $100 \%$ of the slots.   
e) Repeat the test with a Base Station within 120 NM and maintain transmission of Message 20. Stop transmission Message 4.   
f) Repeat test a) using a non-base station MMSI.

# 12.6.7.2 Required results

The following results are required.

a) For the Base Station within 120 NM, confirm that EUT does not use slots allocated by Message 20 for own transmissions until timeout of 4 min to 8 min. Confirm that the EUT does not use the same slots on Channel B.   
b) For the Base Station beyond 120 NM, confirm that the EUT treats the slots as free.   
c) Confirm that the EUT treats the slots as free.   
d) Confirm that the EUT stops transmission.   
e) Confirm that the EUT ignores the slot reservations of a Message 20 which is received after the normal target time-out of Message 4.   
f) Confirm that the EUT treats the slots as free.

# 12.7 Message formats

# 12.7.1 Received messages

(See 7.6)

# 12.7.1.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode. Apply messages according to Table 8 to the VDL including multiple slot messages up to 5 slots. Record messages output by the PI of EUT.

# 12.7.1.2 Required results

Confirm that EUT outputs corresponding message with correct field contents and format via the PI or responds as appropriate.

# 12.7.2 Transmitted messages

# 12.7.2.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode. Initiate the transmission of messages relevant for a mobile station according to Table 8 by the EUT. Record transmitted messages.

# 12.7.2.2 Required results

Confirm that EUT transmits messages with correct field contents and format or responses as defined in Table 8.

# 13 Specific tests of network layer

(See 7.4)

# 13.1 Regional area designation by VDL Message

# 13.1.1 Purpose

The purpose of this test is to ensure that the EUT transmits on the correct channels when transiting adjacent regional areas.

# 13.1.2 Method of measurement

Set up the standard test environment.

a) With no Message 4. Apply channel management messages (Message 22) to the VDL defining two adjacent regional areas, 1 and 2, with different channel assignments for both regions and a transitional zone extending 4 NM either side of the regional boundary, Table 14 and Figure 11.   
b) With a Base Station within 120 NM transmitting Message 4. Apply the same channel management Messages as in a). Make the EUT approach region 1 from outside region 2 more than 5 NM away from the region boundary, transmitting on default channels. Record transmitted Messages on all 6 channels. This can be accomplished by either using a dedicated test input for simulated position information or a GNSS simulator.

![](images/98855b22d3407277dfc7cea3a14984b1cfc1fb00e063276bc1351f77b3618283.jpg)  
Figure 11 – Regional transitional zones

Table 14 – Regional area scenario   

<table><tr><td></td><td>Primary channel</td><td>Secondary channel</td></tr><tr><td>Region 1</td><td>CH A 1</td><td>CH B 1</td></tr><tr><td>Region 2</td><td>CH A 2</td><td>CH B 2</td></tr><tr><td>Default region</td><td>AIS 1</td><td>AIS 2</td></tr></table>

c) Operate the unit in an area with Tx/Rx mode 1.   
d) Operate the unit in an area with Tx/Rx mode 2.   
e) Transmit Message 22 using a non-base station MMSI.

# 13.1.3 Required results

The following results are required.

a) Check that the channel management regions are not stored and not used by the EUT.   
b) Check that the EUT transmits and receives on the primary channels assigned for each region, alternating channels and halving the reporting interval when passing through the transitional zones (see Table 15). Check that the EUT reverts to default autonomous operation on the regional channels after leaving the transitional zones. Check that TXT and ACA sentences are output when defining the area, crossing the boundary of the area and on request. The In-use flag shall be set to "1" if the position is inside the area which is defined by the two corner points of the area setting (e.g. the grey area defining region 2 in Figure 11).

Table 15 – Required channels in use   

<table><tr><td></td><td>Area</td><td>Channels in use</td></tr><tr><td>1</td><td>Default region</td><td>AIS 1, AIS 2</td></tr><tr><td>2</td><td>First transitional zone</td><td>AIS 1, CH A 2</td></tr><tr><td>3</td><td>Region 2</td><td>CH A 2, CH B 2</td></tr><tr><td>4</td><td>Second transitional zone</td><td>CH A 2, CH A 1</td></tr><tr><td>5</td><td>Region 1</td><td>CH A 1, CH B 1</td></tr></table>

c) Check that the EUT transmits on only channel A with the nominal reporting interval (the number of transmissions doubles on the active channel when transmitting on one channel only).   
d) Check that the EUT transmits on channel B only with the nominal reporting rate.   
e) When using a non-base station MMSI, verify that the EUT does not accept the channel management.

# 13.2 Channel management by addressed Message 22

# 13.2.1 Purpose

The purpose of this test is to ensure that the EUT uses the regional operating settings of an addressed Message 22.

# 13.2.2 Method of measurement

Set up a standard test environment and operate the EUT in autonomous mode.

a) Send Message 4 within 120 NM and Message 22 with valid regional operating settings that are different from the default operating settings to the EUT. The regional operating area includes the current position of own station.   
b) Send an addressed Message 22 to the EUT with regional operating settings different from the previous command.   
c) Move the EUT out of the regional operating area defined by the previous addressed command and into an area without regional operating settings.

# 13.2.3 Required results

Check that:

a) the EUT uses the regional operating settings commanded to it in 13.2.2 a);   
b) the EUT uses the regional operating settings commanded to it in 13.2.2 b);   
c) the EUT reverts to default.

# 13.3 Invalid regional operating areas

# 13.3.1 Purpose

The purpose of this test is to ensure that the EUT rejects invalid regional operating areas (three regional operating areas with same corner).

# 13.3.2 Method of measurement

Set up standard test environment and operate the EUT in autonomous mode. Perform, after completion of all other tests related to change of regional operating settings, the following.

a) Send three different valid regional operating settings with adjacent regional operating areas, their corners within 8 NM of each other, to the EUT using Message 22. The current own position of the EUT shall be within the regional operating area of the third regional operating setting.   
b) Move current own position of the EUT consecutively to the regional operating areas of the first two valid regional operating settings.

# 13.3.3 Required results

Check that

a) the EUT uses the operating settings that were in use prior to receiving the third regional operating setting;   
b) the EUT consecutively uses the regional operating settings of the first two received regional operating areas.

# 13.4 Continuation of autonomous mode reporting interval

# 13.4.1 Purpose

The purpose of this test is to ensure that the EUT maintains autonomous reporting interval in a transitional zone.

# 13.4.2 Method of test

When in the presence of an assigned mode command, and in a transition zone, check that the EUT continues to report at the autonomous reporting interval.

# 13.4.3 Required result

Ensure that the autonomous reporting interval is maintained.

# 13.5 Slot reuse and FATDMA reservations

(See 7.3.2.4)

# 13.5.1 Method of measurement

Set up standard test environment and operate EUT in autonomous mode. Assure that at test receiver location the signal level received from EUT exceeds the signal level received from test transmitter.

a) Transmit test targets on channel A with $50 \%$ channel load. Channel B is free. This test covers Rule 0 and 1.   
b) Transmit near and distant test targets with $100 \%$ channel load on channel A in all selection intervals which are under observation. Channel B is free. There shall be enough different targets to allow the EUT to meet the requirement to reuse only one slot of each target per frame.   
c) Transmit near and distant test targets with $100 \%$ channel load on channel B in all selection intervals which are under observation. Channel A is free.   
d) Transmit Message 4 with a position distance $< 1 2 0$ NM and Message 20 with slot reservations on channel A. Transmit near and distant test targets in the unreserved slots on channel A. Channel B is free.

# 13.5.2 Required results

Confirm the following.

a) Only free slots are used for transmission on channel A. Confirm that only slots which are free on channel A are used for transmissions on channel B.   
b) Slots of the most distant test targets are used for transmission on channel A. Check that not more than one slot of a station is reused in a frame.   
c) For transmission on channel A, the candidate slots on channel A are organized according to the most distance station on channel B.   
d) Only unreserved slots are used on channel A. Confirm that slots of the most distant test targets are used for transmission. Confirm that for transmissions on channel B only slots which are not reserved on channel A are used after the next regular time-out 0.

# 13.6 Long-range application by broadcast

(See 7.8)

# 13.6.1 Long-range broadcast

# 13.6.1.1 Method of measurement

Set up standard test environment, enable the EUT to transmit Message 27 and operate EUT in autonomous mode. Use base stations MMSI to transmit Message 4 and Message 23. Record the transmitted messages from the EUT. The long-range channels are channel 75 and channel 76.

a) Do not apply Message 4 and Message 23.

b) Apply the Message 4 with the long range control bit set to 1 and 0. Place the EUT inside the RF footprint (Message 4 receiving area) of a base station.   
c) Apply the Message 4 with the long range control bit set to 1 and 0. Using the same MMSI as the Message 4, broadcast the Message 23 with station type 10 to define the base station coverage area. Place the EUT inside the RF footprint area, but outside the base station coverage area.   
d) Apply the Message 4 with the long range control bit set to 1 and 0. Using the same MMSI as the Message 4, broadcast the Message 23 with station type 10 to define the base station coverage area. Place the EUT inside the base station coverage area. Message 23 fields after station type shall not match current settings of EUT.   
e) Repeat the test d) using different MMSIs for Message 4 and Message 23.   
f) Apply the Message 4 with the long range control bit set to 0. Using the same MMSI as the Message 4, broadcast the Message 23 with station type 10 to define the base station coverage area. Place the EUT inside the base station coverage area. After 6 min, remove transmissions of Message 23.   
g) Apply the Message 4 with the long range control bit set to 0. Using the same MMSI as the Message 4, broadcast the Message 23 with station type 10 to define the base station coverage area. Place the EUT inside the base station coverage area. After 6 min, remove transmissions of Message 4.

# 13.6.1.2 Required results

Check that EUT transmits the appropriate messages. For example, in addition to the normal transmission of Messages 18 and 24 with adequate reporting interval on AIS 1 and AIS 2, confirm the following.

a) EUT transmits Message 27 alternating the long-range channels with 3 min reporting interval. Confirm that the content of Message 27 is correct.   
b) Irrespective of the Message 4 long range control bit status, EUT transmits Message 27 alternating on the long-range channels with 3 min reporting interval.   
c) Irrespective of the Message 4 long range control bit status, EUT transmits Message 27 alternating on the long-range channels with 3 min reporting interval.   
d) EUT transmits Message 27 alternating on the long-range channels with 3 min reporting interval when the Message 4 long-range control bit is set to 1. EUT stops transmitting Message 27 when the Message 4 long-range control bit is set to 0. Verify fields after station type in received Message 23 are ignored.   
e) Irrespective of the Message 4 long range control bit status, EUT transmits Message 27 alternating on the long-range channels with 3 min reporting interval.   
f) EUT begins transmission of Message 27 no sooner than 4 min and no later than 11 min (8 min timeout $^ { + 3 }$ min transmission interval) after Message 23 was removed;   
g) EUT begins transmission of Message 27 beyond 3 min after Message 4 was removed.

# 13.6.2 Multiple assignment operation

# 13.6.2.1 Method of measurement

Set up standard test environment, enable the EUT to transmit Message 27 and operate EUT in autonomous mode with a reporting interval of 10 s. Use base stations MMSI to transmit Message 4 and Message 23. Record the transmitted messages from the EUT.

a) Using different MMSIs, apply the Message 4 with long range control bit set to 1 and 0 from multiple base stations partially overlapping their RF footprints. Broadcast the Message 23 from multiple base stations with station type 10 to define the base station coverage areas not overlapping. Place the EUT inside the overlapped RF footprint area but outside the coverage area of both base stations.   
b) Using different MMSIs, apply the Message 4 with long range control bit set to 1 and 0 from multiple base stations partially overlapping RF footprints. Broadcast the Message 23 from

multiple base stations with station type 10 to define the base station coverage areas partially overlapping the base station coverage areas. Place the EUT inside the overlapped base station coverage area.

c) Using different MMSIs, apply the Message 4 with long range control bit set to 1 and 0 from multiple base stations partially overlapping RF footprints. Broadcast the Message 23 from one base station with station type 10 to define the base station coverage areas. Do not broadcast Message 23 from other base stations. Place the EUT inside the RF footprint area of base station not broadcasting Message 23 but outside the coverage area of the base station transmitting Message 23.

# 13.6.2.2 Required results

Verify that

a) irrespective of the Message 4 long-range control bit status of both base stations, EUT transmits Message 27 alternating on the long-range channels with 3 min reporting interval;   
b) EUT transmits Message 27;   
c) irrespective of the Message 4 long range control bit status of both base stations, EUT transmits Message 27 alternating on the long-range channels with 3 min reporting interval.

# 13.7 Other features

(See 4.1.4)

The performance of other features provided shall be self-certified by the manufacturer.

# Annex A

# (normative)

# DSC channel management

# A.1 DSC functionality

(See 7.2.3.7)

The AIS device shall be capable of performing regional channel designation and regional area designation as defined in ITU-R M.1371, DSC transmissions (acknowledgements or responses) shall not be broadcast.

The DSC functionality shall be accomplished by using a dedicated DSC receiver or by time sharing the TDMA receivers. The primary use of this feature is to receive channel management messages when AIS 1 and/or AIS 2 are not available.

The AIS device shall be capable of processing message type 104 with expansion symbols No. 00, 01, 09, 10, 11, 12, and 13 of Table 5 of ITU-R M.825-3:1998 (DSC test signal number 2 for this test) by performing operations in accordance with ITU-R M.1371 with the regional frequencies and regional boundaries specified by these calls.

Before responding to channel management commands, the AIS device shall check that the sender MMSI is valid (see 6.8).

For DSC channel management using geographical area calls, the end of sequence (EOS) character shall be $\mathsf { E O S } ~ = ~ 1 2 7$ (no response requested). However, for compatibility, AIS receivers shall respond to DSC channel management commands ending in $" \mathsf { E O S } = \mathsf { 1 2 7 " }$ or $" { \sf E O S } = 1 1 7 ( \sf { R Q } ) "$ , even though Class B "SO" is not capable of transmitting DSC acknowledgements.

# A.2 DSC time sharing

In the case of equipment which implements the DSC receive function by time sharing the TDMA receivers, the following shall be observed.

One of the receive processes shall monitor DSC channel 70 for the 30 s time periods in Table A.1. This selection shall be swapped between the two receive processes.

If the AIS is utilising this time sharing method to receive DSC, AIS transmissions shall still be performed during this period. The AIS receivers’ channel switching time shall be such that the DSC monitoring is not interrupted for more than 0,5 s per AIS transmission.

NOTE During the DSC monitoring periods, TDMA receptions will necessarily be disrupted due to this time sharing of the AIS receiver. Proper performance of the AIS assumes that DSC Channel Management messages are transmitted in compliance with ITU-R M.825-3 which requires duplicate messages with a gap of 0,5 s between the two transmissions. This will ensure that the AIS device can receive at least one DSC channel management message during each DSC monitoring time without any consequences to its AIS transmit performance.

These periods shall be programmed into the unit during its configuration. Unless some other monitoring schedule is defined by a competent authority, the default monitoring times in Table A.1 shall be used. The monitoring schedule shall be programmed into the unit during initial configuration. During the DSC monitoring times, scheduled autonomous or assigned transmissions, and responses to interrogations shall continue.

Table A.1 – DSC monitoring times   

<table><tr><td>Minutes past UTC hour</td></tr><tr><td>05:30 to 05:59</td></tr><tr><td>06:30 to 06:59</td></tr><tr><td>20:30 to 20:59</td></tr><tr><td>21:30 to 21:59</td></tr><tr><td>35:30 to 35:59</td></tr><tr><td>36:30 to 36:59</td></tr><tr><td>50:30 to 50:59</td></tr><tr><td>51:30 to 51:59</td></tr><tr><td>NOTE Refer to ITU-R M.1371.</td></tr></table>

For test purposes, the unit may be placed into a mode, which monitors DSC every minute. Entry to this mode shall not be available to the end-user.

Means shall be provided to disable DSC monitoring during setup.

# A.3 DSC test signals

# A.3.1 DSC test signal number 1

A DSC modulated data signal comprising an infinite length of 01010101 (dotting pattern; refer to ITU-R M.825-3).

# A.3.2 DSC test signal number 2

For test purposes, a "DSC channel management standard test call" is defined as a geographical call to an appropriate area, with category 103 and the expansion Messages 9 (primary channel), 10 or 11 (secondary channel), 12 (NE corner) and 13 (SW corner of region) with valid information.

# A.3.3 DSC test signal number 3

This test signal is an ITU-R M.493 geographic call with the position of the EUT inside the addressing area.

# A.3.4 DSC test signal number 4

This test signal is an ITU-R M.493 individual call addressed to the EUT.

# A.4 DSC functionality tests

# A.4.1 General

For the tests in Clause A.4, set the EUT into assigned mode using channels AIS 1 and AIS 2 with a reporting interval of $\boldsymbol { 1 0 \ s }$ .

# A.4.2 Method of measurement

Send a sequence of valid calls consisting of

• DSC test signal number 2,   
• DSC test signal number 3,

• DSC test signal number 2,   
• DSC test signal number 4, and   
• DSC test signal number 2.

# A.4.3 Required results

Check that the EUT AIS operation is not affected by the interleaved calls.

# A.4.4 Regional area designation

Perform the following tests using DSC test signal number 2.

Send DSC test signal number 2 to the EUT but with symbol numbers appropriate to the geographical regions and channels specified in the test. Note the transition boundary is 5 NM in this test.

# A.4.5 Scheduling

# A.4.5.1 General

The purpose of this test is to confirm that the EUT’s AIS reporting is not affected during the DSC monitoring times and a response is not transmitted.

# A.4.5.2 Method of measurement

Send DSC test signal number 2 to the EUT, with $\mathsf { E O S } = 1 2 7$ and another signal with $\mathsf { E O S } = 1 1 7$ (RQ).

# A.4.5.3 Required results

Check that the EUT’s AIS reporting is not affected during the DSC monitoring times.

Check that the EUT accepts the channel management, but a response is not transmitted in either case of $\mathsf { E O S } = 1 2 7$ and 117.

# A.4.6 DSC flag in Message 18

# A.4.6.1 General

The purpose of this test is to confirm that the DSC flag is set properly when DSC functionality is available.

# A.4.6.2 Method of measurement

Perform the following:

a) enable DSC monitoring;   
b) disable DSC monitoring.

# A.4.6.3 Required results

Check that

a) the DSC flag is set to one, and   
b) the DSC flag is set to zero.

# A.4.7 DSC monitoring time plan

# A.4.7.1 General

The purpose of this test is to confirm that DSC commands are received during DSC monitoring times and, if time-sharing is used, are not received outside those times.

# A.4.7.2 Method of measurement

Perform the following:

a) transmit DSC test signal 2 during monitoring time;   
b) transmit DSC test signal 2 outside monitoring time.

# A.4.7.3 Required results

Check that

a) the DSC call is received, and   
b) the DSC call is not received.

# A.4.8 Replacement or erasure of dated or remote regional operating settings

# A.4.8.1 Method of measurement

Set up standard test environment. Send a valid regional operating setting to the EUT by Message 22 with the regional operating area including the own position of the EUT. Consecutively send a further seven (7) valid regional operating settings to EUT, using both Message 22 and DSC test signal number 2, with regional operating areas not overlapping to the first and to each other. Perform the following in the order shown.

a) Send a ninth Message 22 to the EUT with valid regional operating areas not overlapping with the previous eight regional operating areas.   
b) Step 1: set own position of EUT into any of the regional operating areas defined by the second to the ninth telecommands sent to the EUT previously.

Step 2: send a tenth telecommand to the EUT, with a regional operating area which partly overlaps the regional operating area to which the EUT was set by step 1 but which does not include the own position of the EUT.

c) Step 1: move own position of EUT to a distance of more than 500 NM from all regions defined by previous commands.

Step 2: consecutively set own position of EUT to within all regions defined by the previous telecommands.

# A.4.8.2 Required results

After the initialisation, the EUT shall operate according to the regional operating settings defined by the first Message 22 sent.

a) Check that the most distant area is removed.   
b) Step 1: check that the EUT changes its operating settings to those of that region which includes own position of the EUT.

Step 2: check that the EUT reverts to the default operating settings.

NOTE Since the regional operating settings to which the EUT was set in step 1 are erased due to step 2, and since there is no other regional operating setting due to their non-overlapping definition, the EUT returns to default.

c) Step 1: check that the EUT operates with the default settings.   
Step 2: check that the EUT operates with the default settings.

# A.4.9 Test of addressed telecommand

# A.4.9.1 Method of measurement

Set up a standard test environment and operate EUT in autonomous mode. Perform the following tests in the following order.

a) Send a DSC test signal number 2 with valid regional operating settings that are different from the default operating settings, to the EUT with a regional operating area, which contains the current position of own station.   
b) Send an addressed DSC channel management command to the EUT with different regional operating settings than the previous command.   
c) Move the EUT out of the regional operating area defined by the previous addressed telecommand into an area without regional operating settings.

# A.4.9.2 Required results

Check that

a) the EUT uses the regional operating settings commanded to it in A.4.9.1 a);   
b) the EUT uses the regional operating settings commanded to it in A.4.9.1 b);   
c) the EUT reverts to default.

# A.4.10 Invalid regional operating areas

# A.4.10.1 General

Test for invalid regional operating areas (three regional operating areas with same corner).

# A.4.10.2 Method of measurement

Set up standard test environment and operate EUT in autonomous mode. Perform the following tests in the following order after completion of all other tests related to change of regional operating settings:

a) send three different valid regional operating settings with adjacent regional operating areas, their corners within eight miles of each other, to the EUT by DSC test signal number 2. The current own position of the EUT shall be within the regional operating area of the third regional operating setting;   
b) move current own position of the EUT consecutively to the regional operating areas of the first two valid regional operating settings.

# A.4.10.3 Required results

Check that

a) the EUT uses the operating settings that were in use prior to receiving the third regional operating setting;   
b) the EUT consecutively uses the regional operating settings of the first two received regional operating areas.

# A.5 DSC receiver tests

# A.5.1 General

In the case TDMA receiver is used for DSC reception on a time-shared basis, the EUT will need to be placed into a test mode that enables continuous reception of the DSC signals. However, the tests A.5.2 to A.5.7 may be waived at the discretion of the test house and this

fact noted in the test report. This waiver condition also applies if the manufacturer implements a dedicated DSC receiver and declares that it is identical to the TDMA receiver.

# A.5.2 Maximum sensitivity

# A.5.2.1 Definition

The maximum sensitivity of the receiver is the minimum level of the signal dBm at the nominal frequency of the receiver which, when applied to the receiver input with a test modulation, will produce a bit error rate of $1 0 ^ { - 2 }$ .

# A.5.2.2 Method of measurement

The wanted signal shall be DSC test signal number 1. The EUT shall provide a logic level test output from its internal DSC demodulator to measure bit error rate. Alternatively, packet error rate may be measured and interpreted back into bit error rate by calculation.

a) The wanted signal shall be at the nominal frequency (156,525 MHz) and the signal level at the receiver input shall be set to –107 dBm.   
b) The test shall be repeated at the nominal carrier frequency 156,525 MHz + 1,5 kHz and 156,525 MHz – 1,5 kHz.   
c) Repeat the test at nominal frequency with the signal level of –101 dBm under extreme conditions.

# A.5.2.3 Required results

The BER shall not exceed $1 \%$ in all cases.

# A.5.3 Error behaviour at high input levels

# A.5.3.1 Definition

The dynamic range of the equipment is the range from the minimum to the maximum level of a radio frequency input signal at which the bit error rate in the output of the receiver does not exceed a specified value.

# A.5.3.2 Method of measurement

A test signal, in accordance with DSC test signal number 1, shall be applied to the receiver input. The level of the test signal shall be –7 dBm.

# A.5.3.3 Required results

The BER shall not exceed $1 \%$ .

# A.5.4 Co-channel rejection

# A.5.4.1 Definition

The co-channel rejection is a measure of the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of an unwanted modulated signal, both signals being at nominal frequency of the receiver.

# A.5.4.2 Method of measurement

The wanted signal shall be DSC test signal number 1. The level of the wanted signal shall be –104 dBm.

The unwanted signal shall be modulated by $4 0 0 ~ \mathsf { H z }$ with a deviation of ±3 kHz. The input level of the unwanted signal shall be –114 dBm.

Both input signals shall be at the nominal frequency of the receiver under test, and the measurement shall be repeated for displacements of the unwanted signal of up to $\pm 3 \mathsf { k H z }$ .

# A.5.4.3 Required results

The BER shall not exceed $1 \%$ .

# A.5.5 Adjacent channel selectivity

# A.5.5.1 Definition

The adjacent channel selectivity characterises the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of an unwanted modulated signal that differs in frequency from the wanted signal by $2 5 ~ \mathsf { k H z }$ .

# A.5.5.2 Method of measurement

The wanted signal shall be DSC test signal number 1. The level of the wanted signal shall be –104 dBm. The unwanted signal shall be modulated by $4 0 0 ~ \mathsf { H z }$ with a deviation of ±3 kHz. The input level of the unwanted signal shall be –34 dBm.

The unwanted signal shall be tuned to the centre frequency of the upper adjacent channels.

The measurement shall be repeated with the unwanted signal tuned to the centre frequency of the lower adjacent channel.

# A.5.5.3 Required results

The BER shall not exceed $1 \%$ in all cases.

# A.5.6 Spurious response rejection

# A.5.6.1 Definition

The spurious response characterises the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of an unwanted modulated signal with frequencies outside the band of the receiver.

# A.5.6.2 Method of measurement

The wanted signal shall be DSC test signal number 1. The level of the wanted signal shall be –104 dBm.

The unwanted signal shall be unmodulated. The frequency range shall be calculated in the same manner as in 11.2.5. The level of the unwanted signal shall be –34 dBm.

# A.5.6.3 Required results

The BER shall not exceed $1 \%$ .

# A.5.7 Inter-modulation response rejection

# A.5.7.1 Definition

The inter-modulation response ratio characterises the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of two or more unwanted signals with a specific frequency relationship to the wanted signal frequency.

# A.5.7.2 Method of measurement

The wanted signal represented by signal generator A shall be at the nominal frequency of the receiver and shall be DSC test signal number 1. The level of the wanted signal shall be –104 dBm.

The unwanted signal from signal generator B shall be unmodulated and adjusted to a frequency $5 0 ~ \mathsf { k H z }$ above the nominal frequency of the receiver. The second unwanted signal from signal generator C shall be modulated by $4 0 0 ~ \mathsf { H z }$ with a deviation of $\pm 3 \mathsf { k H z }$ and adjusted to a frequency $1 0 0 ~ \mathsf { k H z }$ above the nominal frequency of the receiver. The input level of each unwanted signal shall be –39 dBm. The test shall be repeated with the frequency of the unwanted signals below the nominal frequency of the receiver.

# A.5.7.3 Required results

The BER shall not exceed $1 \%$ .

# A.5.8 Blocking or desensitisation

# A.5.8.1 Definition

The blocking immunity characterises the capability of the receiver to receive a wanted modulated signal without exceeding a given degradation due to the presence of an unwanted modulated signal with frequencies outside the band of the receiver.

# A.5.8.2 Method of measurement

The wanted signal shall be DSC test signal number 1. The level of the wanted signal shall be –104 dBm.

The unwanted signal shall be unmodulated. The frequency shall be varied between –10 MHz and –1 MHz and also between $+ 1$ MHz and $+ 1 0$ MHz relative to the nominal frequency of the wanted signal. The level of the unwanted signal shall be –20 dBm.

# A.5.8.3 Required results

The BER shall not exceed $1 \%$ .

# Annex B

# (normative)

# Calculation of area size

# B.1 Importance of a common method for area size

An AIS unit will need to calculate distances with regard to many aspects. Many of these distances are paramount to how the AIS unit should operate in certain situations. This includes (but is not limited to) calculating distance between own vessel and other vessels within radio range, channel management areas (sizes and distance from its boundaries) and interrogation areas. This annex specifies the methods allowed to use with regard to the different distance and size calculations.

# B.2 Calculation of area sizes

To calculate the size of the areas given in Message 22 and Message 23, along with the channel management message sent by DSC, the following method shall be used.

Coordinates of NE and SW points of the area are given in Table B.1.

Table B.1 – Coordinate points   

<table><tr><td>Corner</td><td>Latitude</td><td>Longitude</td></tr><tr><td>NE</td><td>a deg, b min</td><td>c deg, d min</td></tr><tr><td>SW</td><td>e deg, f min</td><td>g deg, h min</td></tr></table>

The length around equator is defined in Equation (B.1).

The length of the NE-NW side $( L _ { \mathsf { N E - N W } } )$ is defined in Equation (B.2).

The length of the SE-SW side $( L _ { \mathsf { S E - S W } } )$ is defined in Equation (B.3).

The length of the NE-SE $( L _ { \mathsf { N E - S E } } )$ and NW-SW $( L _ { \mathsf { N W - S W } } )$ is defined in Equation (B.4).

$$
L _ {E} = 4 0 0 7 5, 0 1 7 (\mathrm {k m}) / 1, 8 5 2 (\mathrm {k m} / \mathrm {N M}) = 2 1 6 3 8, 7 7 8 (\mathrm {N M}) \tag {B.1}
$$

$$
L _ {\mathrm {N E - N W}} = \left(\left(c + d / 6 0\right) - \left(g + h / 6 0\right)\right) \times \left(L _ {\mathrm {E}} \times \cos \left(a + b / 6 0\right)\right) / 3 6 0 (\mathrm {N M}) \tag {B.2}
$$

$$
L _ {\mathrm {S E} - \mathrm {S W}} = \left(\left(c + d / 6 0\right) - \left(g + h / 6 0\right)\right) \times \left(L _ {\mathrm {E}} \times \cos \left(e + f / 6 0\right)\right) / 3 6 0 (\mathrm {N M}) \tag {B.3}
$$

$$
L _ {\mathrm {N E - S E}} = L _ {\mathrm {N W - S W}} = \left(\left(a + b / 6 0\right) - \left(e + f / 6 0\right)\right) \times L _ {\mathrm {E}} / 3 6 0 (\mathrm {N M}) \tag {B.4}
$$

To achieve the required accuracy in these calculations, the calculation resolution needs to have at least 3 fractional digits (i.e. 16 bits floating point).

# Annex C

# (informative)

# Digital interface sentence to parameter group number equivalence

Digital interface network IEC 61162-3 parameter group numbers are equivalent to the following network IEC 61162-1 sentences as described in Table C.1.

Table C.1 – Digital sentence to PGN equivalence   

<table><tr><td>IEC 61162-1 sentence</td><td>IEC 61162-3 PGN with description</td><td>Source</td></tr><tr><td>ALR</td><td>126983 Alert PGN</td><td>IEC 61924-2: 2012</td></tr><tr><td>ACK</td><td>126984 Alert response</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td rowspan="4">ABM</td><td>129795 AIS addressed binary message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129801 AIS addressed safety related message</td><td>IEC 61162-3:2008/AMD2 2014</td></tr><tr><td>129811 AIS Single Slot binary message</td><td rowspan="2">NMEA 2000® Network Message Database - Ver. 2.100 February 2015</td></tr><tr><td>129812 AIS Multi-slot binary message</td></tr><tr><td rowspan="4">BBM</td><td>129797 AIS binary broadcast message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129802 AIS broadcast safety related message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129811 AIS Single Slot binary message</td><td rowspan="2">NMEA 2000® Network Message Database - Ver. 2.100 February 2015</td></tr><tr><td>129812 AIS Multi-slot binary message</td></tr><tr><td>ABK</td><td>129796 AIS Acknowledge</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td rowspan="24">VDM and VDO</td><td>129038 AIS Class A position report</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129039 AIS Class B position report</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129040 AIS Class B extended position report</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129041 AIS Aids to Navigation (AtoN) report</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129792 AIS DGNSS broadcast binary message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129793 AIS UTC and date report</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129794 AIS Class A static and voyage related data</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129795 AIS addressed binary message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129796 AIS acknowledge</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129797 AIS binary broadcast message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129798 AIS SAR aircraft position report</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129800 AIS UTC /date Inquiry</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129801 AIS addressed safety related message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129802 AIS safety related broadcast message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129803 AIS interrogation</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129804 AIS assignment mode command</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129805 AIS data link management message</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129806 AIS channel management</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129807 AIS group assignment</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129809 AIS Class B &quot;CS&quot; static data report, Part A</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129810 AIS Class B &quot;CS&quot; static data report, Part B</td><td>IEC 61162-3:2008/AMD2:2014</td></tr><tr><td>129811 AIS Single Slot binary message</td><td rowspan="2">NMEA 2000® Network Message Database - Ver. 2.100 February 2015</td></tr><tr><td>129812 AIS Multi-slot binary message</td></tr><tr><td>129813 AIS Long Range Broadcast message</td><td>(ditto)</td></tr></table>

# Bibliography

IEC 61162-3:2008, Maritime navigation and radiocommunication equipment and systems – Digital interfaces – Part 3: Serial data instrument network   
IEC 61162-3:2008/AMD1:2010   
IEC 61162-3:2008/AMD2:2014   
IEC 61924-2:2012, Maritime navigation and radiocommunication equipment and systems – Integrated navigation systems – Part 2: Modular structure for INS – Operational and performance requirements, methods of testing and required test results   
IEC 62287-1, Maritime navigation and radiocommunication equipment and systems – Class B shipborne equipment of the automatic identification system (AIS) – Part 1: Carrier-sense time division multiple access (CSTDMA) techniques   
ISO 9000 (all parts), Quality management and quality assurance standards   
ITU-R Recommendation M.493, Digital selective-calling system for use in the maritime mobile service   
ITU-T O.153, Basic parameters for the measurement of error performance at bit rates below the primary rate   
IMO, International Convention for the Safety of Life at Sea (SOLAS)   
IMO COMSAR.1/Circ.46:2009-02, AIS safety-related messaging   
NMEA $\scriptstyle 2 0 0 0 \ @$ Network Message Database – Ver. 2.100 February 2015

# INTERNATIONAL ELECTROTECHNICAL COMMISSION

3, rue de Varembé

PO Box 131

CH-1211 Geneva 20

Switzerland

Tel: + 41 22 919 02 11

Fax: + 41 22 919 03 00

info@iec.ch

www.iec.ch