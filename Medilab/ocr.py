import cv2
import pytesseract
from tkinter import Tk, Text, Button, Frame, Label
from PIL import Image, ImageTk

# Path to Tesseract executable (change this according to your setup)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to perform OCR on a frame
def perform_ocr(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR
    text = pytesseract.image_to_string(gray)

    return text

# Function to save text to a file
def save_text(text):
    with open("scanned_text.txt", "a") as f:
        f.write(text + '\n')  # Append text with a newline character

# Function to capture frame from webcam, perform OCR, and update GUI
def update_frame():
    # Capture frame from webcam
    ret, frame = cap.read()

    if ret:
        # Perform OCR on the frame
        text = perform_ocr(frame)

        # Display the text in the GUI
        text_box.delete(1.0, "end")
        text_box.insert("end", text)

        # Save the scanned text to a file
        save_text(text)

        # Display the frame in the GUI
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        video_label.config(image=frame)
        video_label.image = frame

    # Schedule the update after a delay (milliseconds)
    root.after(10, update_frame)

# Main function
def main():
    # Initialize webcam
    global cap
    cap = cv2.VideoCapture(0)

    # Create GUI
    global root
    root = Tk()
    root.title("Live Text Recognition")

    # Frame to hold the text box and buttons
    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    # Label to display the video feed
    global video_label
    video_label = Label(root)
    video_label.pack()

    # Text box to display scanned text
    global text_box
    text_box = Text(root, height=10, width=50)
    text_box.pack(pady=10)

    # Start live text scanning
    update_frame()

    # Button to quit the application
    quit_button = Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady=10)

    # Start GUI main loop
    root.mainloop()

    # Release the capture when GUI is closed
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()