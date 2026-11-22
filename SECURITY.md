# 安全策略

## 适用范围

本仓库（`XTOM0706/OnyxProject`）只包含**清单与拉取脚本**，不包含任何产品源码。所以这里的"漏洞"主要指：

- `scripts/` 下的脚本问题（路径穿越、命令注入、不安全的 glob 处理等）；
- `.github/workflows/` 的权限过大、凭据暴露、可被外部输入利用；
- 本仓库误提交的敏感信息。

OnyxUI 系统源码、AriX、GitLab 生态应用的问题不属于本仓库范围，请报到各自仓库：系统层在 [Codeberg/OnyxUI](https://codeberg.org/OnyxUI)，AriX 在 [XTOM0706/arix-app](https://github.com/XTOM0706/arix-app)，生态应用见 [`docs/ECOSYSTEM.md`](docs/ECOSYSTEM.md)。

## 报告漏洞

优先用 GitHub 的私密渠道，不要在公开 issue 里贴细节：

1. **Private vulnerability reporting**：仓库 `Security` 标签页 → `Report a vulnerability`。这个通道已启用，报告只有维护者可见。
2. 如果通道不可用，邮件联系 **tomrz666@163.com**，标题带上 `[OnyxProject security]`。

请尽量给出：受影响文件或 workflow、复现步骤、影响范围、你建议的修复。我们会在确认后回复处理计划；在修复发布前请不要公开细节。

凭据泄露（token、密钥）请直接按上面渠道报告，并说明是否需要立即吊销。

## 永远不要提交这些东西

以下内容一旦进过 git 历史就很难真正清除，请在提交前就挡住：

| 类别 | 例子 | 说明 |
|---|---|---|
| 访问令牌 | GitHub PAT、GitLab token、SSH 私钥 | 本仓库任何地方都不该出现 token 字面量 |
| 签名密钥 | `platform.pk8`、`platform.x509.pem`、`release.keystore`、OTA 签名私钥 | 泄露等于任何人都能签出可被设备接受的包 |
| 设备标识 | IMEI、序列号、`ro.serialno`、ADB 公钥白名单 | 属于用户设备数据 |
| 用户数据 | 日志、`logcat` 抓包、账号、通讯录、定位、备份 | 调试日志常带这些，贴日志前先脱敏 |
| 构建产物 | `sources/`、artifact、`worktree/`、`*.img`、`*.zip` | 已在 `.gitignore` 里排除，别用 `-f` 绕过 |

## token 是怎么用的

- 本地凭据放在仓库之外（例如 `~/.config/gh-token`，权限 `600`），脚本通过环境变量读取，**不写进任何被跟踪的文件**。
- `scripts/` 里没有硬编码凭据；需要认证时由调用方的环境或 `~/.git-credentials` 提供。
- workflow 只用 `GITHUB_TOKEN`，且显式声明最小权限：`fetch-source` 是 `permissions: contents: read`。
- `fetch-source` 不接受任何仓库密钥作为输入，也没有 `pull_request_target` 触发器，外部 PR 拿不到写权限或密钥。

如果你在某个提交里看到了疑似凭据，请按上文渠道报告，不要先开 issue 讨论。

## 依赖与第三方代码

本仓库不 vendor 任何第三方代码，只引用上游 URL。各上游保留自己的许可证与安全策略；本仓库的许可证见 [`LICENSE`](LICENSE) 与 [`NOTICE`](NOTICE)。
