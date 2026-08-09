©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 2 -->

# はじめに

## 必要なもの

- 64 ビット版 Windows と、クリエイターアカウントで実行中の Steam。
- Steam からインストールした最新の BBQ UGC Tool。
- Unreal Engine 5.7、または現在のツールが指定する正確なバージョン。
- Unreal の Cook 出力とパッケージコピー用の空き容量。
- 使用する全素材を公開する権利。

プロジェクトの作成と再ビルドには、常に最新のツールを使用してください。古いプロジェクトからバイナリをコピーしないでください。

## Unreal Engine を設定する

!!! warning "Epic の別ライセンスが必要です"
    Unreal Engine は BBQ ではなく Epic Games が提供し、ライセンスします。プロジェクトを開く、またはビルドする前に、Epic の正規配布元から必要な Unreal Engine バージョンを取得し、適用される [Unreal Engine EULA](https://www.unrealengine.com/eula/unreal) に同意してください。BBQ UGC Tool は Unreal Engine ライセンスを含まず、代替もしません。責任の区分は [UGC クリエイター規約](agreement.md)を確認してください。

1. UGC Tool の **Settings** を開きます。
2. **Select UEPath** を選びます。
3. `C:\Program Files\Epic Games\UE_5.7` などの Unreal インストールルートを選びます。
4. `Engine\Binaries\Win64\UnrealEditor.exe` が含まれることを確認します。

読み取り専用、クラウド同期中、不安定なネットワーク上の場所は避けてください。

## プロジェクトを作成する

**Projects** で **Create** を選び、安定した名前と親フォルダーを指定します。移植性のため、名前には英数字、`_`、`-` を使用してください。

```text
<ProjectRoot>/
├── Content/<PluginName>/
├── BBQ/Resources/
├── BBQ/Build/
└── <PluginName>.uproject
```

プロジェクト名はパッケージ名と必須コンテンツルートになります。初回リリース後は変更しないでください。

## 既存プロジェクトを追加する

**Projects > Add** で直下の `.uproject` を選びます。リストへの追加だけでは古いテンプレートは更新されません。互換性チェックに失敗する場合は、現在のツールで作り直してください。
