<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# パッケージへ登録する

Player は登録済み Primary Asset からカスタムルートを見つけます。Widget Blueprint を作るだけでは
UI プリセット一覧に表示されません。

## Definition を作成する

1. Content Browser で `Content/<PluginName>/UI` 以下に **BBQ UI Root Definition** を作成します。
2. `DA_<PluginName>UIRoot` のように、全体で重複しない安定したアセット名を付けます。
3. **Display Name** にプリセット一覧へ表示するローカライズ済み名称を設定します。
4. **Root Widget Class** に作成したルート Widget Blueprint を設定します。
5. Definition を保存します。

Definition のアセット名が Primary Asset ID になります。名前を変えると選択 ID も変わります。
通常更新では Definition 名と Widget Class Path の両方を維持してください。

## PluginEntry に追加する

1. `Content/<PluginName>/PluginEntry` を開きます。
2. **Asset Register List** を探します。
3. 適切な項目がなければ `BBQPluginAssetRegister` を追加します。
4. その **Asset List** に UI Root Definition を追加します。
5. `PluginEntry` と全パッケージアセットを保存します。

ルートクラスを **Class Register List** に追加したり、Asset Manager 設定を編集したりしないで
ください。Definition の登録済み Soft Reference がサポート対象の検出経路です。

## ID のルール

- パッケージ固有の Definition 名を使い、グローバルな Primary Asset ID の衝突を避ける。
- 同じルート Widget Class を複数 Definition から登録しない。表示されるのは一つだけです。
- 生成された `PluginEntry` を名前付きコンテンツルートに保持する。
- 別プロジェクトの `PluginEntry` をコピーしない。
- Definition、Widget、登録内容を変えたら必ず再ビルドする。

## ビルド出力

BBQ UGC Tool からビルドし、生成されたパッケージディレクトリ全体を配布します。一つの
ペイロードファイルだけを抜き出してアップロードしないでください。テスト前に、新しい
メタデータと対応する Cook 済みペイロード一式があることを確認します。

!!! note "Editor だけでは確認できない理由"
    Editor は Cook 前のアセットを直接読み込めます。Definition、Widget への Soft Reference、
    生成済み Entry が Cook と実行時登録を通過したことは、ビルド済みパッケージでのみ確認できます。
