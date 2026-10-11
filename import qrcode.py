import qrcode
from PIL import Image, ImageDraw, ImageOps

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
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

# Load the logo
logo = Image.open("Breakfast corner.png").convert("RGBA")

# Calculate logo size (about 1/4 of QR code size)
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.25)  # 25% of QR code size
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Create a mask for the logo (circular or square)
mask = Image.new('L', (logo_size, logo_size), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0, 0, logo_size, logo_size), fill=255)

# Apply Circular mask to the logo
circular_logo = Image.new('RGBA', (logo_size, logo_size), (0, 0, 0, 0))
circular_logo.paste(logo, mask=mask)

border = 10
bordered_size = logo_size + border * 2
bordered_logo = Image.new("RGBA", (bordered_size, bordered_size), (0, 0, 0, 0))

# White circle background
bg_mask = Image.new("L", (bordered_size, bordered_size), 0)
bg_draw = ImageDraw.Draw(bg_mask)
bg_draw.ellipse((0, 0, bordered_size, bordered_size), fill=255)

white_bg = Image.new("RGBA", (bordered_size, bordered_size), "white")
bordered_logo.paste(white_bg, mask=bg_mask)
bordered_logo.paste(circular_logo, (border, border), mask=circular_logo)


# Paste logo in the center of QR code
pos_x = (qr_width - bordered_size) // 2
pos_y = (qr_height - bordered_size) // 2
qr_img.paste(bordered_logo, (pos_x, pos_y), mask=bordered_logo)

# Save the image
qr_img.save("Breakfast Corner QR Code.png")

print("QR code with logo generated: Breakfast Corner QR Code.png")
