<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# 根介面生命週期

在 Widget Blueprint 中實作 `BBQUIRoot` 介面事件。

## 必要事件

| 事件 | 職責 |
|---|---|
| `Init BBQUI` | 取得 API、讀取初始快照、繫結事件並初始化顯示狀態。 |
| `On BBQUI Ready` | 啟動需要根介面及橋接子 Widget 已完成掛載的工作。 |
| `Shutdown BBQUI` | 解除監聽、釋放草稿、停止計時器及動畫，並捨棄此根介面擁有的回呼。 |
| `Set HUD Visibility` | 只把傳入的 Slate 可見性套用到介面列。 |

Player 會先掛載根介面及通知顯示，再依序呼叫 `Init BBQUI` 與 `On BBQUI Ready`。選擇其他預設時，
Player 會在移除舊根介面前呼叫 `Shutdown BBQUI`。

不要用一般 Widget 建構代替 `Init BBQUI`。公開 UI 橋接由 BBQ 生命週期保證，而不是由通用 UMG
建構順序保證。

## 託管 Player 覆疊層

若介面需要顯示 3D 播放或 Track Event 創作功能，請實作：

| 函數 | 合約 |
|---|---|
| `Attach Player Overlay Widget` | 將傳入 Widget 插入要求的容器並回傳 `true`；只有不支援該容器時才回傳 `false`。 |
| `Get Player Overlay Size` | 回傳播放容器內部大小，單位為本地 UMG 座標。 |
| `Get Player Overlay Offset` | 回傳所選容器本地空間中的 Player 內容原點。 |

`bForeground = false` 表示背景之上的執行階段播放內容，`bForeground = true` 表示一般介面列之上的
創作或預覽內容。請勿複製、重新掛載，或在關閉後保留 Player 擁有的覆疊 Widget。

## 通知顯示

不設定 `Get Notification Center Widget Class` 時，Player 會保留標準頂層通知中心。

若要提供自訂顯示：

1. 建立實作 `BBQUINotificationSink` 的 Widget Blueprint。
2. 從 `Get Notification Center Widget Class` 回傳該類別。
3. 在 `Attach Notification Center Widget` 中插入 Player 傳入的同一個實例。
4. 使用傳入的通知 ID 實作 `Push Notification`、`Pop Notification` 及 `Clear Notifications`。

實例由 Player 建立及擁有，根介面只負責託管。請測試確認提示、持續通知、自動關閉及多筆通知佇列。

!!! danger "不可見的通知接收器"
    若回傳自訂類別卻未掛載傳入實例，通知可能傳送至不可見 Widget。請完整實作接收器流程，
    否則保持該類別未設定。

## 關閉檢查清單

- 使用繫結時的同一監聽物件呼叫所有對應的 `Unbind...`。
- 即使取消或失敗，也釋放所有 Track Event 草稿。
- 所有草稿關閉後，再關閉已開啟的 Track Event 編輯目標。
- 停止根介面擁有的計時器、動畫及延遲回呼。
- 不要在介面回呼之外移除 Player 擁有的覆疊或通知物件。
