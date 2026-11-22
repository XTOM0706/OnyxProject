# 生态应用清单

官网把生态概括为 **CloX / NeX / TraX / AriX**，系统扩充组件还有 **CalX / OptiX** 等。下表把公开名称映射到实际源码仓库。

| 公开名称 | 定位 | 源码 | 默认分支 | 备注 |
|---|---|---|---|---|
| **AriX** | AI 语音助手 | [XTOM0706/arix-app](https://github.com/XTOM0706/arix-app) | `main` | AGPL-3.0；不并入系统镜像，按应用分发 |
| **CloX** | 桌面启动器 | [ailife8881/clox](https://gitlab.com/ailife8881/clox) | `main` | Codeberg 另有 OnyxUI 平台签名内置版 `android_packages_apps_CloX` |
| **NeX** | 轻量浏览器 | [ailife8881/nex](https://gitlab.com/ailife8881/nex) | `main` | 官网“轻量浏览器” |
| **TraX** | 健康监测 | [ailife8881/better-health-tracker](https://gitlab.com/ailife8881/better-health-tracker) | `master` | 官网“健康监测” |
| **CalX** | 计算器 | [ailife8881/calx](https://gitlab.com/ailife8881/calx) | `main` | Material 3 expressive |
| **OptiX** | 旋转摄像头 | [PlayMcBKuwu/rotating-camera](https://gitlab.com/PlayMcBKuwu/rotating-camera) | `master` | 依澄漂 Sara 维护 |
| OnyxBrowser | 浏览器 | [ailife8881/onyx-browser](https://gitlab.com/ailife8881/onyx-browser) | `main` | 旧命名；新版本见 `onyxbrowser2` |
| OnyxBrowser2 | 浏览器 | [ailife8881/onyxbrowser2](https://gitlab.com/ailife8881/onyxbrowser2) | `lineage-23.2` | A13 线 |
| OnyxIME | 输入法 | [ailife8881/onyx-ime](https://gitlab.com/ailife8881/onyx-ime) | `lineage-23.2` | 系统内置版见 Codeberg |
| RotatingCamera | 旋转摄像头 | [ailife8881/rotating-camera](https://gitlab.com/ailife8881/rotating-camera) | `master` | OptiX 的同源上游 |
| RTOSify | 手表互联 | [ailife8881/rtosify](https://gitlab.com/ailife8881/rtosify) | `master` | 另有 lite / signaling 子项目 |
| OTAManager2 | OTA 管理 | [ailife8881/otamanager2](https://gitlab.com/ailife8881/otamanager2) | `main` | |
| WatchMaker Store | 表盘商店 | [ailife8881/watchmaker-community-store](https://gitlab.com/ailife8881/watchmaker-community-store) | `main` | |
| RaiseToWake | 抬腕亮屏 | [ailife8881/raise-to-wake](https://gitlab.com/ailife8881/raise-to-wake) | `master` | |

## 路径约定

- 能直接进 AOSP 树的系统应用，路径为 `packages/apps/<Name>`；
- 与 Codeberg 内置版重名的上游仓库，放在 `upstream/<owner>/<repo>`，避免同一路径冲突；
- 清单里的 `group=ecosystem` 用于 `repo sync -g ecosystem` 或 `fetch_sources.py --group ecosystem`。

## 未并入清单的仓库

`ailife8881` 与 `PlayMcBKuwu` 名下还有硬件、固件、学校网络、实验项目等，与本穿戴系统无直接关系，不放入默认清单。需要时可手工 clone，避免把生态仓库变成杂物间。
