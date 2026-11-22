# Onyx Project

**唤醒沉睡的 W527。** 为紫光展锐 W527 穿戴平台打造的第三方系统与生态。

> 原厂给不了的轻快，我们自己造。

[官网](https://onyxpj.wikidot.com/) · [源码（Codeberg）](https://codeberg.org/OnyxUI) · [AriX](https://github.com/XTOM0706/arix-app) · QQ 群 `1063208484`

## 这个仓库是什么

`OnyxProject` 是 **清单与同步入口**，不是把 65 个 AOSP 仓库和各应用源码复制一遍的超大单体仓库。

- `projects.json`：唯一清单，记录每个仓库的 host、owner、repo、AOSP 路径、分支、分组；
- `default.xml` / `ecosystem.xml`：由清单生成的 `repo` manifest；
- `scripts/fetch_sources.py`：从 Codeberg / GitLab / GitHub 拉取源码；
- `scripts/sync_repo.sh`：用 Google `repo` 同步完整 AOSP 树；
- `scripts/build_manifest.py`：清单变更后重新生成 manifest；
- `scripts/verify_projects.py`：CI 校验路径、重复项、URL 和 manifest 是否过期。

源码仍然留在各自的上游仓库，**Codeberg 是 OnyxUI 系统源码的事实来源**。这样既保留上游历史，也不会把几十 GB 的 AOSP 历史塞进一个 GitHub 仓库。

## 快速开始

只拉某个模块：

```bash
python3 scripts/fetch_sources.py --host codeberg --only android_frameworks_base --depth 1
```

拉取 OnyxUI 系统层和内置应用：

```bash
python3 scripts/fetch_sources.py --host codeberg --group system,apps,meta --depth 1 --jobs 4
```

拉取生态应用：

```bash
python3 scripts/fetch_sources.py --host all --group ecosystem --depth 1 --jobs 4
```

先看会拉什么：

```bash
python3 scripts/fetch_sources.py --list
```

完整 AOSP 工作树（需要 `repo`）：

```bash
ONYX_MANIFEST_URL=https://github.com/XTOM0706/OnyxProject.git \
  bash scripts/sync_repo.sh
```

## 内容

| 部分 | 内容 |
|---|---|
| OnyxUI 系统 | `frameworks/base`、`frameworks/av`、`frameworks/native`、`build/make`、`build/soong`、`bionic`、`art`、`libcore`、`system/*`、`vendor/lineage` 等 |
| 内置应用 | Settings、Launcher3、ThemePicker、WallpaperPicker2、DeskClock、Dialer、Contacts、Messaging、DocumentsUI、OnyxIME、OnyxBrowser、CloX、CalX、Glimpse、BetterHealth、RotatingCamera 等 |
| 生态应用 | **AriX**（AI 语音助手）、**NeX**（轻量浏览器）、**TraX**（健康）、**CloX**（桌面）、**CalX**（计算器）、**OptiX**（旋转摄像头）、RTOSify、OTAManager2、WatchMaker Store、wftools |
| 工具 | Chromium WebView 预编译、平台测试、OnyxUI validation、watch face tools |

完整清单见 [`docs/INVENTORY.md`](docs/INVENTORY.md)，应用映射见 [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md)，原始数据见 [`projects.json`](projects.json)。

## 团队与状态

- 主导：**茶汤**、**4NF**
- 早期参与：**AI LIFE**、**依橙漂 Sara**
- OnyxUI：基于 AOSP 11 / crDroid，稳定版持续维护；
- CitrineUI：基于 AOSP 13 / crDroid，接棒中；
- 适用：CD 超戴 Watch / XS 行胜 Watch 及其他 W527 穿戴设备。

> W527 与 W377E 刷机包不通用。刷机有变砖风险，请先备份原厂固件。

## 许可证

本清单仓库自身以 [Apache-2.0](LICENSE) 发布。各子项目保留自己的许可证，例如：

- OnyxUI / AOSP 派生代码：以其仓库内 `LICENSE` / `NOTICE` 为准；
- **AriX**：AGPL-3.0；
- GitLab 生态项目：以各项目许可证为准。

本仓库不重新授权任何子项目，也不包含第三方专有素材。
