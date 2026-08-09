©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 2 -->

# 開始使用

## 所需條件

- 64 位元 Windows，以及使用創作者帳號執行的 Steam。
- 透過 Steam 安裝的最新版 BBQ UGC Tool。
- Unreal Engine 5.7，或目前工具版本要求的準確版本。
- 足以容納 Unreal 烘焙輸出和第二份封裝副本的空間。
- 發佈所有使用素材的權利。

請一律使用最新版工具建立及重新建置專案。不要從舊專案複製二進位檔案。

## 設定 Unreal Engine

!!! warning "需要單獨取得 Epic 授權"
    Unreal Engine 由 Epic Games 而非 BBQ 提供和授權。在開啟或建置專案之前，請從 Epic 授權來源取得所需的 Unreal Engine 版本，並接受適用的 [Unreal Engine EULA](https://www.unrealengine.com/eula/unreal)。BBQ UGC Tool 不包含也不取代 Unreal Engine 授權。完整責任劃分請參閱 [UGC 創作者協議](agreement.md)。

1. 啟動 UGC Tool 並開啟 **Settings**。
2. 選擇 **Select UEPath**。
3. 選擇 Unreal 安裝根目錄，例如 `C:\Program Files\Epic Games\UE_5.7`。
4. 確認其中包含 `Engine\Binaries\Win64\UnrealEditor.exe`。

避免將專案放在唯讀、雲端同步或不穩定的網路位置。

## 建立專案

開啟 **Projects**，選擇 **Create**，輸入穩定名稱並選擇上層目錄。為了最佳相容性，請使用英文字母、數字、`_` 或 `-`。

```text
<ProjectRoot>/
├── Content/<PluginName>/
├── BBQ/Resources/
├── BBQ/Build/
└── <PluginName>.uproject
```

專案名稱同時是套件名稱和必要的內容根目錄。首次發佈後請保持不變。

## 加入現有專案

使用 **Projects > Add** 並選擇專案直屬的 `.uproject`。加入清單不會升級舊範本；若相容性檢查失敗，請使用目前工具重新建立專案。
