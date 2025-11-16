# download this file first and Install
# tesseract-ocr-w64-setup-5.5.0.20241111



# install this library
# pip install opencv-python pytesseract pyttsx3






import cv2
import pytesseract
import pyttsx3

# Path to the Tesseract executable (update this path if necessary)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the volume to maximum (range is from 0.0 to 1.0)
engine.setProperty('volume', 1.0)  # 1.0 is the maximum volume

# Set the speech rate (words per minute)
rate = engine.getProperty('rate')  # Get the current rate
engine.setProperty('rate', rate - 50)  # Decrease rate for better clarity (default is 200)

# Function to capture an image from the camera
def capture_image():
    # Open the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return None

    print("Press 's' to capture an image.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow("Camera Feed", frame)

        # Wait for user to press 's' to save the image
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # Save the captured image
            cv2.imwrite("scanned_image.jpg", frame)
            print("Image captured and saved!")
            break

    cap.release()
    cv2.destroyAllWindows()
    return "scanned_image.jpg"

# Function to extract text using OCR
def extract_text_from_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Use Tesseract OCR to extract text
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

# Function to speak the extracted text
def speak_text(text):
    if text.strip():  # Ensure the text is not empty or just spaces
        engine.say(text)
        engine.runAndWait()
    else:
        print("No text found to speak.")

# Main function
def main():
    image_path = capture_image()
    if image_path:
        # Extract text from the captured image
        text = extract_text_from_image(image_path)
        print("Extracted Text:\n", text)

        if text:
            # Speak the extracted text
            speak_text(text)
        else:
            print("No text found in the image.")
            speak_text("No text found in the image")

if __name__ == "__main__":
    main()



# import cv2
# import pytesseract
# import pyttsx3

# # Path to the Tesseract executable (update this path if necessary)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set the volume to maximum (range is from 0.0 to 1.0)
# engine.setProperty('volume', 1.0)  # 1.0 is the maximum volume

# # Set the speech rate (words per minute)
# rate = engine.getProperty('rate')  # Get the current rate
# engine.setProperty('rate', rate - 50)  # Decrease rate for better clarity (default is 200)

# # Function to capture an image from the camera
# def capture_image():
#     # Open the camera (0 is usually the default camera)
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Error: Could not access the camera.")
#         return None

#     # Set camera resolution to Full HD (1920x1080), or adjust to your needs
#     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # Set width to 1920 pixels
#     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  # Set height to 1080 pixels

#     print("Press 's' to capture an image.")

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Error: Failed to capture image.")
#             break

#         cv2.imshow("Camera Feed", frame)

#         # Wait for user to press 's' to save the image
#         key = cv2.waitKey(1) & 0xFF
#         if key == ord('s'):
#             # Save the captured image
#             cv2.imwrite("scanned_image.jpg", frame)
#             print("Image captured and saved!")
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     return "scanned_image.jpg"

# # Function to extract text using OCR
# def extract_text_from_image(image_path):
#     # Read the image using OpenCV
#     image = cv2.imread(image_path)

#     # Use Tesseract OCR to extract text
#     extracted_text = pytesseract.image_to_string(image)
#     return extracted_text

# # Function to speak the extracted text
# def speak_text(text):
#     if text.strip():  # Ensure the text is not empty or just spaces
#         engine.say(text)
#         engine.runAndWait()
#     else:
#         print("No text found to speak.")

# # Main function
# def main():
#     image_path = capture_image()
#     if image_path:
#         # Extract text from the captured image
#         text = extract_text_from_image(image_path)
#         print("Extracted Text:\n", text)

#         if text:
#             # Speak the extracted text
#             speak_text(text)
#         else:
#             print("No text found in the image.")

# if __name__ == "__main__":
#     main()



