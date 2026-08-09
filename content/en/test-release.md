<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# Test and release

Test the built package in the released BBQ Player. Editor preview does not cover startup loading,
cook retention, saved preset restoration, or switching away from an active custom root.

## Local test

1. Close BBQ Player.
2. Copy the complete built package directory into the Player's local Mods directory.
3. Start the Player normally.
4. Open the package manager, locate the local package, and enable it.
5. Restart from a clean process.
6. Open Settings and locate the definition's **Display Name** in the UI preset list.
7. Select it and confirm the root rebuilds.
8. Restart again and confirm the selection is restored.

## Functional matrix

Test every feature your root exposes:

- empty and populated library;
- empty, single-item, and reordered playback queue;
- play, pause, seek, previous, next, mute, and volume;
- active subtitles and subtitle clearing;
- runtime and foreground overlays;
- HUD visibility without removing overlay layers;
- notification, confirmation, persistent, and auto-dismiss behavior;
- minimize, maximize, restore, and safe close;
- settings changes and UI preset recovery;
- failed and unavailable API requests.

Also test narrow, normal, and wide windows; several DPI scales; keyboard focus; long localized text;
missing optional art; and reduced-motion preference.

## Teardown and fallback

1. Switch back to the standard UI and confirm the custom root stops receiving events.
2. Select the custom root again and verify subscriptions are not duplicated.
3. Disable or remove the package.
4. Restart and confirm startup falls back to the standard root.
5. Reinstall an older release, update to the new package, and repeat the selection test.

## Release checklist

- [ ] Built with the latest published BBQ UGC Tool and required engine version.
- [ ] All assets saved beneath `Content/<PluginName>`.
- [ ] Root implements `BBQUIRoot` and separates presentation layers.
- [ ] Lifecycle initializes once and unbinds every listener.
- [ ] Notification presentation is complete or left unset.
- [ ] UI Root Definition has a unique stable name and valid root class.
- [ ] Definition is present in `PluginEntry`'s Asset Register List.
- [ ] Every command and completion path handles failure.
- [ ] Standard UI remains available as recovery.
- [ ] Clean install, restart, switch-away, update, and fallback tests pass.
- [ ] The delivered copy is tested without a competing local package.
