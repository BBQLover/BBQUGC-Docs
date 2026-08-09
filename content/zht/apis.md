<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# UI API

使用 `BBQUIApiLibrary` 取得各功能的公開介面。將根介面或其他具有有效 World 的物件作為
World Context，並在呼叫前確認回傳介面有效。

## 可靠的繫結模式

1. 在 `Init BBQUI` 中取得 API。
2. 讀取並顯示目前快照或清單。
3. 繫結變更 Delegate。
4. 狀態變更時，依需要重新取得權威快照。
5. 透過 `Request...` 函數提交使用者操作。
6. 檢查每個即時 `FPlayerResult` 及非同步完成結果。
7. 在 `Shutdown BBQUI` 中使用監聽物件解除繫結。

事件只是複製狀態的通知或失效訊號，並不允許修改舊陣列或物件。例如，佇列變更後應再次呼叫
`Get Queue Snapshot`。

## API 分組

| Getter | 用途 | 清理 |
|---|---|---|
| `Get Application Api` | 視窗狀態、最小化、最大化或還原、確認關閉 | `Unbind Application Window Events` |
| `Get Playback Api` | 目前曲目、播放控制、跳轉、音量、佇列、順序模式、已創作攝影機 | `Unbind Playback Events` 及 `Unbind Track Changed` |
| `Get Subtitle Api` | 唯讀的目前字幕顯示 | `Unbind Subtitle Changed` |
| `Get Playlist Api` | 播放清單快照及持久化變更 | `Unbind Playlist Changed` |
| `Get Track Library Api` | 媒體庫顯示資料及匯入曲目要求 | `Unbind Track Library Changed` |
| `Get Track Event Api` | 時間軸快照及擁有者管理的事件草稿 | `Unbind Track Events Changed`，再關閉目標及釋放草稿 |
| `Get File Picker Api` | 跨平台單檔、多檔或資料夾選擇 | 僅完成回呼 |
| `Get Notification Api` | 路由通知及確認要求 | 適時關閉保留通知 |
| `Get Plugin Api` | 套件目錄顯示及支援的生命週期要求 | 解除清單及操作事件 |
| `Get Settings Api` | UI 預設、一般選項、歌詞、效能、畫面、事件、語言及快速鍵 | `Unbind Settings Events` |

## 處理命令結果

檢查結果前，不要假定命令成功並確定顯示狀態。失敗時：

- 保留最後一個權威快照；
- 復原僅供預覽的控制項狀態；
- 透過通知 API 顯示簡短且可執行的說明；
- 對可安全重複的操作提供重試。

播放清單及曲目庫的非同步要求透過 Delegate 完成。請讓擁有者 Widget 保持有效直到完成，或忽略
`Shutdown BBQUI` 後抵達的回呼。

## Track Event 草稿擁有權

編輯必須遵循嚴格草稿流程：

1. 對曲目 Handle 呼叫 `Open Track Event Editor`。
2. 透過 API 建立新增、編輯或檢視草稿。
3. 只修改回傳的草稿。
4. 使用 `Commit Track Event Draft` 提交新增或編輯草稿。
5. 每次關閉視窗時呼叫 `Release Track Event Draft`。
6. 所有目標草稿關閉後呼叫 `Close Track Event Editor`。

顯示項目不是可修改的權威物件。Handle 及權限欄位由執行階段擁有者決定；修改複製的 UI 資料
不能取得寫入權限。
