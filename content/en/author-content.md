©︎ BBQ大好き All Rights Reserved.
<!-- source-revision: 1 -->

# Author content

1. Select the project and choose **Open Project**.
2. Keep every authored asset beneath `Content/<PluginName>/`.
3. Create content using features exposed by the current template.
4. Save all assets and resolve missing references, compile errors, and validation warnings.

The cook is scoped to the plugin content root. Assets elsewhere may be omitted even when they work in the editor. Avoid references to editor-only content, absolute local files, test assets, or Player assets not provided for creator use.

## Optional UI package

A project may provide a selectable replacement interface. Start with [Create the root widget](create-root.md), implement the [root lifecycle](lifecycle.md), and use only the documented [UI APIs](apis.md).

## Before closing Unreal

- Save every modified asset.
- Compile Blueprints and resolve errors.
- Check that required references stay inside supported creator content.
- Verify names and paths before other content depends on them.
