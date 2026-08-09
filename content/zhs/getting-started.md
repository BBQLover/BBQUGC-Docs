©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 2 -->

# 开始使用

## 所需条件

- 64 位 Windows，以及使用创作者账户运行的 Steam。
- 通过 Steam 安装的最新版 BBQ UGC Tool。
- Unreal Engine 5.7，或当前工具版本要求的准确版本。
- 足够容纳 Unreal 烘焙输出和第二份打包副本的空间。
- 发布所用全部素材的权利。

始终使用最新版工具创建和重新构建项目。不要从旧项目复制二进制文件。

## 配置 Unreal Engine

!!! warning "需要单独取得 Epic 许可"
    Unreal Engine 由 Epic Games 而非 BBQ 提供和许可。在打开或构建项目之前，请从 Epic 授权来源取得所需的 Unreal Engine 版本，并接受适用的 [Unreal Engine EULA](https://www.unrealengine.com/eula/unreal)。BBQ UGC Tool 不包含也不替代 Unreal Engine 许可。完整责任划分请参阅 [UGC 创作者协议](agreement.md)。

1. 启动 UGC Tool，打开 **Settings**。
2. 选择 **Select UEPath**。
3. 选择 Unreal 安装根目录，例如 `C:\Program Files\Epic Games\UE_5.7`。
4. 确认其中包含 `Engine\Binaries\Win64\UnrealEditor.exe`。

避免把项目放在只读、云同步或不稳定的网络位置。

## 创建项目

打开 **Projects**，选择 **Create**，输入稳定的名称并选择父目录。为了获得最佳兼容性，请使用英文字母、数字、`_` 或 `-`。

```text
<ProjectRoot>/
├── Content/<PluginName>/
├── BBQ/Resources/
├── BBQ/Build/
└── <PluginName>.uproject
```

项目名称同时是包名称和必需的内容根目录。首次发布后请保持不变。

## 添加现有项目

使用 **Projects > Add** 并选择项目直属的 `.uproject`。加入列表不会升级旧模板；如果兼容性检查失败，请使用当前工具重新创建项目。
