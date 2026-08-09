<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# Create the root widget

## Recommended layout

Use a compact, predictable content tree:

```text
Content/<PluginName>/
├── PluginEntry.uasset
└── UI/
    ├── WBP_<PluginName>Root.uasset
    ├── DA_<PluginName>UIRoot.uasset
    ├── Components/
    ├── Icons/
    └── Notifications/          # optional
```

The subfolder names are flexible. The important rule is that every package asset remains under the
project's named content root.

## Create the Widget Blueprint

1. Open the project from the BBQ UGC Tool.
2. Create a **Widget Blueprint** under `Content/<PluginName>/UI`.
3. Give it a full-screen root panel.
4. Open **Class Settings** and add the `BBQUIRoot` implemented interface.
5. Compile and save the widget.

The Player rejects a selected root class that does not implement `BBQUIRoot`.

## Separate presentation layers

Use independent containers, ordered from back to front:

1. Player background;
2. runtime playback overlay;
3. your HUD chrome and primary views;
4. foreground authoring or preview overlay;
5. optional notification center.

This separation lets `Set HUD Visibility` hide only chrome. Playback and foreground content must
remain mounted when the HUD is hidden.

## Design for replacement, not decoration

The custom root replaces the normal Player root. Include the controls users need to recover and
operate the application:

- UI preset selection;
- safe application close;
- playback transport and current-track state;
- visible request failures;
- settings needed by features your UI exposes.

Use responsive UMG layout rather than fixed desktop coordinates. Test narrow and wide windows,
multiple DPI scales, long translated strings, empty lists, and missing optional images.

!!! warning "Do not subclass the built-in root"
    Built-in Player widgets are implementation details. Build your root from `UUserWidget` and the
    public bridge contracts supplied by the creator template.
