import csv

# Define the questions and choices
questions = [
    "What is the unit of resistance?",
    "Which component is used to store electrical charge?",
    "What does a multimeter measure?",
    "What is the symbol for a resistor in a schematic?",
    "Which law relates voltage, current, and resistance?",
    "What is the function of a diode in a circuit?",
    "What does continuity indicate in a circuit?",
    "What is the basic unit of capacitance?",
    "How does increasing resistance affect current in a circuit?",
    "Which of the following best describes a voltage divider?",
    "Why are resistors used in series circuits?",
    "What happens to voltage across each component in a parallel circuit?",
    "How do capacitors differ from batteries?",
    "What role does a potentiometer play in a circuit?",
    "Which property of resistive sensors changes with the measured quantity?",
    "How can you determine the value of a resistor using color bands?",
    "Calculate the total resistance for two resistors of 10Ω and 20Ω in series.",
    "If you need to reduce a 9V input to 3V using a voltage divider, what should be the ratio of resistances (R1/R2)?",
    "A circuit has three paths with currents of 2A, 3A, and 4A respectively. What is the total current supplied by the source in this parallel circuit?",
    "Using Ohm’s Law, find the voltage across a resistor with a current of 2A and resistance of 5Ω.",
    "Given a parallel circuit with resistors of values 100Ω and 200Ω, calculate the total resistance.",
    "Design an LED brightness control using a potentiometer; which configuration would you use?",
    "If you have an LED that requires exactly 2V and you have only a 5V supply, how would you use resistors to achieve this voltage drop?",
    "In designing circuits with capacitors, which factor would most affect their ability to smooth out fluctuations in power supply?"
]

choices = [
    ["Ohm", "Volt", "Ampere", "Farad"],
    ["Resistor", "Capacitor", "Diode", "Transistor"],
    ["Resistance", "Voltage Drop", "Current", "All of the above"],
    ["Zigzag line", "Parallel lines", "Triangle pointing to a line", "Circle with a plus sign"],
    ["Ohm’s Law", "Kirchhoff's Law", "Faraday's Law", "Coulomb's Law"],
    ["Allow current to flow in one direction only", "Provide resistance", "Store charge", "Amplify signals"],
    ["Complete path for electron flow", "High resistance", "Voltage drop", "Open circuit"],
    ["Farad", "Ohm", "Volt", "Ampere"],
    ["Decreases current", "Increases current", "No effect on current", "Doubles the current"],
    ["Reduces voltage using resistors","Increases voltage across components in series","Stores energy for later use","Converts AC to DC"],
    ["To increase total resistance","To decrease total resistance","To store charge","To allow current to bypass components"],
    ["Voltage remains the same across each component","Voltage increases with each component","Voltage decreases with each component","Voltage becomes zero"],
    ["Capacitors charge and discharge faster than batteries","Capacitors store more energy than batteries","Batteries are non-rechargeable; capacitors are rechargeable","Capacitors have higher voltage ratings than batteries"],
    ["Serves as an adjustable voltage divider","Acts as a fixed resistor","Converts AC to DC","Amplifies signals"],
    ["Resistance","Capacitance","Voltage","Current"],
    ["By decoding the color sequence into numerical values","By measuring its length","By counting the number of bands","By checking its weight"],
    ["30Ω","10Ω","20Ω","200Ω"],
    ["1:2 ","2:1 ","3:1 ","1:3"],
    ["9A ","7A ","5A ","4A"],
    ["10V ","5V ","2V ","7V"],
    ["67Ω ","300Ω ","150Ω ","50Ω"],
    ["As an adjustable voltage divider before LED ","Series with LED ","Parallel with LED ","As an independent power source"],
    ["Use two equal resistors in series and take output from one resistor ","Use one resistor directly across LED ","Use no resistor; connect directly ","Use three resistors in parallel"],
    ["The capacitance value (Farads)","The physical size of capacitor","The material used for dielectric","The color coding on capacitor"]
]

# Write to CSV
with open('quiz.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write questions as headers
    writer.writerow(questions)
    
    # Write choices under each question
    for i in range(4):  # Assuming each question has four choices
        writer.writerow([choices[j][i] for j in range(len(questions))])