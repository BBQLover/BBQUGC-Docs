<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# 註冊套件

Player 透過已註冊的 Primary Asset 尋找自訂根介面。僅建立 Widget Blueprint 不會讓它出現在
UI 預設清單中。

## 建立 Definition

1. 在 Content Browser 的 `Content/<PluginName>/UI` 下建立 **BBQ UI Root Definition**。
2. 使用全域唯一且穩定的資產名稱，例如 `DA_<PluginName>UIRoot`。
3. 將 **Display Name** 設為預設清單中顯示的本地化名稱。
4. 將 **Root Widget Class** 設為根 Widget Blueprint。
5. 儲存 Definition。

Definition 資產名稱會成為其 Primary Asset ID。重新命名會改變選擇 ID。一般更新時應保持
Definition 名稱及 Widget Class Path 不變。

## 加入 PluginEntry

1. 開啟 `Content/<PluginName>/PluginEntry`。
2. 找到 **Asset Register List**。
3. 若沒有合適項目，加入一個 `BBQPluginAssetRegister`。
4. 將 UI Root Definition 加入該項目的 **Asset List**。
5. 儲存 `PluginEntry` 及所有套件資產。

不要把根類別加入 **Class Register List**，也不要修改 Asset Manager 設定。Definition 中已註冊的
Soft Reference 是支援的探索路徑。

## 識別規則

- 使用套件專屬 Definition 名稱，避免全域 Primary Asset ID 衝突。
- 不要從多個 Definition 註冊同一個根 Widget Class；它只會顯示一次。
- 將產生的 `PluginEntry` 保留在命名內容根目錄中。
- 不要複製其他專案的 `PluginEntry`。
- 每次修改 Definition、Widget 或註冊資訊後都要重新建置。

## 建置輸出

從 BBQ UGC Tool 建置並散佈完整的產生套件目錄。不要只擷取或上傳某一個承載檔案。測試前確認
套件包含最新中繼資料及與之相符的 Cook 後承載集合。

!!! note "為什麼編輯器成功仍不足夠"
    編輯器可直接載入未 Cook 的資產。只有建置套件才能證明 Definition、Widget 的 Soft Reference
    及產生的 Entry 已通過 Cook 與執行階段註冊。
