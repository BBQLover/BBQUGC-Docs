©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 1 -->

# 构建与本地测试

## 构建包

保存所有资产并关闭 Unreal Editor，在 UGC Tool 中选择项目，然后点击 **Build Selected**。在显示成功或失败前保持日志窗口打开。

```text
<ProjectRoot>/BBQ/Build/<PluginName>/
├── <PluginName>.BBQPlugin
├── Content/Paks/
│   ├── <PluginName>-Windows.pak
│   ├── <PluginName>-Windows.ucas
│   └── <PluginName>-Windows.utoc
└── Resources/
```

完整的 `<PluginName>` 目录是测试和上传单位。不要展平目录，也不要只复制单个文件。排除源素材、日志、调试文件、凭据和无关包。

## 在 BBQ Player 中测试

关闭 BBQ Player，然后把完整的构建目录复制到：

```text
<SteamLibrary>\steamapps\common\BBQ Player\BBQPlayer\Mods\<PluginName>\
```

启动 Player，打开本地包，检查元数据和图片，然后启用。测试所有预期内容和行为；在要求时禁用并重启，然后确认可以再次正常启用。

更新时，请同时测试全新安装和替换先前发布版本。
