#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import matplotlib.pyplot as plt


# In[ ]:


def img2sketch(photo, k_size):
    #Read Image
    photo= r"D:\C DATA\house.jpg"
    image=cv2.imread(photo)
    cv2.imshow("original image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #Convert BGR image to RGB
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  
 
    
    
    # Convert to Grey Image
    grey_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_image=cv2.bitwise_not(grey_image)
    #invert_img=255-grey_img

    # Blur image
    blur_image=cv2.GaussianBlur(invert_image, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_image=cv2.bitwise_not(blur_image)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_image=cv2.divide(grey_image,invblur_image, scale=256.0)

    # Save Sketch 
    cv2.imwrite('sketch.png', sketch_image)

    # Display sketch
    cv2.imshow('sketch image',sketch_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    plt.figure(figsize=(14,8))
    plt.subplot(1,2,1)
    plt.title('Original image', size=18)
    plt.imshow(RGB_image)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.title('Sketch', size=18)
    rgb_sketch=cv2.cvtColor(sketch_image, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_sketch)
    plt.axis('off')
    plt.show()

    
#Function call
img2sketch(photo='image.png', k_size=7)

    


# In[ ]:




