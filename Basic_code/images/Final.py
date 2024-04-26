import cv2

def Load_img(path):
    # Load the image
    path1 =  path
    image = cv2.imread(path1)
    return image

def convert_img(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def gray_img(g_img):
    # Preprocess the image (for example, apply thresholding)
    gray_image = g_img
    _, thresh = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)
    return thresh

def For_contors(thresh_img):
    # Find contours
    thresh = thresh_img
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

# load image
image = Load_img("E:\FYP\code\images\single_plate.png")

# convert_img image 
con_img = convert_img(image)

# gray image 
gray_image =  gray_img(con_img)

# for getting contours
contours = For_contors(gray_image)

    # Create a list to store the cropped solar plates
cropped_plates = []

# Iterate through each contour
for contour in contours:
# Get the bounding box of the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Crop the solar plate from the original image
    cropped_plate = image[y:y+h, x:x+w]

    # Add the cropped plate to the list
    cropped_plates.append(cropped_plate)
# Display the cropped plates (optional)
for i, plate in enumerate(cropped_plates):
    # cv2.imshow(f'Solar Plate {i}', plate)
    cv2.imwrite(f'solar_plate_{i}.jpg', plate)
