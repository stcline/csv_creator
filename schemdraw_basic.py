import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to draw a simple circuit with a resistor and LED
def draw_circuit(resistor_value, led_color):
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Draw battery
    ax.add_patch(patches.Rectangle((0.1, 0.4), 0.1, 0.2, edgecolor='black', facecolor='none'))
    ax.add_patch(patches.Rectangle((0.2, 0.45), 0.05, 0.1, edgecolor='black', facecolor='none'))
    
    # Draw resistor
    ax.add_patch(patches.Rectangle((0.3, 0.45), 0.2, 0.05, edgecolor='black', facecolor='none'))
    ax.text(0.4, 0.5, f'{resistor_value}Ω', fontsize=12, ha='center')
    
    # Draw LED
    ax.add_patch(patches.RegularPolygon((0.6, 0.475), numVertices=3, radius=0.05, orientation=-3.14/2,
                                        edgecolor=led_color, facecolor='none'))
    ax.text(0.65, 0.5, f'{led_color.capitalize()} LED', fontsize=12, ha='left', color=led_color)
    
    # Draw wires
    ax.plot([0.15, 0.3], [0.5, 0.5], 'k-')  # Wire from battery to resistor
    ax.plot([0.5, 0.6], [0.5, 0.5], 'k-')   # Wire from resistor to LED
    ax.plot([0.65, 1], [0.5, 0.5], 'k-')    # Wire from LED to ground
    
    # Ground symbol
    ax.plot([1, 1], [0.4, 0.5], 'k-')
    ax.plot([0.98, 1.02], [0.4, 0.4], 'k-')
    
    # Set plot limits and remove axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Save the figure
    plt.title(f'Circuit with {resistor_value}Ω Resistor and {led_color.capitalize()} LED')
    plt.savefig(f'circuit_{resistor_value}_{led_color}.png')
    plt.close()

# Generate four different schematic diagrams
resistor_values = [220, 330]
led_colors = ['red', 'green', 'blue', 'yellow']

for resistor in resistor_values:
    for color in led_colors:
        draw_circuit(resistor, color)