import cv2
from keras.preprocessing import image
import warnings;

warnings.filterwarnings('ignore')

from skimage.color import rgb2lab, lab2rgb
from skimage.io import imsave
import numpy as np

from skimage.io import imread, imshow
import keras
from matplotlib import pyplot as plt


class image_processing_functions:
    def convert_img(self, img_path):
        img = image.load_img(img_path, target_size=(256, 256, 3))
        img = image.img_to_array(img)
        img = img / 255.
        img = np.array(img)
        return img

    def denoising(self, image):
        autoencoder = keras.models.load_model("denoising-11-5.h5")

        noise = np.random.normal(loc=0, scale=1, size=img.shape)

        noisy = np.clip((img + noise * 0.2), 0, 1)

        noisy = cv2.resize(noisy, (256, 256))

        return noisy

    def pixalate_image(self, image, scale_percent=23):
        autoencoder = keras.models.load_model("pixalate_scale_23_16-5-21.h5")
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)

        small_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        # scale back to original size
        width = int(small_image.shape[1] * 100 / scale_percent)
        height = int(small_image.shape[0] * 100 / scale_percent)
        dim = (width, height)

        low_res_image = cv2.resize(small_image, dim, interpolation=cv2.INTER_AREA)

        low_res_image = cv2.resize(low_res_image, (256, 256))

        return low_res_image

    def colorization(self, image):
        img1_color.append(img1)

        img1_color = np.array(img1_color, dtype=float)
        img1_color = rgb2lab(1.0 / 255 * img1_color)[:, :, :, 0]
        img1_color = img1_color.reshape(img1_color.shape + (1,))

        output1 = model.predict(img1_color)
        output1 = output1 * 128

        result = np.zeros((256, 256, 3))
        result[:, :, 0] = img1_color[0][:, :, 0]
        result[:, :, 1:] = output1[0]
        imsave("result.png", lab2rgb(result))
        imshow(lab2rgb(result))
        plt.imshow(lab2rgb(result))

    def inpainting(self, img):
        autoencoder = keras.models.load_model("inpanting model name")

        # mask = np.full((256,256,3), 255, np.uint8)
        for _ in range(np.random.randint(1, 10)):
            x1, x2 = np.random.randint(1, 256), np.random.randint(1, 256)

            y1, y2 = np.random.randint(1, 256), np.random.randint(1, 256)

            thickness = np.random.randint(1, 7)

            masked = cv2.line(image, (x1, y1), (x2, y2), (1, 1, 1), thickness)
        return masked

    def all_operations(self, image):
        Inpainting = keras.models.load_model("Inpainting-50.h5")
        denoising = keras.models.load_model("denoising-11-5.h5")
        super_res = keras.models.load_model("pixalate_scale_23_16-5-21.h5")
        colorizing = keras.models.load_model("model_350.h5")

        """# **Functions**"""

        def inpaint(img):
            img = np.array([img])
            inpainted = Inpainting.predict(img)
            imsave("inpainted.png", inpainted[0])
            return inpainted[0]

        def denoise(img):
            img = np.array([img])
            denoised = denoising.predict(img)
            imsave("denoised.png", denoised[0])
            return denoised[0]

        def super_resolution(img):
            img = np.array([img])
            super_resolution = super_res.predict(img)
            imsave("super_resolution.png", super_resolution[0])
            return super_resolution[0]

        def colorization(img):
            img_color = []
            img = img * 255.
            img = resize(img, (256, 256))
            # imsave("original.png", img)
            # plt.imshow(img)
            img_color.append(img)

            img_color = np.array(img_color, dtype=float)
            img_color = rgb2lab(1.0 / 255 * img_color)[:, :, :, 0]
            img_color = img_color.reshape(img_color.shape + (1,))

            output = colorizing.predict(img_color)
            output = output * 128

            result = np.zeros((256, 256, 3))
            result[:, :, 0] = img_color[0][:, :, 0]
            result[:, :, 1:] = output[0]
            imsave("colored.png", lab2rgb(result))
            return lab2rgb(result)

        inpainted = inpaint(image)

        denoised = denoise(inpainted)

        HD = super_resolution(image)

        colorizated = colorization(image)
