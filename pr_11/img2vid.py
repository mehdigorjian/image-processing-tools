import cv2, os
def generate_video(): 
    image_folder = 'IMG_floyd'
    video_name = 'videoProcessing.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")] 

    frame = cv2.imread(os.path.join(image_folder, images[0])) 

    # setting the frame width, height width 
    height, width, _ = frame.shape   
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    # Appending the images to the video one by one 
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image)))  
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated 

# Calling the generate_video function 
generate_video() 