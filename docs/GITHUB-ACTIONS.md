# GitHub Actions 使用说明

本仓库有两个 workflow。它们都不构建、不产出刷机包，只做两件事：校验清单，以及让 GitHub runner 代拉一份源码快照。

| Workflow | 触发方式 | 作用 |
|---|---|---|
| `validate` | `push` 到 `main`、`pull_request` | 校验 `projects.json`，并确认 `default.xml` / `ecosystem.xml` 与清单一致 |
| `fetch-source` | **仅手动** `workflow_dispatch` | 在 runner 上把选定的上游仓库 clone 到 `sources/`，再打成 artifact |

`fetch-source` 没有 `push` / `schedule` 触发器，这是刻意的，原因见下文「为什么默认禁止全量」。

## `fetch-source` 参数

| 输入 | 取值 | 说明 |
|---|---|---|
| `host` | `codeberg` / `gitlab` / `github` / `all` | 上游托管平台。清单现有 64 个 Codeberg、15 个 GitLab、1 个 GitHub 仓库 |
| `group` | `""` / `system` / `apps` / `ecosystem` / `tools` | 按分组取。`system` 24 个、`apps` 34 个、`ecosystem` 14 个、`tools` 7 个。`meta` 组不在选项里，需要时用 `only` |
| `only` | repo 名或路径的 glob | 优先级高于 `group`；一旦填写就忽略 `group` |
| `depth` | `1` / `0` | `1` 只取最新一次提交（默认，体积最小）；`0` 取完整历史 |
| `retention_days` | `1` / `3` / `7` / `14` / `30` | artifact 保留天数，默认 7 |

选择规则，与 `scripts/fetch_sources.py` 保持一致：

- 填了 `only`：只拉匹配项，`group` 失效；
- 只填 `group`：拉该组内符合 `host` 的全部仓库；
- **两个都不填：直接失败退出**，不会退化成"拉全部"；
- `depth=0` 必须同时填 `only`，否则失败。

`only` 在 workflow 里只能填一个表达式，但脚本侧的 `--only` 是 `action="append"`，本地可以重复传多次：

```bash
python3 scripts/fetch_sources.py --host codeberg \
  --only android_frameworks_base --only android_packages_apps_Settings --depth 1
```

想先确认会拉什么，用 `--list`（不下载任何东西）：

```bash
python3 scripts/fetch_sources.py --host codeberg --group apps --list
```

## artifact 怎么下载

运行结束后，源码以单个 artifact 保存在该次 run 页面上。

浏览器：`Actions → fetch-source → 选中那次 run → 页面底部 Artifacts`。

命令行（需要 `gh`，且需要 GitHub 登录凭据——公开仓库的 artifact 同样要求认证）：

```bash
gh run list  --workflow fetch-source
gh run download <run-id> -n onyx-source-codeberg -D ./onyx-fetch
```

关于 artifact 的几个事实，别按"镜像"来理解：

- **只有工作树，没有 `.git`**。workflow 显式设了 `include-hidden-files: false`，点开头的目录（含 `.git`）不会进 artifact。depth-1 的 packfile 大部分内容与工作树重复，去掉它体积大约减半。所以下载回来是快照，不是可以直接 `git pull` 的克隆。
- **权限位会丢**。zip 化上传后目录一律 `755`、文件一律 `644`，脚本的可执行位不再保证。需要保权限就自己 `tar`。
- **会过期**。按 `retention_days` 删除，过期即不可下载。
- **artifact 不可变**。同名不可修改，只能整体替换。

## 为什么默认禁止全量

三个独立原因，任何一个都足够：

1. **量级**。清单里 80 个仓库，`system` 组包含 `frameworks/base`、`frameworks/av`、`art`、`bionic`、`build/soong` 这类大仓库；`prebuilts/chromium-webview/*` 是二进制。`ubuntu-latest` runner 的可用磁盘只有十几 GB 级别（系统镜像和预装工具已经占掉一部分），全组全历史会直接写到磁盘满，任务在 120 分钟超时前就先挂了。
2. **本机流量**。代拉的初衷是省本机带宽，如果把 artifact 拉成全量，等于把流量问题从 clone 挪到下载，没有收益。
3. **存储会累积**。每次 run 都产生 artifact，重复跑宽选择就会持续占住 Actions 存储，直到过期。

所以脚本和 workflow 都做了拒绝：没有 `group` 也没有 `only` 时直接 `exit 2`，而不是"默认拉全部"。

## 怎么避免把 Actions 存储打爆

已落实的护栏：

- **体积硬上限**：`Enforce artifact size budget` 步在真实字节数超过 4 GiB 时失败，1 GiB 时只发警告。超限的任务不会上传 artifact，也就不会占存储。
- **稳定名称 + `overwrite: true`**：artifact 名是 `onyx-source-<host>`，同一 `host` 重跑会**替换**上一份，而不是新增一份。最多同时存在 4 个（每个 host 一个）。
- **保留期收紧**：仓库级 artifact 保留上限是 90 天，workflow 的选项刻意只到 30 天，默认 7 天。
- **不取消在跑的任务**：`concurrency` 用 `cancel-in-progress: false`，避免上传到一半被掐断留下半成品。
- **不设定时任务**：`fetch-source` 只能手动触发，不会自己堆积 artifact。
- **默认 `depth=1`，`depth=0` 需配 `only`**：完整历史通常比 depth-1 大一个数量级。

需要清理时，页面上的垃圾桶图标，或：

```bash
gh api repos/XTOM0706/OnyxProject/actions/artifacts --jq '.artifacts[] | "\(.id) \(.name) \(.size_in_bytes)"'
gh api -X DELETE repos/XTOM0706/OnyxProject/actions/artifacts/<artifact-id>
```

## 改了清单之后

`projects.json` 是唯一事实来源，`default.xml` / `ecosystem.xml` 由它生成。改完清单必须重新生成，否则 `validate` 会失败：

```bash
python3 scripts/build_manifest.py
python3 scripts/build_manifest.py --check   # 只检查，不写文件
python3 scripts/verify_projects.py          # CI 跑的就是这个
```

`verify_projects.py` 会检查路径重复、非法 `host`、URL 是否以 `.git` 结尾，以及 manifest 是否过期。

## 本地需要大仓库时

要走完整 AOSP 工作树（需要 Google `repo` 工具）：

```bash
ONYX_MANIFEST_URL=https://github.com/XTOM0706/OnyxProject.git \
  bash scripts/sync_repo.sh
```

想只同步某一组，用 `ONYX_GROUPS`：

```bash
ONYX_GROUPS=system ONYX_JOBS=4 bash scripts/sync_repo.sh
```

这只是本地工作树，和 Actions 无关；不要把它接到任何自动触发上。
