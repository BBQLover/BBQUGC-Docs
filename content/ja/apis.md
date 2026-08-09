<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# UI API

各機能の公開インターフェイスは `BBQUIApiLibrary` から取得します。ルート、または有効な World を
持つオブジェクトを World Context に渡し、戻り値が有効か確認してから呼び出します。

## 安定した購読パターン

1. `Init BBQUI` で API を取得する。
2. 現在のスナップショットまたはリストを取得して表示する。
3. 変更デリゲートを購読する。
4. 変更時に必要であれば正しいスナップショットを再取得する。
5. ユーザー操作を `Request...` 関数で送信する。
6. すべての即時 `FPlayerResult` と非同期完了結果を確認する。
7. `Shutdown BBQUI` でリスナーを指定して購読解除する。

イベントはコピー状態の通知または無効化シグナルです。以前取得した配列やオブジェクトを編集する
許可ではありません。たとえばキュー変更後は `Get Queue Snapshot` を再度呼びます。

## API グループ

| Getter | 用途 | 後片付け |
|---|---|---|
| `Get Application Api` | ウィンドウ状態、最小化、最大化／復元、確認済み終了 | `Unbind Application Window Events` |
| `Get Playback Api` | 現在トラック、再生操作、シーク、音量、キュー、再生順、作成済みカメラ | `Unbind Playback Events` と `Unbind Track Changed` |
| `Get Subtitle Api` | 読み取り専用の字幕表示 | `Unbind Subtitle Changed` |
| `Get Playlist Api` | プレイリストのスナップショットと永続化される変更 | `Unbind Playlist Changed` |
| `Get Track Library Api` | ライブラリ表示データとインポート済みトラック要求 | `Unbind Track Library Changed` |
| `Get Track Event Api` | タイムラインスナップショットと所有者管理ドラフト | `Unbind Track Events Changed`、対象を閉じドラフトを解放 |
| `Get File Picker Api` | プラットフォーム共通のファイル、複数ファイル、フォルダー選択 | 完了コールバックのみ |
| `Get Notification Api` | ルーティングされる通知と確認要求 | 必要に応じ保持通知を閉じる |
| `Get Plugin Api` | パッケージ一覧表示とサポート対象のライフサイクル要求 | 一覧と操作イベントを解除 |
| `Get Settings Api` | UI プリセット、一般、歌詞、性能、グラフィック、イベント、言語、ホットキー | `Unbind Settings Events` |

## コマンド結果を扱う

結果を確認する前に成功したものとして表示を確定しないでください。失敗時は:

- 最後の正しいスナップショットを保つ。
- プレビュー専用コントロールを元に戻す。
- 通知 API で短く対処可能なメッセージを出す。
- 安全に繰り返せる操作では再試行を許可する。

プレイリストとトラックライブラリの非同期要求はデリゲートで完了します。完了まで所有ウィジェットを
有効に保つか、`Shutdown BBQUI` 後のコールバックを無視してください。

## Track Event ドラフトの所有

編集は厳密なドラフト経路を使います。

1. Track Handle に対して `Open Track Event Editor` を呼ぶ。
2. API で新規、編集、閲覧ドラフトを作る。
3. 返されたドラフトだけを変更する。
4. 新規／編集ドラフトを `Commit Track Event Draft` で確定する。
5. モーダルを閉じるたびに `Release Track Event Draft` を呼ぶ。
6. 全ドラフトを閉じた後に `Close Track Event Editor` を呼ぶ。

表示エントリーは変更可能な正データではありません。Handle と権限はランタイム所有者が決めます。
コピーされた UI データを書き換えても更新権限は得られません。
