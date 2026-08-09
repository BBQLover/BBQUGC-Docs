<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# トラブルシューティング

## プリセットが表示されない

UI Root Definition について確認します。

- `Content/<PluginName>` 以下にある。
- 有効な Root Widget Class が設定されている。
- `PluginEntry > Asset Register List > Asset List` に含まれている。
- 全体で重複しないアセット名が付いている。

Widget、Definition、Entry を保存して再ビルドし、インストール済みパッケージ全体を置き換えます。

## 選択すると標準 UI に戻る

選択クラスが `BBQUIRoot` を実装する Widget Blueprint か確認します。ロードできないクラスや
インターフェイス未実装クラスはアクティブになれません。

## UI は表示されるが更新されない

購読前に初期スナップショットを取得します。API インターフェイスを有効に保持し、対応する
デリゲートを購読し、無効化後に新しいスナップショットを取得します。`Init BBQUI` より前に
発生した可能性があるイベントを待たないでください。

## 切り替え後にイベントが複数回届く

購読時と同じリスナーを使い、`Shutdown BBQUI` で対応する全 `Unbind...` を呼びます。タイマーを
止め、削除済みルート所有の遅延コールバックを無視します。

## 通知が表示されない

標準表示を使う場合は独自クラスを返しません。独自通知センターでは
`BBQUINotificationSink` の実装と、`Attach Notification Center Widget` が Player から渡された
インスタンスそのものを可視レイヤーへ挿入していることを確認します。

## オーバーレイ位置がずれる

ホストがローカル UMG 座標を使うことを確認します。`Get Player Overlay Size` と
`Get Player Overlay Offset` は実際のコンテナを表す必要があります。ランタイムと前面ホストでは
原点が異なる場合があるため、別々にテストします。

## コントロール表示だけ変わり Player が変わらない

楽観的 UI 状態を最終状態として確定しないでください。対応 API を要求し、結果を確認してから次の
正しいスナップショットを表示します。失敗時は以前の表示状態へ戻します。

## ビルド成功後もルートクラスがない

Root Definition が `PluginEntry` 経由で登録され、保存済みの意図した Widget Blueprint を参照して
いるか確認します。Editor を保存または終了してから再ビルドし、古いコピーではなく新しく生成された
パッケージを確認します。
