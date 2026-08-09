<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# 故障排除

## 预设没有出现

确认 UI Root Definition：

- 位于 `Content/<PluginName>` 下；
- 设置了有效的 Root Widget Class；
- 已加入 `PluginEntry > Asset Register List > Asset List`；
- 使用全局唯一的资产名。

保存 Widget、Definition 和 Entry，重新构建，然后替换完整的已安装包。

## 选择后返回标准 UI

确认所选类是实现 `BBQUIRoot` 的 Widget Blueprint。无法加载或未实现接口的类不能成为活动根界面。

## 界面加载但不刷新

绑定前先读取初始快照。保持 API 接口有效，绑定正确委托，并在失效后获取新快照。不要等待可能在
`Init BBQUI` 之前已经发生的事件。

## 切换界面后事件触发多次

在 `Shutdown BBQUI` 中使用绑定时的同一监听对象调用所有对应 `Unbind...`。停止计时器，并忽略
由已移除根界面拥有的延迟回调。

## 通知没有显示

使用标准显示时不要返回自定义类。使用自定义通知中心时，确认其实现
`BBQUINotificationSink`，且 `Attach Notification Center Widget` 把 Player 传入的同一个实例
插入可见图层。

## 叠加内容位置错误

确认容器使用本地 UMG 坐标。`Get Player Overlay Size` 和 `Get Player Overlay Offset` 必须描述
实际目标容器。运行时与前景容器原点可能不同，应分别测试。

## 控件外观变化，但 Player 状态未变化

不要把乐观 UI 状态当作最终结果。提交对应 API 请求，检查结果，再显示下一份权威快照。失败时恢复
原有显示状态。

## 构建成功，但根类缺失

确认 Root Definition 已通过 `PluginEntry` 注册，并指向预期的已保存 Widget Blueprint。保存或
关闭编辑器后重新构建，并检查新生成的包，不要继续使用旧副本。
