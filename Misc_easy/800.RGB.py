def similarRGB(color: str):
    """
    Given an arbitrary string consisting of the characters 'R', 'G', 'B', and '#',
    return a string representing the closest corresponding color to the input.
    The input color is represented as a string consisting of the characters 'R', 'G', 'B', and '#'.
    The output color is represented as a string consisting of the characters 'R', 'G', 'B', and '#'.
    """
    # Step 1: Convert the input color to a list of integers
    color_list = [int(color[i:i + 2], 16) for i in range(1, len(color), 2)]
  
    # Step 2: Find the minimum difference between the input color and all the colors in the list
    return '#'+''.join([hex(round(c/int('0x11', 16)))[2]*2 for c in color_list])

def main():
    print(similarRGB("#09f166"))

main()
