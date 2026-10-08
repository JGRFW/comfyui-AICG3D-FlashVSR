# AICG3D-FlashVSR

**FlashVSR 视频超分辨率放大的 ComfyUI 加速节点** · 完全免费 · 开源

> ⚠️ 本仓库是**第三方修改版，非官方版本**，与原加速版作者、FlashVSR 作者均无隶属或背书关系。

## 功能

- 支持 `FlashVSR-v1.1`，`tiny` / `tiny-long` / `full` 三种推理模式
- 独立的执行预算控制、空间分块、显存分阶段策略
- 运动感知动态加速：动态调整保留量与局部注意力范围
- `detail` / `balanced` / `throughput` 三档质量与速度配置
- `sparse_sage2` 与 FlashVSR 原生 `block_sparse_attn` 两种 LCSA 稀疏注意力
- AICG3D Video Combine：视频帧合并加速

## 安装

```
cd ComfyUI/custom_nodes
git clone https://github.com/JGRFW/comfyui-AICG3D-FlashVSR.git
```

依赖：Python 3.12+、`spas_sage_attn`（仓库已附带对应轮子，见下文「依赖安装」）；FlashVSR 模型权重**不随仓库分发**。


## 依赖安装（重要）

本插件依赖 **spas_sage_attn**（SpargeAttn 的预编译轮子）。它**不在 PyPI 上**，
所以本仓库直接附带了与原插件作者分发版本一致的轮子：

```text
wheels/spas_sage_attn-0.1.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl
```

**安装方法**（在插件目录下执行）：

```bash
# Windows：用你 ComfyUI 环境的 python
"路径/到/ComfyUI/python.exe" -m pip install -r requirements.txt
# 或者直接指定轮子
"路径/到/ComfyUI/python.exe" -m pip install wheels/spas_sage_attn-0.1.0+cu130torch2.9.0andhigher.post4-cp39-abi3-win_amd64.whl
```

- 该轮子对应 **CUDA 13.0 + torch ≥ 2.9.0**，`cp39-abi3`（Python 3.9 及以上通用，含 3.13）。
- 环境不匹配时安装会失败，请到上游 `thu-ml/SpargeAttn` 自行编译（编译需要 CUDA 工具链，比较耗时）。
- 该轮子由 SpargeAttn 项目构建，许可证：BSD 3-Clause License（详见其上游仓库）。

## 节点

分类：**`AICG3D/FlashVSR`**

| 显示名 | 节点 ID |
|---|---|
| AICG3D-FlashVSR Model | `TEFlashVSRModelLoader` |
| AICG3D-FlashVSR Settings | `TEFlashVSRTuning` |
| AICG3D-FlashVSR | `TEFlashVSRRestore` |
| AICG3D Video Combine | `AICG3D_VideoCombine` |

> 说明：前三个节点的内部 ID 保持不变，以免破坏既有工作流；视频合并节点的 ID 已改为
> `AICG3D_VideoCombine`（前端预览脚本 `web/aicg3d_flashvsr.js` 已同步更新）。

## 本版改动（相对原加速版）

- 分类 / 显示名 / 日志 / 报错信息 / 编译路径统一到 AICG3D（底层 `.pyd` 等长替换，文件大小不变）
- `web/te_speed_flashvsr.js` → `web/aicg3d_flashvsr.js`，并同步修正里面写死的节点 ID
- 新增 README / LICENSE(Apache-2.0) / THIRD_PARTY_NOTICES / pyproject.toml

## 致谢

感谢 **yun**（原加速版作者：执行预算控制、运动感知动态加速、SpargeAttn 适配等实现者）、
**OpenImagingLab**（[FlashVSR](https://github.com/OpenImagingLab/FlashVSR)，Apache-2.0）、
**thu-ml**（[SpargeAttn](https://github.com/thu-ml/SpargeAttn)）。

---

## 版权与法律声明

**1. 免费开源**：本插件**永久免费、开源**，任何人都可自由使用、修改、再分发（遵循 Apache-2.0）。
不存在任何"付费版""解锁版"。

**2. 署名**：再分发或整合本插件时，请保留本 README、[LICENSE](LICENSE) 与
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 中的全部署名与许可声明。

**3. 非官方声明**：本仓库是**第三方修改版**，与上游作者**无隶属、赞助或背书关系**，
请勿误认为官方发布。第三方名称与商标归其各自所有者，此处仅作说明性引用。

**4. 免责声明**：本插件按"现状"提供，**不提供任何担保**；使用产生的一切后果由使用者自行承担。
请遵守当地法律法规，**不得**用于生成、传播违法违规内容。

**5. 模型权重**：本仓库**不分发**任何模型权重，权重版权与使用条款归其发布者所有。

**6. 侵权处理**：权利人如认为本仓库侵犯其权益，请提 **GitHub Issue**，我们会核实后**立即删除或调整**，
不设任何前置条件。

**7. 二进制组件**：本插件的编译组件（`.pyd`）由原加速版作者发布，原发行版未附带源码与许可证，
本仓库按"原样"再分发并**明确署名原作者**；如原作者有异议，我们会立即下架。
