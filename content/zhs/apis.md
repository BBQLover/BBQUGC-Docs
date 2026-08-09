<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# UI API

使用 `BBQUIApiLibrary` 获取各功能的公开接口。将根界面或其他具有有效 World 的对象作为
World Context，并在调用前确认返回接口有效。

## 可靠的绑定模式

1. 在 `Init BBQUI` 中获取 API。
2. 读取并显示当前快照或列表。
3. 绑定变化委托。
4. 状态变化时按需重新获取权威快照。
5. 通过 `Request...` 函数提交用户操作。
6. 检查每个即时 `FPlayerResult` 和异步完成结果。
7. 在 `Shutdown BBQUI` 中使用监听对象解除绑定。

事件只是复制状态的通知或失效信号，并不允许修改旧数组或对象。例如，队列变化后应再次调用
`Get Queue Snapshot`。

## API 分组

| Getter | 用途 | 清理 |
|---|---|---|
| `Get Application Api` | 窗口状态、最小化、最大化或还原、确认关闭 | `Unbind Application Window Events` |
| `Get Playback Api` | 当前曲目、播放控制、跳转、音量、队列、顺序模式、已创作摄像机 | `Unbind Playback Events` 和 `Unbind Track Changed` |
| `Get Subtitle Api` | 只读的当前字幕显示 | `Unbind Subtitle Changed` |
| `Get Playlist Api` | 播放列表快照和持久化修改 | `Unbind Playlist Changed` |
| `Get Track Library Api` | 媒体库显示数据和导入曲目请求 | `Unbind Track Library Changed` |
| `Get Track Event Api` | 时间线快照和所有者管理的事件草稿 | `Unbind Track Events Changed`，再关闭目标并释放草稿 |
| `Get File Picker Api` | 跨平台单文件、多文件或文件夹选择 | 仅完成回调 |
| `Get Notification Api` | 路由通知和确认请求 | 适时关闭保留通知 |
| `Get Plugin Api` | 包目录显示和受支持的生命周期请求 | 解除列表和操作事件 |
| `Get Settings Api` | UI 预设、常规选项、歌词、性能、画面、事件、语言和快捷键 | `Unbind Settings Events` |

## 处理命令结果

检查结果前，不要假定命令成功并确定显示状态。失败时：

- 保留最后一个权威快照；
- 恢复仅用于预览的控件状态；
- 通过通知 API 显示简短且可执行的说明；
- 对可安全重复的操作提供重试。

播放列表和曲目库的异步请求通过委托完成。请让所有者控件保持有效直到完成，或忽略
`Shutdown BBQUI` 之后到达的回调。

## Track Event 草稿所有权

编辑必须遵循严格草稿流程：

1. 对曲目 Handle 调用 `Open Track Event Editor`。
2. 通过 API 创建新建、编辑或查看草稿。
3. 只修改返回的草稿。
4. 使用 `Commit Track Event Draft` 提交新建或编辑草稿。
5. 每次关闭窗口时调用 `Release Track Event Draft`。
6. 所有目标草稿关闭后调用 `Close Track Event Editor`。

显示条目不是可修改的权威对象。Handle 和权限字段由运行时所有者决定；修改复制的 UI 数据不能
获得写入权限。
