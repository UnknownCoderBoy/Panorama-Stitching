import cv2
import numpy as np
import streamlit as st

st.set_page_config(page_title="Panorama Stitching")

st.title("Panorama Stitching")

image_files = st.file_uploader("Upload Images", type=["png","jpg","jpeg"], accept_multiple_files=True, key="imgs")

imgs = []
for image_file in image_files:
    image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4)
    imgs.append(image)

if imgs and len(imgs)>1:

    columns = st.columns(len(imgs))

    for i, img in enumerate(imgs):
        with columns[i]:
            st.image(img, channels="BGR", caption=f'Image {i+1}', use_column_width=True)

    stitchy=cv2.Stitcher.create()
    (dummy, output) = stitchy.stitch(imgs)

    if dummy != cv2.Stitcher_OK:
        st.error("Stitching is not successful.")
    else:
        st.success("Your Panorama is ready!")

        # Display the final stitched result in Streamlit
        st.image(output, channels="BGR", caption="Final Result", use_column_width=True)
else:
    st.warning("No images were loaded.")
