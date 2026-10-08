# 第三方声明 / Third-Party Notices

本仓库是**第三方修改版**，与下列项目、作者均**无隶属、赞助或背书关系**。

| 项目 | 用途 | 作者 | 许可证 |
|---|---|---|---|
| 原 "TE-Speed" 系列插件（本插件的来源） | 全部加速实现与节点骨架 | **yun** | 原发行版未附带许可证文件，亦未声明授权条款 |
| FlashVSR（含 `flashvsr_core/` 内的实现） | 视频超分辨率推理管线；本插件在其基础上加入执行预算控制、运动感知动态加速等 | OpenImagingLab | Apache-2.0（见 `flashvsr_core/LICENSE.txt`） |
| [SpargeAttn](https://github.com/thu-ml/SpargeAttn)（`spas_sage_attn` 轮子） | 视频超分的稀疏注意力后端，**本仓库附带该轮子**（`wheels/`） | thu-ml 等 | BSD-3-Clause（原文见 `third_party/spas_sage_attn_LICENSE.txt`） |
| [ComfyUI](https://github.com/comfyanonymous/ComfyUI) | 运行宿主（本仓库不含其代码） | comfyanonymous 等 | GPL-3.0 |

## 关于二进制组件

`nodes.pyd` 与 `te_runtime/` 下的 4 个 `.pyd` 是原加速版作者编译发布的二进制组件，原发行版未附带源码，亦未声明许可证。本仓库按“原样”再分发，并明确署名原作者 yun。

## 许可选择说明

本插件包含**没有对应源码的编译二进制组件**，GPL 系列许可证要求分发二进制时提供完整源码，
本项目无法提供，因此本仓库采用 **Apache-2.0**（允许在保留声明的前提下以二进制形式再分发）。

## 侵权处理与下架承诺

如果你是权利人，认为本仓库内容侵犯了你的权益，请通过 **GitHub Issue** 联系我们。
我们会在核实后**立即删除或调整**相关内容，不设前置条件。若原作者提出要求，我们将直接下架相关组件。

## 免责声明

本仓库内容按"现状"（AS IS）提供，不附带任何明示或暗示的担保。请遵守你所在国家/地区的法律法规，
不得将本项目用于任何违法违规用途。本仓库**不包含、也不分发任何模型权重**。
