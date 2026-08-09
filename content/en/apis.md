<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# UI APIs

Use `BBQUIApiLibrary` to obtain the public interface for each feature. Pass the root, or another
object with a valid world, as the world context and check the returned interface before calling it.

## Reliable binding pattern

1. In `Init BBQUI`, get the API.
2. Pull and render its current snapshot or list.
3. Bind its change delegate.
4. On change, pull a fresh authoritative snapshot when required.
5. Submit user actions through `Request...` functions.
6. Inspect every immediate `FPlayerResult` and asynchronous completion result.
7. In `Shutdown BBQUI`, unbind using the listener object.

An event is a copied-state notification or an invalidation signal. It is not permission to edit the
previous array or object. For example, after a queue change, call `Get Queue Snapshot` again.

## API groups

| Getter | Use it for | Cleanup |
|---|---|---|
| `Get Application Api` | Window state, minimize, maximize or restore, and confirmed close | `Unbind Application Window Events` |
| `Get Playback Api` | Current track, transport, seek, volume, queue, sequence mode, and authored cameras | `Unbind Playback Events` and `Unbind Track Changed` |
| `Get Subtitle Api` | Read-only active subtitle presentation | `Unbind Subtitle Changed` |
| `Get Playlist Api` | Playlist snapshots and persisted playlist mutations | `Unbind Playlist Changed` |
| `Get Track Library Api` | Library display data and imported-track requests | `Unbind Track Library Changed` |
| `Get Track Event Api` | Timeline snapshots and owner-managed event drafts | `Unbind Track Events Changed`, then close targets and release drafts |
| `Get File Picker Api` | Platform-neutral file, multi-file, or folder selection | Completion callback only |
| `Get Notification Api` | Routed messages and confirmation requests | Pop retained messages when appropriate |
| `Get Plugin Api` | Package catalog presentation and supported lifecycle requests | Unbind list and operation events |
| `Get Settings Api` | UI presets, general options, lyrics, performance, graphics, events, culture, and hotkeys | `Unbind Settings Events` |

## Handle command results

Never update presentation as if a command succeeded before checking the result. On failure:

- preserve the last authoritative snapshot;
- restore any preview-only control state;
- show a concise, actionable message through the notification API;
- allow retry when the operation is safe to repeat.

Asynchronous playlist and track-library requests complete through delegates. Keep the owning widget
valid until completion or ignore the callback after `Shutdown BBQUI`.

## Track Event draft ownership

Editing uses a strict draft path:

1. Call `Open Track Event Editor` for a track handle.
2. Create a new, edit, or view draft through the API.
3. Modify only the returned draft.
4. Commit create or edit drafts with `Commit Track Event Draft`.
5. Call `Release Track Event Draft` whenever the modal closes.
6. Call `Close Track Event Editor` after all target drafts are closed.

Presentation entries are not authoritative mutable objects. Handles and permission fields come from
the runtime owner; changing copied UI data cannot grant write authority.
