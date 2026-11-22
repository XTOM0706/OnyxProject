# 源码清单

共 **80** 个仓库，**80** 个唯一路径。生成源：`projects.json`，官网：<https://onyxpj.wikidot.com/>。

## 分组统计

| 分组 | 数量 | 用途 |
|---|---:|---|
| system | 24 | AOSP / crDroid / W527 系统层 |
| apps | 34 | OnyxUI 内置应用（含 AOSP 应用与 Codeberg 镜像） |
| ecosystem | 14 | NeX / TraX / AriX / CalX / OptiX 等生态 |
| tools | 7 | 预编译 WebView、测试与表盘工具 |
| meta | 1 | 组织说明/元数据 |

> 本仓库**不包含源码副本**。`sources/` 默认不存在，只有执行拉取脚本才会下载；AOSP 全树很大，建议按 `--only` 或 `--group` 选择性拉取。

## 系统层（24）

| 路径 | 仓库 | Host | 分支 | 说明 |
|---|---|---|---|---|
| `art` | `android_art` | codeberg/OnyxUI | `main` |  |
| `bionic` | `android_bionic` | codeberg/OnyxUI | `main` | OnyxUI bionic fork |
| `build/make` | `android_build` | codeberg/OnyxUI | `main` |  |
| `build/soong` | `android_build_soong` | codeberg/OnyxUI | `fix-mke2fs-android11` |  |
| `device/lineage/sepolicy` | `android_device_lineage_sepolicy` | codeberg/OnyxUI | `main` |  |
| `external/chromium-webview` | `android_external_chromium-webview` | codeberg/OnyxUI | `main` |  |
| `external/e2fsprogs` | `android_external_e2fsprogs` | codeberg/OnyxUI | `fix-mke2fs-android11` |  |
| `external/libjpeg-turbo` | `android_external_libjpeg-turbo` | codeberg/OnyxUI | `main` |  |
| `frameworks/av` | `android_frameworks_av` | codeberg/OnyxUI | `main` |  |
| `frameworks/base` | `android_frameworks_base` | codeberg/OnyxUI | `main` | crDroid android_frameworks_base |
| `frameworks/native` | `android_frameworks_native` | codeberg/OnyxUI | `main` | OnyxUI Android frameworks/native |
| `frameworks/opt/net/wifi` | `android_frameworks_opt_net_wifi` | codeberg/OnyxUI | `main` |  |
| `frameworks/opt/telephony` | `android_frameworks_opt_telephony` | codeberg/OnyxUI | `main` |  |
| `libcore` | `android_libcore` | codeberg/OnyxUI | `main` |  |
| `lineage-sdk` | `android_lineage-sdk` | codeberg/OnyxUI | `main` |  |
| `packages/providers/MediaProvider` | `android_packages_providers_MediaProvider` | codeberg/OnyxUI | `main` |  |
| `packages/services/OmniJaws` | `android_packages_services_OmniJaws` | codeberg/OnyxUI | `main` |  |
| `packages/services/Telecomm` | `android_packages_services_Telecomm` | codeberg/OnyxUI | `main` |  |
| `packages/services/Telephony` | `android_packages_services_Telephony` | codeberg/OnyxUI | `main` |  |
| `system/apex` | `android_system_apex` | codeberg/OnyxUI | `fix-mke2fs-android11` |  |
| `system/netd` | `android_system_netd` | codeberg/OnyxUI | `main` |  |
| `system/sepolicy` | `android_system_sepolicy` | codeberg/OnyxUI | `main` |  |
| `vendor/addons` | `android_vendor_addons` | codeberg/OnyxUI | `main` |  |
| `vendor/lineage` | `android_vendor_lineage` | codeberg/OnyxUI | `main` |  |

## 内置应用（34）

| 路径 | 仓库 | Host | 分支 | 说明 |
|---|---|---|---|---|
| `packages/apps/AudioFX` | `android_packages_apps_AudioFX` | codeberg/OnyxUI | `main` |  |
| `packages/apps/BetterHealth` | `android_packages_apps_BetterHealth` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Bluetooth` | `android_packages_apps_Bluetooth` | codeberg/OnyxUI | `main` |  |
| `packages/apps/CalX` | `android_packages_apps_CalX` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Calendar` | `android_packages_apps_Calendar` | codeberg/OnyxUI | `main` |  |
| `packages/apps/CatShare` | `android_packages_apps_CatShare` | codeberg/OnyxUI | `main` |  |
| `packages/apps/CloX` | `android_packages_apps_CloX` | codeberg/OnyxUI | `main` | CloX launcher (com.ailife.clox) built-in for OnyxUI as a platform-signed privileged app; axmol native engine submodule; A11 privapp-permissions whitelist |
| `packages/apps/Contacts` | `android_packages_apps_Contacts` | codeberg/OnyxUI | `main` |  |
| `packages/apps/DeskClock` | `android_packages_apps_DeskClock` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Dialer` | `android_packages_apps_Dialer` | codeberg/OnyxUI | `main` |  |
| `packages/apps/DocumentsUI` | `android_packages_apps_DocumentsUI` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Eleven` | `android_packages_apps_Eleven` | codeberg/OnyxUI | `main` |  |
| `packages/apps/EmergencyInfo` | `android_packages_apps_EmergencyInfo` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Etar` | `android_packages_apps_Etar` | codeberg/OnyxUI | `main` |  |
| `packages/apps/FaceUnlockService` | `android_packages_apps_FaceUnlockService` | codeberg/OnyxUI | `main` |  |
| `packages/apps/FactoryTest` | `android_packages_apps_FactoryTest` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Gallery2` | `android_packages_apps_Gallery2` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Glimpse` | `android_packages_apps_Glimpse` | codeberg/OnyxUI | `main` | LineageOS Glimpse gallery, adapted for OnyxUI / Android 11 (motion photos, built-in M3 photo+video editor, Monet backport) |
| `packages/apps/InstallerX` | `android_packages_apps_InstallerX` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Launcher3` | `android_packages_apps_Launcher3` | codeberg/OnyxUI | `main` |  |
| `packages/apps/LineageParts` | `android_packages_apps_LineageParts` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Matlog` | `android_packages_apps_Matlog` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Messaging` | `android_packages_apps_Messaging` | codeberg/OnyxUI | `main` |  |
| `packages/apps/OnyxBrowser` | `android_packages_apps_OnyxBrowser` | codeberg/OnyxUI | `main` |  |
| `packages/apps/OnyxIME` | `android_packages_apps_OnyxIME` | codeberg/OnyxUI | `main` |  |
| `packages/apps/PermissionController` | `android_packages_apps_PermissionController` | codeberg/OnyxUI | `main` |  |
| `packages/apps/Recorder` | `android_packages_apps_Recorder` | codeberg/OnyxUI | `main` |  |
| `packages/apps/RotatingCamera` | `android_packages_apps_RotatingCamera` | codeberg/OnyxUI | `main` | Rotating Camera - system camera app for OnyxUI (source: https://gitlab.com/ailife8881/rotating-camera) |
| `packages/apps/Rtosify` | `android_packages_apps_Rtosify` | codeberg/OnyxUI | `main` | RTOSify mirror for OnyxUI system build |
| `packages/apps/Settings` | `android_packages_apps_Settings` | codeberg/OnyxUI | `main` |  |
| `packages/apps/SetupWizard` | `android_packages_apps_SetupWizard` | codeberg/OnyxUI | `main` |  |
| `packages/apps/ThemePicker` | `android_packages_apps_ThemePicker` | codeberg/OnyxUI | `main` |  |
| `packages/apps/WallpaperPicker2` | `android_packages_apps_WallpaperPicker2` | codeberg/OnyxUI | `main` |  |
| `packages/apps/crDroidSettings` | `android_packages_apps_crDroidSettings` | codeberg/OnyxUI | `main` |  |

## 生态应用（14）

| 路径 | 仓库 | Host | 分支 | 说明 |
|---|---|---|---|---|
| `packages/apps/AriX` | `arix-app` | github/XTOM0706 | `main` | AriX AI assistant (AGPL-3.0) |
| `packages/apps/NeX` | `nex` | gitlab/ailife8881 | `main` | NeX lightweight browser |
| `packages/apps/OTAManager2` | `otamanager2` | gitlab/ailife8881 | `main` | OTA manager |
| `packages/apps/OnyxBrowser2` | `onyxbrowser2` | gitlab/ailife8881 | `lineage-23.2` | OnyxBrowser2 |
| `packages/apps/OptiX` | `rotating-camera` | gitlab/PlayMcBKuwu | `master` | OptiX camera |
| `packages/apps/RTOSify` | `rtosify` | gitlab/ailife8881 | `master` | RTOSify |
| `packages/apps/RaiseToWake` | `raise-to-wake` | gitlab/ailife8881 | `master` | Raise to wake |
| `packages/apps/TraX` | `better-health-tracker` | gitlab/ailife8881 | `master` | TraX health tracker |
| `packages/apps/WatchMakerStore` | `watchmaker-community-store` | gitlab/ailife8881 | `main` | WatchMaker community store |
| `upstream/ailife8881/calx` | `calx` | gitlab/ailife8881 | `main` | CalX calculator |
| `upstream/ailife8881/clox` | `clox` | gitlab/ailife8881 | `main` | CloX launcher (upstream) |
| `upstream/ailife8881/onyx-browser` | `onyx-browser` | gitlab/ailife8881 | `main` | OnyxBrowser (legacy) |
| `upstream/ailife8881/onyx-ime` | `onyx-ime` | gitlab/ailife8881 | `lineage-23.2` | OnyxIME |
| `upstream/ailife8881/rotating-camera` | `rotating-camera` | gitlab/ailife8881 | `master` | RotatingCamera |

## 工具与预编译（7）

| 路径 | 仓库 | Host | 分支 | 说明 |
|---|---|---|---|---|
| `platform_testing` | `android_platform_testing` | codeberg/OnyxUI | `main` |  |
| `prebuilts/chromium-webview/arm` | `prebuilt_chromium-webview_arm` | codeberg/OnyxUI | `master` |  |
| `prebuilts/chromium-webview/arm64` | `prebuilt_chromium-webview_arm64` | codeberg/OnyxUI | `master` |  |
| `prebuilts/chromium-webview/x86` | `prebuilt_chromium-webview_x86` | codeberg/OnyxUI | `master` |  |
| `prebuilts/chromium-webview/x86_64` | `prebuilt_chromium-webview_x86_64` | codeberg/OnyxUI | `master` |  |
| `tools/onyxui-validationtest` | `onyxui-validationtest` | gitlab/ailife8881 | `master` | OnyxUI validation |
| `tools/wftools` | `wftools` | gitlab/ailife8881 | `main` | Watch face tools |

## 元信息（1）

| 路径 | 仓库 | Host | 分支 | 说明 |
|---|---|---|---|---|
| `onyxui` | `OnyxUI` | codeberg/OnyxUI | `main` | OnyxUI - Open source lightweight Android system for smartphones and smartwatches |
