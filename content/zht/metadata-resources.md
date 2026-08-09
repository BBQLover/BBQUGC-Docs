©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 1 -->

# 中繼資料與資源

選擇專案，按一下 **Edit Metadata**，填寫面向創作者的欄位。關閉視窗時會儲存變更。

| 欄位 | 指引 |
|---|---|
| `Id` | 工具建立的識別；更新時保留。 |
| `Name` | 專案與套件名稱；保持穩定。 |
| `Version` | 用於相依選擇的數字版本。 |
| `VersionName` | 如 `1.0.0` 的可讀版本。 |
| `FriendlyName` | 向使用者顯示的名稱。 |
| `Description` | 簡短的套件說明。 |
| `Category` | 最符合的分類，或 `Other`。 |
| `CreatedBy` | 創作者或團隊顯示名稱。 |
| URL 欄位 | 公開 HTTPS 連結，或留空。 |

一般更新應保留相同的專案、`Id` 和 `Name`。只有刻意製作不相容的替代作品時才建立新識別。

## 展示資源

將展示檔案放在 `<ProjectRoot>/BBQ/Resources/`：

- `Cover.png`：方形封面；500×500 是實用工作尺寸。
- `Description.png`：寬幅圖片；1920×1080 是實用工作尺寸。

建置工具會複製完整的實體資源目錄樹。請避免符號連結、控制圖片大小，並在最終套件中檢查複製結果。
