©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 1 -->

# ビルドとローカルテスト

## パッケージをビルドする

全アセットを保存して Unreal Editor を閉じ、UGC Tool でプロジェクトを選んで **Build Selected** を実行します。成功または失敗が表示されるまでログを開いておきます。

```text
<ProjectRoot>/BBQ/Build/<PluginName>/
├── <PluginName>.BBQPlugin
├── Content/Paks/
│   ├── <PluginName>-Windows.pak
│   ├── <PluginName>-Windows.ucas
│   └── <PluginName>-Windows.utoc
└── Resources/
```

完全な `<PluginName>` フォルダーがテストとアップロードの単位です。平坦化したり、一部だけコピーしたりしないでください。ソース素材、ログ、デバッグファイル、認証情報、無関係なパッケージを除外します。

## BBQ Player でテストする

BBQ Player を終了し、ビルド済みフォルダー全体を次へコピーします。

```text
<SteamLibrary>\steamapps\common\BBQ Player\BBQPlayer\Mods\<PluginName>\
```

Player を起動してローカルパッケージを開き、メタデータと画像を確認して有効化します。想定する全コンテンツと動作を試し、必要なら無効化して再起動した後、再び正常に有効化できることを確認します。

更新時は、新規インストールと以前の公開版からの置き換えの両方をテストしてください。
