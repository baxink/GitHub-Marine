# GUIDANCE NOTES ON

# CONTROL OF HARMONICS IN ELECTRICAL POWER SYSTEMS

MAY 2006

American Bureau of Shipping

Incorporated by Act of Legislature of

the State of New York 1862

 2006 American Bureau of Shipping. All rights reserved.

1701 City Plaza Drive

Spring, TX 77389 USA

This Page Intentionally Left Blank

# Foreword

Harmonics (or distortion in wave form) has always existed in electrical power systems. It is harmless as long as its level is not substantial. However, with the recent rapid advancement of power electronics technology, so-called nonlinear loads, such as variable frequency drives for motor power/speed control, are increasingly finding their way to shipboard or offshore applications. Harmonics induced by these nonlinear loads are a potential risk if they are not predicted and controlled.

The ABS Guidance Notes for Control of Harmonics in Electrical Power Systems has been developed in order to raise awareness among electrical system designers of the potential risks associated with the harmonics in electrical power systems onboard ships or offshore installations. These Guidance Notes encompass topics from the fundamental physics of harmonics to available means of mitigation to practical testing methods. These Guidance Notes are intended to aid designers to plan an appropriate means of harmonics mitigation early in the design stage of the electrical power distribution systems to make the system robust and predictable.

# Terms of Use

The information presented herein is intended solely to assist the reader in the methodologies and/or techniques discussed. These Guidance Notes do not and cannot replace the analysis and/or advice of a qualified professional. It is the responsibility of the reader to perform their own assessment and obtain professional advice. Information contained herein is considered to be pertinent at the time of publication, but may be invalidated as a result of subsequent legislations, regulations, standards, methods, and/or more updated information and the reader assumes full responsibility for compliance. This publication may not be copied or redistributed in part or in whole without prior written consent from ABS.

This Page Intentionally Left Blank

# GUIDANCE NOTES ON

# CONTROL OF HARMONICS IN ELECTRICAL POWER SYSTEMS

# CONTENTS

SECTION 1 Introduction ...........

1 Background ..   
2 The Use of Electric Drives in Marine Applications .. .. 5   
3 Main Propulsion Drives ... . 7   
4 The Future? . . 9

FIGURE 1 Input Waveforms (440 V) to 6-Pulse DC SCR Drive .. 2   
FIGURE 2 Line-to-line Voltage (440 V) at Input to a 6-Pulse DC SCR Drive .. .. 2   
FIGURE 3 415 V Line-to-line Volts on Ship with Four 1100 kW/ 1500 HP AC SCR Converter-fed Thruster Motors ....... 3   
FIGURE 4 Primary Voltage (11 kV) of Transformer Supplying a 2 MW (2680 HP) Variable Frequency Drive . . 3   
FIGURE 5 Typical Power System Single Line Diagram for DP Class 3 Drilling Rig .. .. 5   
FIGURE 6 Electrically-driven Podded Propulsor .. . 8   
FIGURE 7 Dynamically-positioned Shuttle Tanker Equipped with AC Electric Variable Speed Main Propulsion and Thrusters .. . 8

SECTION 2 The Production of Harmonics ............ ... 11

1 Production of Harmonics . 11   
2 Characteristic Harmonic Currents .. .. 15   
3 Effect of Harmonic Currents on Impedance(s) ........ ... 19   
4 Calculation of Voltage Distortion .... ... 20   
5 Harmonic Sequence Components .. .. 22   
6 Line Notching . . 22   
7 Interharmonics . .. 25   
8 Subharmonics .. .. 27

TABLE 1 Harmonic Sequence Components for 6-Pulse Rectifier .. . 22

FIGURE 1 Voltage and Current Waveforms for Linear Load ......11

FIGURE 2a Single Phase Full Wave Rectifier... .11

FIGURE 2b Load and AC Supply Currents .. .11

FIGURE 3a Simple Single Line Diagram.. ..12

FIGURE 3b Load Current and Volt Drop Waveforms...... ..12

FIGURE 4 How Voltage Distortion is Produced (Simplified) .......12

FIGURE 5 Typical Computer Nonlinear Load . .13

FIGURE 6 Single-phase Switched Mode Power Supply .............13

FIGURE 7 Harmonic Spectrum of Currents Drawn by Computer Switched Mode Power Supply .. .14

FIGURE 8 Construction of Complex Wave . ..14

FIGURE 9 Computer Power Supply with Single-phase Full Wave Bridge Rectifier . .16

FIGURE 10 Computer SMPS Input Current Waveform ................16

FIGURE 11 Typical Waveform from Computer Switched Power Supply . .17

FIGURE 12 Typical 6-Pulse PWM AC Drive ...... ..17

FIGURE 13 6-Pulse AC PWM Drive Input Current Waveforms for One Phase... .18

FIGURE 14 Typical Harmonic Spectrum for 6-Pulse AC PWM Drive .. .18

FIGURE 15 Distorted Currents Induce Voltage Distortion ............19

FIGURE 16 How Individual Harmonic Voltage Drops Develop Across System Impedances .19

FIGURE 17 Simple Three-phase SCR Bridge for Phase Control... .23

FIGURE 18 Exaggerated Example of “Line Notching” . ..23

FIGURE 19 Voltage Notching due to SCR Bridge Commutation.. .24

FIGURE 20 SCR Line Notching and Associated “Ringing”...........24

FIGURE 21 Cycloconverter Current Spectrum – Includes Interharmonics . .25

FIGURE 22 Waveform Containing both Harmonics and Interharmonics . .26

FIGURE 23 Peak Voltage Deviations due to Interharmonics Voltage. .27

# SECTION 3 Effects of Harmonics .......... .. 29

1 Generators . ..29

1.1 Thermal Losses.. .29

1.2 Effect of Sequence Components. .30

1.3 Voltage Distortion . .30

1.4 Line Notching and Generators.. .32

1.5 Shaft Generators .. .33

2 Transformers.. ..33

2.1 Thermal Losses.. .33   
2.2 Unbalance, Distribution Transformers and Neutral Currents . 34   
2.3 Transformer Derating or K-factor Transformer... .. 34

3 Induction Motors .. ..36

3.1 Thermal Losses.. . 36   
3.2 Effect of Harmonic Sequence Components . . 37   
3.3 Explosion-proof Motors and Voltage Distortion .. .38

4 Variable Speed Drives .. ..39   
5 Lighting . ...41

5.1 Flicker . .. 41   
5.2 Effects of Line Notching on Lighting... . 42   
5.3 Potential for Resonance. .. 42

6 Uninterruptible Power Supplies (UPS)... ..42   
7 Computers and Computer Based Equipment.. ...43   
8 Cables... ..45

8.1 Thermal Losses.. . 45   
8.2 Skin and Proximity Effects . 45   
8.3 Neutral Conductors in Four-wire Systems... .. 47   
8.4 Additional Effects Associated with Harmonics .. 48

9 Measuring Equipment.. ..48

10 Telephones . ..51   
11 Circuit Breakers . ..51   
12 Fuses . ..52   
13 Relays .. ..52   
14 Radio, Television, Audio and Video Equipment .. ..53   
15 Capacitors.. ..53

FIGURE 1 Equivalent Circuit for a Generator .. ...31   
FIGURE 2 Low Pass Filter for Generator AVR Sensing on Nonlinear Loads... .33   
FIGURE 3 Typical Transformer Derating Curve for Nonlinear Load .. ..35   
FIGURE 4 Proposed NEMA Derating Curve for Harmonic Voltages .. .38   
FIGURE 5 AC PWM Drive Current Distortion on Weak Source.. ..40   
FIGURE 6 PWM Drive “Flat Topping” due to Weak Source........41   
FIGURE 7 Voltage “Flat Topping” due to Pulse Currents ...........43   
FIGURE 8 Effect of DC Bus Voltage with Flat Topping.. ....43   
FIGURE 9 Flat Topping Reducing Supply Ride-through.. ........44   
FIGURE 10 Cable AC/DC Resistance, $k _ { c }$ as a Function of Harmonic Numbers . ..46   
FIGURE 11 4/0 AWG Cable – Proximity and Skin Effect due to Harmonics.. ...47

FIGURE 12 12 AWG Cable – Proximity and Skin Effect due to Harmonics .. ..47

FIGURE 13 Peak and rms Values of Sinusoidal Waveform..........49

FIGURE 14 Difficulties Conventional Meters Have Reading Distorted Waveforms . .49

# SECTION 4 Sources of Harmonics.......... .... 55

1 Distribution Systems with Single-phase Nonlinear Loads . .55

1.1 Three-wire Distribution Systems.. .55   
1.2 Four-wire Distribution Systems.. .55

2 Single-phase Nonlinear Loads... ..58

2.1 Computer-based Equipment. .58   
2.2 Fluorescent Lighting . ..60   
2.3 Televisions .. ..64   
2.4 Single-phase AC PWM Drives.. ..64

3 Three-phase Nonlinear Loads . ..65

3.1 DC SCR drives .. ..66   
3.2 AC PWM drives .. .70   
3.3 AC Cycloconverter Drives .76   
3.4 AC Load Commutated Inverter (LCI). .84

4 Additional Three-phase Sources of Harmonics ... ..90

4.1 Rotating Machines.. .90   
4.2 Transformers . .90   
4.3 UPS Systems .. .91   
4.4 Shaft Generators .. .92

FIGURE 1 Four-wire System Linear Phase Currents Return via Neutral Conductor where Balanced Phase Current Cancel Out .. .56   
FIGURE 2 Triplen Harmonics Add Up Cumulatively in Neutral Conductors with Single-phase Nonlinear Loads in Four-wire System.. ..56   
FIGURE 3 Neutral Current due to Triplen Harmonics ( $1 5 0 \mathsf { H z }$ for 50 Hz Supply) on Four-wire System. ..57   
FIGURE 4 Harmonic Spectrum Associated with Neutral Current Waveform Shown in Figure 3 . .57   
FIGURE 5 Typical Switched Mode Power Supply for Computer Based Equipment.. .58   
FIGURE 6 Typical Voltage and Current Waveforms Associated with a Switched Mode Power Supply.. .59   
FIGURE 7 Harmonic Current Spectrum of Typical Switched Mode Power Supply - $I _ { t h d }$ is $128 \%$ .. .59   
FIGURE 8 Typical Neutral Current due to Triplen Harmonics in Connected Loads on a Four-wire System... ..60   
FIGURE 9 Waveforms for Lighting Panel Comprising Fluorescent Lighting with Magnetic Ballasts and T-12 Lamps. .61

FIGURE 10 Neutral Current Waveform on Distribution Panel with Fluorescent Lighting with Magnetic Ballasts and T-12 Lamps on a Four-wire System . ..61

FIGURE 11 Same Lighting Panel as per Figure 9, but with Electronic Ballasts (Instead of Magnetic Types) and T-8 Lamps. .62

FIGURE 12 Neutral Current Waveform on Same Fluorescent Lighting Panel as Figure 10, but with Electronic Ballasts and T-8 Lamps on Four-wire System.... ..62

FIGURE 13 Comparison of Phase Current Harmonic Spectrum for Magnetic and Electronic Ballasts for Typical Fluorescent Lighting Distribution Panel $I _ { t h d }$ was $12 . 8 \%$ and $1 6 . 3 \%$ , Respectively .63

FIGURE 14 Comparison of Neutral Current Harmonic Spectrum for Magnetic and Electronic Ballasts for Typical Fluorescent Lighting Distribution Panel $I _ { t h d }$ was $1 7 1 . 2 8 \%$ and $44 \%$ , Respectively . .63

FIGURE 15 Television – Typical Current Waveform... ..64

FIGURE 16 Television – Typical Harmonic Current Spectrum .....64

FIGURE 17 Single-phase AC PWM Drive – Typical $I _ { t h d }$ is $13 5 \%$ . .65

FIGURE 18 Single-phase AC PWM Drive Current Spectrum .......65

FIGURE 19 Typical 6-Pulse DC SCR Drive with Shunt-wound DC Motor... ..66

FIGURE 20 Concept of “Constant Torque” and “Constant Power” with DC Shunt-wound Motors . ...67

FIGURE 21 Typical Dual Converter for DC Shunt-wound Motor ... ..68

FIGURE 22 Concept of “Four Quadrant Control” for DC Motors and Dual Converters .. ...68

FIGURE 23 Typical 6-Pulse DC SCR Drive Current Waveform at $100 \%$ Load.. ..69

FIGURE 24 Harmonic Current Spectrum of Typical 6-Pulse DC SCR Drive at Rated Load . ..69

FIGURE 25 Typical AC PWM Drive Block Diagram.. .70

FIGURE 26 Pulsed Nature of AC PWM Drive Input Current.........71

FIGURE 27 Typical AC PWM Drive Output (Inverter) Bridge Configuration... .72

FIGURE 28 Basic Principle of Pulse Width Modulation ... .72

FIGURE 29a AC Motor/PWM Drives Standard Speed/Torque Characteristics . .73

FIGURE 29b AC Motor/PWM Drives Standard Speed/Power Characteristics . .74

FIGURE 30 Input Current – 150 HP AC PWM Drive with $3 \%$ DC Bus Reactor – $. I _ { t h d } = 3 9 . 2 3 \%$ ... ..75

FIGURE 31 Harmonic Current Spectrum of 150 HP AC PWM Drive with $3 \%$ DC Bus Reactor – $I _ { t h d } = 3 9 . 2 3 \%$ .........75

FIGURE 32 Single-phase-to-Single-phase Cycloconverter ..........76

FIGURE 33 Waveforms for Single-phase-to-Single-phase Conversion.. 77

FIGURE 34 Three-phase 6-Pulse Cycloconverter .. ..79

FIGURE 35 Simplified Connection of Intergroup Reactor on One Phase of Circulating Current Cycloconverters...........80

FIGURE 36 Waveforms for Blocking Mode Cycloconverters ........80

FIGURE 37 Waveforms for Circulating Current Mode Cycloconverters . ..81

FIGURE 38a Input Current Associated with a 20 MW, 12-Pulse Cycloconverter .. ..82

FIGURE 38b Harmonic Current Frequency Spectrum Associated with a 20 MW, 12-Pulse Cycloconverter.. ...82

FIGURE 39 2-Pulse Cycloconverter with Three-phase Synchronous Motor.. .83

FIGURE 40 Harmonic Spectrum of 12-Pulse Cycloconverters Including Interharmonic Sidebands... ..84

FIGURE 41 Typical 6-Pulse ASCI CSI Inverter with a Squirrel Cage Induction Motor.. ..85

FIGURE 42 Output Voltage Commutation Spikes – CSI with Squirrel Cage Induction Motor .. ..85

FIGURE 43 12-Pulse Load Commutated Inverter with Synchronous Motor.. ..86

FIGURE 44 12-Pulse Load Commutated Inverter with Squirrel Cage Motor and Output Filter . ..87

FIGURE 45 Output Voltage of LCI with Synchronous Motor or Squirrel Cage Motor with Output Filter . ..87

FIGURE 46 Six Step Square Wave Current – LCI with Synchronous Motor.. ..88

FIGURE 47 Input Waveform of 6-Pulse Load Commutated Inverter .. ..89

FIGURE 48 Harmonic Spectrum Associated with a 6-Pulse Load Commutated Inverter .. ..89

FIGURE 49 Input Voltage and Current Waveforms of 6-Pulse 37.5 kVA, 480 V, 60 Hz UPS . ..91

FIGURE 50 Harmonic Input Current Spectrum for 6-Pulse 37.5 kVA, 460 V, 60 Hz UPS . ..91

FIGURE 51 Traditional Shaft Generator System... ..92

FIGURE 52 Inverter Output Voltage Waveform .. ..93

# SECTION 5 Harmonics and System Power Factor ....... .. 95

1 Power Factor in Systems with Linear Loads Only ....... ...95

2 Power Factor in Power System with Harmonics..... ..95

3 How the Mitigation of Harmonics Improves True Power Factor .. .97

FIGURE 1 Power Factor Components in System with Linear Load . ..95

FIGURE 2 Power Factor Components in System with Harmonics. .96

# SECTION 6 The Effect of Loading on Harmonic Current Distortion....99

1 Total Harmonic Voltage Distortion $\left( { { V } _ { t h d } } \right)$ . ..99   
2 Total Harmonic Current Distortion $( I _ { t h d } )$ and Reduced Loading . .99

2.1 AC PWM Drives . .. 99   
2.2 DC SCR Drives .. . 102   
2.3 Load Commutated Inverters.. . 103   
2.4 Cycloconverters . . 103   
2.5 Conclusion: Harmonic Current Magnitude and its Effect on Voltage Distortion.. . 105

FIGURE 1 Typical 6-Pulse PWM Drive (with $3 \%$ AC Line Reactor) at $100 \%$ Load – $I _ { t h d }$ Measured at 37.5%....100   
FIGURE 2 Typical Harmonic Spectrum of AC PWM Drive (with $3 \%$ AC Line Reactor) at $100 \%$ Load – $I _ { t h d }$ Measured at $3 7 . 5 \%$ .. ..100   
FIGURE 3 Typical AC PWM Drive (with $3 \%$ AC Line Reactor) at $30 \%$ Load – $I _ { t h d }$ Measured at $6 5 . 7 \%$ . . ...101   
FIGURE 4 Typical Harmonic Spectrum of AC PWM Drive (with $3 \%$ AC Line Reactor) at $30 \%$ Load – $I _ { t h d }$ Measured at $6 5 . 7 \%$ .. ..101   
FIGURE 5 6-Pulse DC Drive at $70 \%$ Loading – $I _ { t h d }$ is $3 5 . 1 \%$ ....102   
FIGURE 6 Harmonic Current Spectrum of 6-Pulse DC Drive at $70 \%$ Loading – $I _ { t h d }$ is $3 5 . 1 \%$ . ..103   
FIGURE 7 Multiple 6-Pulse Cycloconverters Input Current and Voltage Harmonic Spectrums at Low Output Frequency/Low Load . ..104   
FIGURE 8 Multiple 6-Pulse Cycloconverters Input Current and Voltage Harmonic Spectrums at High Output Frequency/High Load... ...104

# SECTION 7 Influence of Source Impedance and kVA on Harmonics... .. 107

1 “Stiff” and “Soft” Sources . ...107   
2 Illustrations of the Effect of kVA and Source Impedance Harmonics.. ...108   
3 Parallel Generator Operation and Calculation of Equivalent Short Circuit Ratings .. ..116

TABLE 1 Variation of $I _ { t h d }$ and $V _ { t h d }$ with Variation of kVA and Impedance (or $X _ { d } ^ { \prime \prime }$ ) ... ...115

FIGURE 1a 2000 kVA and $5 . 2 \%$ Impedance – $I _ { S C } / I _ { L } = 3 3 . 3 { : } 1$ , $I _ { t h d } = 2 4 . 2 \%$ , $V _ { t h d } = 4 . 7 \%$ . ...108   
FIGURE 1b Current and Voltage Waveforms for 2000 kVA/ $5 . 2 \%$ Impedance Source with 950 HP AC PWM Drive Load and 180 kW Linear Load . ..109   
FIGURE 2a 2000 kVA and $1 4 \%$ Subtransient Reactance $I _ { S C } / I _ { L } = 2 9 . 1 { : } 1$ , $I _ { t h d } = 1 9 . 1 \%$ , $V _ { t h d } = 9 . 8 \%$ .. ..110

FIGURE 2b Current and Voltage Waveforms for 2000 kVA/ $1 4 \%$ Subtransient Reactance Source with 950 HP AC PWM Drive Load and $1 8 0 \mathsf { k W }$ Linear Load .. .111

FIGURE 3a 4000 kVA and $5 . 2 \%$ Impedance – $- I _ { S C } / I _ { L } = 6 7 . 1 { : } 1$ , $I _ { t h d } = 2 7 . 1 \%$ , $V _ { t h d } = 2 . 7 \%$ . ..112

FIGURE 3b Current and Voltage Waveforms for 4000 kVA/ $5 . 2 \%$ Impedance Source with 950 HP AC PWM Drive Load and 180 kW Linear Load . .113

FIGURE 4a 4000 kVA and $1 4 \%$ Subtransient Reactance $I _ { S C } / I _ { L } = 2 6 . 6 { : } 1$ , $I _ { t h d } = 2 2 . 9 \%$ , $V _ { t h d } = 5 . 8 \%$ . ..114

FIGURE 4b Current and Voltage Waveforms for 4000 kVA/ $1 4 \%$ Subtransient Reactance Source with 950 HP AC PWM Drive Load and $1 8 0 \mathsf { k W }$ Linear Load .. .115

FIGURE 5 Paralleling of Generators .. ..116

FIGURE 6 Example of Paralleled Generators.... ..117

# SECTION 8 The Effect of Unbalance and Background Voltage Distortion .. .. 119

1 Balanced Systems . ..119   
2 Unbalanced Systems.. ..119   
2.1 Definition of Voltage Unbalance . .120   
2.2 Effect of Unbalanced Loading on Rotating Machines.. .121   
2.3 Effect of Unbalanced Loading on Harmonics . ..123   
2.4 Voltage Unbalance and Multi-pulse Drives and Systems... .125   
2.5 Background Voltage Distortion and Multi-pulse Drives and Systems... ..127   
2.6 The Effect of Voltage Unbalance and Background Voltage Distortion Using Software Modeling . .128   
2.7 Drive Mitigation – Unbalance and Background Voltage Distortion . .134

TABLE 1 Variation in $I _ { t h d }$ and $V _ { t h d }$ with Voltage Unbalance and Pre-existing Voltage Distortion . ..134

FIGURE 1 Balanced System .. ..119   
FIGURE 2 Unbalanced System.. ..119   
FIGURE 3 Symmetrical Components of an Unbalanced System .. .120   
FIGURE 4 Reduction of Insulation Life with Temperature ........122   
FIGURE 5 Derating on Induction Motors of Unbalanced Supplies .. .123   
FIGURE 6 Typical 6-Pulse AC PWM Drive Input Current Waveform on Balanced Voltages... .124   
FIGURE 7 Typical 6-Pulse AC PWM Drive Input Current Waveform on $5 \%$ Voltage Unbalance. .124

FIGURE 8 Typical 6-Pulse AC PWM Drive Input Current Waveform on $1 5 \%$ Voltage Unbalance.. ..124   
FIGURE 9 Harmonic Spectrum of 6-Pulse AC PWM Drive on Unbalanced Voltages (Fundamental Component Removed)... ...125   
FIGURE 10 Unbalance and the Effect on 12-Pulse Drives.........126   
FIGURE 11 Unbalance and the Effect on 18-Pulse Drives.........126   
FIGURE 12 Effect of Background Voltage Distortion on 18-Pulse AC PWM Drive.. ..127   
FIGURE 13a No Voltage Unbalance, No Pre-existing $V _ { t h d }$ – $I _ { t h d } = 5 . 2 \%$ , $V _ { t h d } = 4 . 9 \%$ .. ..129   
FIGURE 13b Voltage and Current Waveforms No Voltage Unbalance, No Pre-existing $V _ { t h d }$ .... ..129   
FIGURE 14a $2 \%$ Voltage Unbalance, No Pre-existing $V _ { t h d }$ – $I _ { t h d } = 1 4 . 5 \%$ , $V _ { t h d } = 5 . 2 \%$ .. ..130   
FIGURE 14b Voltage and Current Waveforms $2 \%$ Voltage Unbalance, No Pre-existing $V _ { t h d }$ .... ..130   
FIGURE 14c Three-phase Current Waveforms $2 \%$ Voltage Unbalance, No Pre-existing $V _ { t h d }$ .... ..131   
FIGURE 15a No Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d }$ – $I _ { t h d } = 1 0 . 9 \%$ , $V _ { t h d } = 6 . 2 \%$ . .131   
FIGURE 15b Voltage and Current Waveforms No Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d }$ ... ..132   
FIGURE 16a $2 \%$ Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d }$ – $I _ { t h d } = 1 8 . 5 \%$ , $V _ { t h d } = 6 . 0 \%$ .. ..132   
FIGURE 16b Voltage and Current Waveforms $2 \%$ Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d }$ ... ..133   
FIGURE 16c Three-phase Current Waveforms $2 \%$ Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d }$ .... ..133

# SECTION 9 Resonance... ... 135

1 What is Resonance?.. ...135   
2 The Conditions under which Resonance Occurs ..............135

2.1 Series Resonance.. . 135   
2.2 Parallel Resonance. . 136

3 Prevention of Resonance ...137   
3.1 The Effect of Adding a Detuning Reactor.. . 139   
4 Possibilities of Resonance on Vessels and Offshore Installations . ..140

FIGURE 1a Series Resonance.. ...135   
FIGURE 1b Parallel Resonance.. ...135   
FIGURE 2 Series Resonance Frequency Response ................137   
FIGURE 3 Typical Industrial Drive Application where Resonance is Possible.. ..138   
FIGURE 4 Simplified Connection of Detuning Reactor to Capacitor Bank . ..139

# SECTION 10 Mitigation of Harmonics ........ ... 141

1 Effect of Phase Diversity on Harmonic Currents ...............141   
2 Effect of Linear Load on Harmonic Currents . ...142   
3 Mitigation of Harmonics on Three-wire Single-phase Systems . .143

3.1 Phase Shifting . ..143   
3.2 Active Filtering .. .144

4 Mitigation of Harmonics on Four-wire Single-phase Systems .. .144

4.1 Zero Sequence Mitigation of Triplens on Four-wire Single-phase Systems. .144   
4.2 Active Filters for Four-wire Systems .. ..146

5 Standard Reactors for Three-phase AC and DC Drives ... .147

5.1 Reactors for AC PWM Drives . .148

6 AC Line Reactors for DC SCR Drives and AC Drives with SCR Input Rectifiers .. .153   
7 Special Reactors for Three-phase AC and DC Drives ......156

7.1 Wide Spectrum Filters . . 156   
7.2 Duplex Reactors.. ..160

8 Passive L-C Filters. ..166   
9 Transformer Phase Shifting (Multi-pulsing) . ..171

9.1 Double-wound Isolating Transformer Phase Shift Systems... .172   
9.2 Polygonal Non-isolating Autotransformer Phase Shift Systems... ..173   
9.3 The Effect of Voltage Unbalance on Phase Shift Performance. .175   
9.4 The Effect of Background Voltage Distortion on Phase Shift Performance. .177

10 Transformer Phase Staggering (Quasi Multi-pulse) Systems . .178   
11 Electronic Filters . ..179

11.1 Active Filters .. .179   
11.2 Hybrid Active-Passive Filters.. .185

12 “Active Front Ends” for AC PWM Drives... ..188

TABLE 1 Estimated Harmonic Current Distortion Using Quasi-24-Pulse Phase Staggering System .. .179   
FIGURE 1 Harmonic Voltage Data to $5 0 ^ { \mathrm { t h } }$ Harmonic with Respective Phase Angle Information.. .142   
FIGURE 2 Phase Shifting of Three-wire Nonlinear Loads ........143   
FIGURE 3 Four-wire System with Nonlinear Loads ... ..144   
FIGURE 4 Operation of a Zero Sequence Transformer............145   
FIGURE 5 Zero Sequence Transformer on Four-wire System .. .145

FIGURE 6 Zero Sequence Transformer and Combined Phase Shift Transformer with ZST to Cancel Triplen and $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ Harmonic Currents. ...146

FIGURE 7 Block Diagram of Active Filter on Four-wire Application... ..147

FIGURE 8 Circuit Diagram of Standard 6-Pulse AC PWM Drive.. ..148

FIGURE 9 Variation of Harmonic Currents with AC Line Reactance Only . ..150

FIGURE 10 DC Bus Reactance Only in AC PWM Drive.............152

FIGURE 11 Variation in $5 ^ { \mathrm { t h } }$ Harmonic Current for Differing Values of AC Line Reactance and DC Bus Reactance.. .153

FIGURE 12 Primary and Secondary Notching .. ...154

FIGURE 13 Line Impedance Distribution and the Effect of Notching.. .154

FIGURE 14 Wide Spectrum Filter Schematic... ...157

FIGURE 15 200 HP/150 kW AC PWM Drive with $3 \%$ DC Bus Reactor – $I _ { t h d } = 3 9 . 9 \%$ .. ...157

FIGURE 16 Typical Wide Spectrum Filter Connection Diagram – AC PWM Drive .. ..158

FIGURE 17 Trapezoidal Output Voltage from Wide Spectrum Filter . ..158

FIGURE 18 Mains Waveform with Wide Spectrum Filter – $I _ { t h d } = 4 . 6 \%$ .. .159

FIGURE 19 Typical Wide Spectrum Filter Performance – 350 HP AC PWM Drive with $3 \%$ AC Line Reactance.. .159

FIGURE 20 Wide Spectrum Filter with 12-Pulse AC Drive.. .160

FIGURE 21 Duplex Reactor Schematic ...161

FIGURE 22a System Voltage Waveform ...161

FIGURE 22b Duplex Reactor Correction Voltage . ...162

FIGURE 22c “Corrected” System Voltage.. ...162

FIGURE 23 Application of Duplex Reactors on Main Propulsion Drives.. ..163

FIGURE 24 Variation of System $V _ { t h d }$ with Number of Generators on Line (Figure 23) . .163

FIGURE 25 Duplex Reactors on Passenger Ships with $2 \times 2 0$ MW Cycloconverters.. .164

FIGURE 26 Application of Duplex Reactors on Shaft Generators . .165

FIGURE 27 Application of Duplex Reactors Vessel with Multiple AC SCR Based Drives.. ..166

FIGURE 28 Absolute Impedance Characteristics for Tuned 7th Harmonic Series Filter .. ...167

FIGURE 29 Common Configuration of Passive Filters .. ....168

FIGURE 30 Simplified Connection of Multi-limbed Passive Filter . .168

FIGURE 31 Impedance Characteristics of Multi-limbed Passive Filter .. ...169

FIGURE 32 Simplified “Drive Applied” or “Trap” Filter for Variable Speed Drives . .170

FIGURE 33 12-Pulse AC PWM Drive with Double-wound Phase Shift Transformer .. .172

FIGURE 34 Double-wound 12-Pulse Phase Shift Transformer Unbalance Between Secondary Voltages . ...173

FIGURE 35 12-Pulse AC PWM Drive with Polygonal Autotransformer . .174

FIGURE 36 Variation on Harmonic Currents vs. AC Reactance for a 12-Pulse AC PWM Drive with Polygonal Autotransformer . .175

FIGURE 37 Typical 18-Pulse Drive System. ..176

FIGURE 38 Effect of $2 \%$ Unbalance on 18-Pulse Drive.......... ...176

FIGURE 39 Effect of Background Voltage Distortion on an 18-Pulse Drive.. .177

FIGURE 40 Quasi-24-Pulse System Using Phase Staggering Techniques... .178

FIGURE 41 Block Diagram of Shunt Connection Active Filter with Associated Current Waveforms.. ..180

FIGURE 42 Simplified Power Circuit of Active Filter ..... ..181

FIGURE 43 Typical AC PWM Drive Input Current Waveform $( L _ { L } )$ as per Figure 41 . .182

FIGURE 44 Active Filter “Compensation Current” Waveform $( L _ { f } )$ as per Figure 41.. .182

FIGURE 45 Source Current Waveform $( L _ { S } )$ as per Figure 41 .....182

FIGURE 46 Typical Active Filter Performance with 150 HP AC PWM with $3 \%$ AC Line Reactor .. .183

FIGURE 47 Theoretical Shunt Passive-Active Hybrid Filter........185

FIGURE 48 Thermal Limits of Shunt Active per Harmonic Current .. .186

FIGURE 49 Practical Example of Hybrid Shunt Passive-Active Filter . .187

FIGURE 50 Application of an IGBT “Active Front End” to an AC PWM Drive. ..188

FIGURE 51 ”Active Front End” Input Current and Voltage Waveforms. .189

FIGURE 52 Typical Harmonic Current Input Spectrum for AC PWM Drive with an “Active Front End”. Note the Harmonic Currents Above the $5 0 ^ { \mathrm { t h } }$ . .190

SECTION 11 Harmonic Limit Recommendations................. .. 191

1 General Systems . ..191

2 Dedicated Systems .. ..191

# SECTION 12 Calculation of Harmonic Voltage Distortion ................ .... 193

1 Manual Calculation of Voltage Distortion... .193   
2 Software Estimation of Harmonic Distortion ...... ...199

TABLE 1 Summary of Harmonics to $2 5 ^ { \mathrm { t h } }$ ..195

TABLE 2 Summary of Harmonics to $2 5 ^ { \mathrm { t h } }$ .198

# SECTION 13 Provision of Information on Harmonics.............. .... 201

1 Information to be requested from Vendors .... ..201   
2 Information to be included with a Harmonic Analysis ........201

# SECTION 14 Harmonic Surveys and Measurement Equipment ..........203

1 Safety Precautions during Harmonic Surveys . .203   
2 Planning the Harmonic Survey or Measurements .............204   
3 Information to be recorded from Harmonic Measurements . .205   
4 Examples of Harmonic Analyzers... .206

4.1 The Fluke 43B.. . 206   
4.2 AEMC 3945.. . 209   
4.3 Hioki 3196 . . 216

5 Measurements on Voltages above 690/750 V AC.............220

FIGURE 1 Fluke 43B Harmonic/Power Quality Analyzer..........206   
FIGURE 2 Fluke 43B Harmonics Screen Data Available (In This Case Current) [Voltage and power harmonic data are also available.] .. .207   
FIGURE 3 Fluke 43B Can Measure Sags and Swells up to 16 Days on a Per Cycle Basis . .207   
FIGURE 4 Up to 40 Transients (Voltage or Current) Can Be Captured with the Fluke 41B... .208   
FIGURE 5 True rms Voltage and Current Waveform Display(s) from Fluke 43B.. .208   
FIGURE 6 AEMC 3945 Three-phase Harmonic/Power Quality Analyzer with Real Time Color Display... .209   
FIGURE 7 AEMC 3945 Connected On-site Illustrating “Wrap-around” Rogowski-type, AmpFlex 6500 A Current Probes . ..210   
FIGURE 8 Sample Displays of Voltage and Current Waveforms.. .211   
FIGURE 9 Three-phase Voltage Waveforms .. ..211   
FIGURE 10 Transient Current Waveforms... .212   
FIGURE 11 Three-phase Voltage Harmonics .. .212   
FIGURE 12 Harmonic Direction . ..213   
FIGURE 13 Harmonic Sequences.. ..213   
FIGURE 14 Phasor Diagram . ..214   
FIGURE 15 AEMC 3945 Configuration via Computer... .214

FIGURE 16 Real Time Current Waveforms via Computer..........215   
FIGURE 17 Real Time Computer Display of Harmonic Currents .. ..215   
FIGURE 18 Unbalance in Real Time via Computer ...... ...216   
FIGURE 19 Hioki 3196 Power Analyzer with Voltage and Current Probes.. ..217   
FIGURE 20 AC VFD Three-phase Voltage and Current Measurements from Hioki 3196.. ..217   
FIGURE 21 Harmonic FFT Measurements from Hioki 3196 with $5 ^ { \mathrm { t h } }$ Harmonic Selected .. .218   
FIGURE 22 Power System $V _ { t h d }$ Trend Recording via Hioki 3196 as a Number of AC VFDs Are Switched On .... ...218   
FIGURE 23 $V _ { t h d }$ of all Three Phases Recorded by Hioki 3196 when Active Filter Switched in on Oil Production Platform ... ..219   
FIGURE 24 Summary of Data Sampled from Hioki 3196 ...........219   
FIGURE 25 Recorded Harmonic Currents by Hioki 3196 on 12-Pulse AC Drive . ..220

APPENDIX 1 Recommended Reading...... ... 221

# S E C T I O N

# 1 Introduction

# 1 Background

Over recent years, there has been a significant increase in the installation and use of power electronic equipment onboard ships and on offshore installations. The operation of this equipment has in many cases significantly degraded the ship or offshore installation electrical power quality to such an extent that measures have to be implemented in order to minimize the resultant adverse effects on the electrical plant and equipment.

The quality and security of voltage supplies are important to the safety of any vessel and its crew and to the protection of the marine environment. Any failure or malfunction of equipment such as propulsion or navigation systems can result in an accident at sea or close inshore with serious consequences. Many power quality issues are transient, for example, the starting of a large electric thruster motor resulting in a momentary dip before the generator regulators correct the situation and reinstate the correct level of voltage and frequency.

However, as the title suggests, the specific power quality issue to be addressed in these Guidance Notes is that of the harmonic distortion of voltage supplies caused by the operation of electronic devices which draw nonlinear (i.e., non-sinusoidal in nature) currents from the voltage supplies. These same items of “nonlinear” equipment can also be affected by harmonic currents and the subsequent voltage distortion they produce, as can the majority of “linear” equipment (particularly generators, AC motors and transformers). As harmonic distortion is “steady state” and continuous, the issue of electrical power quality associated with harmonics is an important concern to the marine safety aspects and in addition, to any adverse effects harmonic distortion has on the performance and reliability of the majority of marine and offshore systems and equipment.

Examples of the serious impact of harmonics and associated power quality effects on marine and offshore supply voltage waveforms, in these instances, due to electrical variable speed drives (the main producer of harmonic currents on marine and offshore installations) are illustrated in Section 1, Figures 1, 2, 3 and 4.

![](images/c47448956b897372196e104d478bf40889781c8ae8b7fb49465636f2e1b9c942.jpg)  
FIGURE 1 Input Waveforms (440 V) to 6-Pulse DC SCR Drive

![](images/965ec7eab594121d43dc9df6d94a60774b62d30501370550bb114f090d8a5ab8.jpg)  
FIGURE 2 Line-to-line Voltage (440 V) at Input to a 6-Pulse DC SCR Drive

![](images/c60e94e8e7e8bf89c43f8a1f013c561454740f15fbb70b054b508d69b87ff0b2.jpg)  
FIGURE 3   
415 V Line-to-line Volts on Ship with Four 1100 kW/1500 HP AC SCR Converter-fed Thruster Motors   
FIGURE 4

![](images/9ec922e2d0c662e0ba3b7e83cc1de6121b50c0ebcd645f0af763ebb96d392ca8.jpg)  
Primary Voltage (11 kV) of Transformer Supplying a 2 MW (2680 HP) Variable Frequency Drive

The American Bureau of Shipping (ABS) is concerned with the effects of harmonic voltage distortion and the possible resultant consequences should some critical item of equipment malfunction or fail. This concern is largely a result of the increasing demand for high power nonlinear equipment, such AC and DC variable speed drives, used for main propulsion, thrusters and other duties. Therefore, ABS has imposed limitations on the magnitude of harmonic voltage distortion permitted on classed vessels.

The aim of these Guidance Notes, which solely address the harmonics issue, is to provide information as to what harmonics are and how they interact with the supply impedances, what effects they have on the different types of equipment, what items of equipment typically produce harmonic currents and how harmonic currents can be attenuated or mitigated such that any adverse effects are significantly reduced.

As indicated in the title, these Guidance Notes are designed to be practical “guidance notes”, not a reference book on harmonics. It is aimed at the “non-expert”, hence the use of a minimum of complex math. There are a number of high-quality harmonics and power quality reference books available, although very few dealing with harmonics and power quality issues specifically from the marine viewpoint. The Appendix recommends some of these books should the reader wish further information.

These Guidance Notes will indicate that there are a number of sources of harmonic currents. “Linear” equipment, such as generators, AC motors and transformers, is also known to produce harmonics, albeit in limited qualities compared to large “nonlinear loads”. However, in the context of the marine and offshore installations, it is the electric variable speed drive (a combination of an electric motor and electronic power converter) whether AC or DC based, which, due to its increased popularity in a host of applications, is the main source of harmonic currents and subsequent voltage distortion. Therefore, the electric variable speed drives and harmonic mitigation of this type of equipment will be a primary focus of these Guidance Notes.

However, single-phase electrical and electronic equipment, including fluorescent lighting, variable speed drives and computer-based equipment all produce harmonic currents and therefore will distort the voltage supplies. On large passenger vessels, 4-wire systems [three-phase and neutral (grounded or insulated)] are now being installed, resulting in potentially high levels of neutral currents due to arithmetic addition of triplen harmonics in that conductor, up to almost twice the phase current values. Therefore, lower voltage single-phase equipment down to $1 1 0 \mathrm { ~ V ~ }$ is also of significant importance in many vessels in terms of harmonics and associated effects.

Section 1, Figure 5, below, illustrates the popularity and the reliance some classes of vessel now have with regard to electrical variable speed drives (in this instance a self-propelled drilling rig).

![](images/797dd8d1d2d3319cd9f539b4b1993bcdde6716b2e9737e9faab6538fbe713985.jpg)  
FIGURE 5 Typical Power System Single Line Diagram for DPS-3 Drilling Rig

# 2 The Use of Electric Drives in Marine Applications

For the first half of the $2 0 ^ { \mathrm { t h } }$ century, the majority of vessels were steam turbine or diesel engine driven. DC generators were common and therefore, ships utilized DC motors to power a host of applications, including cargo winches, windlasses, pumps, fans and other auxiliary driven equipment. Speed control was easily achieved using resistance-based control systems for both armature voltage control (for speed variation up to base speed) and field control (above base speed). As no “voltage conversion” was taking place (e.g., AC to DC) no harmonic currents were produced by this type of equipment.

From the early 1960s, AC generators were installed in new vessels as the benefits of AC voltage supplies became common. With the introduction of AC power, however, the ease in which electric motor speed control was previously achieved was significantly diminished for all but some specialized applications. For duties where speed control was considered necessary (for example, windlass or mooring winch applications), special systems including the “Ward-Leonard” AC motor-DC generator system were developed. The Ward-Leonard set supplied a DC motor which powered the driven load. The voltage, and hence speed and torque, of the DC drive motor was controlled by the excitation of the Ward Leonard DC generator driven by a fixed-speed AC motor and the “field controller” should speeds above base speed be needed. No “voltage conversion” (AC to DC, in this case) was necessary. Therefore, harmonic distortion was not an issue that had to be considered.

Around the mid-to-late 1960s, the first generation of solid state SCR (“silicon controlled rectifier” or “thyristor”) based variable speed drive systems were introduced for the control of DC motors. The power conversion process from AC voltage to DC voltage draws “nonlinear” (non-sinusoidal) currents from the supply, resulting in harmonic voltage distortion as the harmonic currents produced interact with supply impedances. It has to be noted that the theory of harmonics with respect to electrical networks has been known since the start of the $2 0 ^ { \mathrm { t h } }$ Century, but until relatively recently, there was no effective or accurate monitoring equipment available to measure it.

Common applications for DC SCR drives on AC vessels from the mid-to-late 1960s included windlasses, mooring winches and some cargo winches, while the majority of engine room auxiliaries; pumps, fans, compressors and other equipment were driven by fixed-speed AC motors with bypass systems, valve throttling or damper control used to vary flow. It was common on these vessels fitted with DC SCR cargo handling systems to experience light “flicker”, caused by a combination of “line notching”, “interharmonics” and harmonic currents interacting with the generator(s), cabling and other supply impedances when cargo was being worked.

From the mid 1960s, DC SCR drives were used extensively on drilling rigs for main propulsion, mud pumps, draw-works, anchor windlasses and other duties. As can be seen in Section 1, Figure 5, DC SCR drives have now largely been replaced by AC drives.

In the late 1970s and early 1980s, AC variable frequency drives (“VFDs” or “inverters”) were developed in various forms, “quasi square wave drives” and “current source drives”, being two common examples. However, it was only in the late 1980s that AC drive technology (most notably in the form of “pulse width modulation” (“PWM”) drives) started to appear on ships in any numbers, although they were installed on offshore oil production installations from the mid 1980s for a few duties, especially including down-hole pumps, where the initial benefit was as “soft-starters” for the pumps. Shortly thereafter, the speed control feature was utilized as oil reservoirs became depleted and flow rate had to be controlled.

Offshore, on applications where robust, variable speed control was needed, DC SCR drives were most common. DC SCR drives went largely unchallenged until the early-to-mid 1990s. However, from that time on, as the physical size, performance, reduction in maintenance of AC motors compared to DC motors, cost, and reliability of AC drives continued to improve, their popularity increased making AC drives comparable to DC SCR drives. As can be seen from Section 1, Figure 5, AC PWM drives have completely replaced DC drives in the majority of drilling rig applications.

With the exception of large main propulsion drives (above 5-8 MW/6700-10700 HP), where “load commutated inverters” and “cyclo-converters” are still more common, AC PWM drives are popular (for example, for small main propulsion systems, thrusters, cargo pumps and other LV and HV applications). The increased installed drive capacity on vessels, whether based on AC or DC converters, has led to a significant increase in harmonic voltage distortion levels on a large number of vessels. Although in many cases harmonic mitigation has been used, these may not be sufficient to attain the levels of attenuation necessary to guarantee compliance with the harmonic limits imposed by classification societies. In a relatively large number of cases, the harmonic voltage distortion has reached surprising levels, well in excess of the classification societies’ limitations.

AC PWM drives with “active front ends” (sinusoidal input rectifiers), which offer relatively low harmonic current levels compared to present “standard” AC converter drives, have been available for a number of years. There are a number of significant commercial and technological issues still to be completely resolved, including cost, physical size, increased levels of electro-magnetic interference (EMI), input bridge carrier frequency suppression which needs large passive reactor-capacitor-reactor (L-C-L) filters, the production of high order harmonics (usually above the $4 0 ^ { \mathrm { t h } }$ or $5 0 ^ { \mathrm { t h } } ,$ ) and compatibility with generator-derived supplies regarding suitably low values of source impedance. However, despite these issues, their use in marine applications is increasing. There are a number of harmonic mitigation solutions which, when used with “standard” 6-pulse AC drives, offer similar levels of performance at less cost, reduced complexity, higher efficiency, less EMI and higher reliability.

DC SCR drives are still operating in older vessels and in new, specialist survey vessels, for example, where low noise and vibration levels are important. The power ratings of DC drives systems, however, are largely limited to a few MWs due to restrictions on the brush-gear and mass of the DC motor armature.

It should be noted that the present power restrictions with AC PWM converters is due to lack of suitable power semiconductors in terms of current and voltage ratings. It is estimated that ratings up to $5 0 ~ \mathrm { M W }$ for AC PWM drives may be available within a few years based on new types of power devices.

# 3 Main Propulsion Drives

Electric drives for propulsion have been used onboard ship for the majority of the $2 0 ^ { \mathrm { t h } }$ Century, albeit in very small numbers. Indeed, small inland vessels with DC electric motors for propulsion operated in the United Kingdom and Russia as early as 1893.

Large seagoing vessels first appeared with full electric propulsion in the 1920s with the introduction of the Panama Pacific Line ships, Virginia and California, each powered by two synchronous motors each rated at $6 7 5 0 \ \mathrm { H P }$ . In Europe around the same time, four synchronous motors with a total of 116MW (155,500HP) propelled the French passenger liner, Normandie. During the Second World War, DC propulsion motors were used extensively on US-built T2 tankers. Cruise liners in the 1960s, including Canberra, were fitted with 30 MW (40,000 HP) synchronous propulsion motors. In the mid 1980s, Queen Elizabeth II was converted from steam turbine to electric propulsion by installing two 40 MW synchronous motors and converters. A large proportion of modern cruise liners also utilize full electric propulsion, either via conventional shaft arrangements or via podded propulsors.

The application of electric propulsion has increased in the last five years, largely due to the introduction of new classes of vessels and the expansion of new builds, including Ropax ferries, offshore supply vessels, survey ships, “floating production storage and offloading” vessels (FPSOs), shuttle tankers, cable-ships and cruise liners, where electric propulsion provides significant benefits, including increased cargo carrying capabilities, lower running costs, less maintenance, reduced manpower, greater redundancy, lower emissions and improved maneuverability (with podded or azimuth type propulsors – see Section 1, Figure 6.).

As of the year 2000, over $2 \%$ of vessels over 500 gross tons were fitted with electrically-driven propulsion. The percentage of new vessels being built with electric propulsion continues to increase annually.

Section 1, Figure 7, shows a typical application of an electrically-propelled vessel, in this instance a dynamically-positioned shuttle tanker using AC drives; 12 MW cycloconverters for main propulsion and PWM drives for thrusters, fixed and podded, in addition to main cargo pumps.

The decision as to whether to install electric propulsion in a vessel is complex and is usually dependent on the type of vessel and the operating profile envisaged. Naval warship design, however, is currently also being significantly changed with the adoption of fully-integrated electric propulsion systems, which will accrue significant strategic additional benefits from new generations of electric weapon platforms that will utilize the increased onboard power generating capacity necessary for the main electric propulsion systems.

![](images/03dfbcbf2ffde6a91772393acb509d2c6351b97b98487932c79eb2c6446b87e0.jpg)  
FIGURE 6 Electrically-driven Podded Propulsor

![](images/830464ae84ae0a50dedae3adfb77837bfc36fca5931a747555e6b71dffb7f74c.jpg)  
FIGURE 7 Dynamically-positioned Shuttle Tanker Equipped with AC Electric Variable Speed Main Propulsion and Thrusters

# 4 The Future?

The use of electric variable speed drives, particularly AC converters, for main propulsion and a host of other applications within the marine and offshore sectors will continue to increase.

The continual advances in power semiconductors, electromagnetics, control systems, software engineering and other related technologies will lead to the development of higher performance, more compact, more cost effective and more efficient types of electric drives and motors.

The majority of the emerging AC drive converter types, including “matrix converters”, “resonant converters” and “pulse frequency modulated” (PFM) converters will all have low harmonic profiles compared to the majority of generic drive technologies available at present.

However, it may be some years before these emerging AC drive converter developments permeate through from mainly military (naval) development programs and are available to commercial organizations. Their financial viability for any applications other than specialized naval warship duties may also have to be carefully assessed. In the meantime, the issue of harmonic distortion and the effects on plant and equipment has to be addressed to ensure the safety of the ship or offshore installation, the protection of the crew, and where appropriate, the passengers and the marine environment.

This Page Intentionally Left Blank

# 2 The Production of Harmonics

# 1 Production of Harmonics

In a power system, any item of equipment which draws current from the supply which is proportional to the applied voltage is termed a “linear” load. Examples of linear loads include resistance heaters and incandescent lamps. The current and voltage waveforms associated with linear loads are shown in Section 2, Figure 1.

![](images/ce426fc4849b0680ac5337df8c6dc1ee5c0b8713056d1c08872e1382eb8de17f.jpg)  
FIGURE 1 Voltage and Current Waveforms for Linear Load

The term “nonlinear” is used to describe loads which draw current from the supply that is dissimilar in shape to the applied voltage. Examples include discharge lighting, computers and variable speed drives.

In order to explain pictorially how nonlinear current distorts the voltage supply waveform it is necessary to refer Section 2, Figures 2 and 3.

Section 2, Figure 2a illustrates a simple single-phase full wave rectifier supplying a load containing both inductance and resistance. The impedance of the AC supply is represented by the inductance $L _ { a c }$ . Section 2, Figure 2b illustrates the DC load current $( I _ { d c } )$ and AC input current $( I _ { a c } )$ , respectively.

![](images/19a4cc1964b1cf4df6218d80563a566c6adff8e80463fee00c3593798e9aedcb.jpg)  
FIGURE 2a Single Phase Full Wave Rectifier   
FIGURE 2b Load and AC Supply Currents

![](images/9452cbce5a8c1007e24e79687b3b152833412a423d111e87774fb239484e0235.jpg)

Section 2, Figure 3a shows a simple single line diagram comprising source voltage $( u )$ and source impedance $( L _ { N } )$ . The harmonic current $( i _ { N } )$ passing through the source impedance produces a voltage drop $( U _ { L } )$ according the following formula:

$$
U _ {L} = L _ {N} \cdot \frac {d i _ {N}}{d t} \tag {2.1}
$$

Section 2, Figure 3b illustrates the nonlinear current $( i _ { N } )$ and voltage drop $( U _ { L } )$ waveforms.

![](images/59013d5f69423b3f1cb892cb44698305b07f29390560b543f73f04c788bd0053.jpg)  
FIGURE 3a Simple Single Line Diagram

![](images/b7bffc0677b65fd8e037b6205bf639130a3385ccc49ab378738197b05b990f11.jpg)  
FIGURE 3b Load Current and Volt Drop Waveforms

The voltage drop across the source impedance $( U _ { L } )$ is subtracted from the induced voltage (u), resulting in the distortion of the supply voltage waveform, as illustrated in Section 2, Figure 4.

Note: The example below has been exaggerated in order to illustrate the principle graphically of how nonlinear current distorts the supply voltage.

![](images/2fdd98da54d2b87a213418c829f7d42dc38091ab8d829deeaccc2c48a2b8d83b.jpg)  
FIGURE 4   
How Voltage Distortion is Produced (Simplified)

The majority of nonlinear loads is equipment that utilizes power semiconductor devices for power conversion (e.g., rectifiers). They include, for example, computer switched mode power systems (SMPS) for converting AC to DC. Section 2, Figure 5 illustrates a typical current waveform of a computer switched mode power supplier unit.

![](images/63420cde60b8cd8723e491a28442ae2f867117b0bc75e04468391f9b000fe003.jpg)  
FIGURE 5 Typical Computer Nonlinear Load

In order to appreciate why the current waveform shown in Section 2, Figure 5 is of a “pulsed” nature, it is beneficial to consider the design of switched mode power supplies, an example of which is illustrated in Section 2, Figure 6.

![](images/50daee09ce01ca7c28e5e47daa73f4533c5bebd77f800474cb8fa763842c15dd.jpg)  
FIGURE 6 Single-phase Switched Mode Power Supply

This type of power supply uses capacitors to smooth the rectified DC voltage and current prior to it being supplied to other internal subsystems and components. The semiconductor diode rectifiers are unidirectional devices (i.e., they conduct in one direction only). The additional function of the capacitor is to store energy which is drawn by the load as necessary. When the input voltage $( V _ { i } )$ is higher in value than the capacitor voltage $( V _ { c } )$ , the appropriate diode will conduct and non-sinusoidal, “pulsed” current will be drawn from the supply. This non-sinusoidal current contains “harmonic currents” in addition to the sinusoidal fundamental $5 0 \ : \mathrm { H z }$ or $6 0 ~ \mathrm { H z }$ ) current, as illustrated in Section 2, Figure 7.

Note: As can be seen below, the harmonic spectrum contains only “odd” harmonics (1, 3, 5, 7…). This is due to the “full wave rectification” used in the SMPS. If the SMPS were to use “half wave” rectification “even” order (2, 4, 6, 8…) harmonics would also be present.

![](images/2618fa1221ad3e78575b550fcc67510e3718ab9fd03981a64c1b14bf6d525b34.jpg)  
FIGURE 7 Harmonic Spectrum of Currents Drawn by Computer Switched Mode Power Supply

Harmonic voltages and currents are integer multiples of the fundamental frequency. On $6 0 ~ \mathrm { H z }$ supplies, for instance, the $5 ^ { \mathrm { t h } }$ harmonic is $3 0 0 \mathrm { H z }$ ; the $7 ^ { \mathrm { t h } }$ harmonic is $4 2 0 \ \mathrm { H z } ,$ , and so forth. When all harmonic voltages and currents are added to the fundamental, a waveform known as a “complex wave” is formed. An example of complex wave consisting of the fundamental $1 ^ { \mathrm { s t } }$ harmonic) and $3 ^ { \mathrm { r d } }$ harmonic is illustrated in Section 2, Figure 8.

![](images/eea70a43d20b77744eac13de31c402852668ab7b1a658fdf2ca977377fb05706.jpg)  
FIGURE 8 Construction of Complex Wave

Section 2, Figure 8 is an example of a symmetrical waveform in which the positive portion of the wave is identical to the negative portion. It should be noted that symmetrical waveforms only contain odd harmonics, whereas asymmetrical waveforms (where both positive and negative portions are different) contain even and odd harmonics and possibly DC components. An example of an asymmetrical waveform would be that produced by a half wave rectifier.

# 2 Characteristic Harmonic Currents

Power conversion using full wave rectifiers generates idealized characteristic harmonic currents given by the formula:

$$
h = n p \pm 1 \tag {2.2}
$$

where

h = order of harmonics

n an integer 1, 2, 3…

p = number of current pulses per cycle

It should be noted that in the “ideal” harmonic theory, the following hypotheses are assumed for all rectifiers:

• The impedance of the AC supply network is zero.   
• The DC component of the rectifier configuration is uniform.   
• An AC line or commutating reactor is not used in front of the rectifier.   
• The AC supply network is symmetrical (i.e., balanced).   
• The AC supply is sinusoidal, free from harmonics.   
• There are no “overlap” or delay angles for the devices.

Note: Any divergence from any of the above hypotheses will introduce “non-characteristic” harmonics, including possibly DC, into the harmonic series. In practical terms, it has to be noted that supply networks or connected equipment are never “idealized” (i.e., based on the above hypotheses) and, therefore, any actual harmonic currents measured will not be exactly as calculated using the above simplified formula.

In addition, in idealized harmonic theory, the magnitude of the harmonic current is stated as the reciprocal of the harmonic number:

$$
I = \frac {1}{h} \dots \tag {2.3}
$$

Therefore, in theory, the $5 ^ { \mathrm { t h } }$ harmonic current and $7 ^ { \mathrm { t h } }$ harmonic current, for example, should represent $20 \%$ and $14 \%$ of the total rms current, respectively. However, again, this is never transferred into practical reality as the magnitudes of the various harmonic currents are determined by the per-phase inductance of the AC supply connected, the rectifier and the impedance of the rectifier as “seen” by the AC supply.

In rectifiers without added inductance (e.g., AC line reactors) it is not uncommon to measure $5 ^ { \mathrm { t h } }$ harmonic current up to ${ \sim } 8 0 \%$ on single-phase rectifiers and $65 \%$ on three-phase rectifiers.

Section 2, Figure 9 illustrates a typical single-phase computer switched mode power supply with full wave bridge rectifier.

![](images/979271b855b7fd21b8315faf6951453c0cece15064a6b2c45387ce55fc259ce9.jpg)  
FIGURE 9   
Computer Power Supply with Single-phase Full Wave Bridge Rectifier

For the single full wave diode bridge rectifier above, the characteristic harmonic currents based on two rectified current pulses per cycle (i.e., one per half cycle per phase), as shown in Section 2, Figure 10, converted into DC load will be:

$$
h = n p \pm 1
$$

$$
h = n \cdot 2 \pm 1
$$

$$
h = 3, 5, 7, 9, 1 1, 1 3, 1 5 \dots
$$

where

![](images/8112b04bcb3839bb5d09f2f38c8ef2a3b260b30028f9dca0d55a46521092eebd.jpg)  
FIGURE 10   
Computer Switch Mode Power Supply Input Current Waveform

The harmonic series calculated for a single-phase full wave rectifier is shown in Section 2, Figure 11.

FIGURE 11   
Typical Waveform from Computer Switched Power Supply   
![](images/bd8fb963536d8c475501942b74fd859ec7aa215cc4ce0309406b1699c017118a.jpg)  
Note: It should be noted that in four-wire distribution systems (three-phase and neutral), the currents in the three phases return via the neutral conductor, the 120-degree phase shift between respective phase currents causes the currents to cancel out in the neutral, under balanced loading conditions. However, when nonlinear loads are present, any “triplen” $( 3 ^ { \mathrm { r d } } , 9 ^ { \mathrm { t h } } . . . )$ harmonics in the phase currents do not cancel out but add cumulatively in the neutral conductor, which can carry up to $1 7 3 \%$ of phase current at a frequency of predominately $1 8 0 ~ \mathrm { H z }$ $3 ^ { \mathrm { r d } }$ harmonic). This issue will be discussed in more detail in Section 4, “Sources of Harmonics”.

Section 2, Figure 12 shows a typical 6-pulse PWM AC drive, where the rectifier bridge supplies the DC link section of the drive.

![](images/2afb1e778dca83a377bbfa85212035f30500d3f903f346bbc5867afb11d70c8d.jpg)  
FIGURE 12 Typical 6-Pulse PWM AC Drive

For a three-phase full wave diode rectifier bridge [also known as a “6-pulse bridge”, as it rectifies six current pulses (one per half cycle per phase) into the load side of the bridge], the characteristic harmonic currents will therefore be:

$$
h = n p \pm 1
$$

$$
h = n \cdot 6 \pm 1
$$

$$
h = 5, 7, 1 1, 1 3, 1 7, 1 9 \dots
$$

where

$$
h \quad = \quad \text {h a r m o n i c n u m b e r}
$$

$$
n \quad = \quad \text {i n t e g e r}, 1, 2, 3 \dots
$$

$$
p \quad = \quad \text {p u l s e s}, (6)
$$

Similarly, the characteristic harmonic currents for a 12-pulse rectifier will be:

$$
h = n \cdot 1 2 \pm 1
$$

$$
h = 1 1, 1 3, 2 3, 2 4, 3 5, 3 7 \dots
$$

Section 2, Figures 13 and 14, respectively, show the input phase current waveforms and harmonic current spectrum measured on a typical 6-pulse AC PWM drive.

![](images/1ae79c82c55164ed42f97b9e991cbc36f7eef75de3cc5fb202990b6bf7c632a6.jpg)  
FIGURE 13   
6-Pulse AC PWM Drive Input Current Waveforms for One Phase   
FIGURE 14

![](images/1517474978859f876267bea7617688ce159707256fe870dd0a8b7991fdac09e8.jpg)  
Typical Harmonic Spectrum for 6-Pulse AC PWM Drive

# 3 Effect of Harmonic Currents on Impedance(s)

Section 2, Figure 15 shows in a simplified form that when a nonlinear load draws distorted (non-sinusoidal) current from the supply, that distorted current passes through all of the impedance between the load and power source. The associated harmonic currents passing through the system impedance cause voltage drops for each harmonic frequency based on Ohm’s Law ${ \cal V } _ { h } = I _ { h } \times { \cal Z } _ { h } )$ . The vector sum of all the individual voltage drops results in total voltage distortion, the magnitude of which depends on the system impedance and the levels of harmonic currents at each harmonic frequency.

![](images/8eb16829f09f90dbc04861384b41dee4b195ea14520372a64d592e4d58e196ff.jpg)  
FIGURE 15 Distorted Currents Induce Voltage Distortion

Section 2, Figure 16 shows in detail the effect individual harmonic currents have on the impedances within the power system and the associated voltages drops for each. Note that the “total harmonic voltage distortion”, $V _ { t h d }$ (based on the vector sum of all individual harmonics), is reduced as more impedance is introduced between the nonlinear load and the source.

![](images/89b721477dad04d1fc7ce1d94a1345288c50fb50ea88b765aa483c8f121047dd.jpg)  
FIGURE 16 How Individual Harmonic Voltage Drops Develop Across System Impedances

$$
V = I _ {h} \times Z _ {h} (\mathrm {O h m ' s L a w})
$$

At the load: Vh = Ih × (ZCh + ZTh + ZSh)

At the trans.: Vh = Ih × (ZTh + ZSh)

At the source: $V _ { h } = I _ { h } \times ( Z _ { S h } )$

where

$$
Z = \text {i m p e d a n c e} (e. g., 2 5 0 H z)
$$

$$
V _ {h} \quad = \quad \text {h a r m o n i c v o l t a g e a t h - t h h a r m o n i c (e . g . , 5 ^ {\mathrm {t h}})}
$$

$$
I _ {h} \quad = \quad \text {h a r m o n i c c u r r e n t a t h - t h h a r m o n i c (e . g . , 5 ^ {\text {t h}})}
$$

$$
V _ {t h d} = \text {t o t a l h a r m o n i c v o l t a g e d i s t o r t i o n}
$$

# 4 Calculation of Voltage Distortion

Any periodic (repetitive) complex waveform is composed of a sinusoidal component at the fundamental frequency and a number of harmonic components which are integral multipliers of the fundamental frequency. The instantaneous value of voltage for non-sinusoidal waveform or complex wave can be expressed as:

$$
v = V _ {0} + V _ {1} \sin (\omega t + \phi_ {1}) + V _ {2} \sin (2 \omega t + \phi_ {2}) + V _ {3} \sin (3 \omega t + \phi_ {3}) + \dots V _ {n} \sin (n \omega t + \phi_ {n}) \dots \tag {2.4}
$$

where

$$
v = \text {i n s t a n t a n e o u s v a l u e a t a n y t i m e} t
$$

$$
V _ {0} = \text {d i r e c t (o r m e a n) v a l u e (D C c o m p o n e n t)}
$$

$$
V _ {1} = \text {r m s v a l u e o f t h e f u n d a m e n t a l c o m p o n e n t}
$$

$$
V _ {2} = \text {r m s v a l u e o f t h e s e c o n d h a r m o n i c c o m p o n e n t}
$$

$$
V _ {3} = \text {r m s v a l u e o f t h e t h i r d h a r m o n i c c o m p o n e n t}
$$

$$
V _ {n} \quad = \quad \text {r m s v a l u e o f t h e n t h h a r m o n i c c o m p o n e n t}
$$

$$
\phi = \text {r e l a t i v e a n g u l a r f r e q u e n c y}
$$

$$
\omega = 2 \pi f
$$

f = frequency of fundamental component (1/f defining the time over which the complex wave repeats itself)

It is usually more convenient, however, to interpret a complex wave by means of “Fourier Series” and associated analysis methods. Joseph Fourier, a $1 9 ^ { \mathrm { t h } }$ century French physicist introduced a theory that any periodic function in a interval of time could be expressed by the sum of the fundamental and a series of higher order harmonic frequencies which are integral multipliers of the fundamental component.

Ignoring any DC components in the above formula, where $V _ { 1 }$ and $I _ { 1 }$ represent the fundamental voltage and current, respectively, the instantaneous rms voltage, $V _ { h } ,$ can be represented as a Fourier Series:

$$
v (t) = \sum_ {h = 1} ^ {\infty} v _ {h} (t) = \sum_ {h = 1} ^ {\infty} \sqrt {2} V _ {h} \sin \left(h \omega_ {0} t + \phi_ {h}\right) \dots \tag {2.5}
$$

The rms value of voltage can be expressed as:

$$
V _ {r m s} = \sqrt {\frac {1}{T} \int_ {0} ^ {T} v ^ {2} (t) d t} = \sqrt {\sum_ {h = 1} ^ {\infty} V _ {h} ^ {2}} = \sqrt {V _ {1} ^ {2} + V _ {2} ^ {2} + V _ {3} ^ {2} \dots . + V _ {n} ^ {2}} \tag {2.6}
$$

$$
I _ {r m s} = \sqrt {\frac {1}{T} \int_ {0} ^ {T} i ^ {2} (t) d t} = \sqrt {\sum_ {h = 1} ^ {\infty} I _ {h} ^ {2}} = \sqrt {I _ {1} ^ {2} + I _ {2} ^ {2} + I _ {3} ^ {2} \dots . . . + I _ {n} ^ {2}} \tag {2.7}
$$

The rms voltage or current “total harmonic distortion”, $V _ { t h d }$ and $I _ { t h d } ,$ respectively can be expressed as:

$$
V _ {t h d} = \frac {\sqrt {\sum_ {h = 2} ^ {\infty} V _ {h} ^ {2}}}{V _ {1}} \times 100 \% = \frac \sqrt {V _ {2} ^ {2} + V _ {3} ^ {2} + V _ {4} ^ {2} . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \dots}{{V _ {1}}} \times 100 \% \tag{2.8}
$$

$$
I _ {t h d} = \frac {\sqrt {\sum_ {h = 2} ^ {\infty} I _ {h} ^ {2}}}{I _ {1}} \times 100 \% = \frac \sqrt {I _ {2} ^ {2} + I _ {3} ^ {2} + I _ {4} ^ {2} . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . \dots}{{I _ {1}}} \times 100 \% \tag{2.9}
$$

Other simple but practical harmonic formulae include:

Total rms current: (2.10)

or $\begin{array}{c} \begin{array} { l } { { I _ { r m s } = \sqrt { I _ { f u n d } ^ { 2 } + I _ { h a r m } ^ { 2 } } \enspace { \underbrace { \phantom { ( } } } } \\ { { I _ { r m s } = I _ { f u n d } \sqrt { 1 + ( \frac { I _ { t h d } } { 1 0 0 } ) ^ { 2 } } \enspace { \underbrace { \phantom { ( } } } } } \end{array}  }  \end{array}$ (2.11)

Fundamental current:  fundI = $I _ { f u n d } = \frac { I _ { r m s } } { \sqrt { 1 + I _ { t h d } ^ { 2 } } }$ rmsI ... (2.12)

Total fundamental current distortion: $I _ { t h d ( f u n d ) } = \sqrt { \left( \frac { I _ { r m s } } { I _ { f u n d } } \right) ^ { 2 } - 1 } ~ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .$ rms I 1 (2.13)

Total Demand Distortion (TDD) = $\frac { \sqrt { \sum _ { h = 2 } ^ { \infty } { I _ { h } ^ { 2 } } } } { I _ { l o a d } } = I _ { T D D } = \sqrt { \frac { I _ { 2 } ^ { 2 } + I _ { 3 } ^ { 2 } + I _ { 4 } ^ { 2 } . . . . . + I _ { n } ^ { 2 } } { I _ { l o a d } } } . . . . . . . .$ =  TDD I = (2.14) loadI

where

Iload = maximum demand load current (fundamental) at the PCC

$T D D =$ ‘total demand distortion’ of current (expressed as measured total harmonic current distortion, per unit of load current. For example, a $30 \%$ total current distortion measured against a $50 \%$ load would result in a TDD of $1 5 \%$ ).

Note: In the above Equations 2.10 to 2.13, the voltage (V) can be substituted for the current (I).

# 5 Harmonic Sequence Components

Each harmonic has an order (number), a frequency which is an integer multiple of the fundamental frequency and a “sequence”. The sequence refers in vector rotation with respect to the fundamental. Section 2, Table 1 details the harmonic sequence components for an idealized 6-pulse rectifier.

TABLE 1 Harmonic Sequence Components for 6-Pulse Rectifier   

<table><tr><td>Harmonic</td><td>1</td><td>5</td><td>7</td><td>11</td><td>13</td><td>17</td><td>19</td><td>23</td><td>25....</td></tr><tr><td>Sequence</td><td>+</td><td>-</td><td>+</td><td>-</td><td>+</td><td>-</td><td>+</td><td>-</td><td>+</td></tr><tr><td>Rotation</td><td>F</td><td>B</td><td>F</td><td>B</td><td>F</td><td>B</td><td>F</td><td>B</td><td>F</td></tr></table>

Harmonics such as the $7 ^ { \mathrm { t h } }$ , $1 3 ^ { \mathrm { t h } }$ , $1 9 ^ { \mathrm { t h } }$ and $2 5 ^ { \mathrm { t h } }$ , and so on, which rotate in a forward direction (i.e., in the same sequence as fundamental) are termed “positive sequence harmonics” whereas the $5 ^ { \mathrm { t h } }$ , 11th, $1 7 ^ { \mathrm { t h } }$ , $2 3 ^ { \mathrm { r d } }$ , and so on, which rotate in the opposite direction to the fundamental are termed “negative sequence harmonics”.

Triplen harmonics $( 3 ^ { \mathrm { r d } } , 9 ^ { \mathrm { t h } } . . . )$ , as produced in single-phase full wave rectifiers, for example, do not rotate. They are in phase with each other and are therefore termed “zero sequence harmonics”.

The impact of sequence harmonics on rotating machines will be discussed in Section 3, “Effects of Harmonics”.

# 6 Line Notching

Although not strictly “harmonics”, “line notching” is a phenomenon normally associated with the SCR (thyristor) based “phase-controlled” rectifiers such as those utilized in AC and DC variable speed drives and UPS systems, also sources of harmonics. Diode bridges can also exhibit “commutation notches”, but to a lesser extent than those associated with SCR bridges. The effects of “line notching” can have a serious impact on the supply system and other equipment.

Section 2, Figure 17 depicts a simple three-phase full wave SCR bridge network supplying a DC load.

Section 2, Figure 18 illustrates theoretical notching at the terminals of the SCR input bridge and therefore assumes no additional inductance in the circuit. The voltage notches occur when the continuous line current commutates (i.e., transfers) from one phase to another. During the “commutation period”, the two phases are short-circuited (i.e., connected together) for very short durations through the converter bridge and the AC source impedance. The result is that the voltage, as illustrated, reduces to almost zero as the current increases, limited only by the circuit impedance.

![](images/e2dda00e2e6ab1044b6958d6938d71213af8f3de1513bb85d212531ddc13f6ce.jpg)  
FIGURE 17 Simple Three-phase SCR Bridge for Phase Control

![](images/2bd23fa9b6bc69ffd9965b10cbfc6c28fcd119e99d53c5d24466e3321049aa94.jpg)  
FIGURE 18 Exaggerated Example of “Line Notching”

In practical terms, the notches can be present anywhere in the respective half cycles, as the phase angle of SCRs varies according to the needed output voltage (or current for current source AC drives). The disturbances associated with line notching tend to progressively reduce nearer to a “stiff” source impedance (i.e., an impedance of relatively low value with relatively high short circuit capacity) due to the additional impedances downstream in the circuit, including that associated with cabling.

With reference to Section 2, Figure 19, the area of the notch (depth and width) is dependent on the volt-milliseconds absorbed in the circuits in the line from the source generator or transformer to the SCR bridge input terminals. It is common practice to add “commutation reactors” or isolation transformers in the AC line of the SCR bridge to minimize the notch, but regardless of how much inductance is added at the bridge terminals, the notch area tends to remain constant as the addition of AC line inductance will reduce the notch depth but will increase the notch width. It should be noted that the only real practical way to reduce the notch area is to provide part of the necessary commutation energy from a capacitor bank.

![](images/88feaa3c8135e7604877ef029de57979c571d0d8cf2e70b0e8553c29b58ee901.jpg)  
FIGURE 19 Voltage Notching due to SCR Bridge Commutation

In severe cases, especially where no additional AC line reactance is present, the voltage can be reduced to zero creating additional “zero crossovers” (i.e., the points where the voltage would normally change polarity). Section 1, Figures 2 and 3 illustrates the significant effects of line notching. The oscillograph in Section 1, Figure 3 refers to a vessel where up to four AC SCR input bridge drives were operating.

Although secondary to line notching, an important phenomenon associated with SCR phase control is “ringing”. “Ringing” is the term given high frequency oscillations due to the rapid switching of the SCRs, as illustrated in Section 2, Figure 20. It is the result of high frequency “resonance” occurring in the rectifier circuit due to inherent inductance and capacitance in the equipment circuitry.

![](images/d1d96c78e7e65620d596d39de8d1e5dc8502469683bd64b7a24c181f401d16f2.jpg)  
FIGURE 20 SCR Line Notching and Associated “Ringing”

It should be noted that line notching and associated ringing do not usually influence the $V _ { t h d } ,$ as the harmonics associated with them are of high frequency, usually above the highest measured (i.e., $5 0 ^ { \mathrm { t h } } ,$ ). However, line notching and ringing can have significant effects on voltage quality, as shown in Section 1, Figure 4. The effects of line notching on generators and other equipment will be discussed in Section 3.

# 7 Interharmonics

Interharmonics are defined in IEC Standard 1000-2-1 as: “Between the harmonics of the power frequency voltage and current, further frequencies can be observed which are not an integer of the fundamental. They appear as discrete frequencies or as a wide-band spectrum”.

Interharmonics can therefore be considered as the “inter-modulation” of the fundamental and harmonic components of the system with any other frequency components. These can be observed increasingly with nonlinear loads, including large AC frequency converters drives (especially under unbalanced conditions and/or levels of pre-exiting voltage distortion), cycloconverters (see Section 2, Figure 21) and static slip recovery drives.

![](images/9f21d99edd2b62cddd1056854f9de4b9f47c3ad0a5eb5f797a29edd66c49ce79.jpg)  
FIGURE 21 Cycloconverter Current Spectrum – Includes Interharmonics

Both harmonics and interharmonics can be defined in a quasi-steady state in terms of their spectral components over a range of frequencies as detailed below:

Harmonics: $f = h \cdot f _ { 1 }$ where $h$ is an integer $> 0$

DC: f = 0 Hz (f = h ⋅ f1, where h = 0)

Interharmonics: $f$ is not equal to $h \cdot f _ { 1 } .$ , where $h$ is an integer ${ } > 0$

Subharmonics: $f { > } 0$ and $f { < } f _ { 1 }$ , where $f _ { 1 }$ is the fundamental frequency

Waveforms which contain both harmonics and interharmonics of constant amplitude but differing frequencies are rarely periodic (i.e., repetitive), as Section 2, Figure 22 illustrates. The effect of interharmonics on equipment will be discussed in later Sections. See 3/5.1, 3/6, 4/3.3, 6/2.4 and 10/11.1.

![](images/af0c10c8c361e40b97efad81e55dd311c331298e39612aa8796da5ae861ba3e4.jpg)  
FIGURE 22 Waveform Containing both Harmonics and Interharmonics

Due to the modulation of steady state harmonic voltages, the supply voltage will vary in amplitude and rms value according to:

$$
\nu (t) = \sin \left(2 \pi f _ {1} t\right) + a \sin \left(2 \pi f _ {i} t\right). \tag {2.15}
$$

where

f1 = fundamental frequency

a amplitude (per unit) of the interharmonics voltage

(amplitude of the fundamental voltage $= 1 . 0$ per unit *)

$f _ { i }$ = interharmonics frequency

* The per unit system is based on the formula below. Using this method, quantities are expressed as ratios, similar to the use of percentage values.

$$
\text {p e r u n i t} = \frac {\text {a c t u a l q u a n t i t y}}{\text {b a s e q u a t i t i y}}
$$

Note: Maximum voltage change in the voltage amplitude is equal to the amplitude of the interharmonics voltage, while the change in the voltage rms value is dependent on both the amplitude and the interharmonics frequency.

The rms voltage value can be given by:

$$
V = \sqrt {\frac {1}{T} \int_ {0} ^ {T} v (t) ^ {2} d t}. \tag {2.16}
$$

where the period of integration $T = 1 / f _ { 1 }$

The maximum percentage rms voltage deviation over several periods of the fundamental due to interharmonics can be calculated by combining Equations 2.15 and 2.16.

In equipment which utilize capacitors on the DC side (for example, AC PWM drives), current is only drawn from the supply when the AC voltage is greater than the DC side capacitor voltage, and as such, it is the AC peak voltage which normally recharges the capacitor(s). The resultant integer harmonics in the voltage supply do not effect the AC peak voltage as these integer harmonics are synchronized with the fundamental frequency. However, interharmonics are not synchronized with the fundamental and therefore affect the peak amplitude of the AC supply voltage (see Section 2, Figure 23) causing deviations of peak voltage which can adversely effect the connected equipment, both those utilizing capacitors and also several types of lighting.

![](images/271f0f0a28b069ea229db91622f2b943c5e351a869bf13ae4c7c6119c2ba025c.jpg)  
FIGURE 23 Peak Voltage Deviations due to Interharmonics Voltage

The distorted voltage waveform depicted in Section 2, Figure 23 can be calculated as:

$$
V (t) = V _ {1} \sin \left(2 \pi f _ {1} t\right) + V _ {n} \sin \left(2 \pi f _ {n} t\right). \tag {2.17}
$$

where

V1 = amplitude of fundamental voltage

t time

f1 = fundamental voltage

Vn = amplitude of interharmonics n

n fractional real number of interharmonics order

The variation of the supply voltage amplitude is calculated from the difference between the maximum and minimum peak values $V _ { \mathrm { m a x } }$ and $V _ { \mathrm { m i n } } )$ ) recorded over several cycles of the function $V ( t )$ . Therefore:

$$
\Delta V = V _ {\max } - V _ {\min } \dots \tag {2.18}
$$

Note: The measurement of interharmonics, compared to that of integer harmonics, poses considerable problems for traditional harmonic measuring equipment, which uses phase-locked loops and Fast Fourier Transform (FFT) techniques. This is due to the interharmonic frequency components being non-related to the fundamental frequency and non-periodic. However, for the measurement and identification of interharmonics it may not be necessary to perform an analysis which depends on the supply fundamental frequency. Methods of analysis used in the communication industries have been adapted for use in the measurement and analysis of interharmonics components.

# 8 Subharmonics

“Subharmonics” is an unofficial but common definition given to interharmonics whose frequency is less than that of the fundamental (i.e., $f > 0 ~ \mathrm { H z }$ and $f < f _ { 1 } )$ . The more technically correct term, “sub-synchronous frequency component”, is also used to define subharmonics.

Therefore, it should be noted that the calculations provided above associated with interharmonics are valid for “subharmonics” also.

This Page Intentionally Left Blank

# S E C T I O N

# 3 Effects of Harmonics

# 1 Generators

In comparison to shore-based utility power supplies, the effects of harmonic voltages and harmonic currents are significantly more pronounced on generators due to their source impedance being typically three to four times that of utility transformers.

The major impact of voltage and current harmonics is the increase in machine heating caused by increased iron losses, and copper losses, both frequency dependent. [On shore installations, it is relatively common practice to “derate” (reduce the output of) generators when supplying nonlinear loads to minimize the effects of harmonic heating.] In addition, there is the influence of harmonic sequence components, both on localized heating and torque pulsations.

# 1.1 Thermal Losses

The iron losses comprise two separate losses, “hysteresis losses” and “eddy current losses”.

The hysteresis loss is the power consumed due to nonlinearity of the generator’s flux density/magnetizing force curve and the subsequent reversal in the generator’s core magnetic field each time the current changes polarity (i.e., 120 times a second for $6 0 \ : \mathrm { H z }$ supplies). Higher hysteresis losses occur at harmonic frequencies due to the more rapid reversals compared to those at fundamental frequency. Hysteresis losses are proportional to frequency and the square of the magnetic flux.

Eddy currents circulate in the iron core, windings and other component parts of the generator induced by the stray magnetic fields around the turns in the generator windings. Eddy currents produce losses which increase in proportion to the square of the frequency. The relationship of eddy current losses and harmonics is given by:

$$
P _ {E C} = P _ {E F} \sum_ {h = 1} ^ {h _ {\max }} I _ {h} ^ {2} h ^ {2} \dots \tag {3.1}
$$

where

$$
P _ {E C} = \text {t o t a l e d d y c u r r e n t l o s s e s}
$$

$$
P _ {E F} = \text {e d d y c u r r e n t l o s s e s a t f u l l l o a d a t f u n d a m e n t a l f r e q u e n c y}
$$

$$
I _ {h} \quad = \quad \text {r m s c u r r e n t (p e r u n i t) h a r m o n i c} h
$$

$$
h \quad = \quad \text {h a r m o n i c n u m b e r}
$$

On linear loads, the eddy current losses are fairly minor but become more significant as the harmonic loading increases.

Copper losses are dissipated in the generator windings when current is passed through the winding resistance. For a given load, when harmonic currents are present, the total rms value of the current passing through the windings will be increased, thereby increasing the losses according to:

$$
P _ {C U} = I _ {r m s} ^ {2} R \tag {3.2}
$$

where

$$
\begin{array}{l} P _ {C U} = \text {t o t a l c o p p e r l o s s e s} \\ I _ {r m s} = \text {t o t a l r m s c u r r e n t} \\ R = \text {r e s i s t a n c e o f w i n d i n g} \\ \end{array}
$$

The copper losses are also influenced by a phenomenon termed “skin effect”. Skin effect refers to the tendency of current flow to be confined in a conductor to a layer close to its outer surface. At fundamental frequency, the skin effect is negligible and the distribution of current across the cable is uniform. However, at harmonic frequencies, skin effect is substantially more pronounced, significantly reducing the effective cross sectional area of the conductor and increasing its resistance. The higher the resistance, the higher the ${ \hat { I } } ^ { 2 } R$ losses.

The harmonic stator current drawn by the nonlinear load will result in air gap fluxes, similar in shape to the fundamental but rotating at harmonic frequencies, inducing currents in the rotor iron and windings, adding to rotor losses and the associated temperature rise.

# 1.2 Effect of Sequence Components

Harmonic currents occur in pairs each having a negative or a positive sequence rotation. The $5 ^ { \mathrm { t h } }$ harmonic is negative sequence and induces in the rotor a negatively-rotating $6 ^ { \mathrm { t h } }$ harmonic; the $7 ^ { \mathrm { t h } }$ harmonic is positive and similarly induces a positively-rotating $6 ^ { \mathrm { t h } }$ harmonic in the rotor. The two contra-rotating $6 ^ { \mathrm { t h } }$ harmonic systems in the rotor result in “amortisseur” or “damper” winding currents which are stationary with respect to the rotor, causing additional, localized losses and subsequent heating. Within the rotor, this effect is similar to that caused by single-phase or unbalanced-phase operation, and overheating is unlikely provided the rotor pole faces are laminated. Similarly, the $1 1 ^ { \mathrm { t h } }$ and $1 3 ^ { \mathrm { t h } }$ harmonics will induce both negatively and positively rotating $1 2 ^ { \mathrm { t h } }$ harmonics in the rotor.

Harmonic pairs, in addition to causing additional heating, can create mechanical oscillations on the generator shaft. For $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic frequency, for example, the torque pulsations will be at six times for fundamental $3 6 0 \mathrm { H z }$ based on $6 0 \ \mathrm { H z }$ fundamental, relative to the stator). These result from the interaction between harmonic and fundamental frequencies exciting a specific mechanical resonant frequency. Shafts can be severely stressed due to these oscillations.

# 1.3 Voltage Distortion

A generator is designed to produce sinusoidal voltage at its terminals, but when nonlinear current is drawn, the harmonic currents interact with the system impedances to produce voltage drops at each individual harmonic frequency, thereby causing voltage distortion.

A simplified equivalent circuit for one phase of a three-phase generator is shown in Section 3, Figure 1. Note that the resistances are ignored as they are relatively small compared to the reactance. The iron and damper windings, $D _ { d }$ and $D _ { q } ,$ respectively, prevent any rapid flux changes in the rotor.

![](images/1692527a207ad01bb4ed566a08a7d0272e0bfcd3e49f43741e0a5d589a578e0b.jpg)  
FIGURE 1 Equivalent Circuit for a Generator

To calculate the rms harmonic voltage due to the respective harmonic current, the following method can be used:

$$
V _ {h} = \sqrt {3} \times I _ {h} \times h \times X _ {\text {g e n}} \tag {3.3}
$$

where

$$
V _ {h} = \mathrm {L - L r m s v o l t a g e o f t h e h a r m o n i c} h
$$

$$
I _ {h} \quad = \quad \text {h a r m o n i c c u r r e n t a t o r d e r} h
$$

$$
X _ {g e n} = \text {g e n e r a t o r r e a c t a n c e , i n o h m s}
$$

$$
h \quad = \quad \text {h a r m o n i c n u m b e r}
$$

To calculate the L-L rms harmonic voltage as a percentage of rms fundamental voltage:

$$
\frac {V _ {h} \times 100 \%}{V _ {\text {rms}}} \dots \tag{3.4}
$$

where

$$
V _ {h} = \mathrm {L - L r m s v o l t a g e o f t h e h a r m o n i c} h
$$

$$
V _ {r m s} = \quad \text {L - L f u n d a m e n t a l r m s v o l t a g e}
$$

# Example 1

Calculate the L-L rms $5 ^ { \mathrm { t h } }$ harmonic voltage for a $4 8 0 \ \mathrm { V }$ generator with reactance $X$ of 0.0346 ohms when the $5 ^ { \mathrm { t h } }$ harmonic current is 135 A. Also, express the harmonic voltage as a percentage of the fundamental rms voltage.

$$
\begin{array}{l} V _ {h} = \sqrt {3} \times I _ {h} \times h \times X _ {g e n} \\ = 1. 7 3 2 \times 1 3 5 \times 5 \times 0. 0 3 4 6 \\ = 4 0. 4 5 \mathrm {V} \\ \end{array}
$$

$5 ^ { \mathrm { t h } }$ harmonic voltage as a percentage of the fundamental rms voltage:

$$
\begin{array}{l} = \frac {V _ {h} \times 100 \%}{V _ {r m s}} \\ = \frac {4 0 . 4 5 \times 1 0 0}{4 8 0} \\ = 8.43 \% \\ \end{array}
$$

Note: Other percentage harmonic voltage components can be estimated by performing similar calculations for each harmonic current.

As detailed in Equation 2.6, $V _ { r m s } .$ , the total rms voltage including harmonic voltages, can be calculated using:

$$
V _ {r m s} = \sqrt {\frac {1}{T} \int_ {0} ^ {T} v ^ {2} (t) d t} = \sqrt {\sum_ {h = 1} ^ {\infty} V _ {h} ^ {2}} = \sqrt {V _ {1} ^ {2} + V _ {2} ^ {2} + V _ {3} ^ {2} \dots . + V _ {n} ^ {2}}
$$

Similarly, the $V _ { t h d }$ “voltage total harmonic distortion” can be expressed using Equation 2.8:

$$
V _ {t h d} = \frac {\sqrt {\sum_ {h = 2} ^ {\infty} V _ {h} ^ {2}}}{V _ {1}} \times 100 \% = \frac {\sqrt {V _ {2} ^ {2} + V _ {3} ^ {2} + V _ {4} ^ {2} . . . . . . . . . . + V _ {n} ^ {n}}}{V _ {1}} \times 100 \%
$$

Note: See Subsection 12/1 for practical examples of manual voltage distortion calculations.

# 1.4 Line Notching and Generators

Harmonic currents can cause significant problems in generators in addition to those attributable to additional losses and torsional pulsations. Modern generators use electronic governors to regulate the output voltage, to control the speed, and hence frequency, of the prime mover and to proportionally distribute the kW load of parallel connected generators.

Many electronic regulator units utilize measurement and control circuits which depend on “zero crossovers” (the point on a sine wave when the sinusoidal voltage or current cuts through the zero axis). Where “line notching” or “ringing” occurs, for example with large SCR phase control loads, additional zero crossovers may appear. The combination of harmonic distortion and line notching can cause hunting and instability in voltage and frequency regulation control loops. Many of these problems can be resolved, however, using low pass filters at the input of the appropriate sensing circuits, as shown in Section 3, Figure 2.

In addition, line notching often makes it difficult to correctly load share when parallel generators are operating. Load sharing depends on the measurement of the kW load on each generator. The rms value of current, which assumes fundamental only is normally used in the computation of the kW loading. When harmonic currents are present, false readings can occur when measurements based on average values are used. (Based on sinusoidal waveforms, the rms value is 1.11 times the average value. On waveforms containing harmonics, this assumption is no longer valid.)

Only equipment utilizing “true rms” techniques indicate correct readings for supplies containing harmonics. This is also valid for switchboard instrumentation. The effect of harmonics on instrumentation will be discussed in Subsection 3/9.

Note: For generator AVRs subject to voltage distortion, a low pass filter as detailed in Section 3, Figure 2, below, is recommended. This will result in the majority of the distortion from the voltage control signal being attenuated.

![](images/eb0bdb7d6305ad9c5afb3adac740d4012fe61ea183b16aabc5c73cbd01618f49.jpg)  
FIGURE 2 Low Pass Filter for Generator AVR Sensing on Nonlinear Loads

# 1.5 Shaft Generators

Shaft generators are generally unaffected by the import of external power system harmonics due to the filtering effects of the generator converter, rotary condenser and line reactors.

# 2 Transformers

# 2.1 Thermal Losses

Transformer losses comprise “no load losses”, which are dependent on the peak flux levels necessary to magnetize the transformer core and are negligible with respect to harmonic current levels, and “load losses”, which significantly increase at harmonic frequencies when transformers supply nonlinear current.

The effect of harmonic currents at harmonic frequencies in transformers causes increases in core losses through increased iron losses (i.e., eddy currents and hysteresis). In addition, copper losses and stray flux losses which can result in additional heating, winding insulation stress, especially if high levels of dv/dt (i.e., rate of rise of voltage) are present. Temperature cycling and possible resonance between transformer winding inductance and supply capacitance can also cause additional losses. Potential small laminated core vibrations can appear as additional audible noise.

The increased rms current due to harmonics will increase the $I ^ { 2 } R$ copper losses. The copper losses can be calculated using Equation 3.2, as shown below:

$$
P _ {C U} = I _ {r m s} ^ {2} R
$$

where

$$
P _ {C U} = \text {t o t a l c o p p e r l o s s e s}
$$

$$
I _ {r m s} = \text {t o t a l r m s c u r r e n t}
$$

$$
R \quad = \quad \text {r e s i s t a n c e o f w i n d i n g}
$$

The eddy current losses can be calculated using Equation 3.5:

$$
P _ {E C} = P _ {E F} \sum_ {h = 1} ^ {h _ {\max }} I _ {h} ^ {2} h ^ {2} \dots \tag {3.5}
$$

where

$$
P _ {E C} = \text {t o t a l e d d y c u r r e n t l o s s e s}
$$

$$
P _ {E F} = \text {e d d y c u r r e n t l o s s e s a t f u l l l o a d a t f u n d a m e n t a l f r e q u e n c y}
$$

$$
I _ {h} \quad = \quad \text {r m s c u r r e n t (p e r u n i t) h a r m o n i c} h
$$

$$
h \quad = \quad \text {h a r m o n i c n u m b e r}
$$

The hysteresis loss is the power consumed due to nonlinearity of the transformers flux density/magnetizing force curve and the subsequent reversal in the transformer core magnetic field each time the current changes polarity (i.e., 120 times a second for $6 0 \ \mathrm { H z }$ supplies). Higher hysteresis losses occur at harmonic frequencies due to the more rapid reversals compared to that at fundamental frequency. Hysteresis losses are proportional to frequency and the square of the magnetic flux.

# 2.2 Unbalance, Distribution Transformers and Neutral Currents

Distribution transformers used in four-wire (i.e., three-phase and neutral) distribution systems (for example, those used in some cruise liners) have a delta-wye (delta-star) configuration. Triplen (i.e., $3 ^ { \mathrm { r d } }$ , 9th, 15th…) harmonic currents cannot propagate downstream but circulate in the primary delta winding of the transformer causing localized overheating.

With linear loading, the three-phase currents will cancel out in the neutral conductor. However, when nonlinear loads are being supplied, the triplen harmonics in the phase currents do not cancel out, but instead add cumulatively in the neutral conductor, which can carry up to $1 7 3 \%$ of phase current at a frequency of predominately $1 8 0 ~ \mathrm { H z }$ $3 ^ { \mathrm { r d } }$ harmonic), overheating transformers and on occasion, overheating and burning out neutral conductors.

# 2.3 Transformer Derating or K-factor Transformer

Transformers are of prime importance in any power system. When supplying nonlinear loads, they are particularly vulnerable to overheating and early-life failure. In order to minimize the risk of premature failure, two methods are used by designers:-

“Derate” the transformer (i.e., oversize it such that it operates at less than the rated load capacity) or if existing, consider reducing the loading on it.   
Use “K-factor” or “K-rated” transformers. K-rated transformers are specifically designed for nonlinear loads and operate with lower losses at harmonic frequencies. K-rated transformer modifications can include additional cooling ducts, a redesign of the magnetic core based on lower normal flux density by using higher grades of iron, using smaller insulated secondary conductors wired in parallel and transposed to reduce heating due to skin effect and AC resistance and enlarging the primary winding to withstand triplen harmonics present on single-phase nonlinear loads.

K-rated transformers are usually preferred to derated transformers, as they are designed to run at rated kVA loads in the presence of harmonic currents and also they normally comply with Underwriters Laboratory (UL) and NEC requirements for transformers supplying nonlinear loads. Section 3, Figure 3 illustrates a typical relationship with transformer derating and K-factor for nonlinear loads.

![](images/fe8392514b72c6f2574cf78be0d9e4a7b3b0ca83672ddb8ea265b3eb356752bd.jpg)  
FIGURE 3 Typical Transformer Derating Curve for Nonlinear Load

UL developed the K-factor system to indicate the capability of transformers to handle harmonic loads. The subsequent ratings are described in UL1561. Essentially, the K-factor is a weighting of the harmonic current loads according to their effects on transformer heating as derived from ANSI/IEEE C57.110. A K-factor of 1.0 indicates a linear load (i.e., no harmonic loading). The higher the K-factor, the greater the heating effect on a given transformer. The equation for calculating K-factor is the ratio of eddy current losses when supplying nonlinear and linear loads:

$$
K = \frac {P _ {1}}{P _ {f}} = \sum_ {h = 1} ^ {h = h _ {\max }} I _ {h} ^ {2} h ^ {2} \tag {3.6}
$$

where

$$
K = \text {K - f a c t o r}
$$

$$
P _ {1} = \text {e d d y c u r r e n t l o s s e s o n l i n e a r l o a d}
$$

$$
P _ {f} = \text {e d d y c u r r e n t l o s s e s o n n o n l i n e a r l o a d}
$$

$$
h \quad = \quad \text {h a r m o n i c n u m b e r}
$$

$$
I _ {h} \quad = \quad \text {h a r m o n i c c u r r e n t (p e r u n i t)}
$$

One acknowledged problem associated with calculating K-factors is selecting the most appropriate range of harmonic frequencies. Based on the upper limit, for example, of $1 5 ^ { \mathrm { t h } }$ , $\overline { { 2 5 } } ^ { \mathrm { t h } }$ or $5 0 ^ { \mathrm { t h } }$ harmonics, the calculations can yield significantly different K-factors for the same load. IEEE 519 (1992) considers harmonics up the $\bar { 5 } 0 ^ { \mathrm { t h } }$ . However, in many calculations harmonic orders up to $2 5 ^ { \mathrm { t h } }$ are commonly used.

In Europe, the K-factor is termed “Factor K”, with significantly more complicated calculations according to BS 7821 Part 4:

$$
K = \left[ 1 + \frac {e}{1 + e} \left(\frac {I _ {1}}{I}\right) ^ {2} \sum_ {n + 2} ^ {n = N} \left(n ^ {q} \left(\frac {I _ {n}}{I _ {1}}\right) ^ {2}\right) \right] ^ {0. 5}. \tag {3.7}
$$

where

e eddy current loss at fundamental frequency divided by the loss due to DC current equal to the rms value of the sinusoidal current, both a reference temperature

n = harmonic number

I = rms value of the sinusoidal current including all harmonics given by:

$$
= \left(\sum_ {n = 1} ^ {n = N} \left(I _ {n}\right) ^ {2}\right) ^ {0. 5} = I _ {1} \left[ \sum_ {n = 1} ^ {n = N} \left(\frac {I _ {n}}{I _ {1}}\right) ^ {2} \right] ^ {0. 5}. \tag {3.8}
$$

In $I _ { n }$ magnitude of $n$ -th harmonic

$I _ { 1 }$ = magnitude of fundamental current

q an exponential constant which is dependent on the type of winding and frequency. Typical values are 1.7 for transformers with round or rectangular cross sections in both windings and 1.5 for those with foil low voltage windings.

# 3 Induction Motors

# 3.1 Thermal Losses

Harmonics distortion raises the losses in AC induction motors in a way very similar to that apparent in transformers with increased heating, due to additional copper losses and iron losses (eddy current and hysteresis losses) in the stator winding, rotor circuit and rotor laminations. These losses are further compounded by skin effect, especially at frequencies above $3 0 0 \mathrm { H z }$ .

Leakage magnetic fields caused by harmonic currents in the stator and rotor end windings produce additional stray frequency eddy current dependent losses. Substantial iron losses can also be produced in induction motors with skewed rotors due to high-frequency-induced currents and rapid flux changes (i.e., due to hysteresis) in the stator and rotor. The magnitude of the iron losses is dependent on the iron loss characteristic of the laminations and the angle of skew.

The formulae used to calculate copper losses and eddy current losses used for transformers are also applicable for induction motors:

$$
P _ {C U} = I _ {r m s} ^ {2} R
$$

where

The eddy current losses can be calculated using Equation 3.5:

$$
P _ {E C} = P _ {E F} \sum_ {h = 1} ^ {h _ {\mathrm {m a x}}} I _ {h} ^ {2} h ^ {2}
$$

where

$$
P _ {E C} = \text {t o t a l e d d y c u r r e n t l o s s e s}
$$

$$
P _ {E F} = \text {e d d y c u r r e n t l o s s e s a t f u l l l o a d a t f u n d a m e n t a l f r e q u e n c y}
$$

$$
I _ {h} \quad = \quad \text {r m s c u r r e n t (p e r u n i t) h a r m o n i c} h
$$

$$
H = \text {h a r m o n i c n u m b e r}
$$

Motors with deep bar or double cage rotors are susceptible to additional losses, particularly on highly polluted supplies containing high order harmonics. This can in extreme cases, lead to “hot rotors” which, due to conduction along the shaft, can degrade the bearing lubrication and result in bearing collapse. Harmonic currents also can result in bearing currents. This can be prevented through the use of an insulated bearing, a practice common in AC variable frequency drive-fed AC motors.

Overheating imposes significant limits on the effective life of an induction motor. For every $1 0 ^ { \circ } \mathrm { C }$ rise in temperature (continuous) above rated temperature, the life of motor insulation may be reduced by as much as $50 \%$ . Squirrel cage rotors can normally withstand higher temperature levels compared to wound rotors.

The motor’s windings, especially if insulation is class B or below, are also susceptible to damage due high levels of dv/dt (i.e., rate of rise of voltage) such as those attributed to line notching and associated ringing.

# 3.2 Effect of Harmonic Sequence Components

Harmonic sequence components also adversely affect induction motors. Positive sequence components (i.e., 7th, 13th, 19th…) will assist torque production, whereas the negative sequence components $( 5 ^ { \mathrm { t h } } , 1 3 ^ { \mathrm { t h } } , 1 7 ^ { \mathrm { t h } } . . . )$ will act against the direction of rotation resulting in torque pulsations which are significant. Zero sequence harmonics (i.e., triplens) do not rotate (i.e., they are stationary); any harmonic energy associated with them is dissipated as heat. The magnitude of torque pulsations due to sequence components can be estimated as follows to assess possible shaft torsional vibration problems based on a nominal voltage:

$$
T _ {3 k} = \left[ I _ {n +} ^ {2} + I _ {n -} ^ {2} - 2 I _ {n +} I _ {n -} \cos \left(\phi_ {n +} - \phi_ {n -}\right) \right] ^ {1 / 2} \text {p e r u n i t}. \tag {3.9}
$$

where

$$
I _ {n +}, I _ {n -} = \quad \text {p e r u n i t v a l u e s}
$$

$$
n + \quad = \quad \text {r e p r e s e n t s} 1 + 3 k \text {h a r m o n i c o r d e r s}
$$

$$
n - \quad = \quad \text {r e p r e s e n t s} 1 - 3 k \text {h a r m o n i c o r d e r s}
$$

For example, if we consider a $5 0 ~ \mathrm { H z }$ supply with $4 \%$ voltage distortion based on motor harmonic currents of 0.03 and 0.02 per unit for the $5 ^ { \mathrm { { ^ { t h } } } }$ and $7 ^ { \mathrm { t h } }$ harmonics, respectively. Assuming no phase displacement between harmonics and full value of voltage, the torque will have a varying component at $3 0 0 ~ \mathrm { H z }$ with an amplitude of torque fluctuation of 0.01 per unit. If the harmonics have the worst case phase relationship, then the amplitude of the torque fluctuation will be 0.05 per unit

# 3.3 Explosion-proof Motors and Voltage Distortion

A practical application of AC induction motors worth noting is that of “explosion-proof motors” (i.e., flameproof motors). This type of motor relies on the principle that no matter what happens inside the flameproof enclosure (e.g., an internal explosion) it cannot transmit to the surrounding hazardous area. While that may be perfectly valid on pure sinusoidal supplies, it may not be so on supplies distorted by harmonics. An explosion-proof motor relies on the flameproof enclosure and shaft-mounted flameproof seals to contain any internal explosion in the event of an escape of gas or vapor. However, in the presence of harmonics and deep bar or double cage rotors, the rotor may overheat and degrade the flameproof seals, and if there is an internal explosion (more likely due to excessive rotor temperatures), it may not be successfully contained but transmit to the external “hazardous area” with significant consequences. Dependent on the magnitude of the voltage distortion, the rotor temperature may exceed the motor “T class” [i.e., temperature class (for example, $2 0 0 ^ { \circ } \mathrm { C }$ for T3)]. As detailed above, hot rotors can also result in bearing degradation.

It should also be noted that “explosion-proof motors” are designed and certified based on “clean” sinusoidal supplies. According to EN60034-1, explosion-proof protection concepts EExd (flameproof motors), EExe (increased safety) and EExp (pressurised) are permitted only $2 \%$ voltage distortion before they are classed “as operating outside the conditions envisaged when they were certified”. For EExN motors (non-sparking motor) $3 \%$ voltage distortion is permitted under EN60034-12. Higher levels of voltage distortion can be accommodated for all protection concepts, subject to special tests and certification.

Where a certified explosion-proof motor is driven by the variable frequency drive, the safety certificate of the motor is no longer valid unless the safety certification has been based on the tests using that particular variable frequency drive.

In North America, NEMA standard MG-1 “Application Considerations for Constant Speed motors used on Sinusoidal Bus with Harmonic Content and General Purpose Motors used with Variable Voltage or Variable Frequency Controls or both” proposes the amount of motor derating necessary for both fixed-speed motors on distorted supplies or those fed by variable frequency supplies, as illustrated by Section 3, Figure 4. MG-1 refers to explosion-proof motors, on distorted supplies, for use in hazardous areas to NEMA 30.02.2.11.

![](images/021729a2a0ff46da0bc4212237b4e2b4e7328e66544676bbaa9d8aa11227c0db.jpg)  
FIGURE 4 Proposed NEMA Derating Curve for Harmonic Voltages

The “Harmonic Voltage Factor” (HVF) can be defined as:

$$
H V F = \sqrt {\sum_ {n = 5} ^ {n = \infty} \frac {V _ {n} ^ {2}}{n}} \dots \tag {3.10}
$$

where

$$
n \quad = \quad \text {o d d h a r m o n i c , n o t i n c l u d i n g t r i p l e n s}
$$

$$
V _ {n} = \text {p e r u n i t m a g n i t u d e o f t h e v o l t a g e a t t h e} n \text {- t h h a r m o n i c}
$$

# Example 2

Calculate the HVF based on the per unit harmonic voltages of 0.09, 0.065, 0.042, 0.038 for the $5 ^ { \mathrm { t h } }$ , $7 ^ { \mathrm { t h } }$ , $1 1 ^ { \mathrm { t h } }$ and $1 3 ^ { \mathrm { t h } }$ harmonics, respectively.

$$
H V F = \sqrt {\sum_ {n = 5} ^ {n = \infty} \frac {V _ {n} ^ {2}}{n}}
$$

$$
H V F = \sqrt {\frac {0 . 0 9 ^ {2}}{5} + \frac {0 . 0 6 8 ^ {2}}{7} + \frac {0 . 0 4 2 ^ {2}}{1 1} + \frac {0 . 0 3 8 ^ {2}}{1 3}}
$$

$$
H V F = \underline {{0 . 0 5 0 5}} (\text {or} 5. 0 5 \% \text {v o l t a g e d i s t o r t i o n})
$$

# 4 Variable Speed Drives

Electrical variable speed drives of all types (i.e., AC or DC) use power semiconductors to rectify the AC input voltage and current and thereby create harmonics. However, these can be also susceptible to disruption and component damage due to input line harmonics.

However, harmonics can be beneficial for drives as they cause flattening of the peak voltage (i.e., termed “flat topping” – see Subsection 3/7, “Computers and Computer Based Equipment,” for more details) which reduces the stress on rectifiers. Conversely, large numbers of 2-pulse drives (or other single-phase nonlinear loads) can increase the peak-to-peak voltage magnitudes, increasing stress the on rectifiers.

Generally, the larger rating a drive is, the more it is immune to the effects of harmonics and line notching. Line commutated inverters (LCIs, also known as “current source inverters” when used on smaller induction motor applications) and cycloconverters are more commonly used in higher ratings (i.e., above 2000 HP). These are assumed to be relatively immune to the normal level of harmonics.

Both harmonics and line notching effect variable speed drives. The effect of line notching is more pronounced when the drive(s) is at low speed and high load. Ringing, associated with line notching is also problematic.

Small, single-phase (2-pulse) PWM drives with no reactors have high levels of $I _ { t h d } ,$ often up to $1 3 0 \mathrm { - } 1 4 0 \%$ including a large $3 ^ { \mathrm { r d } }$ harmonic which adds cumulatively in the neutral conductor, significantly increasing the neutral current up to $1 7 3 \%$ of phase current and increasing neutral-toground voltages. The resultant excessive localized harmonic current can be reflected into the DC bus, causing overheating on the smoothing capacitors. Ringing associated with line notching increases DC bus levels at no or light loading with consequential over-voltage tripping.

2-pulse (i.e., single-phase) and small 6-pulse SCR DC drives which do not have commutating reactors or isolation transformers can misfire in the presence of line notching and/or high levels of harmonic current.

Small 6-pulse PWM (“pulse width modulation”) drives (i.e., up to $1 0 \mathrm { H P } / 7 . 5 \mathrm { k W }$ ) usually have no AC line or DC bus reactors. On supplies with line notching, any overshoot may increase the DC bus voltage on no-load or light load, resulting in drive “over-voltage trip”. Larger PWM drives with a simple input diode bridge with either AC line or DC bus reactors are usually relatively robust and can operate in a harmonics environment without significant problems.

AC PWM drives with SCRs for pre-charge (i.e., “soft starting” of DC bus voltage) or for variable voltage DC bus control may experience misfiring of SCRs due to incorrect or irregular conduction and excessive heating of DC bus capacitors and smoothing reactors if the supply voltage is significantly contaminated by line notching or high levels of harmonics. Line notching can also result in excessive heating of SCR snubber components.

Standard 6-pulse AC PWM drives, the most common type used, are relatively robust and can usually withstand line disturbances due to harmonics below $5 \%$ $V _ { t h d }$ . Above 10-15 HP (7.5-11 kW), most drives “filter” the harmonics to varying degrees using AC line reactors, and in some cases, passive filters (i.e., this also applies to drives with “active front ends” which synthesize an input sinusoidal current wave shape. These need special filtering to attenuate the input bridge carrier frequency affecting the supply system and to reduce the overall EMI which is significantly more than emitted from standard diode or SCR pre-charge input stages).

6-pulse SCR DC drives above $1 0 ~ \mathrm { H P } / 7 . 5 ~ \mathrm { k W }$ usually have AC commutating reactors or isolation transformers installed between the drive and the line to attenuate the line notches on the supply side. These also reduce the effects of line notching and harmonics impressed on the drive. However, if the line notching or levels of harmonic current are significant, SCR misfiring can result, possibly blowing fuses or tripping circuit breakers downstream.

Phase displacement transformers (i.e., for 12-, 18-, 24-pulse…) for AC or DC drives reduce the effects of downstream harmonics and line notching at the drive terminals.

On weak supplies (i.e., supplies with high source impedance), voltage “flat topping” (see Section 3, Figures 5 and 6) can occur, reducing the DC bus voltage levels, which prevents the drive from achieving the nominal power output for drive and the motor. In addition, it can reduce the drive ride-through in the event of line disturbances and increase the output current to the motor, thereby raising its temperature due to additional $I ^ { 2 } R$ losses.

![](images/a01a3f995d8666b388ffb10aad8ce4fa88a84df95568a2e253c31352c2568156.jpg)  
FIGURE 5 AC PWM Drive Current Distortion on Weak Source

![](images/74ecebf6eae137edc0af0deabd1e0988ad415f995da2edccc2544053dea38afc.jpg)  
FIGURE 6 PWM Drive “Flat Topping” due to Weak Source

Unwanted “electrical noise” (i.e., EMI) can be induced into drive signal and control cables, if power cabling is not sufficiently segregated from the control cables or if shielding or grounding is not adequate, resulting in spurious command and feedback signals into the drive. In severe cases, where rerouting cabling is not feasible, the retrofitting of low pass filters to drive input may be necessary. Control relays may fail to operate correctly and measuring equipment may be adversely effected.

Note: Filtering of the drive high frequency currents is not normally possible in IT power systems (insulated neutrals). The voltage across any input EMC filter capacitors would be 1.73 times higher in the event of a ground fault, damaging or destroying the filter capacitors.

# 5 Lighting

# 5.1 Flicker

One noticeable effect on lighting is the phenomenon of “flicker” (i.e., repeated fluctuations in light intensity). Lighting is highly sensitive to rms voltage changes; even a deviation of $0 . 2 5 \%$ is perceptible to the human eye in some types of lamps.

The severity of the flicker is dependent on a number of factors including:

• The type of light (incandescent, fluorescent or high intensity discharge)   
• The magnitude of the voltage fluctuations   
• The “frequency” of the voltage fluctuations   
The “gain factor” of the lamp (i.e., $\%$ relative change in light level divided by $\%$ relative fluctuation in rms voltage)   
• The amount of ambient light in lighted area

Superimposed interharmonic voltages in the supply voltage are a significant cause of light flicker in both incandescent and fluorescent lamps, albeit at different levels of intensity.

Incandescent lamps at higher voltages are usually more susceptible to voltage changes due to smaller filaments and shorter time constants than lamps of similar power rating but lower voltage. In fluorescent lamps, the type of ballast used impacts on the amount of flicker. The older, magnetic type ballasts are more susceptible to flicker than the more modern, high frequency types.

The luminous flux (i.e., light intensity in “lumens”) of lamps under voltage fluctuations can be expressed by:

$$
\Phi_ {V} = \Phi_ {n} \left(\frac {V}{V _ {n}}\right) ^ {3. 6} \quad \text {f o r i n c a n d e s c e n t l a m p s}. \tag {3.11}
$$

and

$$
\Phi_ {V} = \Phi_ {n} \left(\frac {V}{V _ {n}}\right) ^ {1. 8} \quad \text {f o r f l u o r e s c e n t l a m p s}. \tag {3.12}
$$

where $\Phi _ { V }$ is luminous flux at rated voltage, $V _ { n }$ .

Any voltage fluctuations also impact on the life of lamps, which may have safety implications for the vessel. In the case of incandescent lamps, the reduction in working life with changes in voltage can be expressed as:

$$
T _ {V} = \left(\frac {V}{V _ {n}}\right) ^ {- 1 4} \dots \tag {3.13}
$$

where durability at rated voltage, $V _ { n } ,$ usually equates to 1000 hrs.

# 5.2 Effects of Line Notching on Lighting

Line notching will also effects lighting to varying degrees. The consequential reduction in rms voltage will cause a reduction in the intensity of illumination, especially in incandescent lamps. If the notches are severe or where ringing occurs, transient suppression may be necessary at lighting distribution board level to protect the individual light fittings.

Fluorescent fittings used with occupancy sensors which are based on zero crossover detection may experience difficulties if the notching is severe and multiple crossovers result.

# 5.3 Potential for Resonance

The interaction between harmonic current and power factor correction capacitors inside individual fluorescent lighting units can result in parallel resonances being excited between the capacitors and power system inductances resulting in damage of the lighting units. Ideally, individual power factor correction should be avoided and group power factor correction with detuning reactors should be installed at lighting distribution panel level.

# 6 Uninterruptible Power Supplies (UPS)

Due to the phenomenal increase in “power quality”-sensitive loads such as computers and navigation or radio communications equipment, uninterruptible power supplies (UPSs) are now commonly provided and can range from a 100 VA to several MVA.

UPS are very similar in architecture to variable speed drives. Therefore, the effects of harmonics on components within UPS systems will be almost identical with additional heating on power devices, smoothing capacitors and inductors, where installed. Batteries may overheat due to excessive harmonics and interharmonics on the DC side of the rectifier.

Excessive voltage distortion or notching/ringing can cause misfiring of input rectifier SCRs possibly resulting in fuse rupture. On high levels of distortion, bypass sensing circuits may disable the bypass circuit, inhibiting the alarm system advising of problems in the bypass system.

If resonance occurs, perhaps due to the UPS input filter, UPS may shut down, displaying a “loss of AC supply” alarm and bypass to inverter mode. In the presence of harmonics, the UPS line side filter (to reduce the harmonics from the rectifier input stage) may act as a sink (i.e., attract harmonic currents from upstream) damaging the harmonic filter.

It should be noted that UPS systems do also produce harmonic currents. This will be discussed in Section 4.

# 7 Computers and Computer Based Equipment

The majority of computer based equipment derives the internal voltage supplies from switched mode or similar power supply units and it is often here where harmonic problems are noticed.

Section 2, Figure 7 shows the current drawn from the supply by SMPS with two pulses per cycle while the SMPS capacitors are charging. As can be seen in Section 3, Figure 7, below, the pulsed nature of the current causes a voltage drop at the peak of the voltage wave.

FIGURE 7 Voltage “Flat Topping” due to Pulse Currents

![](images/61cd07228a218015bb97febccc6a75d280b4761492261ac25faeb0d7fb64bc06.jpg)  
FIGURE 8 Effect of DC Bus Voltage with Flat Topping

Voltage flat topping reduces the operating DC bus voltage (Section 3, Figure 8), resulting in increased current being drawn and increased ${ \hat { I } } ^ { 2 } R$ losses in the equipment and associated cabling, which can manifest itself in early life failure of components due to high operating temperatures.

Higher voltage trace $=$ Normal DC bus level

Lower voltage trace $=$ DC bus volts due to flat topping

![](images/b82cfc967d94363ccae74ee52472c49a859d1339c9a3a763dfee2e25fdd96265.jpg)

# Example 3

Determine the per unit increase in ${ \hat { I } } ^ { 2 } R$ losses based on a $10 \%$ decrease in DC bus voltage due to flat topping.

$$
P = V \cdot I
$$

where

$$
P = \text {p o w e r} (\text {p e r u n i t})
$$

$$
V = \text {v o l t a g e (p e r u n i t)}
$$

$$
I = \text {c u r r e n t}
$$

If $V$ is 0.9 per unit, $I = \frac { P } { V } = \frac { 1 . 0 } { 0 . 9 } = 1 . 1 1$ per unit

$$
P _ {l o s s} = I ^ {2} R = (1. 1 1) ^ {2} \cdot (1) = 1. 2 3 \text {p e r u n i t}
$$

Power losses increase by $23 \%$

Note: The above is only valid for circuits where the current is not limited and power control is dominant. If passive components predominate in the circuit, the impedance will remain mostly unchanged and current will decrease in proportion with the voltage. In the case of AC PWM drives (single- or three-phase input), the current is not permitted to rise above a predetermined value by the current control system.

Similarly, Section 3, Figure 9 shows how the reduction in DC bus voltage on the capacitors reduces the stored energy within the power supply thus reducing its ride-through capability.

# FIGURE 9 Flat Topping Reducing Supply Ride-through

Higher voltage trace $=$ Normal DC bus level

Lower voltage trace $=$ DC bus volts due to flat topping

![](images/cce6dbf88e3d73fb409bc77629a6bcc8935fcb38fdfe46a55cb39008188df3d8.jpg)

The energy available from the DC capacitors during ride-through can be expressed as:

$$
W _ {R} = \frac {1}{C} C \left(V _ {1} ^ {2} - V _ {2} ^ {2}\right) \dots \tag {3.14}
$$

where

$$
V _ {1} \quad = \quad \text {n o r m a l v o l t a g e (p e r u n i t)}
$$

$$
V _ {2} = \text {r e d u c e d v o l t a g e (p e r u n i t)}
$$

$$
C = \text {v a l u e o f c a p a c i t o r}
$$

# Example 4

Determine the reduction in ride-through capability in SMPS due to flat topping and $10 \%$ decrease in peak voltage. Assume a system drop-out voltage of $70 \%$ .

$$
V _ {1} = 1 \text {p e r u n i t ,} V _ {2} = 0. 7 \text {p e r u n i t}
$$

At normal voltage, $V _ { 1 } \cdot W _ { R } = ( 1 ^ { 2 } - 0 . 7 ^ { 2 } ) = 0 . 5 1$ per unit

At $10 \%$ reduction (0.9 per unit) $\mathbf { \varepsilon } = ( 0 . 9 ^ { 2 } - 0 . 7 ^ { 2 } ) = 0 . 3 2$ per unit

Therefore, reduction in ride-through = 0.51 0.32− 100%× = 37% 0.51

Note: The above effects are similar to those experiences by single-phase and three-phase AC PWM drives which a diode rectifier and capacitive DC bus.

# 8 Cables

# 8.1 Thermal Losses

Cable losses, dissipated as heat, are substantially increased when carrying harmonic currents due to elevated ${ \hat { I } } ^ { 2 } R$ losses, the cable resistance, $R$ , determined by its DC value plus skin and proximity effect. As stated in Equation 2.7, the rms current $I _ { r m s }$ in a distorted current waveform can be calculates thus:

$$
I _ {r m s} = \sqrt {\frac {1}{T} \int_ {0} ^ {T} i ^ {2} (t) d t} = \sqrt {\sum_ {h = 1} ^ {\infty} I _ {h} ^ {2}} = \sqrt {I _ {1} ^ {2} + I _ {2} ^ {2} + I _ {3} ^ {2} \dots . . . + I _ {n} ^ {2}}
$$

therefore: $I _ { r m s } = I _ { { r U N D } } \sqrt { 1 + \left( \frac { I _ { t h d } } { 1 0 0 } \right) ^ { 2 } }$

# Example 5

Calculate the rms current carried by a power cable based on a current total harmonic distortion $( I _ { t h d } )$ of $42 \%$ and fundamental current of $6 0 0 \mathrm { \ A }$ .

$$
I _ {r m s} = 6 0 0 \sqrt {1 + 0 . 4 2 ^ {2}}
$$

$$
I _ {r m s} = \underline {{6 5 1 A}}
$$

Ignoring the effects of skin and proximity effects, the ${ \hat { I } } ^ { 2 } R$ losses in the cable due to harmonic currents would increase by:

$$
\left(\frac {651}{600}\right) ^ {2} \times 100 \% = \underline {17.73 \%} \text {compared to heating effect at fundamental frequency}.
$$

# 8.2 Skin and Proximity Effects

The resistance of a conductor is dependent on the frequency of the current being carried. Skin effect is a phenomenon whereby current tends to flow near the surface of a conductor where the impedance is least. An analogous phenomenon, proximity effect, is due to the mutual inductance of conductors arranged closely parallel to one another. Both of these effects are dependent upon conductor size, frequency, resistivity and the permeability of the conductor material.

At fundamental frequencies, the skin effect and proximity effects are usually negligible, at least for smaller conductors. The associated losses due to changes in resistance, however, can increase significantly with frequency, adding to the overall ${ \hat { I } } ^ { 2 } R$ losses.

The harmonic frequencies produce a ratio of AC to DC resistance, $k _ { c } .$ , which can be defined as:

$$
k _ {c} = \frac {R _ {A C}}{R _ {D C}} = 1 + k _ {S E} + k _ {P E} \tag {3.15}
$$

where

$$
k _ {S E} = \text {r e s i s t a n c e g a i n d u e t o s k i n e f f e c t}
$$

$$
k _ {P E} = \text {r e s i s t a n c e g a i n d u e t o p r o x i m i t y e f f e c t}
$$

Skin effect parameter, $x _ { \mathrm { { ; } } }$ , as a function of frequency and DC resistance can be found in cable handbooks, but can also be expressed as:

$$
x = 0. 0 2 7 6 7 8 \sqrt {\frac {f u}{R _ {D C}}} \tag {3.16}
$$

where

$$
f \quad = \quad \text {f r e q u e n c y , i n H z}
$$

$$
u \quad = \quad \text {m a g n e t i c p e r m e a b i l i t y o f t h e c o n d u c t o r}
$$

$$
R _ {D C} = \quad \text {D C r e s i s t a n c e i n o h m s / 3 0 4 . 8 m (1 0 0 0 f t)}
$$

The resistance gain due to proximity effect can be expressed by:

$$
k _ {P E} = k _ {S E} \sigma^ {2} \left(\frac {1 . 1 8}{k _ {S E} + 0 . 2 7} + 0. 3 1 2 \sigma^ {2}\right) \tag {3.17}
$$

where $\sigma$ is the ratio of the conductor diameter and the axial spacing between conductors.

Section 3, Figure 10 plots the AC/DC resistance ratio, $k _ { c } ,$ at different harmonic numbers of four sizes of power cable with conductors, 500 kcmil, 4/0 AWG, 1/0 AWG and 12 AWG. The spacing used to obtain the $\sigma$ values for the four cable types is based on National Electric Code (NEC) insulation type THHN.

![](images/675c9ff0fb4eaecf30dcd6ae063a7f551c0bc2c569a2a684142e6bf432739524.jpg)  
FIGURE 10   
Cable AC/DC Resistance, $k _ { c }$ as a Function of Harmonic Numbers

Section 3, Figures 11 and 12 illustrate the difference of varying harmonic numbers on both proximity effect and skin effect for 12 AWG and 4/0 AWG cable, respectively. As can be noted, the proximity effect is more significant in the smaller cable, whereas with the large cable, the proximity effect may be more significant at lower frequencies but not at higher frequencies. Therefore, it can be noted that proximity effects due to harmonics tends to be the more significant in power cables.

![](images/d1df0114288c5f817e4289e7666fc5faaaf2083271c4b056a3c0688451ec11fc.jpg)  
FIGURE 11   
4/0 AWG Cable – Proximity and Skin Effect due to Harmonics

![](images/ee8c5a11ac66a7ad352aa5c918780666166f3730ad3b4b578b37f3f24e388ee2.jpg)  
FIGURE 12   
12 AWG Cable – Proximity and Skin Effect due to Harmonics

# 8.3 Neutral Conductors in Four-wire Systems

On four-wire distribution systems, such as now installed on large passenger vessels, which may have a large percentage of nonlinear loads (e.g., computers, ballast lighting, etc.), a large component of triplen harmonics are often present. The phase currents do not cancel in the neutral conductors as with linear loading but sum in the neutral conductor.

The overloading on the conductors (and the distribution transformer primary, assuming delta-wye configuration), can be significant (up to $1 7 3 \%$ of phase current), therefore, the neutral current should be dimensioned accordingly or mitigation equipment installed to attenuate the level of triplen harmonics. In addition, triplen currents are problematic on generators due to the associated additional temperature rise on the machines.

Refer to 4/1.2 for further information.

# 8.4 Additional Effects Associated with Harmonics

Harmonic currents can on occasion excite parallel resonance between cable capacitance and system inductances, especially when very long cable lengths are used. This has been documented on offshore installations when platforms with no onboard generating capacity are supplied from other platforms a considerable distance away by long subsea cables.

Harmonic voltages increase the dielectric stress on cables, thereby decreasing the reliability and the working life of cables in proportion to the crest voltages.

Power cables carrying harmonic loads act to introduce EMI (electromagnetic interference) in adjacent signal or control cables via conducted and radiated emissions. This “EMI noise” has a detrimental effect on telephones, televisions, radios, computers, control systems and other types of equipment. Correct procedures with regard to grounding and segregation within enclosures and in external wiring systems must be adopted to minimize EMI.

# 9 Measuring Equipment

Conventional meters are normally designed to read sinusoidal-based quantities. Nonlinear voltages and currents impressed on these types of meters introduce errors into the measurement circuits which result in false readings.

Conventional meters are calibrated to respond to rms values. Root mean square (rms) can be defined as the magnitude of sinusoidal current which is the value of an equivalent direct current which would produce the same amount of heat in a fixed resistive load which is proportional to the square of the current averaged over one full cycle of the waveform (i.e., the heat produced is proportional to the mean of the square; therefore the current is proportional to the “root mean square”).

Refer to Section 3, Figure 13. For a pure sine wave, the rms value is 0.707 times the peak value and the peak value is 1.414 times the rms value). If the magnitude of the sine wave is “averaged” (i.e., the negative half cycle is inverted) the mean value will be 0.636 times the peak value or 0.9 times the rms value.

For a sine wave, these two important ratios relevant to current and voltage measurement can be derived:

$$
\text {P e a k} = \frac {\text {P e a k v a l u e}}{\text {r m s v a l u e}} \tag {3.18}
$$

$$
F o r m \quad f a c t o r = \frac {r m s v a l u e}{M e a n v a l u e} \tag {3.19}
$$

Most analogue meters and a large number of digital multi-meters are designed to read voltage and current quantities based on a technique termed “average reading, rms calibrated”. This technique entails taking a measurement of the average (or mean) value $0 . 6 3 6 \times$ peak) and multiplying the result by the form factor (1.11 for a sine wave). The result is 0.7071 times the peak value, which is displayed as “rms”. This assumption is valid only for pure sinusoidal waveforms.

However, only “true rms” instruments are capable of accurately measure distorted values.

![](images/7946dc7d52c1648a0f582dbfc7b25be7827f8724bc911a9e711f7d99e8248984.jpg)  
FIGURE 13 Peak and rms Values of Sinusoidal Waveform

The difficulty in accurately measuring distorted values with conventional meters is illustrated by the current drawn by a switched mode power supply (Section 3, Figure 14). Using a true rms meter, the real current is 1.0 A, the peak value of 2.6 A with an average of 0.55 A. Using a conventional “average reading, calibrated rms” meter the “rms current” displayed would be 0.61 A, almost $40 \%$ lower than the real current value.

![](images/5023ac7e4e4661094c8e89aedfd2f56049703590494bc23c31fd5932c6b13a40.jpg)  
FIGURE 14 Difficulties Conventional Meters Have Reading Distorted Waveforms

The “crest factor” of a waveform can be defined as:

$$
C r e s t \quad f a c t o r = \frac {\text {P e a k v a l u e}}{\text {r m s v a l u e}} \tag {3.20}
$$

For a pure sine wave, the crest factor is 1.414 (1.0/0.707). For pulsed waveforms, this will be significantly higher. The higher the crest factor a true rms instrument has, the more accurate it will be in the measurement of distorted waveforms. The use of meters with crest factors less than three (3) is not recommended.

Standard toroidal-type current transformers used for measuring distorted currents must be of high quality, with linear response and a very wide bandwidth in order to accurately read frequencies up to $\hat { 5 } 0 ^ { \mathrm { t h } }$ harmonic ( $3 \mathrm { k H z }$ based on $6 0 \ : \mathrm { H z }$ fundamental). Hall Effect currents transducers, commonly used with probable instruments (e.g., harmonic analyzers, power meters, etc.) do accurately measure nonlinear currents, but should be calibrated on a regular basis.

On high voltage networks, magnetic voltage transformers designed to operate on fundamental frequencies are commonly used. For use up to $1 1 \ \mathrm { k V }$ , this type of voltage transformer can measure harmonic voltages under $5 \mathrm { k H z }$ (i.e., $8 3 ^ { \mathrm { r d } }$ harmonic at $6 0 ~ \mathrm { H z }$ fundamental) to an accuracy of around $3 \%$ , provided no resonance is introduced which causes phase and ratio errors. The response of the transformer is largely dependent on the burden used on the LV side, whereas the bandwidth is limited by the frequency response of the magnetic core, the winding-to-winding, winding-to-ground and turnto-turn capacitance, plus other stray capacitance.

The accurate measurement of power factor does present a problem with nonlinear loads when two different power factors are present (see Section 5): the “displacement power factor”, which is the power factor of the fundamental component only and the “true” or “real” power factor, which includes both the fundamental and harmonic components. In a sine wave, the power factor is simply a measure of the cosine of phase angle between voltage and current; this is not valid for nonlinear loads. The way to accurately measure nonlinear power factor is to measure the average instantaneous power and divide it by the product of the true rms voltage and true rms current:

$$
\text {T r u e} \cos \phi = \frac {P _ {\text {i n s t}}}{\left(V _ {\text {t r m s}} . I _ {\text {t r m s}}\right)} \tag {3.21}
$$

where

$$
\cos \phi = \text {n o n l i n e a r}
$$

$$
P _ {i n s t} = \text {a v e r a g e i n s t a n t a n e o u s p o w e r (k W)}
$$

$$
V _ {t r m s} = \text {t r u e r m s v o l t a g e}
$$

$$
I _ {t r m s} = \text {t r u e r m s c u r r e n t}
$$

The above method is commonly used in digital power instrumentation.

Note: Any telemetry, protection or other equipment which relies on conventional measurement techniques or the heating effect of current will not operate correctly in the presence of nonlinear loads. The consequences of under measure can be significant; overloaded cables may go undetected with the risk of catching fire. Busbars and cables may prematurely age. Fuses and circuit breakers will not offer the expected level of protection. It is therefore important that only instruments based on true rms techniques be used on power systems supplying nonlinear loads.

# 10 Telephones

On ships and offshore installations where power conductors carrying nonlinear loads and internal telephone signal cable are run in parallel, it is likely that voltages will be induced in the telephone cables. The frequency range, $5 4 0 ~ \mathrm { H z }$ to $1 2 0 0 ~ \mathrm { H z }$ $9 ^ { \mathrm { t h } }$ harmonic to $2 0 ^ { \mathrm { t h } }$ harmonic at $6 0 \ \mathrm { ~ H z }$ fundamental) can be troublesome. On four-wire systems where a large number of single-phase nonlinear loads are present (for example, large amounts of fluorescent lighting or large numbers of lighting dimmers and/or single-phase AC inverter drives on cruise liners), triplen harmonics are troublesome as they are present in all three-phase conductors and cumulatively add in the neutral conductor. The use of twisted pair cables and correct shielding/grounding, as well as correct levels of spacing and segregation should minimize potential problems.

There is also the possibility of both conducted and radiated interference above normal harmonic frequencies with telephone systems and other equipment due to variable speed drives and other nonlinear loads, especially at high carrier frequencies. EMI filters at the inputs may have to be installed on drives and other equipment to minimize the possibility of inference. However, this is often difficult when the vessel or offshore installation is based on an IT power systems (insulated neutrals), and in such instances, other measures have to be adopted.

# 11 Circuit Breakers

The vast majority of low voltage thermal-magnetic type circuit breakers utilize bi-metallic trip mechanisms which respond to the heating effect of the rms current. In the presence of nonlinear loads, the rms value of current will be higher than for linear loads of same power. Therefore, unless the current trip level is adjusted accordingly, the breaker may trip prematurely while carrying nonlinear current.

Circuit breakers are designed to interrupt the current at a zero crossover. On highly distorted supplies which may contain line notching and/or ringing, spurious “zero crossovers” may cause premature interruption of circuit breakers before they can operate correctly in the event of an overload or fault. However, in the case of a short circuit current, the magnitude of the harmonic current will be very minor in comparison to the fault current.

The original type peak-sensing, electronic-type circuit breaker responds to the peak value of fundamental current. When carrying harmonic current, this type of breaker may not operate correctly due to the peak value of nonlinear currents being higher than for respective linear loads. This type of breaker therefore may trip prematurely at relatively low levels of harmonic current.

New designs of electronic breakers include both methods of protection; peak current detection and rms current sensing. The peak detection method of protection, however, may still trip on relatively low values of peak harmonic current and trip levels therefore may have to be readjusted accordingly. Similarly, the rms-sensing measures the heating effect of the rms current (as per the conventional thermal-magnetic type) and may also have to be readjusted to prevent premature tripping on nonlinear loads.

The failure of large air circuit breakers has on occasion been attributed to harmonic distortion which delays the operation of the blow-out coils, especially in cases of high levels of distortion and low current. In these instances, the failure of the blow-out coil prolongs the arcing period and may cause re-ignition of the arc, resulting in failure of the breaker to operate correctly. Vacuum-type circuit breakers, which use magnetic blow-out systems, are less susceptible to harmonics.

# 12 Fuses

Fuse rupture under overcurrent or short-circuit conditions is based on the heating effect of the rms current according to the respective $I ^ { 2 } t$ characteristic. The higher the rms current, the faster the fuse will operate. On nonlinear loads, the rms current will be higher than for similarly-rated linear loads, therefore fuse derating may be necessary to prevent premature opening.

In addition, fuses at harmonic frequencies, suffer from skin effect and more importantly, proximity effect, resulting in non-uniform current distribution across the fuse elements, placing additional thermal stress on the device.

At fundamental frequency, the power loss in the fuses equals:

$$
P _ {N} = I _ {N} ^ {2} \cdot R _ {N} ^ {2}. \tag {3.22}
$$

where $I _ { N }$ and $R _ { N }$ are the nominal fuse rated current and resistance at the fundamental frequency.

At harmonic frequencies the resistance of the fuse will increase to a value, $R _ { H }$ therefore the nominal fuse current rating needs to be decreased to a value, $I _ { H }$ to maintain the total power losses, and hence temperature of the fuse elements, within the value at fundamental frequency, $P _ { H } .$ .

The derating factor, $F _ { P }$ can be expressed as:

$$
F _ {p} = \frac {I _ {H}}{I _ {N}} = \sqrt {\frac {R _ {N}}{R _ {H}}} \tag {3.23}
$$

where

derated value of current due to harmonics

fuse nominal current at fundamental frequency

fuse resistance due to harmonic frequencies

fuse resistance at fundamental frequency

Note: The above formula is used for general guidance only. Fuse manufacturers should be contacted for advice on the correct level derating for a particular application.

# 13 Relays

Conventional electro-mechanical control relays are rarely susceptible to harmonic problems as the operating coils are usually low voltage (e.g., 24 V) or fed via step-down transformers which attenuate the harmonics. However, where the voltage supply to conventional control relays does contain harmonic voltages or current, they may tend to operate more slowly and/or with higher pickup values and may experience early life failure due to additional heating within the coil. Solid state relays may be stressed when subjected to high levels of harmonic distortion and/or line notching thus reducing reliability.

Protection relays usually fall into three types: electro-mechanical, solid state and microprocessorbased. Electro-mechanical relays are operated via the torque proportional to the square of the flux determined by the input current. This type of relay responds to the rms value of current. Solid state relays normally respond to the peak value of the input signal. The operation of both types of relay may be affected by harmonics, although the voltage distortion, $V _ { t h d } ,$ usually has to reach levels of 10- $20 \%$ before significant operational problems occur. The exact performance will vary depending on the relay specification and the manufacture.

Microprocessor-based relays, which can use either rms current or peak values (or both) are more sophisticated and normally utilize digital filters to extract the fundamental component of the signal value. The non-fundamental components can therefore be attenuated.

# 14 Radio, Television, Audio and Video Equipment

Radios and televisions are susceptible to interference by harmonics both radiated and conducted, especially on LW and AM bands, from DC up to $1 5 0 ~ \mathrm { k H z }$ , which is above normal harmonic frequencies $5 0 ^ { \mathrm { t h } }$ harmonic at $6 0 ~ \mathrm { H z }$ fundamental is $3 \mathrm { \ k H z }$ ) and into RFI frequency ranges (radio frequency interference).

Audio and video signals can be affected on four-wire systems due to high ground-to-neutral voltages.

# 15 Capacitors

Conventional power factor correction equipment is rarely installed on ships or offshore installations. Therefore, it is not necessary to describe the interaction between harmonics and power factor correction capacitors, which are generally installed in industrial plants and commercial buildings. Fluorescent lighting, as installed across the shore-based industries, does, however, normally have capacitors fitted internally to improve the individual light fitting’s own power factor.

In general, the effects of harmonics on general capacitors can be summarized as follows:

Capacitors act as a “sink” for harmonic currents (i.e., they attract and absorb harmonics) due to the fact that their capacitive reactance decreases with frequency. The capacitors can become easily overloaded, destroying capacitors and blowing fuses where fitted.   
Capacitors (and on occasion, cable capacitance) combine with source and other inductances to form a parallel resonant circuit (see Section 9). In the presence of harmonics, the harmonics are amplified causing high, often localized, voltages and currents to flow, disrupting and/or damaging plant and equipment.   
The presence of harmonics, especially voltage harmonics, tend to increase the dielectric losses on capacitors increasing the operating temperature and reduces the reliability.

The dielectric loss can be expressed by:

$$
\sum_ {n = 1} ^ {\infty} C (\tan \delta) \omega_ {n} V _ {n} ^ {2}. \tag {3.24}
$$

where

tan δ = $R / ( 1 / \omega C )$ is the loss factor

$$
\omega_ {n} = 2 \pi f _ {n}
$$

V = rms voltage of n-th harmonic

For capacitors directly connected to the power system without series reactance, the additional thermal stress can be approximately calculated via the assistance of a special capacitor weight THD (total harmonic distortion) factor, defined using:

$$
T H D _ {C} = \frac {\sqrt {\sum_ {n = 1} ^ {N} \left(n V _ {n} ^ {2}\right)}}{V _ {1}} \tag {3.25}
$$

where

V1 = fundamental rms voltage

Vn = rms voltage of the nth harmonic

As described in Section 9, the presence of capacitors in the power system can result in series and parallel resonances leading to over-voltages and high currents, with subsequent damage to equipment and additional risks to personnel. However, as conventional capacitor-based power factor correction equipment is rarely used in the marine sector, the possibility of resonance may only exist due to fluorescent lighting integral power factor correction capacitors, cable capacitance and due to other equipment using “external” (i.e., directly connected to the power system), for example, starting capacitors on single-phase motors.

# S E C T I O N

# 4 Sources of Harmonics

Many types of electrical and electronic equipment which are adversely affected by harmonic voltages and currents also produce them in varying degrees, due to, for example, semiconductor power conversion or magnetic saturation in the case of transformers.

# 1 Distribution Systems with Single-phase Nonlinear Loads

# 1.1 Three-wire Distribution Systems

Three-wire, distribution systems (i.e., IT power systems with insulated neutrals) are one of the common types of systems used on vessels for distribution due to the ease of locating and rectifying ground faults and for security of supply of essential equipment during ground faults.

In three-wire systems, unlike the four-wire system detailed below, no “zero sequence harmonics” should exist. If they do exist, however, their phase sequence is determined by the phase angle of the $3 ^ { \mathrm { r d } }$ harmonic current (and other triplens) and its current magnitude in each of the three phases. In a three-wire balanced system, therefore, the $3 ^ { \mathrm { r d } }$ harmonics usually cancel out.

However, depending on the type and nature of the nonlinear loads(s), other harmonic currents will be present in the system, usually in the order $5 ^ { \mathrm { t h } }$ , $7 ^ { \mathrm { t h } }$ , $1 1 ^ { \mathrm { t h } }$ , $1 3 ^ { \mathrm { t h } }$ … and perhaps some uncharacteristic harmonics, including DC and even orders. These harmonics will be very similar to those described for four-wire systems but with no $3 ^ { \mathrm { r d } }$ harmonic present.

# 1.2 Four-wire Distribution Systems

On large passenger liners, it is now relatively common to use four-wire systems [i.e., three-phase and neutral (grounded or insulated)] for “domestic” supplies, including lighting, in order to minimize inconvenience to passengers in the event of a ground fault. Large or multiple single-phase nonlinear loads can be problematic on four-wire systems due to significant triplen harmonics caused by their cumulative addition in the neutral conductor, resulting in:

x Overloaded and overheating neutral conductors   
x Overheated delta winding in distribution transformers   
x High ground-to-neutral voltages   
x Distortion of voltage waveform (flat topping)   
x Poor power factor

As can be seen in Section 4, Figure 1, the phase current’s return path is via the neutral conductor. In a four-wire distribution system with only linear loads, the 120-degree phase shift between linear load currents results in their balanced portions canceling out in the neutral.

However, in distribution systems with nonlinear or mixed linear and nonlinear loads, the current on one phase will not have a “pulse” on either of the two other phases with which to cancel with (see Section 4, Figure 2). These current pulses add together in the neutral conductor, which can carry up to $1 7 3 \%$ of phase current, even if all phases are completely balanced. The frequency of the neutral current is predominately $1 8 0 \mathrm { H z }$ (for $6 \bar { 0 } \ : \mathrm { H z }$ supplies) and mainly $3 ^ { \mathrm { r d } }$ harmonic and other triplens.

![](images/388787ae428c7a9673d7ef66b4941d1278c11979abb1fedd57f4d6270b4b599c.jpg)  
FIGURE 1 Four-wire System Linear Phase Currents Return via Neutral Conductor where Balanced Phase Current Cancel Out

![](images/72d015bc6918a067dd87de0ef9ea12f1aa62a2eb076bbd14563af16c63fd55b9.jpg)  
FIGURE 2 Triplen Harmonics Add Up Cumulatively in Neutral Conductors with Single-phase Nonlinear Loads in Four-wire System

Section 4, Figure 3 illustrates an example of a neutral current waveform on a four-wire installation with a large number of single-phase nonlinear loads.

![](images/0d0a76d35354c03528e3a02eec437d10e97beead1644732c3aa2653ef9a44822.jpg)  
FIGURE 3 Neutral Current due to Triplen Harmonics (150 Hz for 50 Hz Supply) on Four-wire System

Sectoin 4, Figure 4 displays the harmonic spectrum associated with the four-wire system neutral current waveform illustrated in Section 4, Figure 3. Note the presence of $3 ^ { \mathrm { r d } }$ and $9 ^ { \mathrm { t h } }$ (triplen harmonics) and relatively low level of fundamental current.

![](images/9a4ae5b1179ec11bbc57dcb3ed334d1658be9a78a6d8fb587f54817d08afa285.jpg)  
FIGURE 4 Harmonic Spectrum Associated with Neutral Current Waveform Shown in Figure 3

The importance of large numbers of single-phase, nonlinear loads is often underestimated. Large vessels such as cruise ships have large hotel loads often comprising large number of televisions, computers, lighting dimmers, UPS systems, fluorescent lighting, small single-phase cooling fan variable frequency drives and other nonlinear loads. This produces considerable harmonic currents at characteristic frequencies.

On non-passenger vessels, the amount of four-wire (single-phase) nonlinear load can also be significant. The low voltage supplies, fed via distribution transformers, have relatively high source impedance resulting in significant distortion of the voltage waveform. The low voltage supplies are important since the sensitive equipment is connected to it. Appropriate harmonic mitigation may be necessary on distribution systems to reduce the voltage distortion to within permissible levels, thus maintaining the safety of the vessel and the operational integrity and reliability of connected equipment.

# 2 Single-phase Nonlinear Loads

Computer-based equipment and fluorescent lighting represent substantial loading on marine and offshore four-wire distribution systems, especially on larger vessels, such as cruise liners.

Other significant nonlinear single-phase loads include single-phase variable speed drives, lighting dimmers, UPS systems, televisions and video recorders. In small numbers, these types of loads usually are not problematic. However, on large cruise liners, these loads can be significant, creating substantial voltage distortion on the four-wire distribution system and with possible additional overloading of the neutral conductors.

# 2.1 Computer-based Equipment

The majority of computer-based equipment, for example navigation and control systems, have switched mode power supply (SMPS) units similar to that depicted in Section 4, Figure 5, below.

![](images/1b1e2cd59b0cf994f282061342e9924c9b1c3bd3da315c5a757e7b689ec9cab2.jpg)  
FIGURE 5 Typical Switched Mode Power Supply for Computer Based Equipment

As described in Section 2, the SMPS unit only draws current from the supply when the rectified voltage is greater than the DC bus voltage. Typical resultant current and voltage waveforms are illustrated in Section 4, Figure 6 with a typical harmonic current spectrum illustrated in Section 4, Figure 7.

![](images/ca9eba419f185c87eddf26499a9850b04e3fbccad62e7f42a17732670dbd7d42.jpg)  
FIGURE 6 Typical Voltage and Current Waveforms Associated with a Switched Mode Power Supply

![](images/8c16633feb331e4911e629cd19d73973d2d5369ab82f4f87ec435a5e3437221f.jpg)  
FIGURE 7 Harmonic Current Spectrum of Typical Switched Mode Power Supply $I _ { t h d }$ is $128 \%$

As can be seen from Section 4, Figure 7, significant odd zero sequence triplen harmonics $( 3 ^ { \mathrm { r d } } , 9 ^ { \mathrm { t h } } 1 5 ^ { \mathrm { t h } } $ , $2 1 ^ { \mathrm { s t } } )$ harmonics are generated, which add due to other nonlinear single-phase loads in the neutral conductor in four-wire systems, as illustrated in Section 4, Figure 8. Note that the frequency of the neutral current depicted in Section 4, Figure 8 is $1 8 0 \mathrm { H z }$ ( $6 0 \mathrm { H z }$ fundamental).

![](images/200594ef0a8512e55702b10dc51e1a9c3fbf5674143852238019648eac777bdd.jpg)  
FIGURE 8 Typical Neutral Current due to Triplen Harmonics in Connected Loads on a Four-wire System

# 2.2 Fluorescent Lighting

Fluorescent lighting represents substantial loading on marine and offshore four-wire distribution systems, especially larger vessels such as cruise liners.

Fluorescent lights are classed as discharge lamps as they need a “ballast” to initiate the high voltage between the two electrodes in order to facilitate current flow. Once the arc is initiated and the current increases, the voltage reduces. After, initiating the high voltage, the ballast also provides a measure of current limiting for the light fitting.

The total harmonic current distortion $( I _ { t h d } )$ and harmonic current spectrum of fluorescent lighting is dependent on the type of ballast employed. Two types of ballast are in use; the iron cored magnetic ballast, essentially a transformer combined with a capacitor, and the newer electronic ballast. The latter utilizes a switched mode power supply to convert the fundamental frequency to a higher frequency, usually around $2 5 { \mathrm { - } } 4 0 \ \mathrm { k H z }$ . A small inductor is also used in the electronic type to limit the current.

As an example, for comparison purposes, the phase voltage, phase current and neutral current waveforms associated with distribution panels supplying wholly fluorescent lighting, using both magnetic and electronic ballasts are illustrated below.

Section 4, Figures 9 and 10, below, depict an electrical load wholly comprising fluorescent lighting with magnetic ballasts and T-12 lamps. The total harmonic current distortion $( I _ { t h d } )$ for phase currents was $1 3 . 9 \%$ and for the neutral current, $1 4 1 . 3 \%$

![](images/d8846bb0ac05b28e437d709c5f85694f244e70680c9ae127b2a2e7b26e0575c0.jpg)  
FIGURE 9 Waveforms for Lighting Panel Comprising Fluorescent Lighting with Magnetic Ballasts and T-12 Lamps

FIGURE 10 Neutral Current Waveform on Distribution Panel with Fluorescent Lighting with Magnetic Ballasts and T-12 Lamps on a Four-wire System   
![](images/62eeaeb09312edda6fb09974adc39637c0218816eb650bee19fce497c18e91ae.jpg)  
Similarly, Section 4, Figures 11 and 12, below, depict the same lighting panel with electrical load wholly comprising fluorescent lighting with electronic ballasts and T-8 lamps. The total harmonic current distortion $( I _ { t h d } )$ for phase currents was $1 7 . 2 \%$ and for the neutral current, $8 5 . 3 \%$ .

![](images/b54afa537eeaf7309081777a1cdc6ddfdd65a1c56f413d54ce4e4f94f59315bd.jpg)  
FIGURE 11 Same Lighting Panel as per Figure 9, but with Electronic Ballasts (Instead of Magnetic Types) and T-8 Lamps

![](images/7ee5b4630328323601222965bceebf1b3a348f24a31bd30e7666724faea62e2d.jpg)  
FIGURE 12 Neutral Current Waveform on Same Fluorescent Lighting Panel as Figure 10, but with Electronic Ballasts and T-8 Lamps on Four-wire System

As can be seen with reference to Section 4, Figures 13 and 14, fluorescent lighting with electronic ballast have significantly less triplen harmonics $( 3 ^ { \mathrm { r d } } , 9 ^ { \mathrm { t h } } . . . )$ than magnetic types, which suggests that the additive effect in the neutral conductor discussed earlier will be significantly reduced. However, as can also be seen, electronic ballasts have an increased harmonic spectrum up to around the $3 3 ^ { \mathrm { r d } }$ harmonic. The resultant $I _ { t h d }$ for the phase currents for magnetic and electronic ballasts were $1 2 . 8 \%$ and $1 6 . 3 \%$ , respectively. In the neutral conductors, the difference in $I _ { t h d }$ for magnetic and electronic ballasts was more significant, at $1 7 1 . 2 \%$ and $44 \%$ , respectively. The use of electronic ballast would, from this example, significantly reduce the triplen harmonics produced and carried by the neutral conductor although would slightly increase the phase current distortion.

![](images/aa2f15740ce48b4ebc1c385d2e3419f7655018c02ef367a7ceb5a95ecfcc8301.jpg)  
FIGURE 13   
Comparison of Phase Current Harmonic Spectrum for Magnetic and Electronic Ballasts for Typical Fluorescent Lighting Distribution Panel $I _ { t h d }$ was $12 . 8 \%$ and $1 6 . 3 \%$ , Respectively   
FIGURE 14

![](images/2a2111428bca57065f1390fef94c1146338b7271d7fe9800cdd918740fec28c9.jpg)  
Comparison of Neutral Current Harmonic Spectrum for Magnetic and Electronic Ballasts for Typical Fluorescent Lighting Distribution Panel $I _ { t h d }$ was 171. $28 \%$ and $44 \%$ , Respectively

# 2.3 Televisions

Section 4, Figures 15 and 16 illustrate the current waveform and harmonic current spectrum, respectively, from a typical television.

![](images/544aeb7a8a4f82ccb4c852bed4a1f31c0fe17814befc6515779e1f775e002c20.jpg)  
FIGURE 15 Television – Typical Current Waveform

![](images/8125e79585ad0b28c71da8bc5d98595416fce6c214b88ce80b99af6b5f76e78a.jpg)  
FIGURE 16 Television – Typical Harmonic Current Spectrum

# 2.4 Single-phase AC PWM Drives

Single-phase AC drives, commonly used up to $5 \mathrm { H P } / 3 . 7 \mathrm { k W }$ for applications such as cabin fan drives, usually have no additional reactance fitted, resulting in an $I _ { t h d }$ up to $1 3 5 \%$ , as can be appreciated with reference to Section 4, Figures 17 and 18. Note that these results are similar to those produced by single-phase UPS. Section 4, Figure 18 depicts a large triplen component. On large installations, this would result in high neutral currents (as the triplens are additive).

![](images/74b1cd0548f8cbb4448136c9ebde801501df37eccfab456cd96bd0f6009f8b8b.jpg)  
FIGURE 17 Single-phase AC PWM Drive – Typical $I _ { t h d }$ is $135 \%$

![](images/e507c0332fe5087a79971911059116376a3c396054c71ad4ea55170796fc78fd.jpg)  
FIGURE 18 Single-phase AC PWM Drive Current Spectrum

# 3 Three-phase Nonlinear Loads

Onboard ship or on offshore installations, a common type of three-phase nonlinear load is variable speed drives, either AC or DC. UPS systems and shaft generators both also produce harmonic currents. The harmonics produced by these nonlinear items will be discussed in Subsections 4/3 and 4/4.

“Linear” equipment, such as rotating machines (generators and motors), produce harmonics, although relatively minor in magnitude compared to nonlinear loads. In addition, transformers also produce harmonics. These items of equipment will be mentioned briefly in Subsections $4 / 1$ and $4 / 2$ .

# 3.1 DC SCR drives

Up until some 5-10 years ago, DC SCR drives were a common choice for low to medium power electrical variable speed duties on ships, drilling rigs and offshore installations. Common applications included windlasses, winches, propulsion motors, draw-works motors, mud pumps, cranes, etc.

As can be seen with reference to Section 4, Figure 19, below; the DC converter comprises six SCR drives (thyristors) in a full wave bridge configuration with a separately-excited shunt field fed by a full wave diode bridge (note – this can be single- or two-phase supplies). DC motors are available in various designs, including series-wound, shunt-wound and a number of derivatives of compoundwound; the application of which specific type is dependent on the necessary speed/torque characteristic of the given duty. However, the configuration of the SCR drive converter is the same for each type.

![](images/99ed43872f24719444337147f06d2df55ef322cfca187e15f18983860af37e1c.jpg)  
FIGURE 19 Typical 6-Pulse DC SCR Drive with Shunt-wound DC Motor

The above illustration (Section 4, Figure 19) depicts a shunt-wound motor with separately-excited field, one of the common types of DC motor in general use. $L _ { a }$ and $R _ { a }$ are the armature inductance and resistance, respectively, and similarly, $L _ { f }$ and $R _ { f }$ are the shunt field inductance and resistance.

With the shunt field current at constant maximum value, (hence maximum field flux), the speed (and torque) of the DC motor can be controlled infinitely by varying the mean output voltage from the DC converters applied to the DC motor armature. This is achieved by modifying the delay angle of the SCRs over a 120-degree angle (the first 30 deg and final 30 deg of the theoretical 180-degree conduction period cannot be utilized for commutation reasons).

Thus, the motor speed can be controlled up to “base speed” (based on maximum field flux) using “armature voltage control”. In this region, the power of the motor is directly proportional to the applied voltage (less armature reaction), and hence speed. This is termed the “constant torque region”, as the torque is constant while the power rises in direct proportion to speed.

Speed above “base speed” is achievable by maintaining the armature voltage at a maximum value and then reducing the shunt field current, hence flux. Therefore, the use of a variable SCR-based field weakening controller is necessary. Operation above base speed is in the constant power region since the power is constant, but the available flux hence torque is inversely proportional to speed. Section 4, Figure 20, below, illustrates the concepts of constant torque and constant power.

Note: This concept can also be applied to AC PWM drives and induction motors (see 4/3.2 on AC PWM drives).

![](images/251a9e7a7a9d3cf2f6b507dffe2888f77023ccdbe6d8fc10efcd02ae2a5ebbfe.jpg)  
FIGURE 20 Concept of “Constant Torque” and “Constant Power” with DC Shunt-wound Motors

DC motors with single converters can drive in the forward direction and need either field reversal or armature voltage reversal in order to drive in the reverse direction. However, if the DC motor is supplying an overhauling load (i.e., one that feeds converted kinetic energy into the drive) the load current will remain in the same direction but the DC voltage will be reversed. In these circumstances, the DC converter voltage opposes the DC voltage back EMF. The DC motor voltage is therefore limited to a maximum conduction angle of 90 degrees, thus maintaining a stable area of the operation without the potential of losing control of the DC motor.

They cannot brake regeneratively (i.e., dump the excess electrical energy which has been converted from kinetic energy during the braking process into the supply) due to the blocking action of the SCRs, however, DC motors fitted with dual converters (Section 4, Figure 21) are capable of “four quadrant operation” [i.e., motoring and braking (generating)] in both directions of rotation as illustrated in Section 4, Figure 22.

In the four quadrant DC drive system depicted in Section 4, Figure 21, “commutating reactors” have been used to reduce both the line notching and attenuate the harmonic currents. These are recommended for all DC drives. Most DC motors have sufficient inherent inductance to facilitate rapid current reversal during braking and reversal. However, for applications where minimizing noise levels is important (e.g., fishery survey vessels), additional DC side inductors are often used.

![](images/67ce4e4e987c9a76b7da821fa19124d98c94dd4070b5a6d3127a68da60ef355b.jpg)  
FIGURE 21 Typical Dual Converter for DC Shunt-wound Motor

![](images/126cee2f76b7358a5c39aefb6b9a047c7918f4d80f1976d74c0a4bf9d1174561.jpg)  
FIGURE 22 Concept of “Four Quadrant Control” for DC Motors and Dual Converters

The harmonic currents produced by DC SCR drives are a function of the pulse number (“pulse number $\pm \nobreakspace 1 \nobreakspace ^ { \circ } \nobreakspace$ , so for 6-pulse, $5 ^ { \mathrm { t h } }$ , 7th, $1 1 ^ { \mathrm { t h } }$ , $1 3 ^ { \mathrm { t h } } . . . $ ) and the delay angle of the SCRs at a particular operating point as described in Section 6. The harmonic currents will be at a maximum value at full load. A typical current waveform and harmonic current spectrum at rated load are illustrated in Section 4, Figure 23 and 24, respectively.

![](images/06e7339f459fa6bdafee820597efbfb56a3fcb4bfcfc46eb28219d07e7c16fe6.jpg)  
FIGURE 23 Typical 6-Pulse DC SCR Drive Current Waveform at $100 \%$ Load

![](images/b44c92d4138d19ba2ef7025892512cf335931bac73d0c22776756fdac727114d.jpg)  
FIGURE 24 Harmonic Current Spectrum of Typical 6-Pulse DC SCR Drive at Rated Load

For the relationship between the magnitude of the harmonic currents produced and the drive loading, please refer to Section 6, “The Effect of Loading on Harmonic Distortion”. Note that as the drive input rectifier is SCR based, the input displacement power factor will vary as a function of the delay angle of the SCRs.

Due to the use of phase-controlled SCRs (thyristors) line notching will also be present. For further information on line notching, please refer to Section 2).

# 3.2 AC PWM drives

AC voltage-fed pulse width modulated (PWM) drives are a commom type of electrical variable drive used today in marine, offshore and general industrial applications for low to medium power applications.

The benefit of being able to control standard squirrel cage induction motors was significant. However, squirrel cage induction motors are generally designed for pure sinusoidal supplies, and the effects of the often harmonically-rich output waveforms had to be taken into account with regard to the level of motor thermal derating, according to the speed range driven load torque characteristic, high level of dv/dt on motor winding insulation and torque production at low frequencies and bearing currents (more applicable on large machines). Rotor design was also an important factor, as double cage and deep bar rotors (e.g., NEMA C and D designs) tended to significantly rise in temperature when on variable frequency supplies due to considerably increased iron losses, copper losses and skin effect; in the early days of PWM drives (mid 1980s). Some large motors had to be fitted with copper rotors due to the increased heating. With hot rotors, bearing lubrication was also a problem. Often special high temperature grease was necessary.

However, the motor industry took up the challenges in the mid 1990s and currently produces squirrel cage motors more suitable for variable frequency drive operation, subject of course to the necessary thermal derating (TEFC squirrel cage motors in constant torque applications usually still need to be derated according to the speed range). Motors on quadratic duties (centrifugal pumps and fans) rarely need to be derated. Presently, motor cooling options (for large motors) include forced cooling and water cooling, reducing the need for derating, and thereby reducing the necessary motor frame size and rating of the AC PWM drive.

A block diagram configuration of a typical AC PWM drive is shown in Section 4, Figure 25, below.

![](images/0e0bb36a064257bdf5c29a656cb67b98bfa022eabc49c032b52b7cdddf3809fa.jpg)  
FIGURE 25 Typical AC PWM Drive Block Diagram

With reference to Section 4, Figure 25; the incoming three-phase supply is rectified by the input (or “front end”) rectifier. In this instance, a diode full wave bridge has been used, but in larger drives (i.e., above $4 0 \mathrm { \ H P } / 3 0 \mathrm { \ k W }$ , SCR “pre-charge” front ends are used to “soft start” the DC bus to minimize any inrush current. Once the DC bus is fully charged, the SCRs act as diodes (i.e., they are no longer controlled).

The resultant voltage output from the input bridge is in the form of DC voltage with six peaks; one peak for each of the positive and negative half cycles of the rectified three-phase input waveform, thus the term “6-pulse drive”. Similarly, a single-phase AC PWM would be “2-pulse” due to having one rectified peak per positive and negative half cycle. After rectification, the DC voltage is smoothed by the action of the DC bus capacitors.

An AC PWM drive operates similarly to a switched mode power supply. Power is only drawn from the mains supply when the DC bus voltages falls below that of rectified AC mains level, hence the pulse nature of the input current, as shown in Section 4, Figure 26. The “intermediate” (i.e., between the input and output bridges) DC bus serves as a reservoir of energy, only being recharged as necessary. The DC bus voltage is in the order of $1 . 3 5 \times$ the AC L-L rms voltage level (e.g., for $4 8 0 \mathrm { V }$ AC mains the DC bus would be in the order of 648 V DC).

![](images/35c437577eb494bcfef42f5d5bba27af1347d272bcd727cd301aabfa83678852.jpg)  
FIGURE 26 Pulsed Nature of AC PWM Drive Input Current

While the operation of the “front end” of an AC PWM drive is relatively simple, the operation of the output (or “inverter”) bridge is more complex, especially from the control aspect. As can be seen from Section 4, Figure 25, the input bridge rectifies the three-phase voltage supply which is further smoothed by the DC bus capacitors, which act as a power storage unit. The DC bus voltage is maintained at a constant level. The inverter bridge, usually comprises insulated gate bipolar transistors (IGBTs), controls both the output voltage and the output frequency. A constant voltage/frequency (V/F) is needed to maintain the desired level of torque in the driven induction motor.

Section 4, Figure 27, below, depicts a typical IGBT out rectifier. The diodes across the IGBT devices are termed “flywheel diodes” and are in the circuit to assist commutation (i.e., the transfer of current from one device to another).

![](images/de56be2bb8711b32416a8d7d2277ace7c9f4119b75c69e54b9c992e0569cb76e.jpg)  
FIGURE 27 Typical AC PWM Drive Output (Inverter) Bridge Configuration

Pulse width modulation control strategies were introduced in the early 1980s to overcome the heating and torque pulsations of the then “square wave drives” (also known as “quasi-square wave” or “six step drives”). The purpose was to reduce the output harmonics, especially the low order harmonics, to the motor. Since that time, the various PWM strategies have been improved significantly such that present series of drives usually have output current waveforms (i.e., not the output voltage) which are relatively sinusoidal. This was achieved due to a combination of PWM techniques and advances in fast power semiconductors such as IGBTs.

The basic principle of pulse width modulation can be seen with reference to Section 4, Figure 28, below.

![](images/4fb33fbb91d5e8082a7add5365d7416787f82ee24767e2100caf0a6d3479c041.jpg)  
FIGURE 28 Basic Principle of Pulse Width Modulation

As illustrated in Section 4, Figure 28(a), a saw-tooth waveform (shown as “triangle wave”) is produced by the control system based on the desired switching frequency. This is compared to a sinusoidal reference waveform (shown as “reference wave”) whose frequency and output are proportional to the desired output waveform.

In Section 4, Figure 28(b), the voltage $V _ { A N }$ is switched high whenever the sinusoidal reference voltage is larger than the triangular waveform. Similarly, in Section 4, Figure 28(c), $V _ { B N }$ is controlled in a similar manner by the triangular waveform, but in this instance, the sinusoidal reference waveform is shifted by 180 degrees. The result is a phase-to-phase voltage waveform as depicted by Section 4, Figure 28(d), which is the difference between waveforms $V _ { A N }$ and $V _ { B N } ,$ which is a series of voltage pulses whose width is related to the magnitude of the sinusoidal reference waveform at a particular instance in time. It is the rms value of this voltage which the motor “sees”. If this rms voltage was superimposed on the waveform in Section 4, Figure 28(d), the voltage would be seen to be approximately sinusoidal with zero crossovers as per the PWM waveform. The current which the motor “sees” also approximates a sine wave in nature.

In 4/3.1 on DC SCR drives, the possibility of operating the DC motor above base speed was described. It is also possible to operate an AC PWM drive and squirrel cage induction motor similarly, as will be shown in Section 4, Figures 29a and b, below.

Up to base speed (i.e., the motor’s natural synchronous speed) the AC drive maintains a constant voltage/frequency ratio (e.g., at $50 \%$ output frequency on $4 8 0 \ \mathrm { V }$ supplies, the V/F ratio would be approximately $2 4 0 \ \mathrm { V } / 3 0 \ \mathrm { H z } )$ ). Above base speed, it is usually not possible to increase the output voltage, therefore only the frequency is increased. However, similar to DC drives, the torque availability with AC PWM drives reduces with increased output frequency above base speed and limits the maximum frequency achievable. The effect of high speed on the bearings and lubrication are also often a factor regarding the maximum frequency of operation.

![](images/63fc6890d66edf0408b2f287963f29b19953a8b33d91cfcc893788a4c8bdb8f9.jpg)  
FIGURE 29a   
AC Motor/PWM Drives Standard Speed/Torque Characteristics

![](images/791f658391ef74d5d315e932ad11e66b65109aa2f02bf9bd50e13b618c432984.jpg)  
FIGURE 29b AC Motor/PWM Drives Standard Speed/Power Characteristics

As can be seen in Section 4, Figure 29a, the motor has to be thermally derated for constant torque duty. It is possible, however, to use motors with higher pole numbers (e.g., a 6-pole motor operated at $9 { - } 9 0 ~ \mathrm { H z }$ in order to obtain a 10:1 speed range at constant torque plus $40 \%$ higher starting torque) or with non-standard winding configurations (e.g., 5-87 Hz on $5 0 ~ \mathrm { H z }$ mains for 17:1 speed range at constant torque).

The harmonic currents produced by AC PWM drives are dependent on the pulse number (with 6-pulse drives being the most popular) and whether any additional reactance has been installed in the drive (see Section 10, “Mitigation of Harmonics”). Additional reactance, either in the AC line or in the DC bus serves additional purposes other than harmonic attenuation and is commonly fitted to drives above $1 0 \ \mathrm { \ H P }$ $( 7 . 5 \ \mathrm { k W } )$ . Section 4, Figure 30, below, illustrates the input current and voltage waveforms from a 150 HP (110 kW) AC PWM drive with $3 \%$ DC bus reactance running at rated load. The total harmonic current distortion was measured at $3 9 . 2 3 \%$ (without the DC bus reactor the $I _ { t h d }$ would be approximately $67 \%$ ). Section 4, Figure 31 depicts the harmonic current spectrum associated with this particular drive.

Information on how the harmonic current varies with load can be found in Section 6.

Note: Other AC voltage-fed drive output waveform control technologies exist, such as “field vector orientation” (i.e., “vector control”) and “direct torque control” (DTC), both of which provide enhanced motor performance, akin to flux control in DC motors. These types are also used in marine and offshore applications.

However, as the input bridge and DC bus architecture of these drives are almost identical to that of PWM drives, the harmonic currents and input waveforms will be similar to those described in 4/3.2 on AC PWM drives.

![](images/78493492cd59697ab2ba75f0b4fdc036a24c73d61bf4b39abaa9ebeed7e7e092.jpg)  
FIGURE 30 Input Current – 150 HP AC PWM Drive with $3 \%$ DC Bus Reactor – $I _ { t h d } = 3 9 . 2 3 \%$

![](images/73f2ec6bf1eb518abd7e6f33eb10b5a7a0d8aef25ab97e7eb38eb0fb4162e0b4.jpg)  
FIGURE 31 Harmonic Current Spectrum of 150 HP AC PWM Drive with $3 \%$ DC Bus Reactor – $I _ { t h d } = 3 9 . 2 3 \%$

# 3.3 AC Cycloconverter Drives

Cycloconverters are a common form of electrical variable speed drive in the higher power range and, as such, are used for main propulsion drives.

Unlike other forms of AC drives, for example AC PWM drives and load commutated inverters (LCI), both of which have an intermediate stage (i.e., DC bus) to facilitate dual conversion [AC to DC and DC to AC], the cycloconverter is a direct conversion drive which converts one frequency to another without the need for an intermediate stage. Cycloconverters have been in operation since the 1930s (then based on mercury arc rectifiers) on applications such as railway transportation, steel works and coal mine winders.

Cycloconverters are characterized by having a maximum output frequency of $33 \%$ of the input frequency, which often negates the use of gearboxes for final speed reduction with the ability to provide full four-quadrant control with high torque and high dynamic response. When used to control the rotor of a wound rotor induction motor, the cycloconverter is termed a “static Scherbius” drive.

In power conversion terms, the operation of a cycloconverter is complex with both positive and negative bridges necessary per motor phase. In order to briefly describe the operation of cycloconverters, it is necessary to consider the operation of a single-phase-to-single-phase device with full wave rectifiers and a resistive load, as shown in Section 4, Figure 32, below:

![](images/b13272358ca720f479c821d395dbdd3f0d274a73f5aec99b60246f35db092bbf.jpg)  
FIGURE 32 Single-phase-to-Single-phase Cycloconverter

As illustrated in Section 4, Figure 32, $V _ { s }$ is the input voltage at frequency $f _ { 1 }$ . In this example, it is assumed that the SCRs are acting as diodes with $\alpha = 0$ degrees firing angle. Note that $\alpha _ { p }$ and $\alpha _ { n }$ are termed the firing angles of the positive and negative bridges, respectively.

Refer to Section 4, Figure 33(b), below. In order to achieve, for example, an output frequency of $2 5 \%$ of the input frequency (e.g., $1 5 \ : \mathrm { H z }$ output for an input of $6 0 \mathrm { H z }$ ) the positive bridge supplies current to the load for the first two cycles of $V _ { s }$ as it rectifies the incoming AC voltage $V _ { s }$ into four positive half cycles as illustrated.

![](images/d17acf972c729ab19a386cf815cf7d6b0dc506c42e17750c49c4de4e9eb06727.jpg)  
FIGURE 33 Waveforms for Single-phase-to-Single-phase Conversion

During the next two cycles of $V _ { s }$ [Section 4, Figure 33(c)], the negative converter supplies current to the load in the reverse direction. (Note that the current waveform is not depicted in Section 4, Figure 33 as being wholly resistive. It will have the same wave-shape as the voltage). In the configuration above, when one bridge is operating, the other is disabled or “blocked”.

As can be seen above, the frequency of the output voltage, $V _ { o } ,$ in Section 4, Figure 33(b) is $2 5 \%$ of the input voltage $V _ { s }$ (i.e., $f _ { o } / f _ { 1 } = 1 \bar { / 4 } _ { , }$ ). The output frequency, $f _ { o } ,$ can be varied by adjusting the number of cycles the positive and negative converters operate.

Note that cycloconverters can be used for “step up” operation as well as “step down” operation, although the latter is considerably more common.

As can be seen in the above example, the output frequency can be varied (i.e., up to a maximum of one-third the input frequency). The single-phase-single-phase cycloconverter can also supply a voltage based on firing angle, $\alpha .$ . The DC output of each bridge would be:

$$
V _ {d} = \frac {2 \sqrt {2}}{\pi} V \cos \alpha \tag {4.1}
$$

where

$$
V = \text {i n p u t r m s v o l t a g e}
$$

$$
V _ {d} = \mathrm {D C o u t p u t v o l t a g e}
$$

Note: The DC output voltage per half cycle is shown dotted in Section 4, Figure 33(d).

The peak fundamental output voltage will be:

$$
v _ {0 _ {1}} (t) = \frac {4}{\pi} \frac {2 \sqrt {2}}{\pi} V \cos \alpha \tag {4.2}
$$

where

$$
V = \text {i n p u t r m s v o l t a g e}
$$

$$
V _ {0} = \text {p e a k f u n d a m e n t a l v o l t a g e}
$$

Therefore, it follows that the fundamental output voltage $\nu _ { 0 }$ is dependent on firing angle, $\alpha$ . For $\alpha = 0$ degrees:

$$
V _ {0 _ {1}} = V _ {d o} \times 1 = V _ {d o} \text {w h e r e} v _ {0 _ {1}} = \frac {4}{\pi} \frac {2 \sqrt {2}}{\pi} V \cos \alpha .
$$

For example, if $\alpha$ is increased to $\pi 3$ radians, as illustrated in Section 4, Figure 33(d), then output voltage $V _ { 0 _ { 1 } } = V _ { d o } 0 . 5$ .

The above is a simplistic explanation regarding the basic theory of cycloconverters. Please note that operation with a constant firing angle, $\alpha ,$ results in a very crude output waveform with considerable harmonic content. In reality, the square waves shown in Section 4, Figure 33(b) and (c) would be modified to approximate a sine wave by sinusoidally modulating the firing angle $\alpha ,$ as illustrated in Section 4, Figure 33(d). This would serve to reduce the output harmonics and supply a better waveshape to the motor.

Section 4, Figure 34 shows a typical three-phase cycloconverter with three bridges, each phase displaced by $2 \pi / 3$ radians (120 degrees).

As mentioned previously, the cycloconverter can operate in all four quadrants. Both positive and negative bridges can therefore supply voltages of either positive or negative polarity, depending on the necessary duty at any instance in time. It must be noted the positive bridge can only supply positive current and the negative bridge can only supply negative current, and that consequently, the polarity of the current determines which converter supplies the load at that instance. When the polarity of the load current changes, the respective bridge previously supplying the current is disabled and the other bridge is enabled in order to reverse the current (e.g., from rectification to inversion). However, the motor needs the magnitude of the fundamental rms voltage to be continuous at all times, so during current reversal, the average rms voltage supplied by both bridges are “forced” to be of the same magnitude in order to prevent voltage jumps and current “spikes” occurring.

Section 4, Figure 34 shows a typical 6-pulse cycloconverter connected to a star-connected induction motor. However, cycloconverters can be used with both synchronous and squirrel cage induction machines. There are certain advantages, however, when operating with synchronous motors due to the machine’s output power factor characteristics. Cycloconverters, whose input displacement power factor is always lagging, can supply leading, lagging or unity power factor loads. The characteristic that a synchronous motor can draw variable levels of power factor from a converter is ideally suited to the cycloconverters, whereas induction motors can only draw lagging current.

The output voltages produced by cycloconverters have a high harmonic content which can be reduced by careful systemization of the bridge(s) firing angle algorithms. In addition, AC synchronous and squirrel cage induction motors normally filter (i.e., absorb) the majority of higher order harmonics and, in addition, attenuate a measure of lower order harmonics due to their inherent leakage reactance.

![](images/81d5f9a9530ca60902e7cdfa1f8cf3f637978586744cff8a044c913a471bec32.jpg)  
FIGURE 34 Three-phase 6-Pulse Cycloconverter

Since current reversal is necessary, standard cycloconverters are usually designed in two formats; “blocking mode” or “circulating current mode” converters. In the “blocking mode” cycloconverters, as the name implies, one bridge is disabled or “blocked” while the other is operating. If both bridges were operating simultaneously, a short circuit would occur across the supply. To avoid this, an “intergroup reactor” can be connected between the two bridges (per phase), as shown by Section 4, Figure 35, below, to form a “circulating current mode” converter.

Unlike the “blocking mode” converter; in the “circulating current mode” converter, both bridges are enabled during current reversal, thus allowing a circulating current to flow between the bridges and the load. This circulating current is unidirectional due to the blocking action of the other SCR bridge. Most circulating current cycloconverters operate in a circulating current mode, with both bridges enabled when running.

There advantages and disadvantages of both types. Blocking mode converters do not need large intergroup reactors and are therefore physically smaller and less expensive that the circulating current type. In the blocking mode type, when the current decays to zero, awaiting reversal, both bridges (per phase) are disabled. During this delay time period, the current distorts the voltage and current waveforms. It is therefore necessary to program complex harmonic elimination patterns into the firing control software to minimize the level of distortion. The current reversal process also introduces added complexity into the firing and protection control systems. However, the blocking mode converter is more efficient (as only one bridge operates at any one time).

![](images/383832ad9dd578327d9b035120a8d6fc52555666ae0b614bba874dd41a175aa0.jpg)  
FIGURE 35 Simplified Connection of Intergroup Reactor on One Phase of Circulating Current Cycloconverters

The waveforms associated with blocking mode cycloconverters are shown below in Section 4, Figure 36.

FIGURE 36   
Waveforms for Blocking Mode Cycloconverters   
![](images/c8bc45f27939f850e01b099e2d318ed2f41f8d071854e689dbd61e8245647512.jpg)  
(a) Positive bridge output voltage   
(b) Negative bridge output voltage   
(c) Load (motor) voltage

In the circulating current cycloconverters, both bridges operate simultaneously with fundamental rms output voltages of similar magnitudes. When one bridge is converting (AC-DC), the other is inverting (DC-AC). Note that if the output voltage from both bridges were sinusoidal, however, there would be zero circulating current as the instantaneous potential difference between the two bridges would be zero. In reality, however, this is not the case, and the intergroup reactor is necessary to facilitate operation. The waveforms associated with a circulating current cycloconverter and also the voltage waveform across the intergroup reactor, which is the instantaneous potential difference between the two bridges, are depicted in Section 4, Figure 37.

FIGURE 37   
Waveforms for Circulating Current Mode Cycloconverters   
![](images/1797a726d1967fa6562309e9c8ac9ef1cab28f938c90e585fde3153e4b135269.jpg)  
(a) Positive bridge output voltage   
(b) Negative bridge output voltage   
(c) Load (motor) voltage   
(d) Intergroup reactor voltage

The circulating current cycloconverters normally have a smoother output voltage waveform, containing fewer harmonics, than the blocking mode type. Due to the lack of current reversal complications associated with the blocking mode converter, control is simplified. The main disadvantage of the circulating current type is the additional size, weight and cost associated with the intergroup reactor. However, hybrids have been developed which can provide the advantages of both types. One example has architecture similar to a circulating current mode converter but with a much reduced intergroup reactor. When operating unidirectionally, only one bridge is enabled. When the motor current reverses and decreases below a predetermined level, both bridges are enabled and a smooth reversal of current occurs. Similarly, when the reversed current increases above the predetermined level, the other bridge is disabled. The efficiency is still less than the blocking mode type, however, but it has the advantage of reduced inherent distortion around zero current permitting less complex firing control compared to the standard blocking mode converter.

Cycloconverter input current characteristics and associated harmonic content are complex and dependent on a number of factors, including:

• The pulse number of the cycloconverters   
• The relative magnitude of the output fundamental voltage   
• The ratio of the input and output frequencies   
The displacement power factor of the load   
• The firing control strategy

In applications with large drives, 6-pulse drives are not common. Multi-pulse drives, including 12- pulse, are the norm to minimize the input harmonic currents and associated disruption of the power supply system. Section 4, Figure 38(a) illustrates the input current waveform and Section 4, Figure 38(b) the harmonic current frequency spectrum associated with a 20 MW (26,810 HP) 12-pulse cycloconverter.

Section 4, Figure 39 shows a 12-pulse cycloconverter operating with a three-phase synchronous motor with the rotor field current controlled by a separate 6-pulse, fully-controlled rectifier.

![](images/a8fa9d57db8bf83bd6e238714db88cb93932e16b9404fcad81725470e2cb0028.jpg)  
FIGURE 38a Input Current Associated with a 20 MW, 12-Pulse Cycloconverter

![](images/29173c6596357660d9924ac31a91bc5ed03c7e44f3359a00bf807d957f48d091.jpg)  
FIGURE 38b Harmonic Current Frequency Spectrum Associated with a 20 MW, 12-Pulse Cycloconverter

![](images/38f413714df3e10ac7fe46cbd96217fd2beed71de01a3d42c0551972dae62b13.jpg)  
FIGURE 39 2-Pulse Cycloconverter with Three-phase Synchronous Motor

In addition to the production of standard “pulse number $\pm \nobreakspace 1 \nobreakspace ^ { \overrightarrow { \mathbf { \Gamma } } }$ harmonic currents, cycloconverters often produce, due to supply unbalance, uncharacteristic harmonics (including even order and triplen harmonics) in addition to significant magnitudes of interharmonics. Indeed, the attenuation of these interharmonics is often more difficult than the reduction of the integer harmonic currents.

The characteristic harmonics generated by cycloconverters are:

$$
f _ {h} = (p m \pm 1) f \pm 6 n f _ {o}. \tag {4.3}
$$

where

$$
f _ {o} \quad = \quad \text {o u t p u t f r e q u e n c y}
$$

$$
f _ {h} \quad = \quad \text {h a r m o n i c c u r r e n t f r e q u e n c y}
$$

$$
m \quad = \quad \text {a n u m b e r}, 1, 2, 3 \dots .
$$

$$
n \quad = \quad \text {a n u m b e r ,} 0, 1, 2 \dots
$$

With reference to Section 4, Figure 40 (and to an extent, Section 4, Figure 38), it should be noted that each characteristic integer harmonic has a so called “side band” of interharmonics associated with it. This is a result of the modulation of the constant input current frequency with the varying output motor frequency. Therefore, both the fundamental current and the characteristic harmonic currents are accompanied by additional harmonic components of frequencies based on:

$$
f = n \cdot f L \pm k \cdot 6 \cdot f M. \tag {4.4}
$$

where both $n$ and $k$ are integer numbers.

As mentioned previously, cycloconverter input harmonic currents, including the interharmonics, tend to vary according to the operating point, so the harmonic spectrum constantly changes with output frequency.

Section 4, Figure 40 depicts a typical 12-pulse cycloconverter harmonic (including interharmonics) current spectrum.

Note: Cycloconverters generate significant amounts of reactive power which often have to be compensated for, often employing high pass harmonic filters instead of conventional power factor correction capacitor banks. These high pass filters act as a low impedance path for higher order harmonic currents in addition to providing compensation for the reactive power at fundamental frequencies.

![](images/d3ce2dec0507663b9f6f8330cd4096c31e9887a74310e006040a1ac166676a57.jpg)  
FIGURE 40 Harmonic Spectrum of 12-Pulse Cycloconverters Including Interharmonic Sidebands

# 3.4 AC Load Commutated Inverter (LCI)

“Load commutated inverters”, also known as “current source inverters” (CSIs) were, for many years, common in industrial applications where squirrel cage induction motors (rated $6 0 0 \mathrm { H P } / 4 5 0 \mathrm { ~ k W }$ and above); for example: centrifugal pumps and fan loads where high starting torque is not needed. However, their use has diminished due to availability of the less expensive and physically smaller AC PWM drives.

The load commutated inverter (LCI), so called due to the fact that the motor current commutates the inverter bridge (i.e., it facilitates transfer of current from one phase to another). It is characterized by a large inductor included in the DC bus, as depicted in Section 4, Figure 41, below. Load commutated inverters are known as “constant current” drives due to the action of the large DC bus inductor (i.e., it has an “inductive DC bus”), whereas AC PWM drives have a “capacitive DC bus”, due to the presence of the large capacitor bank.

![](images/122065599d5752a71034a46d7a9057b66d02e5003bfd0e58148bcf79c1f33e13.jpg)  
FIGURE 41 Typical 6-Pulse ASCI CSI Inverter with a Squirrel Cage Induction Motor

As can be seen from Section 4, Figure 41, the load current source inverter comprises a fully controlled SCR input bridge which varies the input DC voltage and a large inductor which converts the variable DC voltage into a current source. The output or “inverter” bridge controls the output frequency to the motor. The squirrel cage induction motor has a lagging power factor, so forced commutation is necessary to transfer current through the motor phases.

Another common inverter bridge configuration, used mainly with squirrel cage induction motors, as illustrated below, was the “auto-sequentially commutated inverter” (ASCI). However, this commutation process results in transient overvoltages, termed “commutation spikes”, being superimposed on the output voltage waveform, as shown in Section 4, Figure 42. In recent years, the use of this configuration has diminished due to the AC PWM drives.

![](images/4833bb3eb81e8a6d7f6134a6ea575f768d8a5e3add73b3e36e4629c1ec05def6.jpg)  
FIGURE 42 Output Voltage Commutation Spikes – CSI with Squirrel Cage Induction Motor

Careful design of the squirrel cage motor and the ASCI circuit is necessary to minimize the commutation spikes. The motor insulation also has to be capable of withstanding the dv/dt (i.e., rate of rise of voltage associated with commutation spikes). Squirrel cage induction motors for use with load commutated inverters need a higher level of magnetizing current, to assist commutation, compared to motors for AC PWM drives or for sinusoidal supplies.

Load commutated inverters are mainly used with synchronous motors. It is the synchronous motors, therefore, which provide the commutation current for the converter (hence the term “load commutated inverter”) via the back EMF of the motor. The synchronous motor, therefore, has to operate with a leading power factor and also needs a special excitation circuit for the rotor, as shown in Section 4, Figure 43.

![](images/52f49bcbe28928841bf8337f3e68ec18235b85369a318d81652802c1bb70e0a8.jpg)  
FIGURE 43 12-Pulse Load Commutated Inverter with Synchronous Motor

As described above, load commutated inverters with ASCI inverter bridge configurations result in commutation spikes, the majority of which are within the withstand capability of modern LV motors. However, if squirrel cage motors are to be operated at higher voltages, then special measures are necessary so that commutation is provided by the load, as shown in Section 4, Figure 44, below. In this example, 12-pulse is needed due to the high power necessary, therefore a special output filter (which supplies a leading power factor to the inverter) is selected which supplies the commutating current up to around $50 \%$ of output frequency. Above $50 \%$ output frequency, the commutation is achieved due to a combination of the output filter and the motor.

![](images/38753d140fcf0e79d161a7759e41d96c6f913431973944db9a567168ad1187c7.jpg)  
FIGURE 44   
12-Pulse Load Commutated Inverter with Squirrel Cage Motor and Output Filter

As can be seen from Section 4, Figure 45, the output voltage waveform (for squirrel cage or synchronous motors) does not contain commutation spikes, as associated with ASCI CSIs, but does contain notches, very similar to that associated with the input of phase-controlled drives, such as DC SCR and quasi-square wave drives.

![](images/03f5430ba5c66615e7320c770c8d8050e310438bda1e91f8777c579cf06bb8f5.jpg)  
FIGURE 45 Output Voltage of LCI with Synchronous Motor or Squirrel Cage Motor with Output Filter

One drawback of the load commutated inverter is the difficulty in starting the drive system due to the fact that below around $10 \%$ speed there is insufficient back EMF to commutate the inverter bridge. A method known as “DC link pulsing” is necessary to initiate commutation. This entails the reduction of the DC bus current to zero by temporarily operating the inverter bridge in the inversion mode (i.e., regenerating into the DC bus), thus permitting the SCRs to regain their blocking capability and thereby commutate the motor current and rotate the motor. In high power applications, reactive power may be necessary due to the very low power factor at low output frequencies and low loading. In order to satisfy the needs of SCRs regarding turn-off, the synchronous motor must, as mentioned above, be operated with a leading power factor. Similarly, squirrel cage motors need an output filter with leading power factor.

The starting torque of load commutated inverter-fed squirrel cage motors is poor, as indicated above. Four-quadrant control is inherent in the design. However, the poor dynamic performance, unless utilizing vector control or similar control strategies, results in the LCI being unable to be applied to the more demanding four-quadrant applications. Power factor at $100 \%$ load/speed is usually around 0.88 – 0.9, but due to the input SCR bridge, reduces to zero at very low loads. Speed range is usually restricted to 10:1 due to commutation issues but is improved if vector control or a similar strategy is applied. For continuous operation below $10 \%$ , “pulsed mode” operation is necessary, as a method needed for starting, and is also necessary in order to minimize torque pulsations and associated vibration on the motor rotor and driven load, in addition to providing sufficient commutation current for the inverter bridge.

The output current of a LCI is a “six step” square wave, as shown in Section 4, Figure 46, which contains significant harmonics, the result of which is additional motor heating and torque fluctuations at low speeds due to the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic currents interacting with the fundamental flux to cause $6 ^ { \mathrm { t h } }$ harmonic torque oscillations. On larger installations, six-phase motors with one “star” and one “delta” (30-degree phase displacement) supplied by two inverter bridges reduce torque fluctuations by $50 \%$ .

![](images/400095dfcd34f72db50ac433d44238c7edb2aa71c4cc68de0b061ea036f51e3c.jpg)  
FIGURE 46 Six Step Square Wave Current – LCI with Synchronous Motor

The input current wave shape of load commutated inverters, as shown below in Section 4, Figure 47, is very similar to a DC SCR drive of similar pulse number due to the controlled SCR input bridge and DC bus inductance.

![](images/351f3bbc946f2458d55d42d05363280840db2dca5d09e71675c6e212310048ef.jpg)  
FIGURE 47 Input Waveform of 6-Pulse Load Commutated Inverter

A typical harmonic spectrum associated with a 6-pulse load commutated inverter is shown in Section 4, Figure 48.

![](images/79b174b23d68e76fb71687889a7536746421748f160f3ec8838d9ea38afbbc6c.jpg)  
FIGURE 48 Harmonic Spectrum Associated with a 6-Pulse Load Commutated Inverter

Load commutated inverters are available for large power systems. For loads with 3-5 MW (4000-7000 HP), inverters of this type are used when the system voltage is above 1kVand would commonly use multi-pulse rectifiers at the input to reduce harmonic distortion (12-pulse or higher depending on power and supply limitations) and possibly multi-pulse on the output to reduce the torque ripple on the machine and the load. (Typically, 12-pulse via two discrete motor windings, 30-degree phase displaced. Alternatively, two separate converters could supply the motor with either the converters 12-pulse or the motor 12-pulse. This permits operation on 6-pulse should any converter or a motor winding fail. Typically, the 6-pulse operation is $50 \%$ of the rated motor loading).

# 4 Additional Three-phase Sources of Harmonics

# 4.1 Rotating Machines

Linear loads, such as generators and motors, can also be considered a source of harmonics, albeit relatively small in comparison with electronic nonlinear loads such as adjustable speed drives.

The windings of the rotating machines, irrespective of type, are embedded into slots within the stator pack. As a result, the magneto-motive force (MMF) is not evenly distributed, and therefore, distortion will occur which produces harmonics. In larger machines, “coil spanning” (i.e., careful design of winding/slot profile) is used to attenuate the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonics. However, compared to electronic nonlinear loads, rotating machine harmonics are relatively small in magnitude and rarely troublesome.

In synchronous machines, the magnitude of harmonic electro-motive force (induced voltage) is dependent on the following factors:

• The magnitude of the harmonic fluxes   
• The effective phase spread of the winding   
• The coil span   
• Method of interphase connection

By careful choice of the above four factors the magnitude of the harmonic EMFs and associated harmonics can be minimized.

Harmonics produced by induction motors, are speed dependent and result from the harmonic content of the MMF distribution within the machine air gap. Harmonic production within induction motors (i.e., squirrel cage and wound rotor) can also result from voltage unbalance. During testing, the generator-induced harmonics are usually checked for compliance against the relevant standard.

# 4.2 Transformers

Harmonics are produced by transformers as a result of the nonlinear relationship between voltage and current and the magnetic materials used in manufacture. This results in the transformer magnetizing current being non-sinusoidal and containing harmonics, especially $3 ^ { \mathrm { r d } }$ and other triplens. It should be noted that if the input voltage was perfectly sinusoidal, the current would be nonlinear and would contain harmonics. Conversely, if the magnetizing current were sinusoidal, the output voltage would be nonlinear. However, similar to rotating machines, the magnitude of harmonics are rarely problematic and are almost negligible compared to harmonics from electronic sources.

In order to maintain relatively sinusoidal output voltages, three-phase power transformers are designed with a delta winding or an ungrounded wye (i.e., Y or star) connection which acts as a block for $\bar { 3 } ^ { \mathrm { r d } }$ and other zero sequence triplen harmonics.

Transformers when in saturation (i.e., overly excited), for example if subject to a large increase in voltage, tend to produce odd order harmonics $( 5 ^ { \mathrm { t h } } , 7 ^ { \mathrm { t h } } , 1 1 ^ { \mathrm { t h } } , 1 3 ^ { \mathrm { t h } } \cdots )$ . Triplens are also produced, but are restricted (i.e., absorbed) due to delta or ungrounded wye configuration.

Inrush current, especially in larger transformers, does contain relatively large odd order harmonics, but as the inrush time is only a few seconds, the effects are usually not significant with regard to the harmonic distortion. However, it may initiate shutdown of differential protection systems and ultimately, the generator(s,) although more modern differential protection systems do attempt to compensate and reduce the likelihood of a shutdown. Unbalance can also produces odd order harmonics. This is especially true if there is a large DC component on the secondary of the transformer.

# 4.3 UPS Systems

Uninterruptible power supply systems are usually used to provide “secure power” in the event of generator shutdown or other similar power failure. Dedicated individual computer UPS systems are usually single-phase and have an input current wave-shape and harmonic current spectrum similar to that produced by single-phase switched mode power supplies (SMPS).

Three-phase UPS systems are also available. The majority of three-phase UPS systems have a controlled, SCR input bridge rectifier with characteristic harmonics based on the “pulse number $\pm \nobreakspace 1 \nobreakspace ^ { \circ } \nobreakspace$ format. Section 4, Figure 49, below, shows the voltage and current waveforms from a typical threephase 480 V, 60 Hz UPS rated $3 7 . 5 \mathrm { k V A }$ . The $I _ { t h d }$ at the input is $1 9 . 1 \%$ . Section 4, Figure 50 depicts the harmonic current spectrum associated with this UPS.

Active front ends (i.e., sinusoidal input rectifiers) and 12-pulse configurations are also now available which may have better harmonic performance.

![](images/cce657fea51c4a3a08fdbc1c0a5745ff2c97758318fe24c47e09da4128a995e7.jpg)  
FIGURE 49 Input Voltage and Current Waveforms of 6-Pulse 37.5 kVA, 480 V, 60 Hz UPS

![](images/1f6fd86afcb2cfddf234c7f81cc350143871021cc058e5911748163cc8b318b4.jpg)  
FIGURE 50 Harmonic Input Current Spectrum for 6-Pulse 37.5 kVA, 460 V, 60 Hz UPS

# 4.4 Shaft Generators

Shaft driven generators are sometimes provided, as they provide the vessel with electric power when underway while reducing fuel and decreasing operational costs.

A traditional shaft generator system, shown in Section 4, Figure 51, comprises a synchronous generator, a converter with SCR input rectifier, DC bus inductor and SCR inverter bridge, AC line reactor and “synchronous compensator” (also known as a “rotary condenser”). The synchronous compensator’s duties are to start the system by providing the initial starting voltage for the SCR inverter and to provide reactive power and to facilitate commutation of the inverter bridge SCRs.

![](images/18bbbb5070223560f0b9fef9d157654d72fab164698b2309e6e9d08eb16af9c1.jpg)  
FIGURE 51 Traditional Shaft Generator System

In the above example, the commutation notches in the output voltage waveform (Section 4, Figure 52) of the inverter bridge are largely due to the subtransient inductance $( L _ { s } ^ { \prime \prime } )$ of the synchronous compensator; necessary to provide commutation current to the inverter. The provision of the AC line reactor does serve to reduce the harmonic currents in the output waveform, but the overlap angle of the output current is increased, increasing the notch area.

The inverter output voltage waveform consists of both harmonics and line notches and may not be of sufficient quality to supply the load and/or operate in parallel with diesel or other auxiliary generators.

![](images/8bb49085f7daece613ad57de9d1e5d5d446d4517fa752131dbd2cec173cd1366.jpg)  
FIGURE 52 Inverter Output Voltage Waveform

The harmonics produced by the inverter bridge are based on the “pulse number $\pm \nobreakspace 1 \nobreakspace ^ { \circ } \nobreakspace$ format. A 6-pulse system would therefore produce characteristic harmonic currents of $5 ^ { \mathrm { t h } }$ , $7 ^ { \mathrm { t h } }$ , $1 1 ^ { \mathrm { t h } }$ , $1 3 ^ { \mathrm { t h } }$ …

In addition to providing reactive power and commutation current, the synchronous compensator also provides a measure of harmonic filtering. The low harmonic reactance of the compensator attracts a relatively large degree of harmonic currents which would otherwise be injected into the load. The induced voltages in the compensator are essentially sinusoidal; therefore the output voltage will also be relatively sinusoidal.

The example used was to advise the reader as to the fact that shaft generators, due to their electronic power conversion, are a source of harmonics. There are a number of other shaft generator systems in operation which utilize other techniques. Some use double-wound induction motors, others IGBT converters (very similar to AC PWM drives with “active front ends”) or “duplex reactors”. However, the object is identical: to minimize the harmonics and notching and to address other power quality concerns, such that the output voltage is as sinusoidal as practicable.

This Page Intentionally Left Blank

# S E C T I O N

# 5 Harmonics and System Power Factor

# 1 Power Factor in Systems with Linear Loads Only

In power systems containing only linear loads, the vector relationship between voltage and current, the “power factor” (cos $\phi )$ , can be illustrated with reference to Section 5, Figure 1, below:

![](images/05bfce88f68afb1c7b97ba8931a5e1808be883cf63f084849bd19d889ccac779.jpg)  
FIGURE 1 Power Factor Components in System with Linear Load

Where the power factor, $\cos \phi = \frac { P } { S } = \frac { k W } { k V A }$ .. (5.1)

The apparent power, $S ( k V A ) = \sqrt { P ^ { 2 } + Q ^ { 2 } } = \sqrt { k W ^ { 2 } + k V A r ^ { 2 } }$ .. (5.2)

where

P = active power (i.e., it produces useful work), in kW

S apparent power (kVA)

Q = reactive power, which produces no useful work, (kVAr)

# 2 Power Factor in Power System with Harmonics

In power systems which contain nonlinear loads, there are essentially two power factors; the “displacement power factor” (i.e., the power factor of the fundamental component) and the “true power factor”, which is a measure of the power factor of both the fundamental and harmonic components in the power system.

![](images/92fb4e1fd6d19161582f7e1ed37e7f15320fbd69cf282dc32f2b86bbfd5eea02.jpg)  
FIGURE 2 Power Factor Components in System with Harmonics

With reference to Section 5, Figure 2 above:

The power factor, $\cos \phi = \frac { P } { S } \neq \frac { k W } { k V A }$ (i.e., the power factor does not equal ${ \frac { k W } { k V A } } )$ .

The apparent power, $S ( k V A ) = \sqrt { P ^ { 2 } + Q ^ { 2 } + { D ^ { 2 } } } = \sqrt { k W ^ { 2 } + k V A r ^ { 2 } + k V A r _ { H } ^ { 2 } } ~ . . . . . . . . . . . . . . . . . . . . . . . . . .$ ... (5.3)

The active power, $P$ can be calculated using:

$$
P = \sum_ {h = 0} ^ {\infty} V _ {h} I _ {h} \cos \varphi_ {h} = P _ {0} + P _ {1} + \sum_ {h = 2} ^ {\infty} P _ {h}. \tag {5.4}
$$

where $\phi _ { H }$ is the phase of the $n$ -th harmonic.

Similarly, the reactive power, $Q _ { i }$ , can also be defined as:

$$
Q = \sum_ {h = 1} ^ {\infty} V _ {H _ {r m s}} I _ {H _ {r m s}} \sin \varphi_ {h} = Q _ {1} + \sum_ {h = 2} ^ {\infty} Q _ {h}. \tag {5.5}
$$

where

phase angle between voltage and current of individual harmonics

DC component of active power

fundamental component of active/reactive power respectively

active/reactive component of individual harmonics

The apparent power, $S _ { z }$ , can also be expressed using the following formulae:

$$
\begin{array}{l} S = V _ {r m s} \cdot I _ {r m s}. (5.6) \\ = \sqrt {\sum_ {h = 1} ^ {\infty} V _ {H _ {r m s}} ^ {2} I _ {H _ {r m s}} ^ {2}} (5.7) \\ = V _ {1 _ {r m s}} I _ {1 _ {r m s}} \sqrt {1 + T H D _ {V} ^ {2}} \sqrt {1 + T H D _ {I} ^ {2}} (5.8) \\ = S _ {1} \sqrt {1 + T H D _ {V} ^ {2}} \sqrt {1 + T H D _ {I} ^ {2}} (5.9) \\ \end{array}
$$

where $S _ { 1 }$ is the apparent power at the fundamental frequency.

As can be seen from Section 5, Figure 2; in power systems where harmonics are present, the apparent power, S, comprises active power $( P )$ , reactive power $( \mathcal { Q } )$ and $H$ (distortion power) where the distortion power, $D$ , can be defined as:

$$
D ^ {2} = S ^ {2} - \left(P ^ {2} + Q ^ {2}\right) \dots \tag {5.10}
$$

As detailed above, the power factor is the ratio of the active power in kW to the apparent power in kVA. For systems containing nonlinear loads, the power factor can therefore be expressed as:

$$
\text {P o w e r f a c t o r :} \cos \phi = \frac {P}{S} = \frac {P}{S _ {1}} \frac {1}{\sqrt {1 + T H D _ {V} ^ {2}} \sqrt {1 + T H D _ {I} ^ {2}}} = \cos \phi_ {\text {d i s p}} \cdot \cos \phi_ {\text {d i s t}} \tag {5.11}
$$

$$
\text {D i s p l a c e m e n t} \cos \phi_ {\text {d i s p}} = \frac {P}{S _ {1}} \tag {5.12}
$$

$$
\text {D i s t o r t i o n} \cos \phi_ {\text {d i s t}} = \frac {1}{\sqrt {1 + T H D _ {V} ^ {2}} \sqrt {1 + T H D _ {I} ^ {2}}} = \frac {V _ {1 _ {\text {r m s}}}}{V _ {\text {r m s}}} \cdot \frac {I _ {1 _ {\text {r m s}}}}{I _ {\text {r m s}}} = \frac {S _ {1}}{S} \dots \tag {5.13}
$$

where

$$
\cos \phi_ {d i s p} = \text {d i s p l a c e m e n t p o w e r f a c t o r (f u n d a m e n t a l c o m p o n e n t s)}
$$

$$
\cos \phi_ {d i s t} = \text {d i s t o r t i o n p o w e r f a c t o r (h a r m o n i c c o m p o n e n t s)}
$$

Note: Many AC PWM drive manufacturers cite “high power factor at all loads” as an advantage when selling this type of drive. However, this “high power factor” (typically 0.96-0.98) refers only to the displacement power factor, not the true power factor. Please note that the majority of utility power factor meters can only read displacement power factor.

# 3 How the Mitigation of Harmonics Improves True Power Factor

As can be seen from Section 5, Figure 2, if the distortion power, $D$ , is reduced by mitigation, the true power factor will increase accordingly. Any form of harmonic mitigation, passive or active, will increase the true power factor.

On drives or other loads with fully controlled input bridge rectifiers (e.g., DC drives, AC variable voltage drives, load commutated inverters, UPS systems) the true power factor will also vary, depending on the conduction angle of the bridge rectifier, due to changing speed and/or load demands. On this type of equipment, it can be beneficial, subject to a study of the effects on the power system, to use passive inductor-capacitor (L-C) filters (see Section 10), tuned to a specific harmonic frequency (usually $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonics). These filters can provide harmonic mitigation and a degree of power factor correction via the filter capacitors. However, measures may have to be taken at light loads, such as switching out stages of the filter, to prevent a leading power factor from occurring.

Active filters (see Section 10) can also provide a measure of inherent power factor correction. Active filters are usually rated based on “harmonic cancellation current” [i.e., based on the magnitude of the harmonic currents being produced by the load(s)]. This is injected into the power system and provides the nonlinear load with the harmonic currents it needs in order to function. In theory, and assuming the active filter is rated correctly, the power system then supplies only the fundamental current.

In addition to the harmonic cancellation current, reactive current compensation is also provided which can correct for a leading or lagging power factor at any load (i.e., this statement is based on an active filter with digital control system). For example, for a 300 A, 480 V active filter, the available reactive power would be $2 4 9 . 4 \mathrm { ~ k V } \mathrm { A r }$ . However, the reader has to be aware of one type of analog-controlled active filter which has a tendency to supply uncontrolled reactive current into the power system, producing a leading power factor when the harmonic load is light or the nonlinear equipment is switched off. On utility supplies, this may not cause problems, but it will be problematic when the supplies are generator derived.

S E C T I O N

# 6 The Effect of Loading on Harmonic Current Distortion

# 1 Total Harmonic Voltage Distortion $\left( V _ { t h d } \right)$

As illustrated in Section 2, in power systems containing nonlinear loads, the total harmonic voltage distortion $( V _ { t h d } )$ is dependent on the magnitude of each harmonic current at its specific harmonic frequency acting upon the source impedance and other individual circuit impedances to produce individual harmonic voltage drops, all of which are summed and compared with the fundamental voltage to obtain, in percentage terms, the $V _ { t h d }$ .

The resultant voltage distortion, unless resonance is present in the system, tends to decrease the further it is measured from the harmonic-producing load. It is usually the highest nearer to the harmonic load and progressively reduces the nearer to the source it is measured, due to the effect of cables, transformers and other impedances, and to a degree, the amount of linear load (such as induction motors), which tends to act as a “harmonic sink” (i.e., it absorbs harmonic current) in the circuit. The higher the magnitude of harmonic current, the higher the voltage distortion for a given impedance.

# 2 Total Harmonic Current Distortion $\left( I _ { t h d } \right)$ and Reduced Loading

In nonlinear loads, the magnitude of the characteristic harmonic currents is normally proportional to the load demand. At rated load, the harmonic current levels tend to be at the highest levels, except under resonant conditions where specific harmonic currents at the resonant frequency can have significantly higher values. The effect of loading, therefore, will affect percentage total harmonic current distortion $( I _ { t h d } )$ .

Since the majority of large nonlinear loads installed on marine vessels and offshore installations are variable speed drives, it may be worthwhile to briefly consider the effect of loading on the more common types of variable speed drives used in the marine sector, including AC PWM (variable frequency) drives, AC load commutated inverters (LCIs), DC SCR drives and AC cycloconverters.

# 2.1 AC PWM Drives

AC PWM drives are the common type used in the marine sector. Recent designs have increased power ratings and higher voltage levels. As described in Section 4, this type of drive architecture is characterized by the presence of an input bridge rectifier, a DC bus with capacitor bank and an inverter output bridge.

Section 6, Figures 1 and 2 illustrate the current time domain waveform and harmonic spectrum, respectively, of a typical 6-pulse AC PWM drive at rated load. Note that the drive contains a $3 \%$ AC line reactor which reduces the $I _ { t h d }$ and improves the true power factor. Without the AC line (or DC bus) reactor, the $I _ { t h d }$ and harmonic currents would be significantly higher.

The AC PWM drive illustrated has a total harmonic current distortion $( I _ { t h d } )$ of $3 7 . 5 \%$ at $100 \%$ loading. True power factor was 0.94 lag.

![](images/239942245b8093f6c0fcd478858762094fe709fd995b4fcd9e965723be23bdc6.jpg)  
FIGURE 1 Typical 6-Pulse PWM Drive (with $3 \%$ AC Line Reactor) at $100 \%$ Load $I _ { t h d }$ Measured at $3 7 . 5 \%$

![](images/911e1d1802646ab3b018a51204e8c1838f502f10cfffb2df81f78c2523a0ed62.jpg)  
FIGURE 2 Typical Harmonic Spectrum of AC PWM Drive (with $3 \%$ AC Line Reactor) at $100 \%$ Load – $I _ { t h d }$ Measured at $3 7 . 5 \%$

With AC PWM drives, the $I _ { t h d }$ will increase as the loading is reduced due to the more “discontinuous” nature of the pulsed current drawn from the capacitive DC bus. As described in Section 4, current is only drawn from the mains supply when the instantaneous AC line voltage exceeds the DC bus voltage, hence the pulsed nature of the current. As the drive load is reduced, the current pulse will become “sharper”. Section 6, Figure 3 illustrates this effect on the AC PWM used in this example.

FIGURE 3   
Typical AC PWM Drive (with $3 \%$ AC Line Reactor) at $30 \%$ Load $I _ { t h d }$ Measured at $6 5 . 7 \%$ .   
![](images/ca1327f1f444a2b0bcec155221bf99e2d9a3b909146a71c2436d60aaf4c12be1.jpg)  
Section 6, Figure 4, below, illustrates the harmonic current spectrum associated with the AC PWM drive waveform based on $30 \%$ loading. Note the increased $\bar { 5 } ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic components. True power factor was 0. 83 lag.

![](images/58003f1dd567b60646408b4989262d3ecd5c3d28a479954fafb9c6782e022027.jpg)  
FIGURE 4   
Typical Harmonic Spectrum of AC PWM Drive (with $3 \%$ AC Line Reactor) at $30 \%$ Load – $I _ { t h d }$ Measured at $6 5 . 7 \%$

Although it has been shown that the total harmonic current distortion will increase with reducing load it is the magnitude of the harmonic currents and the resultant effect on circuit impedances (which produce voltage distortion) which are more important. However, it should be noted that if AC PWM drives are “oversized” for any reason, the $I _ { t h d }$ will be higher than expected at any load as the drive is not “matched” to the load as far as the kW/HP rating is concerned. This may have to be taken into account when calculating harmonic mitigation.

# 2.2 DC SCR Drives

Unlike variable frequency drives, DC drives do not have an intermediate circuit between the input rectifier and the output to the DC motor. The input rectifier directly controls the output voltage (i.e., motor armature voltage) by variation of the firing angle of the SCRs. The harmonic current distortion $( I _ { t h d } )$ is largely determined by the SCR firing angles, with the worse case at reduced load being at 90 degrees firing angle (i.e., low voltage and speed) and rated load.

In common with AC PWM and other drive types, the magnitude of harmonic current is usually highest at rated load. As DC drives have, due to the presence of the DC armature, primarily “inductive buses”, the percentage $I _ { t h d }$ will rise with reducing load but be less than with comparable AC PWM drives which have capacitive buses. DC drives tend to operate in continuous current mode (see Section 6, Figures 5 and 6) down to around $10 \mathrm { - } 1 5 \%$ load after which the $I _ { t h d }$ will rise more significantly. However, at low speeds, the magnitude of the harmonic currents is usually relatively small and non-problematic.

![](images/70d5d63e6d5adf5b66939109e27727f48a77c5045476f9b7ff611a04719734a2.jpg)  
FIGURE 5 6-Pulse DC Drive at $70 \%$ Loading $I _ { t h d }$ is 35.1%

Section 6, Figure 5, above, illustrates the typical current waveform of a 6-pulse DC drive at $70 \%$ loading $( 3 5 . 1 \bar { \% } I _ { t h d } )$ . A comparable 6-pulse AC PWM drive with $3 \%$ AC line reactor at similar loading would present an $I _ { t h d }$ of around $42 \%$ . Section 6, Figure 6, below, depicts the harmonic current spectrum of the DC drive at $70 \%$ loading.

![](images/148dc5e783bef1564d464e6ac4548a8f3747858e8189382da167a95dd88b234d.jpg)  
FIGURE 6 Harmonic Current Spectrum of 6-Pulse DC Drive at $70 \%$ Loading $I _ { t h d }$ is 35.1%

# 2.3 Load Commutated Inverters

The input harmonic currents and input current waveforms produced by load commutated inverters (also called current source or current-fed inverters) are similar to those produced by DC SCR drives. This is due to the large inductance inserted in the DC bus to provide a constant current source. As per DC drives, the harmonic current distortion $( I _ { t h d } )$ produced by load commutated inverters is also a function of the input SCR rectifier firing angles, so as with DC drives, the maximum value of $I _ { t h d }$ should occur at very low speed (or zero speed) and high loading.

The variation in $I _ { t h d }$ with load for load commutated converters will be similar to that described for DC SCR drives.

# 2.4 Cycloconverters

As described in Section 4, cycloconverters are very complex drives from both the input and output harmonic perspectives. As also mentioned in Section 4, the characteristic harmonics are generally less than other drive types of the same pulse number, but the interharmonics are usually significantly higher.

As stated previously, the characteristic harmonics are related to the pulse number and system characteristics. Any deviation from the ideal can introduce non-characteristic harmonic currents, such as the $2 ^ { \mathrm { n d } }$ and $3 ^ { \mathrm { r d } }$ , whereas the input interharmonic currents are related to the output frequency, the mode of operation (i.e., blocking mode or circulating mode), the motor loading and the motor ripple current.

At low frequency operation (i.e., low motor speed and load), the magnitudes of the characteristic harmonic currents produced are typically similar to DC drives under the same load conditions. At low speed operation, the interharmonics are generally of low value.

As the output frequency, hence motor speed and load, are increased up to rated speed and load, the characteristic harmonic currents tend to decrease while the interharmonic current sidebands increase. For 6-pulse cycloconverters, the interharmonics associated with the fundamental, $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonics should not be significant, but above those harmonic frequencies, the magnitude of the interharmonic side bands can often exceed those of the characteristic harmonics.

It has to be stated that cycloconverters applied in the marine sector tend to be in the MW range with 12-pulse or higher configurations. Therefore, a measure of both reactive power compensation (i.e., power factor correction) and harmonic filtering may be installed to minimize any adverse effects on the power system of such large drives.

Section 6, Figures 7 and 8 illustrate the effect of output frequency on both the input current and input voltage harmonic spectrums. This application involved six, 6-pulse cycloconverters on a common bus, all operating at identical output frequency and loading.

![](images/438d29d3bfffa4b1c0d38e1613ceaf1bb8569fa39ba78d11dd4229267f2a5da5.jpg)  
FIGURE 7 Multiple 6-Pulse Cycloconverters Input Current and Voltage Harmonic Spectrums at Low Output Frequency/Low Load

![](images/343f2c0691e947d7f1d6e4a09c72aecc639ff883491cfd4205ae511be1c1ad68.jpg)

![](images/316c7bad96a4a18d1a3ab157edee1f7e0fe54b773824bb9da1fc2f0a98a9fa2b.jpg)  
FIGURE 8 Multiple 6-Pulse Cycloconverters Input Current and Voltage Harmonic Spectrums at High Output Frequency/High Load

![](images/2cff7b21013eca5adf45968d299f92e9b1a9167b546baf7e625e7693a86b9420.jpg)

# 2.5 Conclusion: Harmonic Current Magnitude and its Effect on Voltage Distortion

It should be re-emphasized that it is not the percentage of total harmonic current distortion $( I _ { t h d } )$ which is of main concern. It is the magnitude of the harmonic currents associated with the $I _ { t h d }$ which is of more importance, as it is the magnitudes of these harmonic currents which interact with the system impedances to produce the individual harmonic voltage drops at the harmonic frequencies which result in the total harmonic voltage distortion $( V _ { t h d } )$ .

It is therefore the total harmonic voltage distortion $( V _ { t h d } )$ which is to be the main concern in order to minimize any adverse effects on the installed system and equipment. Therefore, it should be the purpose of any harmonic mitigation measure employed to reduce the total harmonic voltage distortion $( V _ { t h d } )$ to within the necessary limits under all operating conditions.

This Page Intentionally Left Blank

S E C T I O N

# 7 Influence of Source Impedance and kVA on Harmonics

# 1 “Stiff” and “Soft” Sources

Power sources in relation to harmonics are often characterized by the terms “stiff source” and “soft source”, and both have a significant effect on both the nonlinear currents drawn by the load and the resultant voltage distortion.

“Stiff sources” are often associated with transformers, whether utility-owned or customer-owned within their system. Their source impedance is often on the order of $5 \text{‰}$ (Z). Generators, however, are considered as “soft sources” whose “source impedance” is actually the “substransient reactance $( X _ { d } ^ { ~ \prime \prime } )$ ,”often in the range of approximately 0.1 – 0.18 per unit.

“Stiff sources”, having higher short circuit capability, permit a given nonlinear load(s) to draw higher magnitudes of harmonic current for a given kW value of nonlinear load, as it is not as limited by the leakage reactance of the source. The higher harmonic current does not usually significantly distort the voltage. The stiffer the source, the higher the harmonic current that will be drawn by the nonlinear load(s) and the less the subsequent voltage distortion for a given load.

“Soft sources”, such as generators, tend to have reduced short circuit capability and limit the magnitude of the harmonic currents drawn by the given nonlinear load(s). However, that lower value of harmonic current will produce significantly higher levels of voltage distortion.

Generators for low harmonic distortion would need a low value of subtransient reactance, $X _ { d } ^ { \prime \prime }$ , such as that achieved by “oversizing” the kVA rating, which results in an increase in short circuit current. The generator rotor damper cage, designed for linear loads, is subject to higher levels of current when nonlinear loads are present. The machine subtransient reactance, $X _ { d } ^ { \prime \prime }$ , should be relatively low to maintain the voltage distortion within the necessary limits. The damper winding is to be designed such that the sinusoidal voltage waveform is maintained. The solution will depend on the type of nonlinear load, the magnitude of the harmonic currents produced and the subsequent voltage distortion permissible in the power system.

The kVA rating also has an impact on the magnitude of harmonic currents and subsequent voltage distortion for a given load as the short circuit capability and associated $I _ { S C } / I _ { L }$ (load current to short circuit current ratio) varies. The higher the kVA (or MVA), the higher the harmonic current distortion, $I _ { t h d } ,$ and the lower the resultant harmonic voltage distortion, $V _ { t h d } ,$ assuming the source impedance is unchanged.

# 2 Illustrations of the Effect of kVA and Source Impedance on Harmonics

In order to illustrate the effect of varying kVA and source impedance (or substransient reactance) of the power source, a harmonic estimated program (SOLV) has been utilized. Note that the illustrations of the power source do not differentiate between transformer and/or generator derived supplies (the illustrations are “transformers”), but the subsequent calculations are unaffected (i.e., the effects of varying the values of impedance (or $X _ { d } ^ { \prime \prime }$ ) and kVA are similar for both transformers and generators).

The voltage and current waveforms at the PCC#1 (point of common coupling are also included).

# Example 1 – 2000 kVA, 5.2% Impedance

This is based on a transformer rated at $2 0 0 0 \ \mathrm { k V A }$ with impedance of $5 . 2 \%$ and secondary voltage of 480 V, 60 Hz. The loads are two AC PWM drives, one of $6 0 0 ~ \mathrm { H P }$ with $3 \%$ AC line reactor and one of $3 5 0 \ \mathrm { H P }$ with $3 \%$ DC bus reactor. Linear load is $1 8 0 ~ \mathrm { k W }$ at 0.85 lag power factor.

![](images/e76ad796b8e03aa44204fd674c678a1593e9e9c4d4968948d6236be500ac1ddc.jpg)  
FIGURE 1a   
2000 kVA and $5 . 2 \%$ Impedance – $I _ { S C } I I _ { L } = 3 3 . 3 { : } 1$ , $I _ { t h d } = 2 4 . 2 \% $ , Vthd = 4.7%   
6 Pulse AC PWM Drives

![](images/b1c6d98e23fa855d50491bed1a0bcde3c4716b08be72a9de6f61cf390d336f56.jpg)  
FIGURE 1b Current and Voltage Waveforms for 2000 kVA/5.2% Impedance Source with 950 HP AC PWM Drive Load and 180 kW Linear Load

# Example 2 – 2000 kVA, 14% Subtransient Reactance

This is based on a generator similarly rated at $2 0 0 0 \ \mathrm { k V A }$ , with substransient reactance $( X _ { d } ^ { ~ \prime \prime } )$ of $14 \%$ and secondary voltage of 480 V, 60 Hz. The loads are as per Example 1, with two AC PWM drives, one of $6 0 0 \mathrm { H P }$ with $3 \%$ AC line reactor and one of $3 5 0 \mathrm { H P }$ with $3 \%$ DC bus reactor. Linear load is $1 8 0 \mathrm { k W }$ at 0.85 lag power factor.

# FIGURE 2a

# 2000 kVA and14% Subtransient Reactance

$I _ { S C } / I _ { L } = 2 9 . 1 \colon$ 1, $I _ { t h d } = 1 9 . 1 \%$ , $V _ { t h d } = 9 . 8 \%$

# SOLV Lite

![](images/0d1b0ae8c6f34b6adbd102f57d1f75b293cdd7595f065f7a064c6da1b18fe5d7.jpg)

EileProject

![](images/343def4dd9c690a82b8e3a9ab5828d62ca08e3baa7b4a045f57848ad289976c8.jpg)

ulateWaveform

Spectrum

Reports

Print ScreenHelp

![](images/8cea5ad63c8cad0964606ff6808aaeb3b1855150d8240af51660447bae2f6b37.jpg)  
6 Pulse AC PWM Drives

# FIGURE 2b Current and Voltage Waveforms for 2000 kVA/14% Subtransient Reactance Source with 950 HP AC PWM Drive Load and 180 kW Linear Load

Project: NEW.slv

Date: 11-12-200

Drive Transformer

2000.0 KVA

14.0%,Z

480.V

60.Hz

Branch #1

No Filtering

Input Line Reactor $3 . 0 \ \%$

Smoothing Capacitor 30.0 mF

Load, HP 600.0

Loading,% 100.0

Branch #2

No Filtering

DC Link Reactor 3.0 %

Smoothing Capacitor 18.0 mF

Load, HP 350.0

Loading,% 100.0

Linear Load

180.0 KW

Disp. PF -0.85

![](images/021d3d43beb5badb5cbb1fe2a9787afbbab7e717f832c53b52b8a62b09d34d88.jpg)  
ELECTRICAL DEGREES

# Example 3 – 4000 kVA, 5.2% Impedance

The transformer rating is now increased to $4 0 0 0 \ \mathrm { k V A }$ , but the impedance of $5 . 2 \%$ and secondary voltage of 480 V, 60 Hz remain the same. The loads are two AC PWM drives, one of $6 0 0 ~ \mathrm { H P }$ with $3 \%$ AC line reactor and one of $3 5 0 ~ \mathrm { H P }$ with $3 \%$ DC bus reactor and linear load is $1 8 0 \mathrm { k W }$ at 0.85 lag power factor are identical to that illustrated in Example 1.

# FIGURE 3a

# 4000 kVA and $5 . 2 \%$ Impedance – $I _ { S C } / I _ { L } = 6 7 . 1 \div$ 1, Ithd = 27.1%, Vthd = 2.7%

![](images/6eb07a7ef1677640fe61b79091c8e141b9f1fd9bfdfa3bbeee89f1481bd35a70.jpg)  
6 Pulse AC PWM Drives

![](images/283a65cfce7be8d8339e8672fa500e6a17adde0b52d0b5a46922d3fe440c19cc.jpg)  
FIGURE 3b Current and Voltage Waveforms for 4000 kVA/5.2% Impedance Source with 950 HP AC PWM Drive Load and 180 kW Linear Load

# Example 4 – 4000 kVA, 14% Subtransient Reactance

The generator is also now increased to $4 0 0 0 \ \mathrm { k V A }$ with substransient reactance $( X _ { d } ^ { ~ \prime \prime } )$ of $14 \%$ and secondary voltage of 480 V, $6 0 \ : \mathrm { H z }$ maintained. The loads are as per Example 2, with two AC PWM drives, one of $6 0 0 \mathrm { H P }$ with $3 \%$ AC line reactor and one of $3 5 0 \mathrm { H P }$ with $3 \%$ DC bus reactor and linear load is $1 8 0 \mathrm { k W }$ at 0.85 lag power factor retained.

# FIGURE 4a

# 4000 kVA and14% Subtransient Reactance

$I _ { S C } / I _ { L } = 2 6 . 6 { : } 1$ , $I _ { t h d } = 2 2 . 9 \%$ , $V _ { t h d } = 5 . 8 \%$

![](images/6e5055449edb6355c5ae284852b9007e5c8ffd7b2a3400f68ad6f683c3bc75a1.jpg)

![](images/a83734b80b43f83e4cb84e148987920ccdcefe2c6eaf4a2937e3dff309c5ef3d.jpg)

# FIGURE 4b Current and Voltage Waveforms for 4000 kVA/14% Subtransient Reactance Source with 950 HP AC PWM Drive Load and 180 kW Linear Load

![](images/7ba2a832aa8bafd1a4c4aa38bab54d9f7f084d73dab7674b2a9e72d42a8afd24.jpg)

A summary of all four examples above is given in Section 7, Table 1 below:

TABLE 1 Variation of $I _ { t h d }$ and $V _ { t h d }$ with Variation of kVA and Impedance (or $X _ { d } ^ { \prime \prime }$ )   

<table><tr><td>kVA - Z orXd&quot;</td><td>ISC/IL</td><td>Ithd</td><td>Vthd</td></tr><tr><td>2000 kVA - 5.2% Z</td><td>33.3</td><td>24.2%</td><td>4.7%</td></tr><tr><td>2000 kVA - 14%Xd&quot;</td><td>12.1</td><td>19.1%</td><td>9.8%</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>4000 kVA - 5.2% Z</td><td>67.1</td><td>27.1%</td><td>2.7%</td></tr><tr><td>4000 kVA - 14%Xd&quot;</td><td>24.6</td><td>22.9%</td><td>5.8%</td></tr></table>

The kVA rating and transformer impedance $( Z )$ or [substransient reactance $( X _ { d } ^ { { \prime \prime } } )$ for generators] have an important effect on the magnitude of the harmonic currents drawn and the resultant voltage distortion. It can be seen that the resultant voltage distortion for a given nonlinear load varies in proportion to the source impedance (i.e., for generators, the lower the $X _ { d } ^ { \prime \prime }$ , the less the resultant voltage distortion) and installed kVA.

Achieving a low level of $X _ { d } ^ { \prime \prime }$ usually involves a special winding design with a high level of excitation and therefore high magnetic flux or the use of “derated” generators (i.e., of a larger kVA rating than one based on the kW load.). The value of $X _ { d } ^ { \prime \prime }$ varies from generator to generator and is inversely proportional to the square of the generator working voltage.

In Example 2 above, the $2 0 0 0 \mathrm { k V A }$ , $4 8 0 \mathrm { V }$ , $6 0 \ \mathrm { H z }$ generator used in the illustrations and calculations above had an $X _ { d } ^ { \prime \prime }$ of $14 \%$ or 0.14 per unit. At $1 0 0 0 \mathrm { k V A }$ loading, the effective subtransient reactance $( X _ { d } ^ { { \prime \prime } } )$ will be:

$$
X _ {d} ^ {"} = \frac {1000 \mathrm {kVA}}{2000 \mathrm {kVA}} \times 14 \% = 7 \%
$$

Therefore, at reduced generator loading, the effective $X _ { d } ^ { \prime \prime }$ will be reduced, thus decreasing the voltage distortion for given nonlinear load. Modern generators have excitation systems which can cope with voltage and current distortion provided that they are correctly designed for the nonlinear load(s) in terms of thermal rating and have an appropriate level of winding insulation.

# 3 Parallel Generator Operation and Calculation of Equivalent Short Circuit Ratings

When calculating harmonic voltage and current distortion, either the short circuit rating or the generator kVA (or MVA) and the subtransient reactance, $X _ { d } ^ { \prime \prime }$ , is necessary. (Similar data is necessary for transformers with impedance, Z, instead of $X _ { d } ^ { \prime \prime }$ .) The calculation based on one generator running is straightforward with the generator kVA and $X _ { d } ^ { \prime \prime }$ inserted into program (or used for manual calculations).

However, when more than one generator, perhaps of differing values of kVA and $X _ { d } ^ { \prime \prime }$ , are running in parallel to share the loading, it is significantly more complicated. Therefore, a method of calculating the parallel system kVA and equivalent $X _ { d } ^ { \prime \prime }$ (illustrated below) is necessary and is similar to that used for short circuit calculations.

![](images/46c85a9a808b534b74c024e0b6fd4cfcbdc2948709a4a1882c39ee53962bdbf8.jpg)  
FIGURE 5 Paralleling of Generators

One of the generators must be selected as the “base unit”. In this case $S _ { 1 }$ will be designated “base unit” in terms of kVA and $X _ { d } ^ { \prime \prime }$ .

If $X _ { d 1 } ^ { \prime \prime }$ $( S _ { 1 } )$ is the base unit, we must determine $X _ { d 2 b a s e } ^ { \prime \prime }$ and $X _ { d 3 b a s e } ^ { \prime \prime }$ , as follows:

$$
X _ {d 2 b a s e} ^ {\prime \prime} = X _ {d 2} ^ {\prime \prime} \frac {S _ {1}}{S _ {2}} \tag {7.1}
$$

$$
X _ {d 3 b a s e} ^ {\prime \prime} = X _ {d 3} ^ {\prime \prime} \frac {S _ {1}}{S _ {3}} \dots \tag {7.2}
$$

Once all generators are on the same base, the total system equivalent subtransient reactance can be calculated, as follows:

$$
X _ {d 1, 2 b a s e} ^ {\prime \prime} = \frac {X _ {d 1} ^ {\prime \prime} \cdot X _ {d 2 b a s e} ^ {\prime \prime}}{X _ {d 1} ^ {\prime \prime} + X _ {d 2 b a s e} ^ {\prime \prime}} \tag {7.3}
$$

$$
X _ {d 1, 2, 3 b a s e} ^ {\prime \prime} = \frac {X _ {d 1 , 2 b a s e} ^ {\prime \prime} \cdot X _ {d 3 b a s e} ^ {\prime \prime}}{X _ {d 1 , 2 b a s e} ^ {\prime \prime} + X _ {d 3 b a s e} ^ {\prime \prime}} \tag {7.4}
$$

The total system short circuit capacity therefore can be calculated:

$$
S _ {S C} = \frac {S _ {\text {b a s e}}}{X _ {d 1 , 2 , 3 , \text {b a s e}}} \tag {7.5}
$$

# Example 5

Calculate the equivalent subtransient reactance and short circuit capacity of three paralleled generators rated at $2 \times 2 0 0 0 \mathrm { k V A } / 1 6 \% X _ { d } ^ { \prime \prime }$ and $1 \times 1 5 0 0 \mathrm { k V } \mathrm { A } / 1 8 \% X _ { d } ^ { \prime \prime }$ depicted in Section 7, Figure 6, below:

![](images/5fb176b03c34028e56ff72219fd35b656d99c9a2d085f96961f7045443e9c50c.jpg)  
FIGURE 6 Example of Paralleled Generators

Generator $S _ { 1 }$ is, in this example, designated the “base unit” $S _ { b a s e }$ , therefore:

$$
X _ {d 2 b a s e} ^ {\prime \prime} = X _ {d 2} ^ {\prime \prime} \frac {S _ {1}}{S _ {2}} = 0.18 \cdot \frac {2000}{1500} = 0.24 (24 \%)
$$

$$
X _ {d 3 b a s e} ^ {\prime \prime} = X _ {d 3} ^ {\prime \prime} \frac {S _ {1}}{S _ {3}} = 0.16 \cdot \frac {2000}{2000} = 0.16 (16 \%)
$$

$$
X _ {d 1, 2 b a s e} ^ {\prime \prime} = \frac {X _ {d 1} ^ {\prime \prime} \cdot X _ {d 2 b a s e} ^ {\prime \prime}}{X _ {d 1} ^ {\prime \prime} + X _ {d 2 b a s e} ^ {\prime \prime}} = \frac {0.16 \cdot 0.24}{0.16 + 0.24} = \frac {0.0384}{0.4} = 0.096 (9.6 \%)
$$

$$
X _ {d 1, 2, 3 b a s e} ^ {\prime \prime} = \frac {X _ {d 1 , 2 b a s e} ^ {\prime \prime} \cdot X _ {d 3 b a s e} ^ {\prime \prime}}{X _ {d 1 , 2 b a s e} ^ {\prime \prime} + X _ {d 3 b a s e} ^ {\prime \prime}} = \frac {0 .096 \cdot 0.16}{0 .096 + 0.16} = \frac {0.01536}{0.256} = 0.06 (6 \%)
$$

$$
S _ {S C} = \frac {S _ {\text {b a s e}}}{X _ {d 1 , 2 , 3 , \text {b a s e}} ^ {\prime \prime}} = \frac {2 0 0 0}{0 . 0 6} = \underline {{3 3 . 3 3 3 M V A}}
$$

The results calculated above are based on one set of generator running conditions and will vary according to the number, kVA and $X _ { d } ^ { \prime \prime }$ of the generators on line at any one time. Consequently, both the magnitude and percentage of total harmonic current and harmonic total voltage will vary also.

Note: The short circuit MVA of parallel transformers can also be calculated using a similar method to that above.

S E C T I O N

# 8 The Effect of Unbalance and Background Voltage Distortion

# 1 Balanced Systems

In a power system with balanced sinusoidal voltages, the three line-to-neutral voltages are all of equal magnitude and displaced by 120 electrical degrees from each other, as shown in Section 8, Figure 1, below:

![](images/fa05aae80b6b000a92dd416e2c4006a458f9eb414fe0c8766d87f29bf36449bd.jpg)  
FIGURE 1 Balanced System

# 2 Unbalanced Systems

An unbalanced power system is so called when the magnitudes of the phase voltages are not equal and/or where the phase shift deviates from the normal phase separation value of 120 degrees, as depicted in Section 8, Figure 2, below:

![](images/e37e45449bd8c3c807c546b9eba032002c816b7d52baf2ef5203d5b9728715b5.jpg)  
FIGURE 2 Unbalanced System

Deviations from a balanced supply system can be attributed to the following:

• Unequal impedances within the power distribution system   
• Asymmetries in AC and DC drive commutation reactances   
• Large or unequal distribution of single-phase loads   
• Negative sequence fundamental frequency components in commutating voltages   
• Harmonic distortion of positive and negative sequence components   
• Unbalanced three-phase loads

# 2.1 Definition of Voltage Unbalance

Power system voltage unbalance can be defined using two methods. The first method is based on the theory of symmetrical components, which mathematically defines an unbalanced system into three separate balanced systems termed “positive sequence”, “negative sequence” and “zero sequence” systems as depicted in Section 8, Figure 3 below.

For a perfectly balanced system, both the negative sequence and zero sequence components would be absent.

![](images/2451c3866172a902e36c97705979941f6c01c854f853f9986a32485ed3a93430.jpg)  
FIGURE 3   
Symmetrical Components of an Unbalanced System   
Positive Sequence

![](images/aa33e3cbb9b6481cf87e43941cb98f94b7d78c5d8763a2b2cad4f9bffd8edf77.jpg)  
Negative Sequence

![](images/3f8d19e51d9b683b81ce2d66491f5d6df2679bc128d64979597f04df8c1714ef.jpg)  
Zero Sequence

As described in Section 3; when negative sequence components are applied to an induction motor, the resultant torque opposes the normal direction of rotation. Zero sequence components cannot produce a rotating magnetic field.

There are generally two definitions using symmetrical components which can be used to determine unbalance:

i) Negative Sequence Voltage Unbalance Factor $= { \frac { V _ { 2 } } { V _ { 1 } } }$ .. (8.1)   
ii) Zero Sequence Unbalance Factor $= \frac { V _ { 0 } } { V _ { 1 } }$ . (8.2)

where

V1 = positive sequence voltages

V2 = negative sequence voltages

V0 = zero sequence voltages

Zero sequence currents cannot flow in three-wire systems. Therefore it is the negative sequence components which must be used as a measure of unbalance. The negative sequence voltage unbalance factor, also known as the “Voltage Unbalance Factor” (VUF), or the “IEC definition” can be expressed as:

$$
\text {N e g a t i v e s e q u e n c e v o l t a g e u n b a l a n c e} = \frac {V _ {2}}{V _ {1}} = \sqrt {\frac {1 - \sqrt {3 - 6 \beta}}{1 + \sqrt {3 - 6 \beta}}} \tag {8.3}
$$

where

$$
\beta = \frac {V _ {a b} ^ {4} + V _ {b c} ^ {4} + V _ {c a} ^ {4}}{\left(V _ {a b} ^ {2} + V _ {b c} ^ {2} + V _ {c a} ^ {2}\right) ^ {2}} \dots \tag {8.4}
$$

However, the NEMA (National Electrical Manufacturers Association, in the USA) has a much simpler definition:

$$
\text {V o l t a g e} = \frac {\text {M a x i m u m d e v i a t i o n f r o m m e a n o f} \left(V _ {a b} , V _ {b c} , V _ {c a}\right)}{\text {M e a n o f} \left(V _ {a b} , V _ {b c} , V _ {c a}\right)} \tag {8.5}
$$

Note that in Equations $8 . 3 / 8 . 4$ and 8.5, line-to-neutral voltages should not be used, as the associated zero sequence components will introduce errors. Also note that the IEC definition (Equations 8.3/8.4), being more mathematical, tends to be the more accurate.

When a balanced three-phase load is connected to an unbalanced supply, the currents then drawn from the supply will also be unbalanced. As it is impossible to guarantee completely balanced supplies, it is normal to stipulate the amount permissible on a power system in order that equipment, especially rotating machines, is not adversely affected (see 8/2.2). $2 \% { - } 2 . 5 \%$ is usually the maximum unbalance specified.

# 2.2 Effect of Unbalanced Loading on Rotating Machines

A significant effect of unbalance is that associated with induction motors, which often form a substantial part of the electric load. As mentioned above on unbalanced voltages, the negative sequence components in the machine air gap oppose the direction of rotation, causing torque pulsations and increasing the temperature rise of the motor as it tries to maintain its output torque and speed. Induction motors on unbalanced supplies will also exhibit additional audible noise.

It is worth re-emphasizing that for every $1 0 ^ { \circ } \mathrm { C }$ rise above rated temperature, the life of motor winding insulation reduces by $50 \%$ (i.e., on a $2 0 \mathrm { { } ^ { \circ } C }$ rise the motor insulation life is reduced by $7 5 \%$ ) as illustrated in Section 8, Figure 4.

![](images/62a8fee84b85ba700e75786b88a1824043a0e54cd2d76aa0076a5a21da8d7e2b.jpg)  
FIGURE 4 Reduction of Insulation Life with Temperature

In addition, when a balanced induction motor is connected to an unbalanced supply, the resultant line currents can be several times that of percentage voltage unbalance as shown below.

For positive sequence voltages the motor slip, $S _ { 1 } ,$ , would be:

$$
S _ {1} = \frac {N _ {s} - N _ {r}}{N _ {s}} \tag {8.6}
$$

where

$$
N _ {s} \quad = \quad \text {s y n c h o n o u s s p e e d}
$$

$$
N _ {r} \quad = \quad \text {r o t o r s p e e d}
$$

For negative sequence voltages, the motor slip, $S _ { 2 }$ , can be expressed in terms of slip, $S _ { i } ,$ as follows:

$$
S _ {2} = \frac {N _ {s} + N _ {r}}{N _ {s}} = \frac {N _ {s} - N _ {r}}{N _ {s}} + 2 \frac {N _ {r}}{N _ {s}} = S _ {1} + 2 \frac {N _ {r}}{N _ {s}}
$$

$$
S _ {1} = \frac {N _ {s} - N _ {r}}{N _ {s}} = 1 - \frac {N _ {r}}{N _ {s}}, \text {t h e r e f o r e ,} \frac {N _ {r}}{N _ {s}} = 1 - S _ {1}
$$

$$
S _ {2} = S _ {1} + 2 \left(1 - S _ {1}\right) = 2 - S _ {1}. \tag {8.7}
$$

The impedance of an induction motor is largely dependent on the motor slip. At conditions of high slip (for example, at start-up or locked rotor), the impedance is small. Consequently, the impedance will be large at conditions of low slip, such as that associated with normal running conditions.

Similarly, the positive sequence slip, $S _ { 1 }$ , is usually negligible (i.e., almost zero), whereas the negative sequence slip, $S _ { 2 } { \mathrm { : } }$ would be large. Therefore, the ratio of positive sequence to negative sequence impedance could be expressed by:

$$
\frac {Z _ {1}}{Z _ {2}} \approx \frac {I _ {\text {s t a r t i n g}}}{I _ {\text {r u n n i n g}}} \tag {8.8}
$$

If the positive sequence current is expressed as $I _ { 1 } = \frac { V _ { 1 } } { Z _ { 1 } } ,$

and the negative sequence current by $I _ { 2 } = \frac { V _ { 2 } } { Z _ { 2 } }$

It can be seen therefore that $\frac { I _ { 2 } } { I _ { 1 } } = \frac { V _ { 2 } } { V _ { 1 } } \times \frac { I _ { s t a r t i n g } } { I _ { r u n n i n g } }$ startingI .. (8.9) runningI

Using the above Equation 8.9, it can be determined that the connection of an induction motor with a locked rotor current of $60 \%$ full load current would result a $30 \%$ unbalance in motor currents if connected to a supply system with $5 \%$ unbalance.

In order to minimize the effect on motors due to unbalanced voltages, NEMA has produced graphically the necessary motor derating factor according to the degree of voltage unbalance (Section 8, Figure 5). Please note that NEMA also do not advise any motor to be operated if the voltage unbalance is more than $5 \%$ , whatever the actual motor loading.

![](images/b0f7cb841caad72437637750d60271711f85e3e4557cfdd458a28b12c629e762.jpg)  
FIGURE 5 Derating on Induction Motors of Unbalanced Supplies

# 2.3 Effect of Unbalanced Loading on Harmonics

The wave shape and characteristic harmonics of rectifier bridges are significantly affected by voltage unbalance. Section 8, Figure 6 shows a typical input current waveform from a three-phase 6-pulse AC PWM drive with additional reactance (AC line reactor or DC bus) on a system with balanced supplies.

![](images/5995d659b40ce6a570c89f3104c58c14cf6f552118cbd936b939ab853f258193.jpg)  
FIGURE 6 Typical 6-Pulse AC PWM Drive Input Current Waveform on Balanced Voltages

The effect when $5 \%$ and $1 5 \%$ voltage unbalance is introduced is illustrated in Section 8, Figures 7 and 8, below:

![](images/17b83c2059ede63d7b84b5d216dd7a5cb9cab09ea9acb205dd20eaba949e752f.jpg)  
FIGURE 7 Typical 6-Pulse AC PWM Drive Input Current Waveform on $5 \%$ Voltage Unbalance

![](images/ed6b8615b7c8135cb850303e3cab9b9bc85cc4974894947c98355e9a74f66f37.jpg)  
FIGURE 8 Typical 6-Pulse AC PWM Drive Input Current Waveform on $15 \%$ Voltage Unbalance

The affect of voltage unbalance is to introduce uncharacteristic harmonics, including $2 ^ { \mathrm { n d } } , 3 ^ { \mathrm { r d } } , 9 ^ { \mathrm { t h } }$ , etc., and possibly DC in the power system. In addition, the unbalanced currents can lead to increased thermal stress on the drive components. The magnitude of the drive DC bus voltage on AC PWM drives would also be reduced, resulting in subsequent tripping on “undervoltage – DC bus”. Unbalance also contributes to the misfiring of SCRs and other power devices, which further increases the production of uncharacteristic harmonics and the total harmonic current distortion.

The problem with the nature of uncharacteristic harmonics is that they are difficult to predict and, consequently, rarely are accounted for in the design of equipment. It is often easier to address the causes of the uncharacteristic harmonics, such as unbalance, than attempt to “design-out” their effect with harmonic filters.

Section 8, Figure 9, below, illustrates the effect of unbalance on the harmonic spectrum of a 6-pulse AC PWM drive. Note the large $3 ^ { \mathrm { r d } }$ harmonic and other triplens $( 6 ^ { \mathrm { t h } } , 9 ^ { \mathrm { t h } } , 1 5 ^ { \mathrm { t h } } , 2 \dot { 1 } ^ { \mathrm { s t } } . . . )$ and even order harmonics (e.g., $4 ^ { \mathrm { t h } }$ and $6 ^ { \mathrm { t h } }$ ) and DC.

![](images/1ec2b71b6dfd4c08bb33af04f3feb49c0eb1473264900091faeb2b3180b30fed.jpg)  
FIGURE 9 Harmonic Spectrum of 6-Pulse AC PWM Drive on Unbalanced Voltages (Fundamental Component Removed)

# 2.4 Voltage Unbalance and Multi-pulse Drives and Systems

Voltage unbalance (and voltage distortion) significantly degrades the performance of phase shift and other multi-pulse harmonic mitigation systems (e.g., quasi-multi-pulse). When 12-pulse, 18-pulse and other configurations are discussed, it is often assumed that there is total harmonic cancellation of specified harmonics due to the respective phase shift. For example, a 30-degree shift in theory cancels the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonics (see Section 10, “Harmonic Mitigation,” for full information). However, due to tolerances in the transformer windings, inter-bridge reactors, rectifier bridges, etc., there will be residual $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic currents present after mitigation.

More significantly, the effect of supply unbalance can erode the performance of multi-pulse drives and other phase-shifted systems. Section 8, Figures 10 and 11 illustrate the effect of $1 \%$ , $2 \%$ and $3 \%$ voltage unbalance on 12-pulse and 18-pulse drive system, respectively.

![](images/a5d34efd93c1b2fa86d0d46d854848f17173bfdab8313c7187cfacdc12ed0263.jpg)  
FIGURE 10 Unbalance and the Effect on 12-Pulse Drives

![](images/0e49f7fe2cbbcd0f1f08f50d21152914679fbfb26b1049a97b366e64d07f39d4.jpg)  
FIGURE 11 Unbalance and the Effect on 18-Pulse Drives

# 2.5 Background Voltage Distortion and Multi-pulse Drives and Systems

Background voltage distortion adversely affects the performance of most forms of harmonic mitigation, especially multi-pulse drive systems, and can cause damage to those types utilizing “front end” capacitors [i.e., directly subject to high levels of distortion (e.g., EMI and carrier frequency filters within active filters)]. With a $V _ { t h d }$ of $5 \%$ on a marine power systems, it is not known to what degree background voltage distortion will further degrade the performance of drive systems which depend on phase shift for harmonic mitigation.

Section 8, Figure 12 illustrates the effect of background distortion on an 18-pulse drive at $50 \%$ and $100 \%$ loading.

Note: To estimate the effect on 12-pulse drives using double-wound phase shift transformers, add around $5 \%$ to the $I _ { t h d }$ figures below. (For example, at $1 0 0 \%$ load and $1 \%$ background $V _ { t h d } ,$ the $I _ { t h d }$ would be $5 \%$ for 18-pulse, therefore approximately $1 0 \%$ for 12-pulse, and so on).

FIGURE 12   
Effect of Background Voltage Distortion on 18-Pulse AC PWM Drive   
![](images/12cd72370afdada78ad87ff4dd247b9a84f98d69549a70258573fb39954cf937.jpg)  
18-Pulse (50% Load)→18-Pulse (100% Load)

# 2.6 The Effect of Voltage Unbalance and Background Voltage Distortion Using Software Modeling

Using harmonic estimation software, it is possible to further illustrate the relationship between voltage unbalance and/or pre-existing voltage distortion on multi-pulse drives (and other types of mitigation), the subsequent production of total harmonic current distortion and the resultant total harmonic voltage distortion.

In the examples cited below, a generator rated at $5 0 0 0 \mathrm { k V A }$ , 480 V, 60 Hz and $X _ { d } ^ { \prime \prime }$ of $14 \%$ was loaded with two off 900 HP, 12-pulse AC PWM drives (e.g., thruster drives) and $1 8 0 \mathrm { k W }$ of linear load. The 12-pulse drives were chosen as being the most common multi-pulse configuration in the marine sector.

Four sets of supply conditions were modeled:

• $0 \%$ voltage unbalance and $0 \%$ pre-existing voltage distortion   
• $2 \%$ voltage unbalance and $0 \%$ pre-existing voltage distortion   
• $0 \%$ voltage unbalance and $5 \%$ pre-existing voltage distortion   
• $2 \%$ voltage unbalance and $5 \%$ pre-existing voltage distortion

The examples below illustrate the differing total harmonic current distortion and associated total voltage distortion and voltage and current waveforms at the PCC#1 for each of the above supply conditions.

Note: If a smaller generator kVA and/or a higher value of $X _ { d } ^ { \prime \prime }$ been chosen for the given load, the resultant total voltage distortion in each supply condition would have been increased. The total harmonic current distortion would be reduced due to being limited by the leakage reactance of the “softer” source.

![](images/00f1d7890d53b54e11f8c54bc463ef47c00e1ca2d6d83ab6d4e30076cbe53c32.jpg)  
FIGURE 13a   
No Voltage Unbalance, No Pre-existing $V _ { t h d } - I _ { t h d } = 5 . 2 \%$ $V _ { t h d } = 4 . 9 \%$   
12 Pulse AC PWM Drives   
FIGURE 13b

# Voltage and Current Waveforms

# No Voltage Unbalance, No Pre-existing $V _ { t h d }$

Project: NEW.slv

Date:

Drive Transformer

5000.0 KVA

14.0%Z

480.V

60.Hz

Branch #1

12-Pulse System (parallel)

Load Balance Reactor $3 . 0 \%$

Smoothing Capacitor 45.0 mF

Load, HP 900.0

Loading,% 100.0

Branch #2

12-Pulse System (parallel)

Load Balance Reactor $3 . 0 \%$

Smoothing Capacitor 45.0 mF

Load, HP 900.0

Loading,% 100.0

Linear Load

180.0 KW

Disp. PF -0.85

![](images/73105e25202a2d5932e433d904e92910dcb301c76ccaf5b638a6921d0d10aead.jpg)  
ELECTRICALDEGREES

![](images/ff9b1953c1089a9cec76be3fe22a91bbaa5afbcd4892551a0605c282d06bd353.jpg)  
FIGURE 14a 2% Voltage Unbalance, No Pre-existing $V _ { t h d } - I _ { t h d } = 1 4 . 5 \%$ , $V _ { t h d } = 5 . 2 \%$

![](images/f4b5faf2c2f04a884dcdae0becd3446fbc553b30fead91bc2f5437ccbf76b4d7.jpg)  
FIGURE 14b Voltage and Current Waveforms $2 \%$ Voltage Unbalance, No Pre-existing $V _ { t h d }$

FIGURE 14c

Three-phase Current Waveforms

2% Voltage Unbalance, No Pre-existing $V _ { t h d }$

Project NEW.slv

Date:

15-12-2004

Voltage Source Distortion

Voltage Unbalance 2.00

Drive Transformer

5000.0 KVA

14.0%,Z

480.V

60.Hz

Current PCC#

Phase B

Phase C

Branch #1

12-Pulse System (parallel) Voltage PCC#

Load Balance Reactor $3 . 0 \ \%$

Smoothing Capacitor 45.0 mF

Load, HP900.0

Loading,% 100.0

Branch #2

12-Pulse System (parallel)

Load Balance Reactor 3.0 %

Smoothing Capacitor 45.0 mF

Load,HP 900.0

Loading,% 100.0

Linear Load

180.0K

Disp. PF -0.85

![](images/92220102f5787fa5d94ad35e1b2bf6bceeed4f98cc5528ee03f5c8b577973e47.jpg)  
FIGURE 15a

No Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d } - I _ { t h d } = 1 0 . 9 \%$ , $V _ { t h d } = 6 . 2 \%$

![](images/7ac817022803f2c359328a075eec9578e5de4bd3355bde919e7d6342bb5ec2b4.jpg)  
SOLV Lite

![](images/985c91fb24a482e9cb58016fdefa3f707d20e1793ae13dc6c8dce086fcb14c96.jpg)  
FIGURE 15b Voltage and Current Waveforms No Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d }$

![](images/444e7c12d34b36eff9828c360e3ba39ce039364de7c43a8f01bdb7785f4d16d4.jpg)  
2% Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d } - I _ { t h d } = 1 8 . 5 \%$ , $V _ { t h d } = 6 . 0 \%$   
12Pulse AC PWMDrives

FIGURE 16b

Voltage and Current Waveforms

2% Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d }$

![](images/cfbc11e5716930f84f5b8d3f33b6eeaebe23003be8f188548c6cb22bc1c16a1f.jpg)  
FIGURE 16c   
Three-phase Current Waveforms

$2 \%$ Voltage Unbalance, $5 \%$ Pre-existing $V _ { t h d }$

![](images/319cb9e5f18ac2c0943e05fef4205d9ddffe2f0f53fe80369c14c8705c4b6da5.jpg)

The summary of results for the resultant total harmonic current distortion $( I _ { t h d } )$ and total harmonic voltage distortion $( V _ { t h d } )$ for the above examples is tabled below:

TABLE 1 Variation in $I _ { t h d }$ and $V _ { t h d }$ with Voltage Unbalance and Pre-existing Voltage Distortion   

<table><tr><td>% Unbalance</td><td>% Vthd</td><td>Ithd</td><td>Vthd</td></tr><tr><td>0%</td><td>0%</td><td>5.2%</td><td>4.9%</td></tr><tr><td>2%</td><td>0%</td><td>14.5%</td><td>5.2%</td></tr><tr><td>0%</td><td>5%</td><td>10.9%</td><td>6.2%</td></tr><tr><td>2%</td><td>5%</td><td>18.5%</td><td>6.0%</td></tr></table>

# 2.7 Drive Mitigation – Unbalance and Background Voltage Distortion

Voltage unbalance and background voltage distortion both have a significant effect on drive harmonic mitigation, especially those using phase shifting techniques. A complete approach may be therefore necessary in order to maximize the performance of multi-pulse drives.

A number of so-called “broadband filters” for smaller drives offer good mitigation performance up to $2 \%$ unbalance and up to $2 \%$ background voltage distortion. Other designs, available up to significantly higher powers, can offer increased performance on both voltage unbalance and background distortion, well above $2 \%$ . (For example, there is a documented case of one patented design of “broadband filter” which is operating successfully on a cableship in excess of $22 \%$ background voltage distortion $( V _ { t h d } )$ due to the vessel having full electric propulsion.)

Active filters, usually designed based on IEEE 519 (1992) (i.e., a maximum of $< 5 \% ~ V _ { t h d } )$ may be unable to function reliably on higher levels of background $V _ { t h d }$ unless specifically designed for the given application.

# S E C T I O N

# 9 Resonance

# 1 What is Resonance?

The presence of capacitance in the power system can have a significant effect on the system impedance as it varies due to harmonic frequencies. In marine and offshore power supplies, conventional capacitor-based power factor correction banks may not be common, however directly connected capacitors are used in fluorescent lighting fittings for power factor correction and in other equipment. In addition, cable capacitance can also be problematic. Resonance results in high voltages and/or currents being present in the power system, causing damage to equipment and endangerment of personnel.

# 2 The Conditions under which Resonance Occurs

The system inductive reactance $( X _ { L } )$ is proportional to the frequency, whereas the capacitive reactance $( X _ { C } )$ is inversely proportional to frequency. “Resonance” is said to be achieved when the values of $X _ { L }$ and $X _ { C }$ are of the same value. There are two forms of resonance which need to be considered: “series resonance” and “parallel resonance”, as shown below in Section 9, Figure 1.

![](images/cb1854f19921ea9a6d512b81a4595bca6f854ec680df6525f73b9a6088fe1f6e.jpg)  
FIGURE 1a Series Resonance

![](images/28a4b4e95053505e228496ddc7a30001dc7ccf8ce6dcbd0d02d888f9f9edc3b2.jpg)  
FIGURE 1b Parallel Resonance

# 2.1 Series Resonance

For the series resistance-inductance-capacitance (RLC) circuit (see Section 9, Figure 1a), the total impedance at the resonant frequency reduces to the resistance component only. Where this value is low, high values of current at the resonant frequency will flow in the circuit at relatively low levels of exciting voltage. Under these conditions, series resonant will exist when:

$$
f _ {s} = f \sqrt {\left(\frac {S _ {t}}{S _ {C} Z _ {t}} - \frac {S _ {l} ^ {2}}{S _ {C} ^ {2}}\right)} \dots \tag {9.1}
$$

where

$$
f _ {s} \quad = \quad \text {s e r i e s}
$$

$$
f \quad = \quad \text {f u n d a m e n t a l f r e q u e n c y}
$$

$$
S = \text {t r a n s f o r m e r (o r g e n e r a t o r) r a t i n g}
$$

$$
Z = \text {t r a n s f o r m e r p e r u n i t i m p e d a n c e (o r g e n e r a t o r X _ {d} ^ {\prime \prime})}
$$

$$
S _ {C} = \text {c a p a c i t o r r a t i n g}
$$

$$
S _ {t} \quad = \quad \text {l o a d r e s i s t i v e r a t i n g}
$$

The main area of concern applicable to series resonance is that high capacitor currents can flow at relatively low levels of harmonic voltages. The actual current magnitudes are determined by the “quality factor”, $\mathcal { Q }$ , of the resonant circuit:

$$
Q = \frac {X _ {r}}{R} \dots \tag {9.2}
$$

where

$$
Q = \text {q u a l i t y f a c t o r}
$$

$$
X _ {r} \quad = \quad \text {r e a c t a n c e}
$$

$$
R \quad = \quad \text {r e s i s t a n c e}
$$

# 2.2 Parallel Resonance

In a parallel resonant circuit (Section 9, Figure 1b), the parallel impedance is significantly different. At the resonant frequency, the impedance is significantly high, resulting in high voltages being present in the circuit for relatively low source current values, although significantly larger magnitudes of circulating current also flow in the inductive-capacitance loop.

If the power system impedance is assumed to be entirely inductive, the resonant frequency, $f _ { p } ,$ can be calculated as:

$$
f _ {p} = f \sqrt {\left(\frac {S _ {s}}{S _ {c}}\right)} \dots \tag {9.3}
$$

where

$$
f _ {p} \quad = \quad \text {r e s o n a n t f r e q u e n c y}
$$

$$
f \quad = \quad \text {f u n d a m e n t a l f r e q u e n c y}
$$

$$
S _ {s} \quad = \quad \text {s h o r t c i r c u i t r a t i n g}
$$

$$
S _ {c} \quad = \quad \text {l o a d r e s i s t i v e r a t i n g}
$$

The above formula can also be written as:

$$
f _ {p} = f \sqrt {\left(\frac {M V A _ {s c}}{k V A r _ {c a p}}\right)} \tag {9.4}
$$

Note: Due to circuit topography, in the majority of systems with series resonance, parallel resonance will also occur, albeit at a lower frequency, as shown in Section 9, Figure 2, due to the contribution of the source inductance.

![](images/012c9f1681a58f30fb70ff01230b6b54482ddffe02720b6a0565651060add7d8.jpg)  
FIGURE 2 Series Resonance Frequency Response

Parallel resonance is, however, generally more common than series resonance as the majority of equipment is connected in parallel with switchboards. The example illustrated in Section 9, Figure 3 will therefore be based on parallel resonance.

Common problems associated with resonance include capacitor fuse failure and damaged capacitors (industrial power systems), spurious protective relay tripping, overheating on equipment and telephone interference.

# 3 Prevention of Resonance

In order to illustrate a common potential parallel resonance condition and how it can be prevented, it is necessary to use, as an application (see Section 9, Figure 3), a typical industrial system where AC variable speed drives are to be connected to a switchboard which also has capacitor-based power factor correction equipment attached.

The above application has two areas of concern:

i) The possibility of parallel resonance due to the presence of the drive harmonic currents and the installed capacitance and   
ii) The effect of the harmonics produced by the $2 \times 1 1 0 ~ \mathrm { k W }$ and $2 \times 1 3 2 \mathrm { k W }$ AC drives on the capacitors.

![](images/d059f1dd8fab45973fa3d98e323dc6930687ce63966fb913498a1a5363eeaf91.jpg)  
FIGURE 3 Typical Industrial Drive Application where Resonance is Possible

The resonance frequency based on the short circuit capacity of 30 MVA and capacitor bank rating of 600 kVAr can be calculated using the formula below:

$$
f _ {p} = f \sqrt {\left(\frac {M V A _ {s c}}{k V A r _ {c a p}}\right)}
$$

$$
f _ {p} = 6 0 \sqrt {\left(\frac {3 0 M V A}{6 0 0 k V A r}\right)}
$$

$$
f _ {p} = \underline {{3 5 3 \mathrm {H z}}}
$$

It will be noted at that the fundamental frequency of $5 0 \ \mathrm { H z }$ , the parallel resonant frequency occurs in the power system illustrated in Section 9, Figure 2 at around the 3rd harmonic $( 1 5 0 \ \mathrm { H z } )$ . In order to prevent resonance, a “detuning reactor” has to be connected to “adjust” the parallel resonance point such that it does not coincide with any major characteristic harmonics $( 5 ^ { \mathrm { t h } } , 7 ^ { \mathrm { t h } } , 1 1 ^ { \mathrm { t h } } , 1 3 ^ { \mathrm { t } }$ h, etc.).

The usual practice is to reduce the resonance point to below the $5 ^ { \mathrm { t h } }$ harmonic. The detuning reactor can be used to tune the circuit to around $2 2 5 ~ \mathrm { \bar { H z } } \mathrm { - } 2 3 5 ~ \mathrm { H z } ~ ( 4 . 5 ^ { \mathrm { t h } } \mathrm { - } 4 . 7 ^ { \mathrm { t h } } )$ $( 4 . 5 ^ { \mathrm { t h } } { - 4 . 7 ^ { \mathrm { t h } } }$ , being typical frequencies). The tuned resonant frequency may be reduced to below the $3 ^ { \mathrm { r d } }$ harmonic if significant triplen harmonics are also present (more common on four-wire systems). On $6 0 ~ \mathrm { H z }$ supplies, the tuned frequencies would be $20 \%$ higher.

# 3.1 The Effect of Adding a Detuning Reactor

The addition of the detuning reactor does not protect the capacitors from the effect of harmonic currents. That problem will still exist. The detuning reactor only prevents resonance with major characteristic harmonics occurring. However, the connection of the reactor to the capacitor bank does increase the voltage at fundamental frequency. This is due to the fact that the inductive reactance subtracts from the capacitive reactance, thus decreasing the circuit reactance overall and increasing the capacitor bank fundamental current. The higher value of fundamental current significantly increases the capacitor voltage, as illustrated in Section 9, Figure 4.

![](images/da9d4faf7936d30d684a2709d217cd98f4ca1e91cfd773ed56ef43e904fbcd5e.jpg)  
FIGURE 4 Simplified Connection of Detuning Reactor to Capacitor Bank

With reference to Section 9, Figure 4 above, the total reactance at fundamental frequency $5 0 ~ \mathrm { H z }$ , in this case) :

$$
X = X _ {C} - X _ {L}. \tag {9.5}
$$

$$
V _ {C} = V _ {\sup } \cdot \frac {X _ {C}}{X} \dots \tag {9.6}
$$

where

$$
V _ {C} = \text {c a p a c i t o r v o l t a g e}
$$

$$
V _ {s u p} = \text {s u p p l y v o l t a g e}
$$

$$
X = \text {r e s u l t a n t r e a c t a n c e}
$$

$$
X _ {C} = \text {c a p a c i t i v e r e a c t a n c e}
$$

$$
X _ {L} = \mathrm {i n d u c t i v e r e a c t a n c e}
$$

For example, using the above formula, a value of reactor $10 \%$ the value of the capacitive reactance is connected to the capacitor bank, therefore:

$$
X = 1 - 0. 1 = 0. 9
$$

$$
\mathrm{so} V _ {C} = 380 \cdot \frac {1}{0 .9} = \underline {{423 \mathrm{~V}}} (11 \% \text {voltage increase})
$$

As capacitor banks are usually rated for a maximum of $10 \%$ overvoltage, ignoring any supply variations and tolerances, the capacitors may have to be replaced. However, a number of reactor manufacturers do produce designs of detuning reactors which do not increase the capacitor voltage levels significantly.

However, if the supply voltage is less than the capacitor rated voltage (capacitor voltage ratings are usually in steps), then it may be possible to retain the original capacitor bank subject to it being derated (i.e., having its kVAr capability reduced) from nameplate value using the following formula:

$$
k V A r _ {\text {a c t u a l}} = k V A r _ {\text {n a m e p l a t e}} \left(\frac {V _ {C}}{V _ {\text {n a m e p l a t e}}}\right) ^ {2} \tag {9.7}
$$

For example, a $4 6 0 ~ \mathrm { V }$ rated, $6 0 0 { \mathrm { ~ k V } } \mathrm { A r }$ capacitor bank nominally used on $3 8 0 ~ \mathrm { V }$ would have to be derated based on a $10 \%$ detuning reactor being connected:

$$
k V A r _ {\text {a c t u a l}} = 6 0 0 \mathrm {k V A r} \left(\frac {4 3 2}{4 6 0}\right) ^ {2} = \underline {{5 3 0 \mathrm {k V A r}}}
$$

# 4 Possibilities of Resonance on Vessels and Offshore Installations

The most likely potential for resonance lies with fluorescent lighting fitting power factor correction capacitors and/or cable capacitance. Resonance is observable when the high voltages and/or currents cause damage to equipment, especially directly connected capacitors, or where unusually high, localized voltage or current readings are measured.

There have been instances of resonance on offshore production installationss with large variable drive installed load, up to $8 5 \%$ of total loading. Fluorescent lights have burned out due to internal capacitor resonance. There have been other instances, when another platform with no onboard power generation has been supplied from a “mother” platform, significant parallel resonance problems were encountered due to the capacitance of the connecting cable between both platforms. Until then, no resonance was apparent on the larger platform, which had both a power generation plant and a high level of power system harmonics.

When using a harmonic analyzer, resonance can be seen where there are abnormally high voltages or current harmonics at particular frequencies which are not characteristic of the type of equipment connected to the power system (i.e., the magnitude of harmonic voltage or current should decrease in inverse proportion to the harmonic number). The harmonic frequency at which the high levels of voltage or current occur is the resonant frequency.

However, damping is usually provided by supply and load resistances, which significantly reduces the peak impedances ( $10 \%$ resistive loading has a significant impact on peak impedances). Loads such as induction motors are mainly inductive and provide limited damping. Long cable lengths, however, do tend to suppress resonance.

# S E C T I O N

# 10 Mitigation of Harmonics

The majority of electrical nonlinear equipment, especially three-phase types, normally associated with larger powers will often cause the need for the addition of mitigation equipment in order to attenuate the harmonic currents and associated voltage distortion to within the necessary limits.

Depending on the type of solution desired, the mitigation may be supplied as an integral part of nonlinear equipment (e.g., an AC line reactor for AC PWM drive) or as a discrete item of mitigation equipment (e.g., an active filter connected to a switchboard). The majority of this Section relates to the mitigation options available for three-phase nonlinear equipment, particularly electronic converters for AC and DC motors, battery chargers, UPS systems, which often share similar input rectifier architecture. Mitigation for both individual applications (e.g., per drive basis) and for “global mitigation” (i.e., a common harmonic mitigation solution for a group of nonlinear equipment) are described. For single-phase three-wire and four-wire (i.e., three-phase and three-phase $^ +$ neutral) systems only “global mitigation” has been addressed.

While a minor amount of “natural mitigation” may occur as described below in Subsections 10/1 and 10/2, mitigation measures may have also to be considered in order that voltage distortion, as a result of the nonlinear load(s), is maintained within permissible limits. The options available, depending on the application and desired level of attenuation, are:-

x Neutral current eliminators and phase shift systems (for four-wire systems)   
Standard AC line and DC bus reactors   
x Wide spectrum (reactor/capacitor) filters   
x Duplex reactors   
x Passive L-C (inductance/capacitance) filters   
Multi-pulse (phase shifting)   
x Quasi-multi-pulse (phase staggering)   
Active filters   
x Active front ends (sinusoidal input rectifiers)

# 1 Effect of Phase Diversity on Harmonic Currents

On power systems with multiple nonlinear loads, some harmonic cancellation may occur due to “phase angle diversification” between the multiple harmonic sources. As can be seen in the example given in Section 10, Figure 1, each harmonic voltage (or current) has a phase angle associated with it. Note that the first column is the harmonic (H00 is the DC component), the second column is the percentage harmonic current distortion and the third column is the respective phase angle (note that the “–” denotes a negative phase angle. The result of multiple harmonic sources is a degree of harmonic cancellation which is determined by the respective individual harmonic voltages (or currents) and the associated phase angles.

![](images/4c3a65d0f2f576d6431302b1d39e8aaeee52288b4ccf6b496bc104ae3781648f.jpg)  
FIGURE 1 Harmonic Voltage Data to ${ \pmb 5 0 } ^ { \mathrm { t h } }$ Harmonic with Respective Phase Angle Information

# 2 Effect of Linear Load on Harmonic Currents

As detailed in Section 3, linear loads such as induction motors and transformers are adversely affected by harmonic currents and voltages. While these linear loads do not “absorb” harmonics as such, the harmonic voltages and currents are dissipated as heat losses within the equipment. Therefore it could be argued that the distortion would be higher on systems without linear loads compared to those with linear loads, based on the same magnitude of harmonic currents. (This “opinion” appears to be confirmed by recent industrial research which suggested that harmonic currents travel to ground through directly connected induction motors in parallel with the path through the utility supply transformer, the supply cabling and the nonlinear loads. Calculations suggested a reduction in the resultant harmonics voltage of some 0.06 per unit on a system with induction motors compared to without induction motors.)

On systems with mixed load (i.e., linear and nonlinear), the “total demand distortion of current” (“TDD”), as defined in IEEE 519 (1992), will be lower the greater the proportion of linear load to nonlinear load. Note that the TDD is not the same as the $I _ { t h d } .$ . (The TDD is expressed as the measure of total harmonic current distortion, per unit of load current. For example, a $30 \%$ total current distortion measured against a $50 \%$ load would result in a TDD of $1 5 \%$ .)

Induction motors are naturally inductive and are often citied as increasing the level of distortion by shifting the natural power system resonant frequency nearer to a significant characteristic harmonic, whereas purely resistive loads generally dampen possible resonance.

Induction motors do have higher impedances at higher frequencies and, therefore, can be seen to “absorb” a portion of the high frequency harmonic currents. However, this does not usually have a significant effect on the overall harmonic currents and subsequent voltage distortion within the power system. The type of rotor (i.e., squirrel cage or wound type) and the air gap has an influence on the absorption of the higher frequency harmonic currents.

# 3 Mitigation of Harmonics on Three-wire Single-phase Systems

If large single-phase nonlinear loads (or large numbers of small single-phase nonlinear loads) are present in the three-wire single-phase distribution system, local harmonic mitigation may be necessary to minimize the contribution of the single-phase nonlinear load(s) to the overall voltage distortion in the power system.

Depending on the nature and magnitude of the necessary mitigation and power system configuration, two common methods of local mitigation can usually be applied:

i) Phase shifting

ii) Active filters

# 3.1 Phase Shifting

Section 10, Figure 2 shows a typical lighting (or distribution) transformer supplying two fluorescent lighting distribution panels. One panel has no phase shift and the other has 30 degrees displacement (i.e., phase shift). (Note: Subsection $1 0 / 7$ , “Phase shifting” describes the theory behind this technique.)

Essentially, the 30-degree phase shift at the input (i.e., primary side) of the phase shift transformer causes the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic currents to be in “anti-phase” (i.e., 180 degrees out of phase) with the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic currents produced by the other lighting panel (and any other connected nonlinear loads). The result is that the majority of the $5 ^ { \mathrm { t h } }$ and $\bar { 7 } ^ { \mathrm { t h } }$ harmonic currents on the busduct are “cancelled” in theory (some residual will remain due to, for example, unbalance). Since the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ are the largest two characteristic harmonics, the resultant $I _ { t h d }$ and the subsequent $V _ { t h d }$ will normally be significantly reduced.

![](images/cf8c509780426c03d65f7547b399246f4a5629e0ae1c7be4a2772e6e3cd526e3.jpg)  
FIGURE 2 Phase Shifting of Three-wire Nonlinear Loads

The above scheme is similar to a “quasi-12-pulse system” for three-phase drives and other large nonlinear loads (see Subsection 10/8, “Phase Staggering”). Similar schemes are configurable using larger pulse numbers (and therefore great harmonic cancellation), depending on the number and ratings of nonlinear loads.

# 3.2 Active Filtering

Active filters can be used on three-wire lighting and other “domestic” distribution (see 10/4.2 and 10/11.1 for further information regarding the theory and operation of this type of equipment).

# 4 Mitigation of Harmonics on Four-wire Single-phase Systems

Some vessels, such as passenger ships, have four-wire systems for “hotel loads”, with either grounded or insulated neutrals. It is necessary to consider how the harmonic currents in these four-wire systems, often with a large number of nonlinear single-phase loads, can be mitigated.

As described in Section 4, in a four-wire single-phase power system (i.e., three-phase $+ \ N )$ the three individual phase currents contain triplens (i.e., odd multiples of three, particularly $3 ^ { \mathrm { r d } }$ harmonic) which add cumulatively in the neutral, often overloading the neutral conductors and distribution transformers and causing other problems.

Two common methods of addressing the problem of excessive neutral currents due to triplens are available. These are specially designed “zero sequence” transformers and active filters, the latter specifically configured to inject into all three phases and the neutral conductor.

# 4.1 Zero Sequence Mitigation of Triplens on Four-wire Single-phase Systems

As discussed in Section 4, triplen currents $( 3 ^ { \mathrm { r d } } , 9 ^ { \mathrm { t h } } , 1 5 ^ { \mathrm { t h } } . . . )$ add cumulatively in the neutral conductor, resulting in neutral currents being well in excess of phase currents. On some passenger vessels, this load can be in the range of ${ 5 { - } 8 \mathrm { M W } }$ . It is therefore important that any excessive neutral currents (and the associated problems thereof due to nonlinear loads) are attenuated as far as practicable. Section 10, Figure 3 re-emphasizes why that on four-wire systems with nonlinear load the neutral current can often exceed the phase currents, even when perfectly balanced.

![](images/5f465e86ec235a3114210805680f30560e60bb8541c2549362a9cc8897c4d26d.jpg)  
FIGURE 3 Four-wire System with Nonlinear Loads

An effective method of reducing the neutral currents in a four-wire system is to use “zero sequence transformers”, also called “zig-zag transformers”. As illustrated in Section 10, Figure 4, below, a zero sequence transformer comprises multiple windings on a common core. The windings of at least two phases are wound in opposition around each core leg in order that the magnetic fluxes created by the zero sequence currents will oppose, and therefore cancel out, providing an alternative low impedance path when connecting in parallel on a four-wire system. Note that the positive and negative sequence fluxes (e.g., due to 5th, 7th, $1 1 ^ { \mathrm { t h } }$ , $1 3 ^ { \mathrm { t h } }$ harmonics, etc.) remain 120 degrees out of phase and are not cancelled out.

![](images/6675848a17bb362f23619d51a6993230933e755a34d0e172acd424e82103b4d9.jpg)  
FIGURE 4 Operation of a Zero Sequence Transformer

Section 10, Figure 5 shows the connection of a zero sequence transformer to the four-wire systems depicted in Section 10, Figure 2. In practical terms, the zero sequence transformer removes the majority of the triplen harmonics from the neutral current and returns them to the three-phases, and in doing so, also balances the phase currents.

![](images/56de876b0dbee5affbb15561e6e3468fb1c3e9bdf2397e9528bf2657d32c964f.jpg)  
FIGURE 5 Zero Sequence Transformer on Four-wire System

# 4.1.1 Combined Zero Sequence Mitigation and Phase Shifting for Neutral Current Reduction and Harmonic Mitigation

“Zero sequence transformers” (ZST) can also be used in conjunction with phase shift transformers to provide effective harmonic attenuation from $3 ^ { \mathrm { r d } }$ to up to $1 9 ^ { \mathrm { t h } }$ harmonics, depending on the numbers and rating of discrete loads. Section 10, Figure 6, below, illustrates the use of ZST and a combined phase shift and zero sequence transformer with 30 degrees phase shift to treat the $3 ^ { \mathrm { r d } }$ harmonic current and other triplens and to provide “cancellation” of the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonics within the system.

# FIGURE 6 Zero Sequence Transformer and Combined Phase Shift Transformer with ZST to Cancel Triplen and $5 ^ { \mathrm { t h } }$ and ${ \boldsymbol { 7 } } ^ { \mathrm { t h } }$ Harmonic Currents

![](images/5a43f5e36cf4f2c1b4a9f4a809027fd93cab4ccd3818a998e28ba6a7c63dcfe9.jpg)

# 4.2 Active Filters for Four-wire Systems

An alternative method to reduce the triplen harmonics is an active filter. The theory of operation of active filters in covered in Subsection 10/7. With reference to Section 10, Figure 7, below, the active filter monitors the current in the three phases (and also the neutral, depending on manufacturer) via the current transformers (CTs) installed on the load side of the connection (note that source side monitoring is also used on occasion).

The voltage signal is fed into, for example, a “notch filter”, which removes the fundamental component (i.e., $5 0 \ \mathrm { H z }$ or $6 0 \ \mathrm { H z }$ component). The remainder of the signal is termed a voltage signal which is an “image” of the harmonic distortion current. That voltage signal is then converted into a current signal, amplified and injected into the load as “harmonic cancellation current” which matches the needs of the nonlinear load. In theory, therefore, the active filter, if rated correctly in terms of “harmonic cancellation current”, provides the load with the harmonic current it needs to function and the source is only supplies the fundamental current which is sinusoidal.

Note: The active filter should be dimensioned in terms of “harmonic cancellation current” based on the actual currents drawn with the filter in circuit.

![](images/12ecc4cc44832dc5023f969425779c931ce42928f6a99e3e6e8adb39d300782e.jpg)  
FIGURE 7 Block Diagram of Active Filter on Four-wire Application

# 5 Standard Reactors for Three-phase AC and DC Drives

Reactors, also known as “inductors”, are coils of wire wound around a laminated steel core, similar in construction to power transformers. The laminated steel core is usually impregnated to reduce audible noise due to eddy currents. Reactors are a simple but effective method to reduce the harmonics produced by nonlinear loads and are usually applied to individual loads such as variable speed drives.

In order to understand the benefit of a reactor, one must consider the impact it has on the power circuit. When the current through a reactor changes, the result is an induced voltage (in opposition to the applied voltage) across its terminals according to the formula:

$$
E = L \frac {d i}{d t} \tag {10.1}
$$

where

$$
E = \text {i n d u c e d v o l t a g e}
$$

$$
L \quad = \quad \text {i n d u c t a n c e , i n H e n r y s}
$$

$$
\frac {d i}{d t} = \text {r a t e o f r i s e o f v o l t a g e}
$$

It can therefore be seen that if the voltage available is limited, consequently, the rate of rise of voltage will also be limited. Similarly, if the circuit current or supply conditions are such that they create a voltage step change, then the reactor tends to limit the rate of raise of voltage, thus slowing the rate of rise of current. It is the latter characteristic which is useful in limiting the harmonic currents produced by electrical variable speed drives and other nonlinear loads.

In addition, the AC line reactor does reduce the total harmonic voltage distortion $( V _ { t h d } )$ at the input to the reactor compared to that at the terminals of the drive or other nonlinear load.

In electrical variable speed drives, reactors are used in both AC and DC types. They are often used in addition to other harmonic mitigation methods. On AC drives, reactors are used on the AC line side (called AC line reactors), in the DC bus (called DC bus reactors) or both, depending on the type of drive design and/or necessary performance of the supply.

# 5.1 Reactors for AC PWM Drives

A simple block diagram illustrating a standard 6-pulse AC PWM variable frequency drive is shown in Section 10, Figure 8, below. Depending on the drive rating, most manufacturers offer reactors either standard or as options.

![](images/b60efd8487ca3ba6af2aecd97b43b7058b14d6f93bd74e74d020bc618b509018.jpg)  
FIGURE 8 Circuit Diagram of Standard 6-Pulse AC PWM Drive

In Section 10, Figure 8, above, the following are represented:

• R1 represents the resistance of the DC bus reactor L1 (if fitted).   
• R1 and R2 have negligible effects on the harmonic currents, so will not be considered further.   
• L1 represents the inductance of a DC bus reactor of various values (where fitted).   
• L2 represents the AC line inductance of various values plus that of the supply.

Please note that in a perfectly-balanced system, the harmonic currents drawn by a 6-pulse AC PWM drive will consist of the fundamental and the characteristic harmonics as represented by:

$$
h = n \cdot p \pm 1
$$

where ${ \begin{array} { r l r l } { h } & { } & { = } & & { { \mathrm { h a r m o n i c ~ n u m b e r } } } \\ { p } & { } & { = } & & { { \mathrm { p u l s e ~ n u m b e r } } } \\ { n } & { } & { = } & & { { \mathrm { i n t e g e r } } } \end{array} }$

For 6-pulse drives: $h = 6 n \pm 1$ . The harmonics are therefore 5, 7, 11, 13, 17, 19….

In order to simplify comparisons regarding the performance of the various inductances of AC line and DC bus reactors, the DC bus reactor is divided into two discrete elements, as shown in Section 10. Figure 8 (i.e., the total DC bus reactance is $2 \times$ the value of L1).

To maintain the results independent of current rating, all the values of reactors will be referred to as “percentage reactances” referred to the current flowing in the AC supply. This means that the voltage at the fundamental frequency across the AC line reactor will be “x” percent of input voltage of the drive [i.e., the voltage will be $\mathit { \Omega } ^ { \omega } \mathbf { \Sigma } _ { x } ^ { o } \mathbf { \Lambda } _ { o } ^ { \prime \prime }$ of the L-L voltage/1.732 (i.e., the phase voltage)].

Percentage reactance can be defined as follows:

$$
\% X = \frac {2 \cdot \pi \cdot f \cdot L \cdot I _ {A C} \cdot 100}{\frac {V _ {A C}}{\sqrt {3}}} \dots \tag{10.2}
$$

where

$$
f \quad = \quad A C \text {l i n e f r e q u e n c y}
$$

$$
I _ {A C} = A C \text {l i n e c u r r e n t}
$$

$$
V _ {\mathrm {A C}} = \quad \mathrm {A C l i n e v o l t a g e}
$$

$$
L \quad = \quad \text {i n d u c t a n c e , i n H e n r y s}
$$

$$
X = \text{reactance,in}\%
$$

The formula can be transformed to calculate the necessary reactance in Henrys for any given percentage impedance as follows:

$$
L = \frac {\% X \cdot \frac {V _ {A C}}{\sqrt {3}}}{2 \cdot \pi \cdot f \cdot I _ {A C} \cdot 100} \dots \tag{10.3}
$$

# Example 1

Calculate the value of reactance in henrys necessary for a $3 \%$ reactor for a 630 kW (845 HP), AC PWM drive having a full load input current of 670 A. The supply to the drive is three-phase, 690 V, 60 Hz.

$$
\begin{array}{l} \text {Necessary reactance} L = \frac {\% X \cdot \frac {V _ {A C}}{\sqrt {3}}}{2 \cdot \pi \cdot f \cdot I _ {A C} \cdot 100} \\ = \frac {3 \cdot \frac {6 9 0}{\sqrt {3}}}{2 \cdot \pi \cdot 6 0 \cdot 6 7 0 \cdot 1 0 0} \\ = \frac {1 1 9 5 . 2}{2 5 2 5 8 4 0 5} \\ = 4 7. 3 \times 1 0 ^ {- 6} \\ = 4 7. 3 \mu \mathrm {H} (\text {m i c r o - H e n r y s}) \\ \end{array}
$$

# Example 2

Calculate the percentage reactance of three-phase line reactor having of value of $7 7 ~ \mu \mathrm { H }$ for use with a $3 1 5 \mathrm { k W }$ (400 HP) PWM drive on a 480 V, 60 Hz supply. Drive rated input current is 395 A.

$$
\begin{array}{l} \% X = \% X = \frac{2\cdot\pi\cdot f\cdot L\cdot I_{AC}\cdot 100}{\frac{V_{AC}}{\sqrt{3}}} \\ = \frac {2 \cdot \pi \cdot 6 0 \cdot 7 7 \times 1 0 ^ {- 6} \cdot 3 9 5 \cdot 1 0 0}{\frac {4 8 0}{\sqrt {3}}} \\ = \frac {1 1 4 7}{2 7 7} \\ = 4.14 \% \\ \end{array}
$$

It should be noted that the attenuation of the drive harmonic currents is dependent on the value of percentage reactance inserted into the drive, whether in the AC line, DC bus or both. The effects of varying percentage reactance for both AC line and DC bus reactors and their resultant effect on both the magnitude and harmonic number can be observed by reference to the following illustrations:-

# 5.1.1 AC Line Reactors Only

The use of AC line reactors are more common than DC bus reactors, and in addition to reducing harmonic currents, also provide a measure of surge suppression for the drive input rectifier. The disadvantage, as mentioned in 10/4.1, is that there is a voltage drop at the terminals of the drive, approximately in proportion to the percentage reactance at the terminals of the drive.

![](images/8d6d4808ae076a08f76baa70d43b18adaf854b980f5615ac619c8fcde436a70c.jpg)  
FIGURE 9 Variation of Harmonic Currents with AC Line Reactance Only

As illustrated above (Section 10, Figure 9), the input harmonics produced by PWM drives with no reactance is relatively high when the AC line reactor is less than $1 \%$ . As the percentage AC line reactance increases, however, the harmonic currents decrease, although the rate of decrease diminishes somewhat as percentage reactance increases. AC line reactors of values $2 \div 3 \%$ are common which $5 \%$ being the usual maximum.

# Example 3

Using the information in Section 10, Figure 9, the harmonic currents for a $3 \%$ AC line reactor can be estimated:

5th harmonic – 40%   
• 7th harmonic – 15%   
• 11th harmonic – 5%   
• 13th harmonic – 4%   
• 17th harmonic – 4%   
• 19th harmonic – 3%

Based on the above estimation, the total harmonic current distortion $( I _ { t h d } )$ as a percentage of the fundamental current based on harmonics 5, 7, 11, 13, 17, 19 would be:

$$
\begin{array}{l} I _ {t h d} = \sqrt {4 0 ^ {2} + 1 5 ^ {2} + 5 ^ {2} + 5 ^ {2} + 4 ^ {2} + 3 ^ {2}} \\ I _ {t h d} = 43.49 \% \\ \end{array}
$$

# Example 4

Using similar information from Section 10, Figure 9, we can also estimate the harmonic currents and $I _ { t h d }$ for a $5 \%$ AC line reactor.

5th harmonic – 32%   
• 7th harmonic – 9%   
• 11th harmonic – 4%   
• 13th harmonic – 3%   
• 17th harmonic – 3%   
• 19th harmonic – 2%

The total harmonic current distortion $( I _ { t h d } )$ as a percentage of the fundamental current based on harmonics 5, 7, 11, 13, 17, 19 would again be as follows:

$$
\begin{array}{l} I _ {t h d} = \sqrt {3 2 ^ {2} + 9 ^ {2} + 4 ^ {2} + 3 ^ {2} + 3 ^ {2} + 2 ^ {2}} \\ I_{thd} = \underline{33.8\%} \\ \end{array}
$$

# 5.1.2 DC Bus Reactors

A relatively small number of AC PWM drive manufacturers do insert reactance in the DC bus, thus avoiding any voltage drops associated with AC line reactors. These drives normally need discrete surge suppression to protect the input bridge rectifier devices and to limit any surges which could affect the DC bus voltage levels. A similar exercise can be carried out to estimate the respective harmonic currents when a DC bus reactance is installed (Section 10, Figure 10).

Note that below rated load, the DC bus reactor percentage reactance is lower than at rated load. Therefore, at less than rated load, the percentage harmonic currents will be higher than anticipated. This is due to the reactors being designed (usually for economic reasons) to partially saturate at rated load. Therefore, at reduced load, the inductance increases.

![](images/6b2af84af187de6cbdd95156a9487e60b622ee814ece61d95d90143131cfe421.jpg)  
FIGURE 10 DC Bus Reactance Only in AC PWM Drive

# Example 5

Using the information in Section 10, Figure 10, the harmonic currents for a $3 \%$ DC bus reactor can be estimated:

5th harmonic – 30%   
• 7th harmonic – 20%   
• 11th harmonic – 8%   
13th harmonic – 7.5%   
• 17th harmonic – 5%   
• $1 9 ^ { \mathrm { t h } }$ harmonic – 5%

Based on the above estimation, the total harmonic current distortion $( I _ { t h d } )$ as a percentage of the fundamental current based on harmonics 5, 7, 11, 13, 17, 19 would be:

$$
I _ {t h d} = \sqrt {3 0 ^ {2} + 2 0 ^ {2} + 8 ^ {2} + 7 . 5 ^ {2} + 5 ^ {2} + 5 ^ {2}}
$$

$$
I _ {t h d} = \underline {{38.35 \%}}
$$

# 5.1.3 Reactance on Both Sides of the Input Rectifier

On larger drives, both AC line and DC bus reactors may be used. Both are used when the short circuit capacity of a dedicated supply is relatively low compared to the drive kVA or if the supply susceptible to disturbances.

Section 10, Figure 11, below, illustrates the effect on the $5 ^ { \mathrm { t h } }$ harmonic of varying values of AC line and DC bus reactance.

![](images/0bbaebaf712071be50d24d2a6bfca082dd8232ea9d83561c7c7389514824bc71.jpg)  
FIGURE 11 Variation in ${ \pmb 5 } ^ { \dagger \hbar }$ Harmonic Current for Differing Values of AC Line Reactance and DC Bus Reactance

Note that when the percentage reactance in the DC bus is low, increasing the AC line reactance does result in a significant reduction in the $5 ^ { \mathrm { t h } }$ harmonic, as depicted above. A similar effect is apparent for higher order harmonics. However, when the percentage reactance in the DC bus is high $4 \%$ or more), increasing the percentage reactance in the AC line results in a smaller reduction in the harmonic currents, the reduction diminishing as the harmonic number diminishes.

It should be stated that harmonic current magnitudes are also dependent to a lesser extent on the value of the DC bus capacitance per amp of load current. More importantly, it is the short circuit capacity of the source which largely determines the harmonic current magnitudes. As described previously, a “stiff” source (e.g., $5 \%$ transformer) will permit more harmonic current to be drawn by the nonlinear load without unduly distorting the voltage, whereas a “soft” source (e.g., $X _ { d } ^ { \prime \prime }$ of $1 7 \%$ ) will restrict the magnitude of harmonic current due to its leakage reactance, but this harmonic current may significantly distort the supply voltage.

# 6 AC Line Reactors for DC SCR Drives and AC Drives with SCR Input Rectifiers

AC line reactors for use with AC and DC drives having full controlled SCR input bridges reduce harmonic currents in a similar manner to that illustrated in 10/4.1.1 on a pro rata basis (i.e., similar percentage attenuation, but perhaps based on differing individual harmonic current magnitudes depending on the type of drive and inductance on the DC side of the bridge rectifier). They also improve the true power factor and provide surge suppression.

However, another important function of the AC line reactors in these applications is the reduction of line notching (see Subsection 2/6, “Line Notching”). In DC drives, AC line reactors are therefore often termed “commutation reactors”.

With reference to Section 10, Figure 12, below; it should be re-emphasized that the line notching occurs 6 times per cycle on a 6-pulse bridge and is the result of the commutation of the load current from one pair of SCRs to another. During this process, the line voltage is short circuited, producing two primary notches per cycle. In addition, there are four secondary notches of lower amplitude which are “notch reflections” due to the commutation of the other two legs of the three-phase bridge rectifier. The short circuit current duration, or “notch width”, is a function of the DC output current of the rectifier and the total inductance in the power system.

![](images/aa35a52900307759c38be78cee9a9d6e015852d22245dffb348d8d0a4bcf5e5d.jpg)  
FIGURE 12 Primary and Secondary Notching

The notch depth is a function of where the notch is viewed on the power system. The further away it is seen from the terminals of the bridge rectifier, the less significant it will seem. This can be explained with reference to Section 10, Figure 13, below.

![](images/970129a5aa228b76d8e325b1250a27dc77fdca2ae03ed329094b83faf2dabe1f.jpg)  
FIGURE 13 Line Impedance Distribution and the Effect of Notching

At Point “A” (the rectifier terminals), the notching will be at its most severe, similar to that illustrated in Section 10, Figure 13, if it is assumed that all the inductances $L _ { 1 } , L _ { 2 }$ and $L _ { 3 }$ are all equal. Due to the voltage divider type circuit over the three identical inductances, the notch depth at Point “B” (the input to the AC line reactor), will be $6 6 \%$ of the maximum depth seen at Point “A”. At Point $^ { \circ \circ } \mathrm { C } ^ { \circ \circ }$ , it will be $33 \%$ of the depth seen at Point “A”. Therefore, it can be seen that the more the inductance between the source of the notch the less the depth. However, as explained in Section 2, the insertion of additional inductance will reduce the notch depth but will increase the notch width.

Note: It is the notch depth which is usually the more important due to interference with equipment which relies of zero crossing for operation.

The notch size can be calculated using the line side inductance and the bridge rectifier load current during the commutation period.

$$
\text {N o t c h D e p t h} = \frac {L _ {1} + L _ {2}}{L _ {1} + L _ {2} + L _ {3}} \tag {10.4}
$$

If all inductance are equal, as per the example (Note: Actual $L$ values of inductances will have to be inserted for practical calculations):

$$
\text {Notch Depth} = \frac {2 L _ {1}}{3 L _ {1}} = 66 \%
$$

$$
\text {N o t c h} = L \cdot I \cdot (\text {V o l t s} - \mu \text {S e c s}) \tag {10.5}
$$

where

$$
L = \text {i n d u c t a n c e o f d i s t r i b u t i o n t r a n s f o r m e r a n d s u p p l y i n d u c t a n c e (c a b l e s , e t c .) i n}
$$

$$
I = \text {D C l o a d c u r r e n t a t t i m e o f c o m m u t a t i o n , A m p s}.
$$

Note that the inductance, $L$ , is frequency-dependent and is expressed in Henrys. For generators, the substransient reactance, $X _ { d } ^ { \prime \prime }$ , is the impedance of the fundamental harmonic frequency and is expressed in Ohms. In order to compare transformers with generators, one needs to compare the inductance $L$ and reactance $X$ for both. $X _ { d } ^ { \prime \prime }$ mainly comprises reactance $X$ and can be expressed in Ohms [this value, divided by 2πf (frequency)] will result in inductance $L$ .

$$
\text {N o t c h D e p t h} = \frac {\text {N o t c h A r e a}}{\text {C o m m u t a t i o n V o l t a g e}} \tag {10.6}
$$

where the commutation voltage $= \sqrt { 2 } E _ { L L } r m s \sin \alpha$ and

$$
\alpha = \text {d e l a y a n g l e o f S C R i n d e g r e e s}
$$

$$
E = \text {l i n e t o l i n e v o l t a g e a t t i m e o f c o m m u t a t i o n}.
$$

It should also be noted that only additional reactance at the rectifier terminals will have a desired effect in attenuating the notching. Placing additional reactance elsewhere usually results in little improvement.

Note that standard AC line reactances are usually available on a per drive size basis and that calculations as illustrated above are not normally necessary. The industry standard is a $3 \%$ AC line reactor. This can reduce the notch depth by up to $50 \%$ of the depth seen at the rectifier terminals. Larger reactors, up to $5 \%$ , are not common, as the larger reduction in notch depth is accompanied by a large increase in the notch width, which may interfere with the rectifier operation.

The effectiveness of any additional inductance is dependent on the impedance of the system. The lower the impedance, the less effective any additional inductance will be in reducing the notch depth.

Notch limits are specified in North American Harmonic Recommendation IEEE 519 (1992) and are currently as follows:

<table><tr><td></td><td>Special Applications (2)</td><td>General Systems</td><td>Dedicated Systems (3)</td></tr><tr><td>Notch Depth</td><td>10%</td><td>20%</td><td>50%</td></tr><tr><td>Vthd</td><td>3%</td><td>5%</td><td>10%</td></tr><tr><td>Notch Area (AN) (1)</td><td>16,400</td><td>22,800</td><td>36.500</td></tr></table>

# Notes

The value of AN for other than $4 8 0 \mathrm { V }$ systems should be multiplied by V/480.

1 In volt-microseconds at rated voltage and current.   
2 Special applications include airports and hospitals.   
3 A dedicated system is exclusively dedicated to a converter load.

# 7 Special Reactors for Three-phase AC and DC Drives

As can be seen above, “standard” reactors provide only a limited measure of harmonic attenuation which is normally not sufficient to maintain compliance with harmonic standards, harmonic recommendations or to allow problem-free installations. For higher performance, more sophisticated reactor designs (for example, wide spectrum filter and the “Duplex” reactor) may be considered.

# 7.1 Wide Spectrum Filters

Wide spectrum filters are multi-limbed reactors fitted with a small capacitor bank, as shown in Section 10, Figure 14, below. The three reactor windings are wound on a common core. L1 on the source side is the “high impedance winding”, whose design is such that it is “tuned” to prevent the importation of upstream harmonics. On the load side, the “compensating winding”, L2, decreases the through impedance, reducing the voltage drop. The output of L2 is tuned to remove a wide spectrum of load-side harmonics. A unique design of reactor, L3, permits a smaller capacitor bank to be used to reduce voltage boost and reactive power at no load.

Note: The capacitor bank KVAr is around $3 0 \%$ of installed filter KVA and should operate with any generator.

The wide spectrum filter tend to be largely unaffected by voltage unbalance and background voltage distortion (e.g., there is a documented case of a marine wide spectrum filter successfully operating with $2 2 . 1 \%$ background distortion on a cableship with full electric propulsion) and can be used on both 6-pulse single drive and multiple drive applications. As it is a serial device (see Section 10, Figure 14), it effectively isolates the loads from the effects of any upstream (i.e., background) harmonics.

![](images/3598988dffaa243ba5b085f9719bb1dba177760c3ed2f6e78aac4c3a649c79aa.jpg)  
FIGURE 14 Wide Spectrum Filter Schematic

Section 10, Figure 15 illustrates the current and voltage waveform from a standard 6-pulse 200 HP/150 kW AC PWM drive with $3 \%$ DC link inductance. The $I _ { t h d }$ is $3 9 . 9 \%$ .

![](images/bcaef84f2cff7e8a2aa7067c2f9e47bdf3e771a35c0023625b1594da0dba652b.jpg)  
FIGURE 15 200 HP/150 kW AC PWM Drive with $3 \%$ DC Bus Reactor – $I _ { t h d } = 3 9 . 9 \%$

The wide spectrum filter is connected to the drive(s) as per a standard AC line reactor (i.e., between the mains supply and the drive, as shown in Section 10, Figure 16). The output voltage of the wide spectrum filter is trapezoidal (Section 10, Figure 17), which forces the drive input bridge rectifier devices (e.g., diodes or SCRs) to conduct over a longer time period at a lower peak value, thus reducing the harmonics produced at the input. The performance on 6-pulse AC PWM drives reduces the $I _ { t h d }$ to around $5 \text{‰}$ , irrespective of whether the drive has AC line or DC bus reactors.

![](images/e9eae9f923ac7a6bb485ad860996b75934785329934d2cd3b25f1f54378c10fe.jpg)  
FIGURE 16 Typical Wide Spectrum Filter Connection Diagram – AC PWM Drive

![](images/fb4256af34ea9c43c214510b8b528f97c6654355bd138bb48d5c1e8b6a1611ff.jpg)  
FIGURE 17 Trapezoidal Output Voltage from Wide Spectrum Filter

The effect of the wide spectrum filter on the $2 0 0 ~ \mathrm { H P } / 1 5 0 ~ \mathrm { k W }$ AC PWM drive (Section 10, Figure 15) is to reduce the $I _ { t h d }$ from $3 9 . 9 \%$ to $4 . 6 \%$ , as illustrated below in Section 10, Figure 18.

The wide spectrum filter can be applied to AC drives, DC drives with fully controlled SCR input bridges and UPS systems.

![](images/264e8d49f0c88830dc1399ace997c75b6dec599c5a53ec034e179bf4005d5b6d.jpg)  
FIGURE 18 Mains Waveform with Wide Spectrum Filter – $I _ { t h d } = 4 . 6 \%$

A typical example of a the performance of a wide spectrum filter and a 350 HP, 480 V, $6 0 \ : \mathrm { H z }$ AC PWM drive is shown in Section 10, Figure 19, below. The drive has a standard $3 \%$ AC line reactor and has an $I _ { t h d }$ of $3 3 . 8 1 \%$ . With a wide spectrum filter connected in series, the $I _ { t h d }$ reduces to $3 . 4 8 \%$ .

Without Filter $I _ { t h d }$ is $3 3 . 2 8 \%$ . With Filter $I _ { t h d }$ is $3 . 4 8 \%$ .

![](images/1c434e2a4f504438c48367040b0e1e5229e3ace38f96077cd3b8dedf65c47dd2.jpg)  
FIGURE 19 Typical Wide Spectrum Filter Performance 350 HP AC PWM Drive with $3 \%$ AC Line Reactance

Wide spectrum filters are available in a range up to around $3 0 0 0 \ \mathrm { H P } / 2 2 5 0 \ \mathrm { k W }$ and can be applied to multiple drives on the basis that the rating (in $\mathrm { H P / k W ) }$ is a sum of all the connected drives. However, no fixed speed induction motors or other non-drive load should be connected to a wide spectrum filter, due to trapezoidal nature of output voltage. Typical applications in the marine and offshore sectors are drives with power ratings of less than $2 . 5 ~ \mathrm { M W }$ , for main propulsion, thrusters, cableship winches, compressors, fan and pump drives, etc.

Wide spectrum filters can be retrofitted to existing drives without the need for drive modifications, whether for single drive or for multiple drive applications.

Wide spectrum filters may be developed for systems with voltages above 1 KV and with higher power ratings (above 2.5 MW) for those applications with 6-pulse AC drives in systems with voltages above 1 KV.

Note: For 12-pulse drives and other loads, a variant of the wide spectrum filter is available. As can be seen from Section 10, Figure 20, below, a wide spectrum filter is inserted in the primary of the phase shift transformer and results in an $I _ { t h d }$ of around $3 . 4 \%$ , similar to that expected from a 24-pulse drive, but without the susceptibility to performance degradation due to voltage unbalance and background voltage distortion normally associated with phase shift drives. The unit is around $3 0 { - } 3 5 \%$ the physical size of a standard 6-pulse wide spectrum filter.

![](images/8278a4e42c7982f45abe35d649df3fd7e63fa8a82f9742a3c286ce7d8692ef95.jpg)  
FIGURE 20 Wide Spectrum Filter with 12-Pulse AC Drive

The 12-pulse variants may be useful, perhaps as retrofits, in applications where the use of single or multiple 12-pulse drives and/or other equipment are insufficient to guarantee compliance with harmonic recommendations, rules or standards or where levels of voltage distortion are proving troublesome.

# 7.2 Duplex Reactors

Duplex reactors originated in Europe in the 1930s and have been used on a number of vessels since the mid 1980s, mainly for mitigation of the harmonics produced by main propulsion drives and also with shaft generators to minimize the distortion of the voltage supplied to the ship’s busbar system.

Duplex reactors have two galvanically separated but tightly magnetically coupled coils (Section 10, Figure 21). The primary coil is connected similarly to that when using standard reactors (i.e., in series with the load). The secondary coil is connected to the primary coil using an anti-parallel connection so that a corrective voltage is induced which, when “added” to the primary distorted voltage, produces a clean compensated voltage, as illustrated in Section 10, Figures 22a, 22b and 22c.

![](images/6a752c0c2cf2581584d5a242b0054330682aa541c94f84e2ddc14257db282976.jpg)  
FIGURE 21 Duplex Reactor Schematic

The generator $X _ { G }$ should be determined from short circuit calculations. The inductance of the duplex reactor is designed to be equal to the subtransient reactance $( X _ { d } ^ { { \prime \prime } } )$ of the generator(s). The addition of the duplex reactor into the system results in the short circuit capacity in “Subsystem 1”, as shown in Section 10, Figure 21, being $50 \%$ of that if it were connected directly to the generator(s). This results in the system impedance being doubled in value, and therefore, the voltage distortion on this side of reactor will increase accordingly (if $X _ { G } ^ { \prime \prime } = X _ { D 1 } = X _ { D 2 } )$ .

![](images/8c8eff5521e5e1015d36e60013a0f14038f4ae2be16f472778697d582e668778.jpg)  
FIGURE 22a System Voltage Waveform

![](images/8c581c69f7ce98b04ce2e8b8659f71fa22aef8968ab3562fecdedf3db8f9c553.jpg)  
FIGURE 22b Duplex Reactor Correction Voltage

![](images/fa0969e4814d6f75090b97db647faa4a11c9642382493735ed87c10ba3ddadb4.jpg)  
FIGURE 22c “Corrected” System Voltage

Section 10, Figure 23 illustrates a typical application of duplex reactors, applied instead of standard AC line or “commutating” reactors for the mitigation of inrush voltage during the commutation of SCR based drive current (in this instance, on a research vessel with two DC SCR main propulsion drives). The accuracy and quality of the correction voltage is dependent on a number of factors. The optimum ratio of the winding turns on the duplex reactor results from the ratio of the subtransient reactance $( X _ { d } ^ { \prime \prime } )$ of the generator(s) to the primary reactance of duplex reactor.

As the reactance at the generators is dependent on the rating and number of generators on line, it is necessary to either have some means of switching the ratio of turns on the duplex reactor or to base optimization on one operational condition with a given number of generators on line. For the system illustrated in Section 10 Figure 23, the optimum condition was with two generators running, as can be seen from Section 10, Figure 24.

In Section 10, Figure 23, note the differentiation of the “distorted bus”, fed via the primary windings of the reactors which are connected to the DC converters, and the “clean bus” (which may contain “distortion” due to the reduced fault rating), fed via the secondary windings of the duplex reactors.

![](images/e98b98f226877d0cab265b1fd4251b434c90165d5824441742042f53021d9583.jpg)  
FIGURE 23   
Application of Duplex Reactors on Main Propulsion Drives   
FIGURE 24

![](images/2e61807920a398dbefad6af7b16cb4b5100cf910f88f911d26857a3993838b04.jpg)  
Variation of System $V _ { t h d }$ with Number of Generators on Line (Figure 23)

The performance of duplex reactors depends upon the system subtransient reactance, and hence the number of generators on line at any one time. However, for the duplex reactor performance to be as independent as possible from the number of generators in service, a configuration is needed such that the reactors are closely coupled to the generators, as illustrated in Section 10, Figure 25. Some recent passenger ships with full electric propulsion based on cycloconverter drives have this configuration of duplex reactors. With reference to Section 10, Figure 25, as the branch for supply of the propulsion bus carries higher load current than the general service bus, the number of turns on the propulsion branch of the duplex reactor is $50 \%$ of that on the general service branch. As a consequence, there is a small variation in the voltages on the two systems. However, the generator voltage regulators both maintain general service bus voltages constant and the variation in voltage between both the propulsion and general service buses within tolerable limits.

![](images/ad043cca9b8485520208d3d881ef5054e0681959eabddf0974152901db7639d2.jpg)  
FIGURE 25 Duplex Reactors on Passenger Ships with ${ \bf 2 } \times { \bf 2 0 }$ MW Cycloconverters

The important points of the configuration in Section 10, Figure 25 are:

i) According to actual measurements performed on one of these passenger vessels (with $2 \times 2 0$ MVA cycloconverter drives) on differing numbers of generators operating, the voltage distortion $( V _ { t h d } )$ in the general service bus will not unduly affected by the propulsion load. (The $2 . 7 \%$ $V _ { t h d }$ measured on the general service bus was largely attributed to the nonlinear loads connected to the service bus, not a reflection the propulsion load voltage distortion.)   
ii) The prospective short circuit current in the general service bus will be reduced to $33 \%$ of that without the duplex reactors in the circuit. Therefore, any voltage distortion due to the nonlinear load connected to the general service bus will be slightly higher than without the diplex reactors.

iii) The prospective short current in the propulsion bus will be reduced to $6 6 \%$ of that apparent without duplex reactors. The voltage distortion, $V _ { t h d }$ on the propulsion bus will therefore be around $33 \%$ higher than without duplex reactors installed.   
iv) The general bus and propulsion bus are effectively isolated. Therefore any disturbances, transient or continuous, including any short circuit effects emanating from the propulsion bus, will not be reflected on the general service bus.

As mentioned previously, duplex reactors are now applied to shaft generators where they can reduce the $V _ { t h d }$ of the voltage supplied to the ship’s busbars to $- 8 \%$ (Section 10, Figure 26).

![](images/4a3b2757cbc0d2fae10d29f4f79724dc17507d9118419cc0105e5a34325d06de.jpg)  
FIGURE 26 Application of Duplex Reactors on Shaft Generators

Power systems with multiple converter loads can utilize duplex reactors as illustrated in Section 10, Figure 27, below. This example needed two duplex reactors and optimization would have to be designed for the parallel operation of two generators. However, it has to be stated that for other than two-generator operation, only partial performance would be achieved. The application of duplex reactors is often a compromise between economics, as mentioned above, and performance. It should be noted that the generators supplying systems with duplex reactors are subjected to higher levels of distortion due to reduction in fault rating. This will have to be taken into account in generator design(s). In addition, on power systems with duplex reactors, large fixed speed AC squirrel cage motors may have an increased voltage dip and reduced torque at start-up. Special design and/or precautions will be necessary to minimize these effects.

The development and application of duplex reactors may not yet have reached their full potential, and therefore, their use may not be as straightforward or as well-understood as other technologies. Duplex reactors have to be encompassed in the design of the vessel at an early stage and retrofitting may be difficult.

![](images/379bc50ac360f0f662d91da60e0d423a749a3f735194d880ce8475b085a504b4.jpg)  
FIGURE 27 Application of Duplex Reactors Vessel with Multiple AC SCR Based Drives

# 8 Passive L-C Filters

Passive L-C filters, comprising inductors, capacitors and occasionally resistors have been utilized for harmonic mitigation for many years. Their operation relies on the “resonance phenomenon” which occurs due to variations in frequency in inductors and capacitors; (see Section 9 for further information) which is:

$$
Z = 2 \pi f L \quad \text {f o r a n i n d u c t o r}. \tag {10.8}
$$

where

$$
Z \quad = \quad \text {i m p e d a n c e}
$$

$$
f \quad = \quad \text {s u p p l y f r e q u e n c y}
$$

$$
L \quad = \quad \text {i n d u c t a n c e}
$$

Therefore the impedance of an inductor increases with frequency.

$$
Z = \frac {1}{2 \pi f C} \quad \text {f o r a c a p a c i t o r} \tag {10.9}
$$

where

$$
C = \text {c a p a c i t a n c e}
$$

The impedance of a capacitor decreases with frequency.

At series resonance, the impedance of an inductor $( X _ { L } )$ and capacitive reactance $( X _ { C } )$ of the capacitor are equal, and therefore, the resistance, which is generally low, is the only impedance in the circuit. The circuit $^ { \mathrm { { e } } } Q ^ { \mathrm { { , } } }$ (i.e., quality factor), which determines the “sharpness” of the “tuning” of the passive filter, is calculated thus:

$$
Q = \frac {X _ {r}}{R} \dots \tag {10.10}
$$

where

$$
Q = \text {q u a l i t y f a c t o r (u s u a l l y i n t h e r a n g e o f 2 0 t o 1 0 0)}
$$

$$
X _ {r} \quad = \quad \text {r e a c t a n c e}
$$

$$
R \quad = \quad \text {r e s i s t a n c e}
$$

The resonant frequency for a series resonant circuit, and in theory, for a parallel resonant circuit, can be given as:

$$
f _ {0} = \frac {1}{\left(2 \pi \sqrt {L \cdot C}\right)} \dots \tag {10.11}
$$

where

$$
f _ {0} \quad = \quad \text {r e s o n a n t f r e q u e n c y , H z}
$$

$$
L = \text {f i l t e r}
$$

$$
C = \text {f i l t e r c a p a c i t a n c e , F a r a d s}
$$

The series passive filters, usually connected in parallel with nonlinear load(s), are “tuned” to offer very low impedance to the harmonic frequency to be mitigated (Section 10, Figure 28 shows the tuned characteristics of $7 ^ { \mathrm { t h } }$ harmonic filter). However, the inductance of the source has to be taken into account due to the production of parallel resonance at a frequency lower than that for series resonance (perhaps causing power system positive feedback and also resulting in the misfire of power devices, such as SCRs, for example). Section 10, Figure 28, below, illustrates absolute impedance for a $7 ^ { \mathrm { t h } }$ harmonic tuned filter over a range of frequencies.

Therefore, the formula above can be modified as follows for parallel resonance:

$$
f _ {0} = \frac {1}{\left(2 \pi \sqrt {\left(L _ {F} + L _ {\text {S o u r c e}}\right) \cdot C _ {F}}\right)} \dots \tag {10.12}
$$

where

$$
L _ {F} = \text {f i l t e r i n d u c t a n c e}
$$

$$
L _ {\text {S o u r c e}} = \quad \text {i n d u c t a n c e o n b u s b a r s}
$$

$$
C _ {F} = \text {f i l t e r c a p a c i t a n c e}
$$

![](images/8a2ed9ae94418adb32428b3b81c34d6da9e8e95d10579a6da21947fff8222763.jpg)  
FIGURE 28   
Absolute Impedance Characteristics for Tuned ${ \boldsymbol { 7 } } ^ { \mathrm { t h } }$ Harmonic Series Filter

There are a number of common passive filter configurations which are depicted in Section 10, Figure 29, below, with the “single tuned” filter being one of the most common. In practical use, $5 ^ { \mathrm { t h } }$ tuned filters, often with additional $7 ^ { \mathrm { t h } }$ tuned filters, are the most common configuration. Other multi-limbed filters; including possible $1 1 ^ { \mathrm { t h } }$ and $1 3 ^ { \mathrm { t h } }$ can also be applied. However, above the $1 3 ^ { \mathrm { t h } }$ harmonic, passive filter performance is poor, and they are rarely applied on higher-order harmonics.

![](images/0354cb774afb4516f53062d26e863ae49959754fd2437db602a20b31574e6b29.jpg)  
FIGURE 29 Common Configuration of Passive Filters

Section 10, Figure 30, shows the impedance characteristic for a multi-limbed filter with four discrete limbs tuned to the $5 ^ { \mathrm { t h } }$ (300 Hz), $7 ^ { \mathrm { t h } }$ (420 Hz), $1 1 ^ { \mathrm { t h } }$ $( 6 6 0 ~ \mathrm { H z } )$ and $1 3 ^ { \mathrm { t h } }$ $( 7 8 0 ~ \mathrm { H z } )$ harmonics depicted in Section 10, Figure 31). Note the respective parallel resonance for each filter below the series resonant points (these have been highlighted for the $1 \bar { 1 } ^ { \mathrm { t h } }$ harmonic in the example given).

![](images/ba7ebf2a7f8f4d7c24bd5d8091faa02b21f1ce892ea56880c957f06cf31bab2f.jpg)  
FIGURE 30 Simplified Connection of Multi-limbed Passive Filter

![](images/4349b02ee7d3220e63fe0da008ba94acf4568c0e5f290903dd67769d701a8b92.jpg)  
FIGURE 31 Impedance Characteristics of Multi-limbed Passive Filter

In the example (Section 10, Figure 30, above), the filter-tuned limbs would normally be tuned below the respective characteristic frequencies to prevent possible overloading and to compensate for the variation in capacitance over time due to the degradation of the capacitor dielectric (i.e., as the capacitor ages and/or if subject to higher temperatures, the capacitance decreases, increasing the reactance and thereby increasing the tuned filter’s resonant frequency). Typical values for each limb would be $4 . 7 ^ { \mathrm { t h } }$ (for $5 ^ { \mathrm { { t h } } }$ harmonic), $6 . 6 ^ { \mathrm { t h } }$ (for $7 ^ { \mathrm { t h } }$ harmonic), $1 0 . 5 ^ { \mathrm { t h } }$ (for ${ \dot { 1 } } 1 ^ { \mathrm { t h } }$ harmonic) and $1 2 . 4 ^ { \mathrm { t h } }$ (for $1 3 ^ { \mathrm { t h } }$ harmonic).

The passive resonance shown in Section 10, Figure 31 could be problematic, as the high impedances could result in additional voltage distortion of the respective harmonic currents at those frequencies. The parallel resonance frequencies can, however, be modified (i.e., shifted) by careful design of the $\boldsymbol { Q }$ factor (via the sharpness of the tuning) or by connecting resistance in parallel with the filter reactors, such as not to coincide with a major characteristic harmonic frequency. This practice is called “dampening”. A reduction in the $\mathcal { Q }$ factor has only a minor effect, and therefore, the addition of resistance in parallel with the reactor is often preferred, as it can achieve the necessary damping with relatively low fundamental losses compared to $\boldsymbol { Q }$ factor control. Dampening reduces the “sharpness” at the tuned frequency and increases the bandwidth of the filter, but at increased cost and reduced filter harmonic reduction performance.

Passive filters are susceptible to changes in source and load impedances. They do attract harmonics from other sources (i.e., from downstream of the PCC), and this must be taken into account in their design. Harmonic and power system studies are usually undertaken to calculate their effectiveness and to explore possibility of resonance in a power system due to their proposed use.

In order to address the problems above for specific applications, “drive applied” (or “trap”) filters are available, as illustrated in Section 10, Figure 32, below.

![](images/2929de325bb9031b344876d75c3cd9517bbc6eaf34318d97220e6bef4d3e356f.jpg)  
FIGURE 32 Simplified “Drive Applied” or “Trap” Filter for Variable Speed Drives

As can be seen above, a reactor (typically $5 \%$ reactance) is connected between the tuned passive filter and the source (reducing the supply voltage accordingly). The $5 \%$ reactor serves two functions:

i) It effectively isolates the passive filter from the source (and any pre-existing voltage distortion) and reduces the possibility of overloading due to downstream harmonics.   
ii) It further reduces the harmonic current spectrum on the source side.

It may be possible for “trap filters” to be applied to drive applications irrespective of source impedance and possibility of system resonance.

On marine power systems, frequency variations of $\pm 5 \%$ are common and would have an adverse impact on the performance of tuned passive filters. Similarly, if the source impedance were to change, filter performance would suffer. An example may be a passive filter for a bank of winch drives on a cableship. The design of the filter is based on that one vessel – if the drives and filter (often containerized) were moved to another vessel, the source impedances will most probably differ.

Tuned passive filters perform best a rated load with around $1 4 - 1 8 \% \ I _ { t h d } ,$ usually achievable from a well-engineered $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ limbed filter. At lesser loads, and especially at light load, the passive filter “leading” kVAr is impressed on the source. On industrial applications and utility supplies, this may not be problematic, but if connected to marine generators, this can be a significant issue, as most generators cannot support any more than around $20 \%$ leading kVAr due to the potential of “armature reaction” and resultant over-excitation and AVR (automatic voltage regulator) instability. Also, as alluded to above, design of passive filters is more complicated on generators due to increased frequency variations.

In marine and offshore applications, passive filters normally need in-depth studies to assess their suitability. They are often more suited to “dedicated systems” where the usually large, nonlinear loads, such as main electric propulsion drives and their associated power generation, are discrete from other loads.

# 9 Transformer Phase Shifting (Multi-pulsing)

For drives supplying $4 0 0 ~ \mathrm { H P } / 3 0 0 ~ \mathrm { k W }$ motors (or larger) and other large nonlinear equipment, “phase shifting” techniques have been commonly employed to reduce the input harmonic currents. Therefore, multiple input converter bridges are necessary, connected such that the harmonics produced by one bridge(s) cancels certain harmonics produced by other(s). In theory, certain harmonics, as determined by the number of converter bridges in the system, are eliminated at the input (i.e., primary side) of the phase shift transformer.

The technique of “phase shifting” the harmonic currents produced by one converter against those produced by another is also termed “multi-pulsing”, hence the term “multi-pulse drives”. The number of discrete converters in a system determines the “pulse number”. For example, a standard three-phase drive with one input converter is known as a “6-pulse” drive (the number of pulses relates to the number of pulses on the DC side of the rectifier):

$$
\text {N o . o f P u l s e s} = 6 \times \text {N o . o f 6 - p u l s e i n t r a c t i e r s i n c o n v e r t e r} \tag {10.13}
$$

If a drive, for example has two input rectifiers, it is known as a “12-pulse drive”, as depicted in Section 10, Figure 33, below. Similarly, with three input rectifiers it becomes an “18-pulse drive”. Pulse configurations up to 48-pulse are possible for very large systems. In addition to reducing the line side harmonics, phase shifting also reduces the voltage ripple on the DC side of the rectifier(s).

The theoretical cancellation of certain harmonic current is dependent on the “pulse number” based on the format, as known:

$$
P u l s e \quad N u m b e r \pm 1
$$

Therefore, in a 12-pulse system, the characteristic harmonic currents will be 11, 13, 23, 25, 35, 37, etc. It will be noted that the $5 ^ { \mathrm { t h } }$ , $7 ^ { \mathrm { t h } }$ , $1 7 ^ { \mathrm { t h } }$ and $1 9 ^ { \mathrm { t h } }$ harmonic are not listed. These are theoretically cancelled in a 12-pulse system where the lowest harmonic is now the $1 1 ^ { \mathrm { t h } }$ . Similarly, in an 18-pulse system, the characteristic harmonics will be 17, 19, 35, 37, 47, 49, etc. As can therefore be seen, the higher the pulse number, the more the lower order harmonics will be theoretically cancelled.

The amount of phase shift, in degrees, necessary is also a function of the number of converters employed:

$$
\text {P h a s e S h i f t} ^ {\circ} = \frac {6 0}{\text {N u m b e r o f c o n v e r t e r s}} \tag {10.14}
$$

For example, in the 12-pulse drive system illustrated in Section 10, Figure 31 (which has two 6-pulse converters) the necessary phase shift is:

$$
\text {P h a s e S h i f t} = \frac {6 0}{2} = \underline {{3 0 ^ {\circ}}}
$$

Similarly, an 18-pulse system having three converters would need a 20 degrees phase shift.

Historically, 12-pulse systems were the most common configuration, but in recent years, 18-pulse systems have become common in North America due to the requirements of IEEE 519 (1992). 12- pulse systems are still used in other parts of the world, but they are becoming less common due to the introduction of harmonic recommendations in an increasing number of countries. In the marine and offshore environment, however, 12-pulse systems were still relatively common, but it is now recognized that they have increasing difficulty complying with current harmonic recommendations, especially on larger or multiple loads.

In general terms, there are two main types of phase shift transformer used for drive harmonic mitigation:

i) Double-wound isolating transformer

ii) Polygonal non-isolating autotransformer

# 9.1 Double-wound Isolating Transformer Phase Shift Systems

The drive system depicted below (Section 10, Figure 33) comprises a double-wound isolating transformer with 30 degrees phase shift between the star and delta secondary windings, two 6-pulse input bridges, an “interbridge reactor”, a DC bus and an inverter bridge. This configuration provides for optimum cancellation of the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic, providing, however, that the circuit is carefully balanced and 120-degree conduction is forced in each of the rectifier bridges through the use of the DC interbridge reactor. AC interbridge reactors can also be used, but due to the voltage drop across them, DC reactors tend to be more common.

# FIGURE 33 12-Pulse AC PWM Drive with Double-wound Phase Shift Transformer

![](images/bf20daf958b0ccd6d947cf66a7656346674a06eb79a47330adf4dd32b837b8f5.jpg)

All phase shift systems, irrespective of pulse number, are susceptible to degradation in performance due to unbalance, whether in the voltage supply or through inaccuracies or tolerances during manufacturing of the transformer and/or the rectifiers. Section 10, Figure 34 illustrates the effect of minor unbalance $( < 1 . 5 \% )$ on performance of the double-wound-based 12-pulse system shown in Section 10, Figure 33, and is based on the following conditions:

• Transformer leakage impedance of $\sim 5 \%$   
• Supply impedance is $1 . 4 \%$   
• Completely balanced phase group impedances   
• Rectified voltage drops are completely balanced   
The interbridge reactor was dimensioned to limit the p-p current between bridges to $1 5 \%$ rated DC current

Note: There will always be some impedance unbalance, which will lead to an increase in the theoretical level of harmonics.

As can be seen from Section 10, Figure 34, below, a small increase in unbalance can result in significant increases in the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonics at the primary side of the phase shift transformer. In order to reduce the effects of unbalance in the secondary windings and rectifiers, the transformer leakage impedance should be relatively high, with $5 \%$ being typical. In order to provide as near to specified performance, the transformer should be designed with a relatively low value for secondary voltage unbalance (for example, around $0 . 3 \%$ ) to allow for other practical unbalances (e.g., from rectifiers).

![](images/3f46a04a66c95330dfb7d3aa2ee1db16b4fdb3e0eece4ca0ed08a0fdef3dd512.jpg)  
FIGURE 34 Double-wound 12-Pulse Phase Shift Transformer Unbalance Between Secondary Voltages

Double-wound transformers need an accurately design system and increased leakage reactance. Note that on carefully designed systems, the interbridge reactor may not be necessary. However, if balance is not achieved, the results are higher than expected harmonic levels, poor bridge rectifier and transformer utilization and possible problems in rating the bridge electronic devices (i.e., diodes or SCRs).

A well-designed 12-pulse drive system, based on a double-wound phase shift transformer can give a practical performance of around $1 0 \small { - } 1 2 \% I _ { t h d }$ based on ideal supply conditions in terms of background voltage distortion and voltage unbalance.

Double-wound transformers tend to be common on marine applications, as they can provide common mode noise attenuation (i.e., between conductors and ground) via the use of copper shielding between windings. This can serve the purpose of a crude, but effective, EMI filter for the drive. On vessels with IT power systems (i.e., insulated neutrals), standard drive EMC or EMI filters cannot be used, as one side of the filter capacitors needs a connection to ground. The capacitors would be damaged, therefore, if a ground fault appeared on the system. In these applications, the double-wound isolating transformer provides galvanic isolation between input and output, thus attenuating the common mode and other conducted emissions.

# 9.2 Polygonal Non-isolating Autotransformer Phase Shift Systems

For some marine and offshore applications an alternative to the double-wound transformer-based phase shift system is that based on the polygonal, non-isolating autotransformer. The performance may not be as effective, with around $1 5 \mathrm { - } 1 7 \% I _ { t h d }$ being typical for a 12-pulse system.

A polygonal autotransformer is essentially a delta winding structure which permits the unbalancing $3 ^ { \mathrm { r d } }$ harmonics to circulate. A typical 12-pulse drive system based on a polygonal autotransformer is shown in Section 10, Figure 35, below.

![](images/af3caf2141a15e0624b04521f216aae9775afe85085348fa416d3f1c98b71620.jpg)  
FIGURE 35 12-Pulse AC PWM Drive with Polygonal Autotransformer

The 12-pulse polygonal autotransformer above provides $\pm 1 5 ^ { \circ }$ phase shift relative to the input and thereby $3 0 ^ { \circ }$ between the two bridge rectifiers. Two large interbridge reactors are necessary in this configuration in order to:

i) Attenuate the significant amounts of $3 ^ { \mathrm { r d } }$ harmonics, which would otherwise flow between bridge rectifiers   
ii) Force the bridge rectifiers to appear as balanced loads to each of the two three-phase groups of the polygonal autotransformer

iii) Maintain a relatively-balanced utilization of the rectifier

The performance of a typical polygonal autotransformer-based 12-pulse drive system is shown in Section 10, Figure 36 and is based on the following conditions:

• Transformer impedance of $\sim 1 \%$ .   
Both interbridge reactors are approximately six (6) times the value for a similar rating of drive with double-wound transformer.   
• Additional AC line reactance of up to $2 \%$ is present.   
• The impedances per phase group are completely balanced.   
• The rectifier voltage drops are completely balanced.   
• The drive is operating at rated load.

![](images/c174a012a3e1f3ac7adaeee6a56521ccb453ec9444e7d3e3824c7b4129d85031.jpg)  
FIGURE 36 Variation on Harmonic Currents vs. AC Reactance for a 12-Pulse AC PWM Drive with Polygonal Autotransformer

As can be seen from above, the performance of polygonal autotransformers is not as effective as that offered by double-wound transformers, but may be sufficient for many applications.

# 9.3 The Effect of Voltage Unbalance on Phase Shift Performance

As mentioned earlier, unbalance does have a detrimental effect of the performance of phase shift transformers. This unbalance may be due to manufacturing tolerances in the transformers and/or the rectifiers. However, no supply is completely balanced. In North America, unbalanced voltages between $1 - 3 \%$ readily exist in many power systems, impacting on the performance of the phase shifting scheme, irrespective of pulse number.

Section 10, Figure 38 illustrates the effect on the performance of a typical 18-pulse (20-degree phase shift) system, as shown in Section 10, Figure 37. As can be seen with the example, on a balanced system, the $I _ { t h d }$ at rated load is around $5 . 6 \%$ . This level of performance is maintained down to below $1 5 \%$ load. However, when $2 \%$ unbalance is introduced, the performance at $100 \%$ load is reduced to around $2 1 \% I _ { t h d } .$ . At reduced load, the performance is markedly poorer, with distortion significantly increased.

![](images/256667e02609d574620b40cfc7816d9a6dd41650e18ba2e10290c400ed0f931c.jpg)  
FIGURE 37 Typical 18-Pulse Drive System

![](images/fd230f60dee04b7a2bb2c93a52845fe668a893a9e9bb77d9b783d53600e74ba1.jpg)  
FIGURE 38 Effect of $2 \%$ Unbalance on 18-Pulse Drive

# 9.4 The Effect of Background Voltage Distortion on Phase Shift Performance

The presence of “pre-existing” or “background” voltage distortion also significantly affects the performance of phase shifting systems. Section 10, Figure 39 shows the degradation of performance of a similar 18-pulse to that described above, using background voltage distortion values up to $5 \%$ .

![](images/233a98dda0e301b8bf2c982ddd7834a8d2c491d72cddc98c716a6059ba13feff.jpg)  
FIGURE 39 Effect of Background Voltage Distortion on an 18-Pulse Drive

As illustrated above, the performance is largely unaffected on background distortion up to $2 \%$ Vthd at rated load and up to $1 \% \ \bar { V } _ { t h d }$ at $50 \%$ load. However, beyond these levels, the performance diminishes to around $1 5 \%$ $I _ { t h d }$ at rated load and $23 \%$ Ithd at $50 \%$ load, respectively, with $5 \%$ background distortion.

It should be noted that background voltage distortion on some classes of existing ships and offshore installations may be excess on $10 \%$ , with a number of instances recorded where the background $V _ { t h d }$ was in excess of $20 \%$ . This may be the case where full electric propulsion has been installed on a common bus system or where the majority of the electrical load is nonlinear (e.g., on drilling rigs, dynamically positioned drillships, etc.).

The performance of phase shift-based drive systems, therefore, has to be carefully considered, if the necessary level of mitigation is to be achieved under high levels of background distortion. In such applications, separate mitigation may have to be considered for retrofitting to other nonlinear equipment in order to reduce the overall voltage distortion such that any installed phase shift systems can operate more effectively.

# 10 Transformer Phase Staggering (Quasi Multi-pulse) Systems

A derivation of “phase shifting” is “phase staggering”. This technique can be used when there are multiple loads, ideally of similar or identical ratings, which can be fed from different phase shift transformers. The degree of phase shift per transformer is dependent on the number of discrete loads and the desired overall pulse number (e.g., a “quasi-18- or 24-pulse system”) necessary.

Section 10, Figure 40, below, depicts a system comprising $4 \times 1 3 2 \mathrm { k W }$ AC PWM drives fed from an $1 8 0 0 { \mathrm { ~ k V A } }$ transformer with $6 \%$ impedance. To facilitate the “quasi-24-pulse system”, a minimum of four drives are necessary. For optimum performance, all the loads should be of identical ratings. In this case, as in many practical applications, there may not be an ideal load profile. However, it can still be feasible to construct a quasi-24-pulse system (or any other pulse number based on a phase staggering based scheme), albeit with slightly less performance than it would have had if all the loads were balanced, as illustrated in this example.

FIGURE 40 Quasi-24-Pulse System Using Phase Staggering Techniques   
![](images/055b8cab8e0aec9a7d6e2d6487511408ac0ccc3c9155cbfa1fa014d45efc7246.jpg)  
30 DEGREE PHASE SHIFT PRODUCES 180 DEGREE PHASE SHIFT AT 5,7,17 AND 19TH.   
15DEGREE PHASE SHIFT PRODUCES180 DEGREE PHASE SHIFT AT11TH &13TH.

As can be seen from Section 10, Figure 40, one $1 3 2 { \mathrm { ~ k W } }$ drive (No. 1) has a 1:1 (i.e., no voltage transformation) transformer connected with 30 degrees phase shift between primary and secondary windings. Drive No. 2 is fed directly from the busbars of the switchboard. Drive No. 3 has a 15-degree phase shift transformer connected, as has Drive No. 4. This combination of phase shifting results in the $I _ { t h d }$ reducing to $8 . 5 \%$ when all four drives are operating at rated load, as shown in Section 10, Table 1.

TABLE 1 Estimated Harmonic Current Distortion Using Quasi-24-Pulse Phase Staggering System   

<table><tr><td>Harmonic</td><td>6-pulse</td><td>1 drive</td><td>2 drives</td><td>3 drives</td><td>4 drives</td></tr><tr><td>5</td><td>36.6%</td><td>36.6%</td><td>25.9%</td><td>12.2%</td><td>7.3%</td></tr><tr><td>7</td><td>13%</td><td>13%</td><td>9.2%</td><td>4.3%</td><td>2.6%</td></tr><tr><td>11</td><td>8%</td><td>8%</td><td>1.6%</td><td>2.7%</td><td>1.6%</td></tr><tr><td>13</td><td>3%</td><td>3%</td><td>0.6%</td><td>1%</td><td>0.6%</td></tr><tr><td>17</td><td>4%</td><td>4%</td><td>2.8%</td><td>1.3%</td><td>0.8%</td></tr><tr><td>19</td><td>1.8%</td><td>1.8%</td><td>1.3%</td><td>0.63%</td><td>0.4%</td></tr><tr><td>23</td><td>2.5%</td><td>2.5%</td><td>2.5%</td><td>2.5%</td><td>2.5%</td></tr><tr><td>25</td><td>1.7%</td><td>1.7%</td><td>1.7%</td><td>1.7%</td><td>1.7%</td></tr><tr><td>Ithd</td><td>40.1%</td><td>40.1%</td><td>27.9%</td><td>13.5%</td><td>8.5%</td></tr></table>

Note: Polygonal, non-isolating autotransformers were used in this example, hence the slightly lower performance than may have been expected with regard to the use of double-wound transformers. Also, please note that in the table above, the calculations were based on ALL drives having similar loading, and therefore balanced, and $2 0 \%$ residual for phase angle diversity.

Phase staggering can offer good harmonic mitigation performance. It is, however, prone to performance degradation due to voltage unbalance and background voltage distortion as are conventional drive dedicated phase shift transformers.

Phase staggering is not as effective in reducing harmonic currents as individual drives with multi-pulse, phase shifted inputs of similar pulse number. Nevertheless, phase staggering is an effective method of reducing the harmonic currents from a number of drives and other nonlinear loads to within the necessary limits.

Both double-wound and polygonal autotransformers can be used to construct phase staggering schemes. Double-wound tend to be larger, but offer better mitigation performance, and also importantly, galvanic isolation (normally a stipulation when EMI/EMC attenuation is necessary for the drives or other loads in a marine or offshore environment). Polygonal autotransformers are smaller, but offer lower levels of performance with no galvanic isolation, and therefore will not be as common on marine and offshore installations.

# 11 Electronic Filters

# 11.1 Active Filters

Active filters have been available since the late 1990s and are now relatively common in industrial applications for both harmonic mitigation and reactive power compensation (i.e., electronic power factor correction). Unlike passive L-C filters, active filters do not present potential resonance to the network and are unaffected to changes in source impedance.

Shunt-connected active filters (i.e., parallel with the nonlinear load, as shown in Section 10, Figure 41, below) are the common configuration of active filter. Less common series-connected types are available.

As can be seen in Section 10, Figure 41, there are three currents in the circuit:

$$
I _ {S} = I _ {L} - L _ {F}. \tag {10.15}
$$

where

$$
\begin{array}{l} I _ {S} \quad = \quad \text {s o u r c e c u r r e n t (f u n d a m e n t a l)} \\ I _ {L} \quad = \quad \text {n o n l i n e a r l o a d c u r r e n t} \\ I _ {F} \quad = \quad \text {a c t i v e f i l t e r c u r r e n t (h a r m o n i c)} \\ \end{array}
$$

![](images/14705a808db53352006be1c9474813eeba9e8b294875d1cfc7e34035f0f570f3.jpg)  
FIGURE 41 Block Diagram of Shunt Connection Active Filter with Associated Current Waveforms

With reference to Section 10, Figure 41, the active filter measures the wave shape of the nonlinear load current waveform via current transformers (CTs) in the line, the actual number of which varies according to the manufacturer. The reference voltage derived from the CTs is fed into a notch filter or similar circuit, where the fundamental component is removed. The remaining signal is a measure of the “distortion current” (i.e., the load current less the fundamental current). This signal is then fed into the control system which generates the respective IGBT firing patterns necessary in order to replicate and amplify the “distortion current” (now termed the “compensation current”), which is injected into the load in anti-phase (i.e., $1 8 0 ^ { \circ }$ displayed) to compensate for the harmonic current.

Note: The active filter should be dimensioned in terms of “harmonic cancellation current” based on the actual nonlinear currents drawn with the filter in circuit [i.e., due to the filter’s low impedance $( < 1 \% Z )$ , the nonlinear loads will draw more harmonic current than without the filter in the circuit. $10 \mathrm { - } 1 5 \%$ higher current is typical for three-phase loads].

When rated correctly in terms of “harmonic compensation current”, the active filter provides the nonlinear load with the harmonic current it needs to function while the source provides only the fundamental current (i.e., $5 0 \mathrm { H z }$ or $6 0 \mathrm { H z }$ component).

Section 10, Figure 42, below, illustrates a typical power circuit schematic of a shunt-connected active filter. The electromagnetic interference (EMI) and carrier filters are passive L-C networks. The EMI filter provides common mode filtering [i.e., between all phases and ground (earth) and a measure of differential mode filtering (i.e., between phases)]. On European Union (EU) applications, an uprated EMI filter or additional electromagnetic compatibility (EMC) filter is usually necessary in order to comply with the EU EMC Directive regarding limits of EMI emissions in the range $1 5 0 ~ \mathrm { k H z }$ to 30 MHz.

![](images/a1af3fa4f6037db5372cee076f8ee7ff46eb81091ca7e9c8819d936126d922f9.jpg)  
FIGURE 42 Simplified Power Circuit of Active Filter

The “carrier filter” attenuates the IGBT bridge carrier frequency (i.e., ${ \sim } 5 \ \mathrm { k H z }$ to $2 0 ~ \mathrm { M H z }$ depending on the rating of the active filter – on higher ratings $( > 3 0 0$ A) the switching frequency is usually reduced to minimize device power losses). However, after carrier frequency filtering, some leakage may be apparent which can adversely affect snubber components on SCR front end based drives and other equipment. In these applications, a $3 \%$ AC line reactor between the point of connection of the active filter and the nonlinear load is normally sufficient to prevent any adverse interaction and to reduce the harmonic current magnitude. The pre-charge resistors and associated contactor attenuate the DC bus inrush current during initial power-up, thereby maximizing the life of the capacitors. [This is a technique also used in AC variable frequency drives via either pre-charge (or ‘soft start’) resistors, mainly used in smaller $\mathrm { H P / k W }$ drives, or via 6-pulse, half controlled diode/SCR pre-charge input bridges (i.e., this is to provide voltage control from power-up to full conduction when DC bus is charged). The input bridge rectifier acts as diode bridge rectifier during normal operation].

The IGBT bridge and DC bus architecture are similar to that seen in AC PWM drives. The DC bus is used as an energy storage unit. The pre-charge contactor and pre-charge resistor are used to “soft start” the DC bus (i.e., reduce the inrush current to the DC bus capacitors during initial power-up). The DC bus is continually recharged via the IGBT package diodes, as shown in Section 10, Figure 42. The IGBT bridge generates a current wave shape for the harmonic compensation based on the “distortion current” signal derived from the CTs and notch filter or similar circuit.

Section 10, Figure 43 illustrates a typical current waveform for a 6-pulse AC PWM drive:
![](images/75c95c1cc445436e39449412d3bcd73ced018f50038ed99e3f93b08bde80e89c.jpg)  
FIGURE 43 Typical AC PWM Drive Input Current Waveform $( L _ { L } )$ as per Figure 41

The active filter “compensation current” is illustrated in Section 10, Figure 44, below:

![](images/e68cd9db3c68576a68df57754037fa87d6fdc8af6c21a3795b2b360e257dff37.jpg)  
FIGURE 44 Active Filter “Compensation Current” Waveform $( L )$ as per Figure 41

The corrected source current is shown below in Section 10, Figure 45:

![](images/f42d7f04b4901d07420e371fe535f014ef3b8e40fb6dab5d3f1b952c81cda9dd.jpg)  
FIGURE 45 Source Current Waveform $( L _ { S } )$ as per Figure 41

Section 10, Figure 46, below, illustrates typical performance of a correctly rated active filter. The nonlinear load is an AC PWM drive with $3 \%$ AC line reactor. Without the active filter in the circuit, the $I _ { t h d }$ is $3 5 . 2 8 \%$ . With the active filter operating, the $I _ { t h d }$ is reduced to $3 . 6 7 \%$ .

The active filters should be rated in terms of “harmonic cancellation current”, based on the currents actual drawn with the filter in circuit. To assist in the reduction of the magnitude of the harmonic current, AC line reactors of least $3 \%$ should be connected between the filter and load(s). The AC line reactor also serves to provide protection to SCR front end-based drives from the active filter carrier frequency.

Most active filters cannot operate on high levels of voltage background distortion $( > 8 - 1 0 \% )$ , due to damage to capacitive elements in the filter input.

The rating of an active filter should be based on the load current drawn with the active filter connected, as detailed above. Failing to do so may result in the active filter being “saturated” prematurely (i.e., current limited at its maximum rating), with any additional harmonic current spilling over into the mains as “distortion current” and raising the source side voltage distortion. However, many active filters regularly operate intermittently at maximum output current levels without any known problems.

Without Active Filter, $I _ { t h d }$ is $3 5 . 2 8 \%$ . With Active Filter, $I _ { t h d }$ is $3 . 8 7 \%$ .

![](images/6cfe93d6620bd3ba8f958b74dcd9a05d6d9c6288ac7ba4f0a30a29e37c5af5c7.jpg)  
FIGURE 46 Typical Active Filter Performance with 150 HP AC PWM with $3 \%$ AC Line Reactor

Active filters compensate for harmonic currents and provide reactive power compensation (i.e., electronic power factor correction). On digitally controlled filters, the amount of each can be selected via the user interface keypad. However, on older analog control system designs, it is not usually possible to control the reactive current. This may be problematic. For example, on power systems where the nonlinear load has been switched off or the load is at low levels, it is possible that uncontrolled reactive current up to almost the maximum capacity of the active filter can be imposed on the source. This may not be of concern on “stiff” shore-side utility supplies, but may well be problematic on “soft” marine and offshore generator-derived voltage supplies.

The control of the amount of harmonic compensation current to reactive current on digital active filters is based on its rated capacity and is based on the following formula:

$$
I _ {A F} = \sqrt {\left(I _ {h} ^ {2} + I _ {r} ^ {2}\right)} \dots \tag {10.16}
$$

where

$$
I _ {A F} = \text {t o t a l o u t p u t c u r r e n t o f t h e a c t i v e f i l t e r}
$$

$$
I _ {h} \quad = \quad \text {i n j e c t e d h a r m o n i c c u r r e n t o f t h e f i l t e r}
$$

$$
I _ {r} \quad = \quad \text {i n j e c t e d r e a c t i v e c u r r e n t}
$$

# Example

An active filter is rated at 300 A. Calculate the available reactive current if the injected harmonic current is 220 A.

$$
I _ {A F} = \sqrt {\left(I _ {h} ^ {2} + I _ {r} ^ {2}\right)}
$$

$\mathrm { T h u s } , I _ { r } { = } \sqrt { ( I _ { A F } ^ { 2 } - I _ { h } ^ { 2 } ) }$

$$
I _ {r} = \sqrt {\left(3 0 0 ^ {2} - 2 2 0 ^ {2}\right)}
$$

$$
I _ {r} = \underline {{2 0 4 A}}
$$

Active filters have the ability to compensate for any load-side current unbalances, but have been known to be susceptible to voltage unbalance on the source side of the connection. Please note that little research has been undertaken with regards to the performance of active filter under unbalance conditions, but published research work suggests the unbalanced voltages can generate a $2 ^ { \mathrm { n d } }$ harmonic voltage in the DC bus, and thereby a $2 ^ { \mathrm { n d } }$ harmonic current, whose amplitude is dependent on the DC bus capacitance. This $2 ^ { \mathrm { n d } }$ harmonic can be reflected on the AC side of the filter as a $3 ^ { \mathrm { r d } }$ harmonic, reducing its harmonic compensation effectiveness.

Excessive background voltage distortion (i.e., >8-10% $V _ { t h d } )$ may, in addition to damaging the capacitive elements in the active filter input, also interfere with the generation of reference and other signals. Therefore, in the presence of high levels of background voltage distortion, the “supply voltage signals” (i.e., those necessary for control and protection purposed) should be filtered.

For operation above 1 KV, LV active filters can inject into the supply via interposing transformers with a small loss in performance at higher frequencies. These transformers have to be specifically designed based on the injection of harmonic currents at frequencies up to $2 . 5 \ \mathrm { k H z }$ or 3 kHz $( 5 0 ^ { \mathrm { { \bar { t h } } } }$ harmonic based on $5 0 \mathrm { H z }$ and $6 0 \ : \mathrm { H z }$ fundamentals).

Active filters are relatively simple to apply. They can be connected to any nonlinear load or point of common coupling (PCC). Their effectiveness in reducing “line notching” due to fully controlled SCR drives and other similar equipment is dependent on the operating speed of the filter, which varies according to the manufacturer and/or the amount of commutating reactance in the line. Active filters can usually reduce the notching, but cannot eliminate it completely.

Note: Some active filters treat only up to the $2 5 ^ { \mathrm { t h } }$ harmonic. Some impose limits on the maximum number treated up to the $5 0 ^ { \mathrm { t h } }$ (e.g., up to ten). Unlike the filter described in this Section, the majority of active filters do not treat interharmonics. Performance depends on the control strategy adopted [“FFT” (selected characteristic harmonics)- based or “broadband” (all nonlinear current)-based].

Active filters are complex products, and it may not be possible for them to be repaired by any party other than the manufacturer’s service engineers. Also, full commissioning by manufacturers is necessary to obtain optimum performance, although “self tuning” models are now becoming available. Active filters do offer good performance in the reduction of harmonics and the control of power factor. Their use should be examined on a project-by-project basis, depending on the application criteria.

# 11.2 Hybrid Active-Passive Filters

The application of hybrid passive-active filters may be considered as an alternative to the use of shunt active filters. For example: on installations needing large amounts of harmonic cancellation. The use of passive filter elements is often seen as a means to reduce the current rating of the active filter while still retaining the benefits. In return, the connection of an active filter to a passive filter can eliminate the disadvantages of conventional passive filters (i.e., the possibility of resonance in a power system and the effects on the performance of a passive filter should the load characteristic or source impedance change).

The schematic diagram for a shunt-connected hybrid passive-active filter is depicted in Section 10, Figure 47, below, and comprises an active filter and a passive L-C filter with $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ tuned harmonic limbs.

![](images/4b1b83a9a575afe840266f2df75904462090456345918886af6ba19babd3dfe9.jpg)  
FIGURE 47 Theoretical Shunt Passive-Active Hybrid Filter

There is a misconception regarding the operation of hybrid shunt passive-active filters using “standard” industrial active filters as depicted in the example shown in Section 10, Figure 47, above. It is assumed that the passive filter, tuned to the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic, removes the majority of those harmonics and, therefore, the active filter only has to be rated, based on the filter’s rated current, to provide harmonic cancellation for the $1 1 ^ { \mathrm { t h } }$ harmonic and above. However, it is usually not possible using “standard” shunt active filters due to thermal considerations. Section 10, Figure 48, below, illustrates the maximum output currents per harmonic available from a typical “standard” shunt active filter.

![](images/ec38693faf7f60b310167a2496a109201923fa078b623d8cfa5dfb8e1eff3604.jpg)  
FIGURE 48 Thermal Limits of Shunt Active per Harmonic Current

Operation above the limits illustrated (Section 10, Figure 48) per harmonic is “prohibited”, as the active filter thermal protection circuitry would initiate “saturation” (i.e., the active filter would current limit) to protect the IGBTs from damage due to over-temperature.

Note: Most active filters are designed to mitigate typical harmonic spectrums, most notably that associated with 6-pulse drives and other nonlinear equipment, which consists mainly of low order harmonics (e.g., 5th, 7th, $1 1 ^ { \mathrm { t h } }$ , $1 3 ^ { \mathrm { t h } }$ , $1 7 ^ { \mathrm { t h } }$ and $1 9 ^ { \mathrm { t h } }$ etc.). At higher order characteristic harmonic frequencies, there are lower values of currents to mitigate. For similar rms current levels, the losses in the output devices, usually IGBTs, increase significantly, and sometimes exponentially, with increases in frequency. Therefore, the power that devices have to be derated thermally as per Section 10, Figure 48. This is accomplished automatically with the active filter.

The majority of standard active filters, whether they are based on ‘broadband’ performance (i.e. inject all the non linear current components into the load) and/or ‘selective FFT’ (i.e. they have the option of individual harmonic attenuation selection’), are affected by these thermal constraints.

Based on the graph in Section 10, Figure 48 and the circuit in Section 10, Figure 47, only $45 \%$ of the active filter current rating would be available to compensate from the $1 1 ^ { \mathrm { t h } }$ harmonic upwards without temperature limits being exceeded (which would be prevented by saturation). Similarly, from the same graph, if the passive filter contained $5 ^ { \mathrm { t h } }$ , $7 ^ { \mathrm { t h } }$ , $1 1 ^ { \mathrm { t h } }$ and $1 3 ^ { \mathrm { t h } }$ tuned limbs, the available active filter current to mitigate from $1 5 ^ { \mathrm { t h } }$ harmonic upwards would be $33 \%$ rated capacity.

Therefore, as illustrated above, it is not always possible to reduce the rating of a standard shunt active filter when operated with a passive filter. For example, a 400 A active filter will have 400 A maximum current available for all harmonic currents from $2 ^ { \mathrm { n d } }$ to the $5 0 ^ { \mathrm { t h } }$ harmonic. Based on the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic currents being attenuated by the passive filter, as depicted in Section 10, Figure 47, only 180 A will be available from the active filter for remainder of the harmonic currents from the $1 1 ^ { \mathrm { t h } }$ upward. The active filter will of course also mitigate any residual $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonics not attenuated by the passive filter. If the total harmonic current above the $1 1 ^ { \mathrm { t h } }$ is above $1 8 0 ~ \mathrm { A }$ , a larger rating of active filter may be necessary. The larger rating of active filter will also have the same thermal constraints per harmonic current compensation.

Similarly, for example, if a nonlinear load needed 280 A of mitigation after the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonics were attenuated by a passive filter, then the necessary rating of active filter would be, according to Section 10, Figure 48:

$$
I _ {A F} = \frac {2 8 0 \mathrm {A}}{0 . 4 5} = 6 2 3 \mathrm {A}
$$

Therefore an active filter of rated current of at least 623 A would be necessary. Likely ratings may be 650 A, 750 A or 800 A. It could be argued, therefore, that the rating of the “standard” active filter cannot be reduced when used in conjunction with passive filter and that the larger active filter rating necessary for operation with the passive filter could in fact mitigate all the harmonics of the nonlinear load without the need for passive filtration. Therefore, it is important that manufacturers be consulted closely when considering the use of “standard” shunt active filters with a hybrid passive-active configuration.

Hybrid passive-active filters for installations with large nonlinear loads are often custom designed, some shunt-connected (an example of which is illustrated in Section 10, Figure 49, below) and some series-connected, depending on the application.

![](images/955d11991e2e82130513136df1ef96a51a257d8fc6289e36d166afaf92339d02.jpg)  
FIGURE 49 Practical Example of Hybrid Shunt Passive-Active Filter

As can be seen in Section 10, Figure 49, above, the configuration of the example of custom designed, hybrid passive-active filter comprises an active filter connected in series with a passive filter having two tuned limbs for the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { { \hat { t } h } } }$ harmonic, respectively.

The active filter and passive filter are connected via coupling transformers. The operation of the hybrid scheme is such that the active filter, connected in series to the passive filter via the coupling transformer imposes a voltage at the terminals at connection with the nonlinear load, which forces the harmonic currents to circulate through the passive filter, attenuating the $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic. The residual $5 ^ { \mathrm { t h } }$ and $7 ^ { \mathrm { t h } }$ harmonic and the harmonic currents above the $7 ^ { \mathrm { t h } }$ would be compensated for by the active filter.

The active filter may improve, depending on the configuration, the passive filter compensation characteristics while also maintaining that the passive filter operates independently of any variations in natural resonant frequencies or filter characteristics (e.g., due to aging of components which would normally adversely affect operation). However, the passive filter kVAr at harmonic light load may be problematic on generator-derived supplies injecting leading reactive current into the source.

By their nature hybrid passive-active filters are not as simple to apply as standard active filters.

# 12 “Active Front Ends” for AC PWM Drives

“Active front ends”, also known as “sinusoidal input rectifiers”, are offered by a number of AC drive and UPS system companies in order to offer a low input harmonic footprint. An example of the application of an “active front end” (AFE) to an AC PWM drive is shown in Section 10, Figure 50, below.

As can be seen below, the normal 6-pulse diode input bridge has been replaced by a fully controlled IGBT bridge, an identical configuration to the output inverter bridge. The DC bus and the IGBT output bridge architecture are similar to that in standard 6-pulse AC PWM drives with diode input bridges.

![](images/6cfe033745caa53e41a05a34ebd64e484517d661a7d6eb70907154d3644dd7a7.jpg)  
FIGURE 50   
Application of an IGBT “Active Front End” to an AC PWM Drive

Employing PWM (pulse width modulation) waveform control techniques, similar to that utilized in the construction of the output voltage waveform, the input IGBT bridge synthesizes a sinusoidal input current waveform as shown in Section 10, Figure 51.

![](images/23b1436d727e681127c7780a2c657cc850516f2ad17971d6fb04c8a707c202c1.jpg)  
FIGURE 51 ”Active Front End” Input Current and Voltage Waveforms

As can be seen in Section 10, Figure 52, below, the operation of the input IGBT input bridge rectifier does significantly reduce low order harmonics compared to conventional AC PWM drives with 6-pulse diode bridges with a typical $I _ { t h d }$ of $2 \div 3 \%$ ${ < } 5 0 ^ { \mathrm { t h } }$ harmonic). However, they can also introduce significant high order harmonics, above the $5 0 ^ { \mathrm { t h } }$ , as also illustrated below. The $I _ { t h d }$ of the harmonics above the $5 0 ^ { \mathrm { t h } }$ , according to the information below, are well in excess of the $I _ { t h d }$ for those harmonics below the $5 0 ^ { \mathrm { t h } }$ . (It should be noted that only harmonics up to $5 { \cal O } ^ { t h }$ are usually considered in harmonics calculations, standard harmonic measurements and harmonic rules and recommendations. Harmonics above the $5 { \cal O } ^ { t h }$ may have an adverse effect on plant and equipment unless suitably mitigated).

In addition, the action of IGBT switching introduces a pronounced “ripple” at carrier frequencies $( { \sim } 2 { \cdot } 3 \ \mathrm { k H z } )$ into the voltage waveform which must be attenuated by a combination of AC line reactors (which also serve as an energy store that allows the input IGBT rectifier to act as a boost regulator for the DC bus) and capacitors to form a passive inductance-capacitance-inductance filter (L-C-L filter), as illustrated in the schematic (Section 10, Figure 50). Although a significant amount of the AC voltage ripple is attenuated, some residual may still appear on the system network, possibly exciting parallel resonance. Therefore, depending of the magnitude and nature of this residual ripple, further filtering may be necessary.

In order to minimize the effect of the residual voltage ripple, the ratio of short circuit power to drive power should be as high as possible, for example, above 20:1, although this may not always be practicable in many marine installations.

Compared to similarly-rated conventional 6-pulse AC PWM drives, AFE drive have significantly higher conducted and radiated EMI emissions, and therefore, special precautions and installation techniques may be necessary when applying them.

![](images/fb9abdc2270bfd5183980a1dff5306747d2e02b048690d45970270148a52159b.jpg)  
FIGURE 52 Typical Harmonic Current Input Spectrum for AC PWM Drive with an “Active Front End”. Note the Harmonic Currents Above the 50th

AFE drives are inherently “four quadrant” (i.e., they can drive and brake in both directions of rotation with any excess kinetic energy during braking regenerated to the supply), and unlike SCR based drives, will not result in fuse rupture, in the event of a power failure during regenerative braking commutation. AFE AC drives offer high dynamic response and are relatively immune to voltage dips. However, the effect of severe regenerative braking on the generators, for example, on main propulsion drives during emergency reversal, may have to be investigated.

The true power factor of AFE drive is high (approximately 0.98-1.0). The reactive current is usually controllable via the drive interface keypad.

# S E C T I O N

# 11 Harmonic Limit Recommendations

# 1 General Systems

In general systems, the total harmonic voltage distortion $( V _ { t h d } )$ should not exceed $5 \%$ , as measured at any point of common coupling (PCC), with any individual harmonic voltage distortion not exceeding $3 \%$ of the fundamental voltage value.

The range of harmonics to be taken into account should be up to the $5 0 ^ { \mathrm { t h } }$ harmonic.

# 2 Dedicated Systems

On dedicated systems, such as a dedicated propulsion switchboard, where other ships service loads are supplied by a separate switchboard, higher levels of total harmonic voltage distortion $( V _ { t h d } )$ may be permissible, provided the equipment is designed to operate at the higher limits.

For example: when all of the equipment and consumers connected to the dedicated system are designed and rated for a total harmonic voltage distortion of $10 \%$ , then the system should be operated within this $10 \%$ limit, in lieu of the general $5 \%$ limit. Further when the system is operated at the $10 \%$ limit, the voltage distortions from each of the individual harmonics are to be within the ratings of all of the equipment and consumers connected to the dedicated system.

This method is generally not practical on power systems where propulsion loads, ship service loads and/or industrial loads are all supplied from a common power system. Generally, there are too many different manufacturers and too many different branch circuits, for all of the equipment connected to the system to be designed for an increased level of harmonic voltage distortion.

For example: Most of the large drives on a main 4160V switchboard may be rated for $12 \%$ , but the equipment supplied by one branch circuit off the 4160V switchboard may be rated for only $5 \%$ . Further, the transformers to the 480V system may only be rated for $8 \%$ and the equipment supplied from the branch circuits off the 480V system may only be rated for $5 \%$ .

This increased limit of harmonic voltage distortion should be based on formal guarantees or formal declarations from equipment manufacturers, such that the faultless operation, safety and long term reliability of all connected equipment can be demonstrated.

The range of harmonics to be taken into account should be up to the $5 0 ^ { \mathrm { t h } }$ harmonic.

# 3 Operating Modes

All operating modes of the vessel and associated electrical power demands should be considered. The harmonic limit recommendations would be applicable during all operating modes. However, if the harmonic limit recommendations are exceeded during those operating modes that do not occur frequently or those operating modes that will not last for an extended period, then it may not be necessary to provide any further harmonic mitigation provided that immediate adverse effects of harmonics (e.g. instrumentation errors) will not result.

This Page Intentionally Left Blank

# S E C T I O N

# 12 Calculation of Harmonic Voltage Distortion

The operation of both large individual and/or large cumulative nonlinear loads needs to be considered with regard to their impact on the power system voltage distortion and subsequent effect on other loads. These calculations are usually undertaken using dedicated harmonic estimation software which often have models of various types of nonlinear loads (e.g., 6-pulse drives with varying values of AC line and/or DC bus reactance, 12-pulse drives, 18-pulse drives, etc.) and include the effects of phase angle diversity, the connection of linear loads and the effects of cables and other system inductances on the resultant harmonics at a point of common connection (PCC).

However, in order to appreciate the methodology of harmonic estimation software, examples of “simple” manual harmonic calculations are given.

Note: For simplicity, these examples do not consider any harmonics above the $2 5 ^ { \mathrm { t h } }$ (the exact procedure can be used up to the $5 0 ^ { \mathrm { t h } }$ ) nor the effects of phase angle diversification, connected linear loads, the effect of cables or other system inductance on the resultant harmonic currents and subsequent voltage distortion.

# 1 Manual Calculation of Voltage Distortion

Simple voltage distortion calculations can be undertaken based on specific information being available regarding the nonlinear load(s) percentage harmonic currents and source data [e.g., course kVA, impedance (or $X _ { d } ^ { ~ \prime \prime }$ ) or short circuit capacity].

# Example 1

An 850 HP/630 kW 6-pulse AC PWM drive with full load input current of 962 A is to be supplied from a 2000 kVA 6000 V/480 V transformer with $6 \%$ impedance. The drive manufacturer has advised the characteristic harmonic currents to the $2 5 ^ { \mathrm { { \bar { t h } } } }$ based on a $2 \%$ DC bus reactor on this transformer source to be as below.

Note: The harmonics up to the $5 0 ^ { \mathrm { t h } }$ should be used in all practical applications. In this instance, only up to the $2 5 ^ { \mathrm { t h } }$ harmonic is used for simplicity in order to demonstrate the principles. For higher order harmonics, the calculations are exactly the same).

Harmonic spectrum to $2 5 ^ { \mathrm { t h } }$ is:

$5 ^ { \mathrm { t h } } - 3 2 . 2 7 \%$   
$7 ^ { \mathrm { t h } } - 1 1 . 2 1 \%$   
11th – 7.37%   
13th – 3.91%   
17th – 3.45%   
19th – 2.35%   
23rd – 1.82%   
25th – 1.51%

Calculate the source short circuit capacity and supply reactance on secondary of transformer:

Transformer kVA i) Transformer full load current (A) = .. (12.1) Secondary V × 3

$$
= \frac {2 0 0 0 \times 1 0 ^ {3}}{4 8 0 \times 1 . 7 3 2}
$$

Transformer full load current (A) = 2406 A

ii) Short circuit current $=$ Transformer full load current .. (12.2) Transformer impedance

$$
= \frac {2 4 0 6}{0 . 0 6}
$$

Short circuit current = 40,100 A (40.1 kA)

iii) Short circuit MVA = 3 × V × Short Circuit Current .. (12.3)

$$
= 1. 7 3 2 \times 4 8 0 \times 4 0 1 0 0
$$

Short circuit $\mathrm { M V A } = 3 3 . 3 4 \mathrm { N }$ VA

iv) Supply reactance = V 2 .. (12.4) Short Circuit MVA

$$
= \frac {4 8 0 ^ {2}}{3 3 . 3 4 \times 1 0 ^ {6}}
$$

Supply reactance $= \underline { { 0 . 0 0 6 9 2 \Omega } }$

Once the above information has been established, the individual voltage per harmonic order can be calculated using the following method:

Harmonic current per order $= I _ { r m s } \times I _ { h } ^ { \% }$ . ... (12.5)

where

Irms = total rms input current

Ih% percentage harmonic current at harmonic order (e.g., $3 2 . 2 7 \%$ at $5 ^ { \mathrm { t h } }$ )

Voltage (L-L) per harmonic order $= \sqrt { 3 } \times h \times X _ { s u p p l y } \times I _ { h }$ ... ... (12.6)

where

h = harmonic order (i.e., $5 ^ { \mathrm { t h } } = 5 , 1 1 ^ { \mathrm { t h } } = 1 1 \ldots )$

Xsupply = supply reactance, in ohms

Ih = harmonic current (A) at harmonic order, $h$

Harmonic voltage as a percentage of L-L rms voltage =  hV ×100% ... (12.7) rmsV

where

Vh = harmonic voltage at order, h

Vrms = system L-L rms voltage

For $5 ^ { \mathrm { t h } }$ harmonic:

$$
\begin{array}{l} 5 ^ {\mathrm {th}} \text {harmonic current} = I _ {r m s} \times I _ {h} \\ = 9 6 2 \times 0. 3 2 2 7 \\ = 3 1 0. 4 4 \mathrm {A} \\ \end{array}
$$

$$
\begin{array}{l} 5 ^ {\text {t h}} \text {h a r m o n i c v o l t a g e (L - L)} = \sqrt {3} \times h \times X _ {\text {s u p p l y}} \times I _ {h} \\ = 1. 7 3 2 \times 5 \times 0. 0 0 6 9 2 \times 3 1 0. 4 4 \\ = 1 8. 6 \mathrm {V} \\ \end{array}
$$

$$
\begin{array}{l} 5 ^ {\mathrm {th}} \text {harmonic voltage (L - L) as percentage of rms voltage} = \frac {V _ {h} \times 100 \%}{V _ {r m s}} \\ = \frac {108.6 \times 100 \%}{480} \\ \end{array}
$$

$5 ^ { \mathrm { t h } }$ harmonic voltage (L-L) as percentage of rms voltage $= 3 . 8 8 \%$ Similarly for $7 ^ { \mathrm { t h } }$ harmonic:

$$
\begin{array}{l} 7 ^ {\mathrm {th}} \text {harmonic current} = I _ {r m s} \times I _ {h} \\ = 9 6 2 \times 0. 1 1 2 1 \\ = 1 0 7. 8 4 \mathrm {A} \\ \end{array}
$$

$$
\begin{array}{l} 7 ^ {\text {t h}} \text {h a r m o n i c v o l t a g e (L - L)} = \sqrt {3} \times h \times X _ {\text {s u p p l y}} \times I _ {h} \\ = 1. 7 3 2 \times 7 \times 0. 0 0 6 9 2 \times 1 0 7. 8 4 \\ = 9. 0 4 \mathrm {V} \\ \end{array}
$$

$$
\begin{array}{l} 7 ^ {\mathrm {th}} \text {harmonic voltage (L - L) as percentage of rms voltage} = \frac {V _ {h} \times 100 \%}{V _ {r m s}} \\ = \frac {9.04 \times 100 \%}{480} \\ \end{array}
$$

$7 ^ { \mathrm { t h } }$ harmonic voltage (L-L) as percentage of rms voltage $= 1 . 8 8 \%$

Using the above method for all harmonics up to $2 5 ^ { \mathrm { t h } }$ , the following summary table can be constructed:

TABLE 1 Summary of Harmonics to $2 5 ^ { \mathrm { t h } }$   

<table><tr><td>Harmonic</td><td>\( I_h\%^% \)</td><td>\( I_h(A) \)</td><td>\( V_h(V) \)</td><td>\( V_h\%^% \)</td></tr><tr><td>5</td><td>32.27</td><td>310.44</td><td>18.60</td><td>3.88</td></tr><tr><td>7</td><td>11.21</td><td>107.84</td><td>9.04</td><td>1.88</td></tr><tr><td>11</td><td>7.37</td><td>70.9</td><td>9.35</td><td>1.95</td></tr><tr><td>13</td><td>3.91</td><td>37.61</td><td>5.85</td><td>1.22</td></tr><tr><td>17</td><td>3.45</td><td>33.2</td><td>6.76</td><td>1.41</td></tr><tr><td>19</td><td>2.35</td><td>22.61</td><td>5.14</td><td>1.71</td></tr><tr><td>23</td><td>1.82</td><td>17.51</td><td>4.83</td><td>1.01</td></tr><tr><td>25</td><td>1.51</td><td>14.52</td><td>4.35</td><td>0.91</td></tr></table>

Once the above table has been constructed, the total harmonic voltage distortion $( V _ { t h d } )$ can be calculated (based on Equation 2.6 in Section 2):

$$
V _ {t h d} = \sqrt {\sum_ {h = 5} ^ {2 5} V _ {h} ^ {\% 2}} = \sqrt {V _ {5} ^ {\% 2} + V _ {7} ^ {\% 2} + V _ {1 1} ^ {\% 2} \dots . + V _ {2 5} ^ {\% 2}} \tag{12.8}
$$

$$
V _ {t h d} = \sqrt {3 . 8 8 ^ {2} + 1 . 8 8 ^ {2} + 1 . 9 5 ^ {2} + 1 . 2 2 ^ {2} + 1 . 4 1 ^ {2} + 1 . 7 1 ^ {2} + 1 . 1 0 ^ {2} + 0 . 9 1 ^ {2}}
$$

$$
V _ {t h d} = 5.55 \%
$$

Alternatively, the sum of individual harmonic voltages can be used to also obtain the $V _ { t h d }$

$$
V _ {t h d} = \frac {\sqrt {\sum_ {h = 5} ^ {25} v _ {h} \times 100 \%}}{V _ {r m s}} = \frac {\sqrt {v _ {5} ^ {2} + v _ {7} ^ {2} + v _ {11} ^ {2} \dots \dots . v _ {25} ^ {2}}}{V _ {r m s}} \dots \tag{12.9}
$$

$$
V _ {t h d} = \frac {26.64 \times 100 \%}{480}
$$

$$
V _ {t h d} = \underline {{5 . 5 5}}
$$

# Example 2

The same 850 HP/630 kW, 480 V, 962 A, 6-pulse AC PWM is to be supplied by a generator of rating $2 0 0 0 \mathrm { k V A }$ and subtransient reactance $( X _ { d } ^ { { \prime \prime } } )$ of $1 6 \%$ . Calculate the voltage distortion on the generator attributed to drive.

The percentage harmonic current spectrum based on the generator connection is given below. Note that compared to Example 1, the values are lower. This is normal, as the harmonic currents drawn from this “soft source” are limited by the leakage reactance of the source. However, this reduced harmonic current can result in significantly higher voltage distortion, as can be seen below.

Harmonic spectrum to $2 5 ^ { \mathrm { t h } }$ is:

$$
\begin{array}{l} 5 ^ {\mathrm {t h}} - 25.63 \% \\ 7 ^ {\mathrm {th}} - 7.8 \% \\ 11 ^ {\mathrm {th}} - 5.27 \% \\ 13^{\mathrm{th}} - 3.43\% \\ 17 ^ {\mathrm {th}} - 1.73 \% \\ 19^{\mathrm{th}} - 1.55\% \\ 23 ^ {\mathrm {rd}} - 0.93 \% \\ 25 ^ {\mathrm {th}} - 0.78 \% \\ \end{array}
$$

Calculate the source short circuit capacity and reactance of the generator:

i) Generator full load current (A) =  Generator kVA $( \mathrm { A } ) = { \frac { G e n e r a t o r \ : k V A } { V \times { \sqrt { 3 } } } }$ .. (12.10)

$$
= \frac {2 0 0 0 \times 1 0 ^ {3}}{4 8 0 \times 1 . 7 3 2}
$$

Generator full load current $( \mathrm { A } ) = \underline { { 2 4 0 6 } } \ _ { i }$ A

ii) Short circuit current (A) = Generator full load current $=$ ... (12.11) Generator X d′′

$$
= \frac {2 4 0 6}{0 . 1 6}
$$

$$
\text {S h o r t c i r c u i t c u r r e n t (A)} = 1 5. 0 3 8 \mathrm {A} (1 5. 0 3 8 \mathrm {k A})
$$

iii) Short circuit $\mathbf { M } \mathbf { V } \mathbf { A } = { \sqrt { 3 } } \mathbf { \Omega } \times V \mathbf { \times } \mathbf { \Omega }$ Generator Short Circuit Current . .. (12.12)

$$
= 1. 7 3 2 \times 4 8 0 \times 1 5 0 3 8
$$

$$
\text {S h o r t c i r c u i t M V A} = 1 2. 5 \mathrm {M V A}
$$

V 2 iv) Generator reactance = .. (12.13) Short Circuit MVA

$$
= \frac {4 8 0 ^ {2}}{1 2 . 5 \times 1 0 ^ {6}}
$$

$$
\text {G e n e r a t o r r e a c t a n c e} = 0. 0 1 8 4 \Omega
$$

Once the above information has been established, the individual voltage per harmonic order can be calculated using exactly the same method as per Example 1:

For $5 ^ { \mathrm { t h } }$ harmonic:

$$
\begin{array}{l} 5 ^ {\mathrm {th}} \text {harmonic current} = I _ {r m s} \times I _ {h} \\ = 9 6 2 \times 0. 2 5 6 3 \\ = 2 4 6. 6 \mathrm {A} \\ \end{array}
$$

$$
\begin{array}{l} 5 ^ {\text {t h}} \text {h a r m o n i c v o l t a g e (L - L)} = \sqrt {3} \times h \times X _ {\text {s u p p l y}} \times I _ {h} \\ = 1. 7 3 2 \times 5 \times 0. 0 1 8 4 \times 2 4 6. 6 \\ = 3 9. 2 9 \mathrm {V} \\ \end{array}
$$

$$
\begin{array}{l} 5 ^ {\mathrm {th}} \text {harmonic voltage (L - L)} \text {as percentage of rms voltage} = \frac {V _ {h} \times 100 \%}{V _ {r m s}} \\ = \frac {39.29 \times 100 \%}{480} \\ \end{array}
$$

$$
5 ^ {\mathrm {th}} \text {harmonic voltage (L - L)} \text {as percentage of rms voltage} = 8.18 \%
$$

Again, similarly for $7 ^ { \mathrm { t h } }$ harmonic:

$$
\begin{array}{l} 7^{\mathrm{th}}\text{harmonic current} = I_{rms}\times I_{h}^{\%} \\ = 9 6 2 \times 0. 0 7 8 \\ = 7 5. 0 \mathrm {A} \\ \end{array}
$$

$$
\begin{array}{l} 7 ^ {\text {t h}} \text {h a r m o n i c v o l t a g e (L - L)} = \sqrt {3} \times h \times X _ {\text {s u p p l y}} \times I _ {h} \\ = 1. 7 3 2 \times 7 \times 0. 0 1 8 4 \times 7 5. 0 \\ = 1 6. 7 3 \mathrm {V} \\ \end{array}
$$

7th harmonic voltage (L-L) as percentage of rms voltage $= \frac { V _ { h } \times 1 0 0 \% } { V _ { r m s } }$

$$
= \frac {16.73 \times 100 \%}{480}
$$

$7 ^ { \mathrm { t h } }$ harmonic voltage (L-L) as percentage of rms voltage $= 3 . 4 9 \%$

As per Example 1, data regarding all the harmonics to $2 5 ^ { \mathrm { t h } }$ can be calculated. A summary table can be constructed as follows:

TABLE 2 Summary of Harmonics to 25th   

<table><tr><td>Harmonic</td><td>\( I_h \) %</td><td>\( I_h(A) \)</td><td>\( V_h(V) \)</td><td>\( V_h \) %</td></tr><tr><td>5</td><td>25.63</td><td>246.6</td><td>39.29</td><td>8.19</td></tr><tr><td>7</td><td>7.8</td><td>75.0</td><td>16.73</td><td>3.49</td></tr><tr><td>11</td><td>5.27</td><td>50.7</td><td>17.77</td><td>3.70</td></tr><tr><td>13</td><td>3.43</td><td>33.0</td><td>13.68</td><td>2.85</td></tr><tr><td>17</td><td>1.73</td><td>16.65</td><td>9.02</td><td>1.88</td></tr><tr><td>19</td><td>1.55</td><td>14.91</td><td>9.04</td><td>1.88</td></tr><tr><td>23</td><td>0.93</td><td>8.95</td><td>6.56</td><td>1.37</td></tr><tr><td>25</td><td>0.78</td><td>7.5</td><td>5.98</td><td>1.25</td></tr></table>

Also, as per Example 1, once the above values have been established, the total harmonic voltage distortion $( V _ { t h d } )$ can be calculated (based on Equation 2.6 in Section 2):

$$
\begin{array}{l} V _ {t h d} = \sqrt {\sum_ {h = 5} ^ {2 5} V _ {h} ^ {\% 2}} = \sqrt {V _ {5} ^ {\% 2} + V _ {7} ^ {\% 2} + V _ {1 1} ^ {\% 2} \dots . . . + V _ {2 5} ^ {\% 2}} \\ V _ {t h d} = \sqrt {8 . 1 9 ^ {2} + 3 . 4 9 ^ {2} + 3 . 7 0 ^ {2} + 2 . 8 5 ^ {2} + 1 . 8 8 ^ {2} + 1 . 8 8 ^ {2} + 1 . 3 7 ^ {2} + 1 . 2 5 ^ {2}} \\ V_{thd} = \underline{10.57\%} \\ \end{array}
$$

Alternatively, the sum of individual harmonic voltages can be used to also obtain the $V _ { t h d }$ :

$$
V _ {t h d} = \frac {\sqrt {\sum_ {h = 5} ^ {25} v _ {h} \times 100 \%}}{V _ {r m s}} = \frac {\sqrt {v _ {5} ^ {2} + v _ {7} ^ {2} + v _ {11} ^ {2} . . . . . . v _ {25} ^ {2}}}{V _ {r m s}} \dots \tag{12.9}
$$

$$
V _ {t h d} = \frac {50.73 \times 100 \%}{480}
$$

$$
V _ {t h d} = \underline {{10.57 \%}}
$$

Note: From the above examples, the source impedance has a significant effect on the harmonic currents drawn and their resultant impact on the subsequent voltage distortion.

For information on the calculation of source short circuit MVA for harmonic distortion estimation purposes on parallel power sources (generators or transformers), please refer to Subsection 7/3).

# 2 Software Estimation of Harmonic Distortion

As indicated in Subsection 12/1, the manual calculation for a simple system with one nonlinear load can be rather repetitive and tiresome. There is also a significant chance of human error being introduced. However, on a very simple system, it may prove valuable to undertake manual calculations to provide an indication of harmonic voltage distortion.

In some cases, there may be multiple harmonic current sources, and therefore, some cancellation via phase angle diversification. The effect of any connected linear load, especially induction motors, may attenuate higher order harmonics. In addition, the effect of cable and other system inductances will have an impact on the harmonic currents and subsequent voltage distortion.

There are a number of harmonic estimation software packages available which are relatively easy to use. Often, they form part of a comprehensive electrical design and analysis suite where a harmonics estimation program is only a small part of the overall package.

A number of drive and harmonic mitigation equipment manufacturers do have their own harmonic estimation software available, either for customers to use via CD or download or indirectly via company application engineers. However, these simulations should be seen as “estimates” only. Written guarantees of drive(s) and/or any harmonic mitigation performance should be requested from the vendor.

Comprehensive power system analysis software packages are also available from dedicated engineering software engineering companies. These software packages are not provided by the equipment manufacturers and are therefore should give impartial results.

Many of the harmonics modeling and dedicated electrical design and simulation software packages can be tailored to individual customer needs.

A comprehensive harmonics software package should have the following capabilities:

i) Have a large number of nodes available for full power system simulations.   
ii) Be able to simultaneously model individual harmonic current data and subsequent voltage distortion based on a range of multiple nonlinear loads types.   
iii) Be able to introduce varying values of voltage unbalance and background voltage distortion into the model.   
iv) Be capable of handling all harmonic sequences: positive, negative and zero.   
v) Be able to perform frequency scans based on small increments of frequency and to develop frequency response curves and other data to establish possible resonance points within the power system.   
vi) Have in a library, a full range of nonlinear load models [including AC PWM 6-pulse drives with varying values of AC and/or DC reactance, DC drives (including notching simulations) with values of AC side commutation reactance together with 12-pulse, 18-pulse, 24-pulse versions of AC PWM and DC drives, AC cycloconverters, load commutated inverters, four-wire distribution systems, etc.].

The package should be able to model the more common types of harmonic mitigation, including passive L-C filter, phase staggering, wide spectrum filters, active filters, AFE drives, etc. In addition, the effect of any connected linear loads should be able to be modeled.

vii) Calculate and display a full range of time domain voltage and current waveforms, full FFT harmonic voltage and current spectra to at least $5 0 ^ { \mathrm { t h } }$ harmonic at each node.   
viii) Be able to adjust automatically for harmonic phase angles based on variations in the fundamental frequency phase angles.   
ix) Be able to model any range or number of transformer and/or generator data (including equivalent data for paralleled units).   
x) Should be easy to understand and have report facilities such as comprehensive report writing.

# 13 Provision of Information on Harmonics

# 1 Information to be requested from Vendors

The following should be the minimum information provided to shipbuilders, consultants, designers, ship-owners and ship-operators et al (as applicable) in order to calculate harmonic voltage distortion:

i) Description of equipment, including type, voltage supply specifications, pulse number and kW rating.   
ii) Details of the total number of units proposed to be installed on vessel or offshore installation.   
iii) Total harmonic current distortion $( I _ { t h d } )$ , harmonic current spectrum up to $5 0 ^ { \mathrm { t h } }$ harmonic (or up to $1 0 0 ^ { \mathrm { t h } }$ for equipment with “active front ends”) and total magnitude of total harmonic current per unit, per circuit and per installation at rated load, as applicable.

[The actual source impedance (if transformer) or subtransient reactance $( X _ { d } ^ { \prime \prime } )$ (if generator) used shall be stated for each calculation.]

[If four-wire systems (three-phase and neutral, either grounded or insulated) are utilized for domestic or lighting supplies, calculations of the estimated neutral currents shall be provided on a per distribution panel at rated load basis].

iv) Full details of any proposed harmonic mitigation per unit, including estimated attenuation in total harmonic current distortion $( I _ { t h d } )$ and total harmonic current per unit, per circuit or per installation up to $5 0 ^ { \mathrm { t h } }$ harmonic (or up to $1 0 0 ^ { \mathrm { t h } }$ for equipment with “active front ends”), as applicable.

# 2 Information to be included with a Harmonic Analysis

The following information should be included with a harmonic analysis:

i) Single line electrical diagram of vessel showing connection of any significant (singular or cumulative) nonlinear load(s) on the system.   
ii) Description of significant nonlinear load(s), including duty, pulse number, voltage supply specifications and kW rating.   
iii) Total number, type and kW rating of nonlinear loads proposed to be installed in vessel or offshore installation.   
iv) If four-wire systems (three-phase and neutral, either grounded or insulated) are utilized for domestic or lighting supplies, calculations of the estimated neutral currents should be provided on a per distribution panel at rated load basis.   
v) Full details of any proposed mitigation, including estimated attenuation in total harmonic current distortion $( I _ { t h d } )$ and total harmonic current per unit, per circuit or per installation up to $5 0 ^ { \mathrm { t h } }$ harmonic (or up to $1 0 0 ^ { \mathrm { t h } }$ for equipment with “active front ends”), as applicable.

vi) Calculations of total harmonic voltage distortion $( V _ { t h d } )$ on the system based on all significant nonlinear loads operating as designed and on a worse case scenario with regards to the number and rating of generators running. The calculations should be on a per-switchboard basis, including any emergency switchboards, and at the terminals of the generators.

The total harmonic voltage distortion $( V _ { t h d } )$ should be measured in additional to all individual voltage harmonics up to $5 0 ^ { \mathrm { t h } }$ (or up to $1 0 0 ^ { \mathrm { t h } }$ if equipment with “active front ends”) that are being proposed.

The source impedance or subtransient reactance $( X _ { d } ^ { \prime \prime } )$ used in the calculations should be stated for each case.

vii) Full details of any proposed mitigation, including estimated attenuation in total harmonic voltage distortion $( V _ { t h d } )$ and total harmonic voltage up to $5 0 ^ { \mathrm { t h } }$ harmonic (or up to $1 0 0 ^ { \mathrm { t h } }$ harmonics for equipment with “active front ends”), as applicable on each switchboard, including any emergency switchboards and on the generator terminals, based on the worst case scenario basis as per vi) above.

# S E C T I O N

# 14 Harmonic Surveys and Measurement Equipment

This Section outlines the safety precautions, planning, methodology and typical harmonic measurement/power quality meters and analyzers available to vessel, rig, platform staff or shipyard electrical engineers should they wish to carry out their own measurements.

There are also a number of specialist independent companies available to carry out harmonic and power quality surveys in most countries should this be needed. It is standard procedure for a comprehensive report to be written following the survey.

# 1 Safety Precautions during Harmonic Surveys

As with all electrical tasks, safety is the main concern. Some of the following recommendations are common sense, but are necessary for the safety of the vessel, rig or platform and of the individuals concerned:

i) Measurements should not be undertaken in heavy or rolling seas due to the possible exposure of live equipment and the risk of injury or death due to individuals coming in contact with live busbars, terminals, etc., due to the vessel’s movement.   
ii) The harmonic measurements should be undertaken by two individuals; one a qualified electrical engineer conversant with the measurement equipment and a second individual to assist, who is also fully trained in CPR and other first aid. The latter is necessary when connecting and disconnecting the harmonic analyzer voltage leads and current probes on to live equipment.   
iii) Proper protective clothing and other safety equipment should be worn when undertaking measurements.

This should include:

x Fire resistant clothing   
x Safety glasses or full face shields   
Safety helmets   
x Rubber electrical gloves with full length sleeves

In addition, rubber mats should be placed on the deck where the harmonic analyzer is being used. They should be moved to each site as necessary.

iv) For safety reasons, it is not recommended that directly connected harmonic measurements above 690 V/750 V AC (e.g., on high voltage, up to or over $1 1 \ \mathrm { k V }$ on some vessels) are undertaken unless by experienced staff with suitable equipment or by a dedicated, specialist company with appropriate equipment to safely undertake measurements above these levels.

A number of harmonic analyzers (and accompanying test leads and current probes) are only suitable for use up to 600 V AC. Others are rated up to 830 or 1000 V AC. Therefore, the maximum voltage rating of the harmonic analyzer has to be checked against the power system voltage before undertaking the survey.

v) All electrical equipment should be de-energized and locked off before connecting the harmonic measuring equipment. There are a number of safety and operational issues. If the equipment is provided with door locking mechanism when the equipment is operating, it may be necessary to stop the equipment in order to gain the necessary access.

Similarly, removing covers from equipment while the equipment is operating is not recommended. However, if this has to be undertaken, great care must be taken in order that the metal covers do not touch parts. Rubber gloves, rubber mats and other protective clothing are therefore recommended as mentioned above.

vi) Before connecting any harmonic measurement equipment, a true rms voltage meter should be used to confirm the voltage levels OR that the voltage is zero (i.e., the equipment has been disconnected).

vii) Care should be taken when connecting the harmonic analyzer voltage leads (these can be of the crocodile type and if not fixed to a suitable point may spring off. Prior to connection, the most appropriate voltage test points should be established.

Current probes of the “clamp on” type (available to around 1200 A), which usually have round or rectangular jaws, are simply for use on cables. However, for some types of busbars, this type of current probe may be problematic, and therefore, AmpFlex type probes are necessary. (These are flexible current probes, available up to at least 6500 A, which have to be passed around the busbar and clipped into place. This process entails the individual placing his/her hands adjacent to and often behind the busbars. Without thick rubber gloves with full rubber sleeves this can be extremely dangerous and should not be undertaken unless these are worn with other appropriate protective equipment and a CPR-trained assistant is available.)

Note: The type of current probe necessary should be established prior to surveys or a range of suitable probes should be available.

viii) Before undertaking the harmonic measurements, it is advised that the individuals become fully conversant with the harmonic/power quality analyzer. It is often worthwhile to undertake some simple measurements, even in a workshop environment, in order to gain this initial experience.

# 2 Planning the Harmonic Survey or Measurements

In order to minimize the time necessary to undertake the harmonic survey and/or measurements, some simple planning is necessary.

A single line diagram is often the most significant source of information. From this, the main sources of harmonics (i.e., larger nonlinear loads) can be identified (e.g., large variable speed drives). However, on some power systems (for example, four-wire systems on cruise liners), the large numbers of nonlinear single-phase loads and their impact may not be apparent from a single line diagram.

Once the nonlinear loads have been identified, a list or schedule should be compiled of every major nonlinear load to be measured and recorded.

In addition to measurements at the terminals of every major nonlinear load, recordings should also be taken on all switchboards, including emergency switchboards, and if possible, on the generators in operation.

All measurements should be undertaken based on a “worst-case scenario” (i.e., maximum nonlinear loading, therefore. maximum harmonic distortion, with minimum generators on line based on real operational conditions). Failing that, measurements must be recorded at full operational loads. It is important that the information gathered reflects the expected operational conditions.

With the electrical loading constant, the nonlinear loads furthest away physically from the main switchboard should be measured first. Then measurements should be recorded for other nonlinear equipment, progressively towards the main switchboard(s) and generator(s).

Finally, although most harmonic analyzers have sufficient onboard memory and/or can download to a laptop computer, a paper list of nonlinear equipment to be measured is recommended. Information such as total harmonic voltage distortion $( V _ { t h d } )$ , total harmonic current distortion $( I _ { t h d } )$ , current and kW of each nonlinear load is useful in the event of misnaming a given load on the harmonic analyzer or laptop computer (i.e., it often helps in identifying the correct load based on that data).

# 3 Information to be recorded from Harmonic Measurements

Prior to measurements being undertaken, the equipment should be confirmed to be within calibration time limits and that the necessary voltage and current probes and full protective equipment are to hand. Only then should the actual harmonic survey and/or harmonic measurements proceed.

As stated earlier, it is essential that the measurements are taken based on a worst-case scenario, or failing that, at maximum operational loading and maximum harmonic distortion with regard to the various nonlinear loads. It should be remembered that the higher the magnitude of harmonic current in the system, the higher the voltage distortion.

Note: Always connect the ground lead (if applicable), followed by the voltage leads and finally the current probes with the correct polarity. Removal of the equipment leads and probes should be in the reverse order.

For each nonlinear load selected, the following data should be measured and recorded on all three phases, (and neutral, if appropriate, on four-wire distribution systems), starting with those further away from the generators. In addition, similar data should be recorded on the main switchboard(s) and generators.

Information to be recorded:

i) rms voltage and rms current   
ii) Total harmonic voltage distortion $( V _ { t h d } )$   
iii) Total harmonic current distortion $( I _ { t h d } )$   
iv) Full harmonic spectrum up to $5 0 ^ { \mathrm { t h } }$ harmonic (up to $1 0 0 ^ { \mathrm { t h } }$ harmonic for active front end drives).   
v) Harmonic text (i.e., FFT data of harmonic spectrum in text) for voltage and current harmonics giving magnitudes and phase angles.   
vi) Time domain waveforms of both voltage and current   
vii) Voltage unbalance between phases   
viii) Background total voltage distortion $( V _ { t h d } )$ without the specific nonlinear load currently under test operating would be desirable but may not be practical due to operational reasons.

The majority of harmonic analyzers can capture the data detailed in i) to vi) simultaneously, either internally and/or via download to a laptop computer. Some can also capture voltage unbalance [vii)].

In addition to the information downloadable to a laptop or stored in the harmonic analyzer, the data in i) to iii) should also be recorded on paper, as recommended in the previous Subsection. This may help to identify any misnamed loads.

Once a complete set of measurements have been taken, a full report, complete with waveforms, harmonic spectra and other data as above, should be compiled. In addition, a simple diagram detailing the total harmonic voltage distortion $( V _ { t h d } )$ at the various points in the power system is recommended. (This may be via an enlarged single line diagram). The gathered harmonics data can then be compared against the appropriate harmonic limit recommendations and/or used to aid the consideration of harmonic mitigation for specific items of equipment of nonlinear (e.g., electric variable speed drives) and/or for other specific items of equipment such as switchboards.

# 4 Examples of Harmonic Analyzers

There are a number of high quality harmonic and power quality analyzers currently on the market, some of which are illustrated in the following Paragraphs, together with some sample screen displays.

When selecting a suitable harmonic/power quality analyzer, check that it can read up to at least the $5 0 ^ { \mathrm { t h } }$ harmonic, so that the voltage range is suitable for use on all envisaged applications and that a suitable range of current probes are available for that particular analyzer. [Some equipment is rated to only measure safely up to 600 V rms. If above that (e.g., $6 9 0 \mathrm { ~ V ~ }$ or 750 V), another type of analyzer may be necessary.]

Most “harmonic analyzers” are “power quality analyzers”, and perform a range of other measurements and record, in addition to harmonic data, for example, voltage sags and swells, transients, power usage and power factor measurements. However, most are not normally suitable for measuring the output data from AC PWM variable speed drives. (For this, special digital multi-meters with shielding and low pass filters are necessary.)

Typical harmonic/power quality analyzers include:

# 4.1 The Fluke 43B

The Fluke 43B is a harmonic/power quality analyzer, rated up to 600 V rms. It is not a full threephase unit (i.e., it does not measure all three phases simultaneously) – it measures one phase at a time (assuming all phases are balanced and data from each is similar, this may be sufficient). It is compact, lightweight and can store a number of readings (up to 20 screen or data readings based on a maximum of two selectable parameters) onboard without the need for downloading to computer.

The Fluke 43B measures up to the $5 0 ^ { \mathrm { t h } }$ harmonic and is supplied with appropriate software for downloading and to assist in report compilation. Using suitable proprietary current probes, measurements up to 2000 A (up to 600 V rms) are possible.

![](images/37a33f86e0b6066344625b24ccc8535336a4752a63d6f82461c12d16022ae534.jpg)  
FIGURE 1 Fluke 43B Harmonic/Power Quality Analyzer

A few samples of screen/computer download data from the Fluke 43B include:

# FIGURE 2

# Fluke 43B Harmonics Screen Data Available (In This Case Current) [Voltage and power harmonic data are also available.]

![](images/ad332e04c5cd096d897a862a33624aa399798e39304abb4e8b17f664d250ef5e.jpg)

![](images/80d4e25b3835445dbb67c3af4d63c3f7b2e282c15081e690299fd2eac86f8c4f.jpg)  
FIGURE 3 Fluke 43B Can Measure Sags and Swells up to 16 Days on a Per Cycle Basis

![](images/795ac7c7a05e2297049e6f3c24a38666343d944df0ac63e55eef2197b01d085a.jpg)  
FIGURE 4 Up to 40 Transients (Voltage or Current) Can Be Captured with the Fluke 41B

![](images/6f545f72805b5aa22aed11dbc0ac122901f4089d640adacf6eceba3e767a06a9.jpg)  
FIGURE 5 True rms Voltage and Current Waveform Display(s) from Fluke 43B

The Fluke 43B is a good example of a relatively low cost harmonic/power quality analyzer for applications needing measurements to $6 0 0 \mathrm { ~ V ~ }$ rms and up to 2000 A. This meter may be more suited to fault finding and/or “snapshot sampling”.

A full three-phase analyzer may be used for full harmonic surveys and/or for other power quality tasks, whereby all three phases are measured and/or monitored simultaneously, to prevent data being “missed” (which may occur with the type of analyzer above if the event occurred on the phase not being monitored).

Fluke, recognizing the limitation of the 43B for “real” three-phase applications has recently launched the Fluke 433/434 series of three-phase harmonic/power quality analyzers which have an excellent range of features, including voltage to $1 0 0 0 \mathrm { V }$ rms and current to 2000 A.

# 4.2 AEMC 3945

This is a good example of a three-phase harmonic/power quality analyzer which can measure and record harmonics to the $5 0 ^ { \mathrm { t h } }$ on voltages up to $8 3 0 \mathrm { V }$ rms and current per phase up to 6500 A.

![](images/e235c1248d91be091d66b21bf55f6dc700ce2a568ee76204fc1c1f625a816acd.jpg)  
FIGURE 6 AEMC 3945 Three-phase Harmonic/Power Quality Analyzer with Real Time Color Display

# FIGURE 7 AEMC 3945 Connected On-site Illustrating “Wrap-around” Rogowski-type, AmpFlex 6500 A Current Probes

A range of clamp-on current probes (to 1200 A) and a scalable adaptor box for use with up to three existing CTs are also available.

![](images/e53cc9f37fdca0a1d05c1506e97754118553d3073b38bec92004d10a7eb33562.jpg)

In addition to the full range of harmonic measurements, the AEMC 3945 can measure and record short-term flicker, capture up to 50 transients or other disturbances to $1 / 2 5 6 ^ { \mathrm { t h } }$ of a cycle, record voltage and current unbalance, trend recordings and monitoring of a number of parameters based on min/max limits and “photograph” up to twelve data displays. Comprehensive software is provided to assist in report compilation.

Samples of analyzer real time displays on the instrument include:

![](images/9f95f01e843b82982d6646001496d4cfaee537e0f56154dffccf75d9e9af49b3.jpg)  
FIGURE 8 Sample Displays of Voltage and Current Waveforms

![](images/cef6473ed274974875878f67b865679292d47f4c415be3ec360257b6b965e6d3.jpg)  
FIGURE 9 Three-phase Voltage Waveforms

![](images/b96b291c312a14f625bd3b3dfb6e70103f3e2715997d0956edf9d309fb8a84cd.jpg)  
FIGURE 10 Transient Current Waveforms

![](images/f072d3b474d32db5b679b1c9b6f31ee523712368930e48b507e813a691a6a58b.jpg)  
FIGURE 11 Three-phase Voltage Harmonics

![](images/8c6fa46198ef27120d7b25027ff8b2e11f7ccc78153fc5558ac6957e38d6a5c0.jpg)  
FIGURE 12 Harmonic Direction

![](images/6c70e967f6547c07e3f24b9a850d32e94471b923cd9c85443ee794971c5e2a80.jpg)  
FIGURE 13 Harmonic Sequences

![](images/885edf1ad2c82a3179237f1f007d4f9aa0f24bbc4b0c7af475f20ee46673bb88.jpg)  
FIGURE 14 Phasor Diagram

Examples of real-time data via a computer from the AEMC 3945 include:

![](images/e9ddcf97ab538f530c92b0d9f70b53f2f65bf91800e60847f3b0ec6b1bf0d192.jpg)  
FIGURE 15 AEMC 3945 Configuration via Computer

![](images/3ec64a107aa99e65e79ec3418401057e714f7cce7278807aa5d5b989d217580d.jpg)  
FIGURE 16 Real Time Current Waveforms via Computer

![](images/4e74066cc3cabefe2d3cf718da8b45253e9800778b581993640b9c14bd5d5c0f.jpg)  
FIGURE 17 Real Time Computer Display of Harmonic Currents

![](images/d82fb72242cc2f2e94354c2feec5988f7dd1c986f193cf6079dd81ee32dcd8a3.jpg)  
FIGURE 18   
Unbalance in Real Time via Computer

Up to $8 3 0 \mathrm { V }$ rms voltage measurement and 6500 A, capability of the AEMC 3945 should favor its use on a wide range of marine power quality applications.

# 4.3 Hioki 3196

This harmonic/power quality analyzers can offer some advantages, for example in the area of longer term monitoring plus data recorded and displayed.

The Hioki 3196 can measure currents up to 5000 A and voltages up to 600 V rms, which means, as per the Fluke 43B, it is unsuitable for 690 V or $7 5 0 ~ \mathrm { V }$ systems (the new Fluke 433/434 series can, however, operate at these higher voltage levels).

![](images/741d4c9c5c8d325e320209c2d0119b94bccb0ca8ac073b77521a652e36705fb4.jpg)  
FIGURE 19 Hioki 3196 Power Analyzer with Voltage and Current Probes

Examples of actual survey measurements from a Hioki 3196 follow:

![](images/143eb7a828caf83c81a6fd53816d5d7cd5ec0a320a98aad00d9ca0d27ce070b4.jpg)  
FIGURE 20 AC VFD Three-phase Voltage and Current Measurements from Hioki 3196

![](images/aad6ae347c0013b4b653a789d06f303b7d141b1323e0ca45af0685bc7f376198.jpg)  
FIGURE 21 Harmonic FFT Measurements from Hioki 3196 with $5 ^ { \mathrm { t h } }$ Harmonic Selected

![](images/97061eb15593f883c274c7684cb0f18420decee6ecce85ea8b4e63be071658a8.jpg)  
FIGURE 22 Power System $V _ { t h d }$ Trend Recording via Hioki 3196 as a Number of AC VFDs Are Switched On

![](images/cdee3f1fba803dab2b377271369594035dac87b4e67cfaea32d6c31e70aa0be3.jpg)  
FIGURE 23 $V _ { t h d }$ of all Three Phases Recorded by Hioki 3196 when Active Filter Switched in on Oil Production Platform   
FIGURE 24 Summary of Data Sampled from Hioki 3196

<table><tr><td colspan="6">DMM [No.25 09/02 18:51:44.586 U harm CH1 IN]</td></tr><tr><td>POWER</td><td></td><td>VOLTAGE</td><td></td><td>CURRENT</td><td></td></tr><tr><td>P1</td><td>0.1590MW</td><td>U1</td><td>487.56 V</td><td>I1</td><td>0.6452kA</td></tr><tr><td>P2</td><td>0.1624MW</td><td>U2</td><td>486.43 V</td><td>I2</td><td>0.6580kA</td></tr><tr><td>P3</td><td>0.1591MW</td><td>U3</td><td>486.78 V</td><td>I3</td><td>0.6460kA</td></tr><tr><td>Psum</td><td>0.480MW</td><td>THD-U1</td><td>10.61 %</td><td>THD-I1</td><td>34.55 %</td></tr><tr><td>S1</td><td>0.1816MVA</td><td>THD-U2</td><td>10.49 %</td><td>THD-I2</td><td>34.03 %</td></tr><tr><td>S2</td><td>0.1850MVA</td><td>THD-U3</td><td>10.72 %</td><td>THD-I3</td><td>34.56 %</td></tr><tr><td>S3</td><td>0.1814MVA</td><td>Upk+1</td><td>0.7510kV</td><td>Ipk+1</td><td>1.355kA</td></tr><tr><td>Ssum</td><td>0.548MVA</td><td>Upk+2</td><td>0.7530kV</td><td>Ipk+2</td><td>1.445kA</td></tr><tr><td>Q1</td><td>0.0877Mvar</td><td>Upk+3</td><td>0.7515kV</td><td>Ipk+3</td><td>1.403kA</td></tr><tr><td>Q2</td><td>0.0886Mvar</td><td>Upk-1</td><td>-0.7560kV</td><td>Ipk-1</td><td>-1.398kA</td></tr><tr><td>Q3</td><td>0.0872Mvar</td><td>Upk-2</td><td>-0.7560kV</td><td>Ipk-2</td><td>-1.321kA</td></tr><tr><td>Qsum</td><td>0.263Mvar</td><td>Upk-3</td><td>-0.7487kV</td><td>Ipk-3</td><td>-1.428kA</td></tr><tr><td>PF1</td><td>0.8757</td><td>Uave</td><td>486.92 V</td><td>KF1</td><td>5.98</td></tr><tr><td>PF2</td><td>0.8779</td><td>Unb</td><td>0.16 %</td><td>KF2</td><td>5.89</td></tr><tr><td>PF3</td><td>0.8768</td><td></td><td></td><td>KF3</td><td>5.90</td></tr><tr><td>PFsum</td><td>0.8768</td><td></td><td></td><td>lave</td><td>0.6497kA</td></tr><tr><td></td><td></td><td></td><td></td><td>lunb</td><td>1.23 %</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

# FIGURE 25 Recorded Harmonic Currents by Hioki 3196 on 12-Pulse AC Drive

HARMONICS LIST[No.1 12/14 17:34:52.425 Ext (Stop)]

CH1 I VALUE iHarm OFF

<table><tr><td>Order</td><td>(A)</td><td>Order</td><td>(A)</td><td>Order</td><td>(A)</td></tr><tr><td>1</td><td>100.00</td><td>18</td><td>0.23</td><td>35</td><td>0.94</td></tr><tr><td>2</td><td>0.20</td><td>19</td><td>0.43</td><td>36</td><td>0.17</td></tr><tr><td>3</td><td>0.63</td><td>20</td><td>0.40</td><td>37</td><td>0.60</td></tr><tr><td>4</td><td>0.19</td><td>21</td><td>0.43</td><td>38</td><td>0.33</td></tr><tr><td>5</td><td>0.37</td><td>22</td><td>0.22</td><td>39</td><td>0.22</td></tr><tr><td>6</td><td>0.16</td><td>23</td><td>2.69</td><td>40</td><td>0.18</td></tr><tr><td>7</td><td>0.49</td><td>24</td><td>0.25</td><td>41</td><td>0.20</td></tr><tr><td>8</td><td>1.02</td><td>25</td><td>2.13</td><td>42</td><td>0.26</td></tr><tr><td>9</td><td>0.54</td><td>26</td><td>0.40</td><td>43</td><td>0.09</td></tr><tr><td>10</td><td>1.18</td><td>27</td><td>0.40</td><td>44</td><td>0.29</td></tr><tr><td>11</td><td>8.12</td><td>28</td><td>0.22</td><td>45</td><td>0.09</td></tr><tr><td>12</td><td>0.31</td><td>29</td><td>0.37</td><td>46</td><td>0.21</td></tr><tr><td>13</td><td>6.03</td><td>30</td><td>0.27</td><td>47</td><td>0.21</td></tr><tr><td>14</td><td>0.40</td><td>31</td><td>0.14</td><td>48</td><td>0.09</td></tr><tr><td>15</td><td>0.57</td><td>32</td><td>0.39</td><td>49</td><td>0.06</td></tr><tr><td>16</td><td>0.21</td><td>33</td><td>0.24</td><td>50</td><td>0.19</td></tr><tr><td>17</td><td>0.66</td><td>34</td><td>0.24</td><td>THD</td><td>11.05(%)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The Hioki 3196 is a good harmonic/power quality analyzer, limited by the maximum voltage rating of 600 V rms.

# 5 Measurements on Voltages above 690/750 V AC

Some harmonic analyzers do have the capability to measure harmonics on power systems with voltages up to 690/750/1000 V AC. Above these levels, it is not recommended due to safety reasons, that shore, vessel, rig or platform staff undertake directly-connected harmonic measurements/surveys. In these instances, a specialist company should be subcontracted, who with fully experienced personnel, specialist safety and measurement equipment rated for higher voltage, can safely carry out such measurements.

Note: Some vessels and offshore installations have main power systems based on voltages up to or over 11 kV. At these voltage levels, due to danger of death, special techniques and equipment have to be used in order to directly measure the harmonic currents and voltages. However, these high voltage systems may have on the main switchboards, potential transformers (i.e., voltage transformers) and current transformers (e.g., for the Rogowski type) already installed. Depending on bandwidth (i.e., frequency response) of the transformers (may relatively accurately measure up to the $5 0 ^ { \mathrm { t h } }$ harmonic), the secondaries of the PTs and CTs may be suitable for direct connection to standard harmonic measurement equipment, subject to suitable scaling being taken into account on the measurements (i.e., the actual harmonic voltages and currents will have to be scaled up to match ratios of the transformers) and voltage limits. In these instances, standard harmonic analyzers, including those illustrated, should be able to be used with reasonable accuracy, subject to the above limitations re PT and CT bandwidth and scaling accuracy, etc. To this end, scaleable CT adaptor boxes are available as options with some harmonic analyzers, such as the AEMC 3945.

# A P P E N D I X

# 1 Recommended Reading

Power System Harmonics, $2 ^ { n d }$ Edition. (2003). Jos Arrillaga and Neville Watson.   
ISBN 0-470-85129-5.   
Assessment of Electric Power Quality in Ships fitted with Converter Sub-systems. (2004). Janusz Mindykowski.   
ISBN 83-88621-07-6   
Electrical Power Systems Quality, $2 ^ { n d }$ Edition. (2002). Roget Dugan, Mark Mc Granaghan et al.   
ISBN 0-07-1386220-X.   
Power Electronic Converter Harmonics. (1996). Derek Paice.   
ISBN 0-7803-5394-3.   
Voltage Quality in Electrical Power Systems. (2001). J Schlabbach, D Blume et al.   
ISBN 0-85296-975-9.   
Variable Frequency AC Motor Drive Systems. (1988). David Finney.   
ISBN 0-86341-1142.   
IEEE Recommended Practices and Requirements for Harmonic Control in Power Systems. (1992). IEEE.   
ISBN 1-55937-239-7.   
Hazardous Areas – A User’s Guide to AC Drive Systems. (1989). Ian C Evans & Des Horne, Elekotrotek Drives Ltd.   
Maritime Electrical Installation and Diesel Electric Propulsion. (2004). Alf-Kare Adnanes. ABB AS, Norway.   
AC Drives : Mitigation – A look at the options. Ian C Evans, Harmonic Solutions Co.Uk. Electricity + Control (November 2004).   
Handbook of Electrical Calculations, $3 ^ { r d }$ Edition. (2001). H Wayne Beatty.   
ISBN 0-07-136298-3.   
Harmonic Mitigation for Offshore AC Variable Frequency Drives. Ian C Evans, Harmonic Solutions Co.Uk. Offshore Visie (October 2002).   
The Future is Electric – The Progress of Electric Propulsion. Ian C Evans. Motor Ship (September 2003).   
From Oars to Reactors – Electric Drive: The Future of Naval Propulsion. Ian C Evans. Motor Ship (October 2003).   
Electrical Power Quality and Ships Safety. (2004). Janusz Mindykowski, Edward Szmit and Tomasz Tarasiuk. Polish Academy of Sciences.   
Harmonic Mitigation for AC Thruster and Small Propulsion Drives. Ian C Evans, Harmonic Solutions Co.Uk. Marine Propulsion International (October 2002).

This Page Intentionally Left Blank