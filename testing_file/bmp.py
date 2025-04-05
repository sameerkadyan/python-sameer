import struct

def create_bmp(sample1):
    # BMP file header
    bmp_header = b'BM'  # Signature
    file_size = 54 + 1  # 54 bytes for header + 1 byte for the pixel data
    reserved = 0
    offset = 54  # Offset where the pixel data starts

    # DIB header (BITMAPINFOHEADER)
    header_size = 40  # Size of the DIB header
    width = 1  # Image width (1 pixel)
    height = 1  # Image height (1 pixel)
    planes = 1  # Number of color planes
    bit_count = 24  # 24 bits per pixel (RGB)
    compression = 0  # No compression
    image_size = 1 * 3  # 1 pixel, 3 bytes (RGB)
    x_resolution = 0  # No resolution
    y_resolution = 0  # No resolution
    colors_used = 0  # Color table not used
    important_colors = 0  # All colors are important

    # Pixel data (RGB color)
    pixel_data = b'\x00\x00\xff'  # Blue (BMP uses BGR instead of RGB)

    # Write to the file
    with open(sample1, 'wb') as bmp_file:
        # Write the BMP header
        bmp_file.write(bmp_header)
        bmp_file.write(struct.pack('<I', file_size))  # File size
        bmp_file.write(struct.pack('<H', reserved))  # Reserved
        bmp_file.write(struct.pack('<H', reserved))  # Reserved
        bmp_file.write(struct.pack('<I', offset))  # Offset to pixel data
        
        # Write the DIB header
        bmp_file.write(struct.pack('<I', header_size))  # Header size
        bmp_file.write(struct.pack('<I', width))  # Width
        bmp_file.write(struct.pack('<I', height))  # Height
        bmp_file.write(struct.pack('<H', planes))  # Planes
        bmp_file.write(struct.pack('<H', bit_count))  # Bits per pixel
        bmp_file.write(struct.pack('<I', compression))  # Compression
        bmp_file.write(struct.pack('<I', image_size))  # Image size
        bmp_file.write(struct.pack('<I', x_resolution))  # X resolution
        bmp_file.write(struct.pack('<I', y_resolution))  # Y resolution
        bmp_file.write(struct.pack('<I', colors_used))  # Colors used
        bmp_file.write(struct.pack('<I', important_colors))  # Important colors
        
        # Write pixel data (1 pixel in this case)
        bmp_file.write(pixel_data)

# Create the BMP file
create_bmp('sample1.bmp')
