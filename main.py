from configs import *
from generator import img_generator

def main():
    title_dict = {}
    with open(INPUT_DIR+TITLES_DATA, "r", encoding="utf8") as rfile:
        for line_id, line_data in enumerate(rfile.readlines()):
            if line_id == 0:
                continue
            line_data = line_data.strip()
            [title, mileage, src_img] = line_data.split(',')
            title_dict[title] = {
                "mileage": int(mileage),
                "src_img": src_img
            }
    
    runners_list = []
    with open(INPUT_DIR+RUNNERS_DATA, "r", encoding="utf8") as rfile:
        for line_id, line_data in enumerate(rfile.readlines()):
            if line_id == 0:
                continue
            line_data = line_data.strip()
            [name, per_title, real_mileage] = line_data.split(',')
            real_mileage = float(real_mileage)
            if per_title not in title_dict.keys():
                print("第{}行称号名称错误：{}".format(line_id, per_title))
                continue
            title_mileage = title_dict[per_title]["mileage"]
            if real_mileage < title_mileage:
                print("{}未达标".format(name))
                continue
            coefficient = round(real_mileage/title_mileage, 2)
            img = img_generator(IMG_SRC+title_dict[per_title]["src_img"], name, round(real_mileage, 1), coefficient)


if __name__ == "__main__":
    main()

