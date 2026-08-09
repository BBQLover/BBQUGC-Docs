<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# ルート UI を作成する

## 推奨レイアウト

予測しやすい小さなコンテンツツリーにします。

```text
Content/<PluginName>/
├── PluginEntry.uasset
└── UI/
    ├── WBP_<PluginName>Root.uasset
    ├── DA_<PluginName>UIRoot.uasset
    ├── Components/
    ├── Icons/
    └── Notifications/          # 任意
```

サブフォルダー名は変更できます。重要なのは、パッケージの全アセットをプロジェクト固有の
コンテンツルート以下に置くことです。

## Widget Blueprint を作成する

1. BBQ UGC Tool からプロジェクトを開きます。
2. `Content/<PluginName>/UI` に **Widget Blueprint** を作成します。
3. ルートパネルを全画面レイアウトにします。
4. **Class Settings** を開き、Implemented Interface に `BBQUIRoot` を追加します。
5. コンパイルして保存します。

`BBQUIRoot` を実装していないクラスは、選択済みルートとして Player に受理されません。

## 表示レイヤーを分離する

背面から前面へ、独立したコンテナを用意します。

1. Player 背景
2. ランタイム再生オーバーレイ
3. HUD クロームと主要ビュー
4. オーサリングまたはプレビュー用の前面オーバーレイ
5. 任意の通知センター

この分離により、`Set HUD Visibility` はクロームだけを隠せます。HUD が非表示でも、再生と
前面コンテンツはマウントされたままにします。

## 装飾ではなく置き換えとして設計する

カスタムルートは通常の Player ルートを置き換えます。操作と復旧に必要な機能を含めます。

- UI プリセットの選択
- アプリケーションの安全な終了
- 再生操作と現在トラックの状態
- 失敗した要求の表示
- UI が提供する機能に必要な設定

固定座標ではなくレスポンシブな UMG レイアウトを使います。狭い／広いウィンドウ、複数の
DPI スケール、長い翻訳文、空のリスト、任意画像がない状態をテストしてください。

!!! warning "組み込みルートを継承しない"
    Player 組み込みウィジェットは実装詳細です。クリエイターテンプレートが提供する
    `UUserWidget` と公開ブリッジ契約からルートを構築してください。
