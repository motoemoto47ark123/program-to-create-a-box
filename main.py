def draw_box(width, height):
    # Draw top border
    print("┌" + "─" * (width - 2) + "┐")

    # Draw middle lines
    for _ in range(height - 2):
        print("│" + " " * (width - 2) + "│")

    # Draw bottom border
    print("└" + "─" * (width - 2) + "┘")


# Get user input for box dimensions
box_width = int(input("Enter the width of the box: "))
box_height = int(input("Enter the height of the box: "))

# Draw the box
draw_box(box_width, box_height)
