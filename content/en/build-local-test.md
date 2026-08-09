©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 1 -->

# Build and local test

## Build the package

Save all assets, close Unreal Editor, select the project in the UGC Tool, and choose **Build Selected**. Keep the log open until it reports success or failure.

```text
<ProjectRoot>/BBQ/Build/<PluginName>/
├── <PluginName>.BBQPlugin
├── Content/Paks/
│   ├── <PluginName>-Windows.pak
│   ├── <PluginName>-Windows.ucas
│   └── <PluginName>-Windows.utoc
└── Resources/
```

The complete `<PluginName>` directory is the test and upload unit. Do not flatten it or copy only one file. Exclude source assets, logs, debug files, credentials, and unrelated packages.

## Test in BBQ Player

Close BBQ Player, then copy the complete built directory to:

```text
<SteamLibrary>\steamapps\common\BBQ Player\BBQPlayer\Mods\<PluginName>\
```

Start BBQ Player, open **Mods & UGC**, select **Local**, inspect the metadata and images, then enable the package. Exercise all expected content and behavior. Disable it and restart when prompted, then confirm it can be enabled cleanly again.

For updates, test both a clean installation and replacement of the previously released package.
