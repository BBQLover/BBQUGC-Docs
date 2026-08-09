©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 1 -->

# 元数据与资源

选择项目，点击 **Edit Metadata**，填写面向创作者的字段。关闭窗口时会保存更改。

| 字段 | 指引 |
|---|---|
| `Id` | 工具创建的标识；更新时保留。 |
| `Name` | 项目与包名称；保持稳定。 |
| `Version` | 用于依赖选择的数字版本。 |
| `VersionName` | 如 `1.0.0` 的可读版本。 |
| `FriendlyName` | 向用户显示的名称。 |
| `Description` | 简短的包说明。 |
| `Category` | 最符合的分类，或 `Other`。 |
| `CreatedBy` | 创作者或团队显示名称。 |
| URL 字段 | 公开 HTTPS 链接，或留空。 |

普通更新应保留同一个项目、`Id` 和 `Name`。只有有意制作不兼容的替代作品时才创建新标识。

## 展示资源

把展示文件放在 `<ProjectRoot>/BBQ/Resources/`：

- `Cover.png`：方形封面；500×500 是实用工作尺寸。
- `Description.png`：宽幅图片；1920×1080 是实用工作尺寸。

构建器会复制完整的实体资源目录树。请避免符号链接、控制图片大小，并在最终包中检查复制结果。
