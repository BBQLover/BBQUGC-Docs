©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 1 -->

# 建置與本機測試

## 建置套件

儲存所有資產並關閉 Unreal Editor，在 UGC Tool 中選擇專案，然後按一下 **Build Selected**。在顯示成功或失敗前保持記錄視窗開啟。

```text
<ProjectRoot>/BBQ/Build/<PluginName>/
├── <PluginName>.BBQPlugin
├── Content/Paks/
│   ├── <PluginName>-Windows.pak
│   ├── <PluginName>-Windows.ucas
│   └── <PluginName>-Windows.utoc
└── Resources/
```

完整的 `<PluginName>` 目錄是測試和上傳單位。不要將目錄攤平，也不要只複製單一檔案。排除原始素材、記錄、偵錯檔案、憑證和無關套件。

## 在 BBQ Player 中測試

關閉 BBQ Player，然後將完整建置目錄複製到：

```text
<SteamLibrary>\steamapps\common\BBQ Player\BBQPlayer\Mods\<PluginName>\
```

啟動 Player，開啟本機套件，檢查中繼資料和圖片，然後啟用。測試所有預期內容與行為；在要求時停用並重新啟動，然後確認可以再次正常啟用。

更新時，請同時測試全新安裝和替換先前發佈版本。
