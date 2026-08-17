# import the cv2 library
import cv2
# Load an color image
img = cv2.imread('iris-1.jpg',1)

if img is None:
    print("Error: Image not found or unable to read.")
else:
    print("Image loaded successfully!")

height, width, channels = img.shape
size = img.size
data_type = img.dtype

print(f"A. Height:    {height} pixels")
print(f"B. Width:     {width} pixels")
print(f"C. Channels:  {channels}")
print(f"D. Size:      {size} ")
print(f"E. Data type: {data_type}")

cam = cv2.VideoCapture(1)

# Get the default frame width and height and fps
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))

# Save camera properties in a text file
with open("camera_outputs.txt", "w") as file:
    file.write(f"A. fps:    {fps}\n")
    file.write(f"B. height: {frame_height}\n")
    file.write(f"C. width:  {frame_width}\n")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    # Write the frame to the output file
    out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
out.release()
cv2.destroyAllWindows()