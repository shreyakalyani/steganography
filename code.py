from PIL import Image

# Function to hide a message in an image
def hide_message(image_path, message, output_path):
    image = Image.open(image_path)
    encoded_image = image.copy()

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Add a delimiter to mark the end of the message
    binary_message += '1111111111111110'

    data_index = 0

    # Iterate through each pixel and modify the least significant bit of each color channel
    for x in range(encoded_image.width):
        for y in range(encoded_image.height):
            pixel = list(encoded_image.getpixel((x, y)))

            for color_channel in range(3):
                if data_index < len(binary_message):
                    pixel[color_channel] = pixel[color_channel] & ~1 | int(binary_message[data_index])
                    data_index += 1

            encoded_image.putpixel((x, y), tuple(pixel))

    encoded_image.save(output_path)
    print("Message hidden successfully!")

# Function to extract a message from an image
def extract_message(image_path):
    image = Image.open(image_path)
    binary_message = ''
    data_index = 0
    message = ''

    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))

            for color_channel in range(3):
                binary_message += str(pixel[color_channel] & 1)
                data_index += 1

                # Check for the delimiter to mark the end of the message
                if data_index % 16 == 0:
                    if binary_message[-16:] == '1111111111111110':
                        return message

            message = ''.join([chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8)])

    return message

# Example usage
if __name__ == "__main__":
    # Hide a message in an image
    hide_message("image.jpg", "This is a secret message.", "encoded_image.png")

    # Extract the message from the encoded image
    extracted_message = extract_message("encoded_image.png")
    print("Extracted Message:", extracted_message)
