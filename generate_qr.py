import qrcode
from PIL import Image

# Data to encode
data = "https://breakfastcorner.netlify.app/"  # Replace with actual URL if needed

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the logo
logo = Image.open("Breakfast corner.png")

# Calculate logo size (about 1/4 of QR code size)
qr_width, qr_height = qr_img.size
logo_size = qr_width // 4
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Create a mask for the logo (circular or square)
mask = Image.new('L', (logo_size, logo_size), 0)
mask_draw = Image.new('L', (logo_size, logo_size), 255)
mask_draw.paste(0, (logo_size//4, logo_size//4, 3*logo_size//4, 3*logo_size//4))
mask = mask_draw

# Position the logo in the center
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste the logo onto the QR code
qr_img.paste(logo, pos, mask)

# Save the image
qr_img.save("Breakfast Corner QR Code.png")

print("QR code with logo generated: Breakfast Corner QR Code.png")
