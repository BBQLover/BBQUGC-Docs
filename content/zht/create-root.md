<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# 建立根介面

## 建議配置

使用簡潔、可預期的內容目錄：

```text
Content/<PluginName>/
├── PluginEntry.uasset
└── UI/
    ├── WBP_<PluginName>Root.uasset
    ├── DA_<PluginName>UIRoot.uasset
    ├── Components/
    ├── Icons/
    └── Notifications/          # 選用
```

子目錄名稱可以調整。關鍵要求是套件內所有資產都位於專案命名內容根目錄之下。

## 建立 Widget Blueprint

1. 從 BBQ UGC Tool 開啟專案。
2. 在 `Content/<PluginName>/UI` 下建立 **Widget Blueprint**。
3. 將根面板設為全螢幕配置。
4. 開啟 **Class Settings**，在已實作介面中加入 `BBQUIRoot`。
5. 編譯並儲存 Widget。

Player 不會接受未實作 `BBQUIRoot` 的已選根類別。

## 分離顯示圖層

由後至前使用獨立容器：

1. Player 背景；
2. 執行階段播放覆疊層；
3. 自訂介面列及主要檢視；
4. 前景創作或預覽覆疊層；
5. 選用通知中心。

分離圖層後，`Set HUD Visibility` 只會隱藏介面列。隱藏 HUD 時，播放及前景內容必須繼續掛載。

## 以完整替代介面設計

自訂根介面會取代一般 Player 根介面，因此必須包含使用者操作及復原所需的功能：

- UI 預設選擇；
- 安全關閉應用程式；
- 播放控制及目前曲目狀態；
- 清楚顯示失敗要求；
- 介面所提供功能需要的設定。

使用響應式 UMG 配置，不要依賴固定桌面座標。測試窄視窗、寬視窗、多種 DPI、較長翻譯、空清單，
以及缺少選用圖片的情況。

!!! warning "不要繼承內建根介面"
    Player 內建 Widget 屬於實作細節。請從 `UUserWidget` 及創作者範本提供的公開橋接合約建立根介面。
