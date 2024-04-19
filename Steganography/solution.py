from PIL import Image
import io

class Frame:
    def __init__(self, graphical_control_extension, image_descriptor, image_data):
        self.graphical_control_extension = graphical_control_extension
        self.image_descriptor = image_descriptor
        self.image_data = image_data


def parse_gif_frame(frame_data):
    # Find indexes of frame components
    gce_start = frame_data.find(b'\x00\x21\xF9')
    gce_end = frame_data.find(b'\x00\x2C', gce_start + 1)

    if gce_start == -1 or gce_end == -1:
        return None

    image_descriptor_start = gce_end + 1
    image_descriptor_end = image_descriptor_start + 4

    image_data_start = image_descriptor_end + 1
    image_data_end = frame_data.rfind(b'\x00')

    # Extract frame components
    graphical_control_extension = frame_data[gce_start:gce_end + 1]
    image_descriptor = frame_data[image_descriptor_start:image_descriptor_end + 1]
    image_data = frame_data[image_data_start:image_data_end]

    return Frame(graphical_control_extension, image_descriptor, image_data)

def processImage(infile):
    try:
        image = Image.open(infile)
    except IOError:
        print("Cant load", infile)
        exit(1)
    i = 0
    mypalette = image.getpalette()

    try:
        while 1:
            image.putpalette(mypalette)
            new_image = Image.new("RGBA", image.size)
            new_image.paste(image)
            new_image.save('frame'+str(i)+'.png')

            i += 1
            image.seek(image.tell() + 1)

    except EOFError:
        pass # end of sequence


if __name__ == "__main__":
    gif_path = input("Enter the path to the GIF file: ")

    frames = []
    with open(gif_path, "rb") as f:
        gif_data = f.read()

    # Find indexes of frame boundaries
    frame_start_indexes = [i for i in range(len(gif_data)) if gif_data[i:i + 3] == b'\x00\x21\xf9']

    # Split the GIF data into frames
    for start_index in frame_start_indexes:
        # Find the end of the frame
        end_index = gif_data.find(b'\x00\x21', start_index + 1)
        if end_index < start_index:
            end_index = gif_data.find(b'\x00\x3B', start_index + 1)
        if end_index == -1:
            continue

        # Extract frame data
        frame_data = gif_data[start_index:end_index + 1]

        # Parse frame and add to list
        frame = parse_gif_frame(frame_data)
        if frame is not None:
            frames.append(frame)

    # Display frames
    for i, frame in enumerate(frames):
        print(f"Frame {i + 1}:")
        print("Graphical Control Extension:", frame.graphical_control_extension.hex())
        print("Image Descriptor:", frame.image_descriptor.hex())
        print("\n")

    processImage(gif_path)
