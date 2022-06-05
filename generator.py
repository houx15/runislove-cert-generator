import os
from PIL import Image, ImageDraw, ImageEnhance, ImageFont
from configs import TTF_SRC, TTF, OUTPUT_DIR


def text2img(text, font_size=28):
    font = ImageFont.truetype(TTF_SRC+TTF, font_size)
    (w, h) = font.getsize(text)
    timg = Image.new("RGBA", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(timg, "RGBA")
    draw.text((0, 0), text, font=font, fill="#000000")
    return timg

def img_generator(src_img, name, mileage, coefficient):
    """
    图片生成
    传入【已达标】同学的名字、里程、系数等，生成图片
    参数说明：
    - src_img: 对应称号背景图路径，字符串
    - name: 同学名字，字符串，应该为2-4个字
    - mileage: 里程，float，只保留一位小数
    - coefficient：蘑菇系数，float，只保留两位小数
    """
    img = Image.open(src_img)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    position_dict = {
        "name": {
            "x": 140,
            "y": 300
        },
        "mileage": {
            "x": 140,
            "y": 440
        },
        "coefficient": {
            "x": 370,
            "y": 440
        }
    }
    # layer = Image.new("RGB", img.size)
    name_img = text2img(name)
    mileage_img = text2img(str(mileage))
    coef_img = text2img(str(coefficient))

    img.paste(name_img,(position_dict["name"]["x"], position_dict["name"]["y"]))
    img.paste(mileage_img,(position_dict["mileage"]["x"], position_dict["mileage"]["y"]))
    img.paste(coef_img,(position_dict["coefficient"]["x"], position_dict["coefficient"]["y"]))

    img.show()
    img = img.convert("RGB")
    new_name = OUTPUT_DIR + name + ".jpg"
    img.save(new_name)
    return img

if __name__ == "__main__":
    img_generator("src/img/1.jpg", "猴子", "200.1", "1.25")
    # text2img("哈哈")


