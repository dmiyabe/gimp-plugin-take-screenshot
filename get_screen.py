#!/usr/bin/python
# -*- coding: utf-8 -*-

"""スクリーンショットを取得しファイルに保存する GIMP のプラグイン"""

import datetime

from gimpfu import *


def get_filepath():
    """ファイルパスの取得"""
    dt_now = datetime.datetime.now()
    filename = "imgScreen_" + dt_now.strftime('%Y-%m-%d %H-%M-%S') + ".png"
    return "/home/daiki/Pictures/" + filename

def plugin_main(image, layer):  # pylint: disable-msg=W0613
    """スクリーンショットを取得して保存"""
    scale = 2

    width = 1920
    height = 1080

    point_x = 70
    point_y = 30

    select_w = width - point_x
    selecr_h = height - point_y

    img = pdb.plug_in_screenshot(1, 1, 0, 0, 0, 0)
    pdb.gimp_rect_select(img, point_x, point_y, select_w, selecr_h, 2, False, 0)
    pdb.gimp_edit_copy(img.layers[0])
    new_img = pdb.gimp_edit_paste_as_new_image()

    pdb.gimp_image_scale(new_img, select_w / scale, selecr_h / scale)

    pdb.gimp_display_new(new_img)

    pdb.gimp_file_save(new_img, new_img.active_layer, get_filepath(), "")

    pdb.gimp_image_delete(img)

register(
        "python_fu_getscreen",
        "Save screenshot from an area of necessary range",
        "Save screenshot from an area of necessary range",
        "dmiyabe",
        "dmiyabe",
        "2020/04/08",
        "<Image>/Filters/Languages/Python-Fu/getscreen",
        "RGB*, GRAY*",
        [(PF_IMAGE, "変数名", "説明", "初期値"),
         (PF_DRAWABLE, "変数名", "説明", "初期値")],
        [],
        plugin_main)

main()
