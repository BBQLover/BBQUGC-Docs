<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# ルートのライフサイクル

Widget Blueprint で `BBQUIRoot` インターフェイスイベントを実装します。

## 必須イベント

| イベント | 責務 |
|---|---|
| `Init BBQUI` | API の取得、初期スナップショットの取得、イベント購読、表示状態の初期化を行う。 |
| `On BBQUI Ready` | ルートとブリッジ所有の子ウィジェットが取り付け済みであることを必要とする処理を始める。 |
| `Shutdown BBQUI` | リスナー解除、ドラフト解放、タイマーとアニメーションの停止、このルート所有コールバックの破棄を行う。 |
| `Set HUD Visibility` | 指定された Slate Visibility を HUD クロームだけに適用する。 |

Player はルートをマウントし、通知表示を取り付け、`Init BBQUI`、`On BBQUI Ready` の順に
呼び出します。別プリセットを選ぶと、古いルートを削除する前に `Shutdown BBQUI` を呼びます。

通常のウィジェット構築を `Init BBQUI` の代用にしないでください。公開 UI ブリッジは一般的な
UMG 構築順ではなく、BBQ ライフサイクルによって保証されます。

## Player オーバーレイをホストする

3D 再生または Track Event オーサリングを表示する UI では、次を実装します。

| 関数 | 契約 |
|---|---|
| `Attach Player Overlay Widget` | 渡されたウィジェットを要求先ホストへ挿入して `true` を返す。ホスト非対応時だけ `false` を返す。 |
| `Get Player Overlay Size` | 再生ホスト内部の大きさをローカル UMG 単位で返す。 |
| `Get Player Overlay Offset` | 選択ホストのローカル空間における Player コンテンツ原点を返す。 |

`bForeground = false` は背景より前のランタイム再生、`bForeground = true` は通常クロームより
前のオーサリング／プレビューを要求します。Player 所有オーバーレイを複製したり、別の場所へ
付け替えたり、シャットダウン後に保持したりしないでください。

## 通知表示

`Get Notification Center Widget Class` を未設定にすると、Player 標準の最前面通知センターを
使用します。

独自表示を提供する場合:

1. `BBQUINotificationSink` を実装する Widget Blueprint を作成します。
2. そのクラスを `Get Notification Center Widget Class` から返します。
3. `Attach Notification Center Widget` で、渡されたインスタンスそのものを挿入します。
4. 渡された通知 ID を使って `Push Notification`、`Pop Notification`、`Clear Notifications` を
   実装します。

インスタンスの生成と所有は Player が行い、ルートはホストだけを担当します。確認、永続表示、
自動消去、複数通知のキューをテストしてください。

!!! danger "見えない通知先"
    独自クラスを返しながらインスタンスを取り付けないと、通知が見えないウィジェットへ送られます。
    完全な通知先を実装するか、クラスを未設定にしてください。

## シャットダウン確認

- 購読時と同じリスナーを使い、対応する全 `Unbind...` を呼ぶ。
- キャンセルや失敗の場合も、全 Track Event ドラフトを解放する。
- ドラフトを閉じた後、開いている Track Event 編集対象を閉じる。
- ルート所有のタイマー、アニメーション、遅延コールバックを止める。
- インターフェイスコールバック外で Player 所有オブジェクトを削除しない。
