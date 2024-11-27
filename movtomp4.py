import av

def convert_mov_to_mp4(input_file, output_file):
    input_container = av.open(input_file)
    output_container = av.open(output_file, 'w')

    # Get the first video stream
    stream = input_container.streams.video[0]
    
    # Set the output stream with the proper codec and frame rate
    out_stream = output_container.add_stream('libx264', rate=stream.average_rate)

    # Decode frames from the input container and encode them to the output container
    for frame in input_container.decode(stream):
        packet = out_stream.encode(frame)
        output_container.mux(packet)

    # Flush the encoder
    packet = out_stream.encode(None)
    if packet:
        output_container.mux(packet)

    # Close the output container
    output_container.close()

input_file = '/Users/karanraj/Desktop/Screen Recording 2024-11-14 at 1.31.15 PM.mov'
output_file = "/Users/karanraj/Desktop/output.mp4"

convert_mov_to_mp4(input_file, output_file)
