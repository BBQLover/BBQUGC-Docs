<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# Root lifecycle

Implement the `BBQUIRoot` interface events in the Widget Blueprint.

## Required events

| Event | Responsibility |
|---|---|
| `Init BBQUI` | Get APIs, pull initial snapshots, bind events, and initialize presentation state. |
| `On BBQUI Ready` | Start work that requires the root and bridge-owned child widgets to be attached. |
| `Shutdown BBQUI` | Unbind listeners, release drafts, stop timers and animations, and discard callbacks owned by this root. |
| `Set HUD Visibility` | Apply the supplied Slate visibility to HUD chrome only. |

The Player mounts the root, attaches notification presentation, calls `Init BBQUI`, and then calls
`On BBQUI Ready`. When another preset is selected, it calls `Shutdown BBQUI` before removing the old
root.

Do not substitute generic widget construction for `Init BBQUI`. The public UI bridge is guaranteed
by the BBQ lifecycle, not by ordinary UMG construction order.

## Host Player overlays

Support these functions when the UI presents 3D playback or Track Event authoring:

| Function | Contract |
|---|---|
| `Attach Player Overlay Widget` | Insert the supplied widget into the requested host and return `true`. Return `false` only if the host is unsupported. |
| `Get Player Overlay Size` | Return the playback host's internal bounds in local UMG units. |
| `Get Player Overlay Offset` | Return the Player-content origin in the selected host's local space. |

`bForeground = false` requests runtime playback above the background. `bForeground = true` requests
authoring or preview content above normal chrome. Never clone, reparent elsewhere, or retain a
Player-owned overlay after shutdown.

## Notification presentation

Leave `Get Notification Center Widget Class` unset to keep the Player's standard top-level
notification center.

For custom presentation:

1. Create a Widget Blueprint implementing `BBQUINotificationSink`.
2. Return that class from `Get Notification Center Widget Class`.
3. Insert the exact supplied instance in `Attach Notification Center Widget`.
4. Implement `Push Notification`, `Pop Notification`, and `Clear Notifications` using the supplied
   notification IDs.

The Player creates and owns the instance. Your root only hosts it. Test confirmations, persistent
messages, automatic dismissal, and multiple queued notifications.

!!! danger "Invisible sink"
    Returning a custom class without attaching the supplied instance can route notifications to an
    invisible widget. Either implement the complete sink path or leave the class unset.

## Shutdown checklist

- Call every matching `Unbind...` function with the listener used during binding.
- Release every Track Event draft, even after cancel or failure.
- Close any open Track Event editor target after its drafts are closed.
- Stop root-owned timers, animations, and deferred callbacks.
- Do not remove Player-owned overlay or notification objects outside the interface callbacks.
