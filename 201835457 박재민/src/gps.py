from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_gps_info(image_path):
    img = Image.open(image_path)
    exif_data = img._getexif()
    if not exif_data:
        return None
    gps_info = {}
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        if tag_name == "GPSInfo":
            for key, val in value.items():
                gps_tag = GPSTAGS.get(key, key)
                gps_info[gps_tag] = val
    return gps_info
