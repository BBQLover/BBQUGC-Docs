<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# Troubleshooting

## The preset does not appear

Confirm that the UI Root Definition:

- is beneath `Content/<PluginName>`;
- has a valid Root Widget Class;
- is included in `PluginEntry > Asset Register List > Asset List`;
- has a globally distinctive asset name.

Save the widget, definition, and entry, rebuild, then replace the complete installed package.

## Selection returns to the standard UI

Confirm the selected class is a Widget Blueprint implementing `BBQUIRoot`. A class that fails to
load or does not implement the interface cannot become active.

## The UI loads but does not refresh

Pull the initial snapshot before binding. Keep the API interface valid, bind the matching delegate,
and pull a fresh snapshot after invalidation. Do not wait for an event that may have happened before
`Init BBQUI`.

## Events fire more than once

Call every matching `Unbind...` function from `Shutdown BBQUI` using the same listener object used
when binding. Stop timers and ignore deferred callbacks owned by the removed root.

## Notifications are missing

If using standard presentation, return no custom class. If using a custom center, verify it
implements `BBQUINotificationSink` and that `Attach Notification Center Widget` inserts the exact
Player-supplied instance into a visible layer.

## Overlay content is misplaced

Verify the host uses local UMG coordinates. `Get Player Overlay Size` and
`Get Player Overlay Offset` must describe the real target container. Test runtime and foreground
hosts separately because their origins may differ.

## A control changes visually but the Player does not

Do not commit optimistic UI state as the final result. Submit the matching API request, inspect its
result, and render the next authoritative snapshot. Restore the previous display state after
failure.

## Build succeeds but the root class is missing

Confirm the root definition is registered through `PluginEntry` and points to the intended saved
Widget Blueprint. Rebuild after closing or saving the editor, then check the newly generated package
rather than reusing an older copy.
