# Copyright (C) 2026 AICG3D
# SPDX-License-Identifier: GPL-3.0-or-later
# -*- coding: utf-8 -*-
"""AICG3D-FlashVSR —— FlashVSR 视频超分辨率放大的 ComfyUI 加速节点"""

from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

# 底层 .pyd 里的品牌字符串是等长替换的（改短会破坏文件内部偏移），
# 短出的字节用空格补在尾部，这里统一去掉首尾空格。
for _cls in NODE_CLASS_MAPPINGS.values():
    _cat = getattr(_cls, "CATEGORY", None)
    if isinstance(_cat, str):
        _cls.CATEGORY = _cat.strip()

NODE_DISPLAY_NAME_MAPPINGS = {
    _k: (_v.strip() if isinstance(_v, str) else _v)
    for _k, _v in NODE_DISPLAY_NAME_MAPPINGS.items()
}
