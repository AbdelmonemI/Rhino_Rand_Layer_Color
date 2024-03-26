import rhinoscriptsyntax as rs
import random

def assign_random_colors_to_layers():
    # Get all the layers in the document
    layers = rs.LayerNames()

    # Iterate through each layer
    for layer in layers:
        # Generate random RGB values
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        # Combine RGB values into a color string
        color = (red, green, blue)

        # Assign the random color to the layer
        rs.LayerColor(layer, color)

# Call the function to assign random colors to layers
assign_random_colors_to_layers()
