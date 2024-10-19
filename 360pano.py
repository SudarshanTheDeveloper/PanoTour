import cv2
import numpy as np

def cube_map_to_360(front, back, right, left, top, bottom):
    width, height = 16384, 8192  # 4K equirectangular resolution
    output = np.zeros((height, width, 3), dtype=np.uint8)

    # Cube map coordinates
    for y in range(height):
        for x in range(width):
            theta = (x / width) * 2 * np.pi  # Angle in radians
            phi = (y / height) * np.pi - np.pi / 2  # Angle from top to bottom
            sx, sy, sz = np.cos(phi) * np.cos(theta), np.sin(phi), np.cos(phi) * np.sin(theta)

            if abs(sx) >= abs(sy) and abs(sx) >= abs(sz):
                if sx > 0:
                    img = right
                    u = -sz / sx * 0.5 + 0.5
                    v = -sy / sx * 0.5 + 0.5
                else:
                    img = left
                    u = sz / -sx * 0.5 + 0.5
                    v = -sy / -sx * 0.5 + 0.5
            elif abs(sy) >= abs(sx) and abs(sy) >= abs(sz):
                img = top if sy > 0 else bottom
                u = (sx / sy * 0.5) + 0.5
                v = (sz / sy * 0.5) + 0.5
            else:
                img = front if sz > 0 else back
                u = (sx / sz * 0.5) + 0.5
                v = (sy / sz * 0.5) + 0.5

            u = int(u * img.shape[1])
            v = int(v * img.shape[0])

            if 0 <= u < img.shape[1] and 0 <= v < img.shape[0]:
                output[y, x] = img[v, u]

    return output

# Function to blend seams between adjacent cube faces
def blend_seams(img1, img2, blend_width=5):
    alpha = np.linspace(0, 1, blend_width)
    for i in range(blend_width):
        img1[:, -blend_width + i] = (img1[:, -blend_width + i] * (1 - alpha[i]) + img2[:, i] * alpha[i]).astype(np.uint8)
        img2[:, i] = img1[:, -blend_width + i]
    return img1, img2

# Load your cube map images and apply transformations
front = cv2.flip(cv2.imread('File_5.jpg'), 1)  # Flip horizontally
back = cv2.rotate(cv2.imread('File_4.jpg'), cv2.ROTATE_180)
right = cv2.rotate(cv2.imread('File_2.jpg'), cv2.ROTATE_180)
left = cv2.rotate(cv2.imread('File_3.jpg'), cv2.ROTATE_180)

top = cv2.transpose(cv2.imread('File_1.jpg'))
top = cv2.flip(top, 1)

bottom = cv2.transpose(cv2.imread('File_0.jpg'))
bottom = cv2.flip(bottom, -1)

# Blend the seams between adjacent cube faces (e.g., front and right, back and left)
right, front = blend_seams(right, front, blend_width=5)
back, left = blend_seams(back, left, blend_width=5)

# Create the 360-degree image
result_image = cube_map_to_360(front, back, right, left, top, bottom)

# Save the result
cv2.imwrite('360_image_4k_seam_blended.jpg', result_image)

# Display the result (optional)
cv2.imshow('360 Image 4K Seam Blended', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
