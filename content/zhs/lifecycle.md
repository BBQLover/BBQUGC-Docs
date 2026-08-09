<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# 根界面生命周期

在 Widget Blueprint 中实现 `BBQUIRoot` 接口事件。

## 必需事件

| 事件 | 职责 |
|---|---|
| `Init BBQUI` | 获取 API、读取初始快照、绑定事件并初始化显示状态。 |
| `On BBQUI Ready` | 启动需要根界面和桥接子控件已完成挂载的工作。 |
| `Shutdown BBQUI` | 解除监听、释放草稿、停止计时器和动画，并丢弃此根界面拥有的回调。 |
| `Set HUD Visibility` | 只把传入的 Slate 可见性应用到界面栏。 |

Player 会先挂载根界面和通知显示，然后依次调用 `Init BBQUI` 与 `On BBQUI Ready`。选择其他预设时，
Player 会在移除旧根界面前调用 `Shutdown BBQUI`。

不要用普通控件构造代替 `Init BBQUI`。公开 UI 桥接由 BBQ 生命周期保证，而不是由通用 UMG
构造顺序保证。

## 托管 Player 叠加层

如果界面要显示 3D 播放或 Track Event 创作功能，请实现：

| 函数 | 协议 |
|---|---|
| `Attach Player Overlay Widget` | 将传入控件插入请求的容器并返回 `true`；只有不支持该容器时才返回 `false`。 |
| `Get Player Overlay Size` | 返回播放容器内部大小，单位为本地 UMG 坐标。 |
| `Get Player Overlay Offset` | 返回所选容器本地空间中的 Player 内容原点。 |

`bForeground = false` 表示背景之上的运行时播放内容，`bForeground = true` 表示普通界面栏之上的
创作或预览内容。不要复制、再次挂载或在关闭后保留 Player 所有的叠加控件。

## 通知显示

不设置 `Get Notification Center Widget Class` 时，Player 会保留标准顶层通知中心。

若要提供自定义显示：

1. 创建实现 `BBQUINotificationSink` 的 Widget Blueprint。
2. 从 `Get Notification Center Widget Class` 返回该类。
3. 在 `Attach Notification Center Widget` 中插入 Player 传入的同一个实例。
4. 使用传入的通知 ID 实现 `Push Notification`、`Pop Notification` 和 `Clear Notifications`。

实例由 Player 创建和拥有，根界面只负责托管。请测试确认提示、持久通知、自动关闭和多条通知队列。

!!! danger "不可见的通知接收器"
    如果返回自定义类却不挂载传入实例，通知可能被发送到不可见控件。请完整实现接收器流程，
    否则保持该类未设置。

## 关闭检查清单

- 使用绑定时的同一监听对象调用所有对应的 `Unbind...`。
- 即使取消或失败，也释放所有 Track Event 草稿。
- 所有草稿关闭后，再关闭已打开的 Track Event 编辑目标。
- 停止根界面拥有的计时器、动画和延迟回调。
- 不要在接口回调之外移除 Player 所有的叠加或通知对象。
