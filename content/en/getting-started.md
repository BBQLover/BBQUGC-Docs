©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 2 -->

# Getting started

## What you need

- 64-bit Windows and Steam running with the creator account.
- The latest BBQ UGC Tool installed through Steam.
- Unreal Engine 5.7, or the exact version requested by the current tool release.
- Space for Unreal cook output and a second packaged copy.
- Permission to publish every asset you use.

Always create and rebuild projects with the latest tool release. Do not copy binaries from an older project.

## Configure Unreal Engine

!!! warning "Separate Epic license required"
    Unreal Engine is provided and licensed by Epic Games, not BBQ. Before opening or building a project, obtain the required Unreal Engine version from an authorized Epic source and accept the applicable [Unreal Engine EULA](https://www.unrealengine.com/eula/unreal). The BBQ UGC Tool does not include or replace an Unreal Engine license. See the [UGC Creator Agreement](agreement.md#3-epic-games-and-unreal-engine-terms) for the complete separation of responsibilities.

1. Start the UGC Tool and open **Settings**.
2. Choose **Select UEPath**.
3. Select the Unreal installation root, such as `C:\Program Files\Epic Games\UE_5.7`.
4. Confirm it contains `Engine\Binaries\Win64\UnrealEditor.exe`.

Avoid read-only, cloud-synchronized, or unreliable network locations for your project.

## Create a project

Open **Projects**, choose **Create**, enter a stable name, select a parent directory, and confirm. Use ASCII letters, digits, `_`, or `-` for the most portable name.

```text
<ProjectRoot>/
├── Content/<PluginName>/
├── BBQ/Resources/
├── BBQ/Build/
└── <PluginName>.uproject
```

The project name becomes both the package name and required content root. Keep it unchanged after the first release.

## Add an existing project

Choose **Projects > Add** and select the project's direct-child `.uproject`. Adding it to the list does not upgrade an old template; recreate older projects with the current tool if compatibility checks fail.
