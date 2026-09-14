from PIL import Image
from IPython.display import display


# ============================================================
# 1. Open an image using Pillow
# ============================================================

img = Image.open("/content/spaceship.webp")

print("1. Image opened successfully")


# ============================================================
# 2. Display an image using Pillow
# ============================================================

print("\n2. Original Image:")
display(img)


# ============================================================
# 3. Print mode, size, and format
# ============================================================

print("\n3. Image Information")
print("Mode:", img.mode)
print("Size:", img.size)
print("Format:", img.format)


# ============================================================
# 4. Rotate an image by 40 degrees
# ============================================================

rotated = img.rotate(40)

print("\n4. Rotated Image (40 degrees):")
display(rotated)


# ============================================================
# 5. Flip image vertically and save as vertical.png
# ============================================================

vertical = img.transpose(Image.FLIP_TOP_BOTTOM)

vertical.save("/content/vertical.png")

print("\n5. Vertically Flipped Image:")
display(vertical)
print("Saved as vertical.png")


# ============================================================
# 6. Resize image to 100 x 300 pixels
# ============================================================

print("\n6. Resize to 100 x 300")

print("Before resizing:", img.size)
display(img)

resized = img.resize((100, 300))

print("After resizing:", resized.size)
display(resized)


# ============================================================
# 7. Resize image to 40 x 40 using BILINEAR
# ============================================================

print("\n7. Resize to 40 x 40 using BILINEAR")

print("Before resizing:", img.size)
display(img)

resized_test = img.resize((40, 40), Image.BILINEAR)

print("After resizing:", resized_test.size)
display(resized_test)

resized_test.save("/content/resized_test.jpg")

print("Saved as resized_test.jpg")


# ============================================================
# 8. Display original size and new size
# ============================================================

print("\n8. Original and New Size")

print("Original size:", img.size)

new_image = img.resize((100, 300))

print("New size:", new_image.size)


# ============================================================
# 9. Crop an image using specified coordinates
# ============================================================

print("\n9. Cropping Image")

print("Original Image:")
display(img)

cropped = img.crop((100, 100, 400, 400))

print("Cropped Image:")
display(cropped)


# ============================================================
# 10. Open, crop and store in separate variable
# ============================================================

print("\n10. Crop and Store in Separate Variable")

cropped_image = img.crop((100, 100, 400, 400))

print("Cropped image stored in variable: cropped_image")
display(cropped_image)