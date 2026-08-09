<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# Register the package

The Player discovers custom roots through registered primary assets. A Widget Blueprint by itself
does not appear in the UI preset list.

## Create the definition

1. In the Content Browser, create a **BBQ UI Root Definition** under
   `Content/<PluginName>/UI`.
2. Give it a globally distinctive, stable asset name such as `DA_<PluginName>UIRoot`.
3. Set **Display Name** to the localized name shown in the preset list.
4. Set **Root Widget Class** to your root Widget Blueprint.
5. Save the definition.

The definition asset name becomes its primary-asset identity. Renaming it changes the selection ID.
Keep both the definition name and widget class path stable during ordinary updates.

## Add it to PluginEntry

1. Open `Content/<PluginName>/PluginEntry`.
2. Find **Asset Register List**.
3. Add a `BBQPluginAssetRegister` entry if no suitable entry exists.
4. Add the UI Root Definition to that entry's **Asset List**.
5. Save `PluginEntry`, then save all package assets.

Do not place the root class in **Class Register List** and do not edit Asset Manager configuration.
The definition's registered soft reference is the supported discovery path.

## Identity rules

- Use a package-specific definition asset name to avoid global primary-asset identity collisions.
- Do not register the same root widget class from multiple definitions; only one is presented.
- Keep the generated `PluginEntry` in the named content root.
- Never copy a `PluginEntry` from another project.
- Rebuild after every definition, widget, or registration change.

## Build output

Build from the BBQ UGC Tool and distribute the complete generated package directory. Do not extract
or upload only one payload file. Before testing, confirm the package has fresh metadata and its
matching cooked payload set.

!!! note "Why editor success is not enough"
    The editor can load uncooked assets directly. Only a built package proves that the definition,
    soft widget reference, and generated entry survived cooking and runtime registration.
