<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# 疑難排解

## 預設沒有出現

確認 UI Root Definition：

- 位於 `Content/<PluginName>` 下；
- 設定了有效的 Root Widget Class；
- 已加入 `PluginEntry > Asset Register List > Asset List`；
- 使用全域唯一的資產名稱。

儲存 Widget、Definition 及 Entry，重新建置，然後取代完整的已安裝套件。

## 選擇後回到標準 UI

確認所選類別是實作 `BBQUIRoot` 的 Widget Blueprint。無法載入或未實作介面的類別不能成為
作用中根介面。

## 介面載入但不重新整理

繫結前先讀取初始快照。保持 API 介面有效、繫結正確 Delegate，並在失效後取得新快照。不要等待
可能在 `Init BBQUI` 之前已發生的事件。

## 切換介面後事件觸發多次

在 `Shutdown BBQUI` 中使用繫結時的同一監聽物件呼叫所有對應的 `Unbind...`。停止計時器，並忽略
由已移除根介面擁有的延遲回呼。

## 通知沒有顯示

使用標準顯示時不要回傳自訂類別。使用自訂通知中心時，確認其實作
`BBQUINotificationSink`，且 `Attach Notification Center Widget` 把 Player 傳入的同一個實例
插入可見圖層。

## 覆疊內容位置錯誤

確認容器使用本地 UMG 座標。`Get Player Overlay Size` 及 `Get Player Overlay Offset` 必須描述
實際目標容器。執行階段與前景容器的原點可能不同，應分別測試。

## 控制項外觀改變，但 Player 狀態未改變

不要把樂觀 UI 狀態視為最終結果。提交對應 API 要求、檢查結果，再顯示下一份權威快照。失敗時
復原原有顯示狀態。

## 建置成功，但根類別缺失

確認 Root Definition 已透過 `PluginEntry` 註冊，並指向預期的已儲存 Widget Blueprint。儲存或
關閉編輯器後重新建置，並檢查新產生的套件，不要繼續使用舊副本。
