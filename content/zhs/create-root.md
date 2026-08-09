<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# 创建根界面

## 推荐布局

使用简洁、可预测的内容目录：

```text
Content/<PluginName>/
├── PluginEntry.uasset
└── UI/
    ├── WBP_<PluginName>Root.uasset
    ├── DA_<PluginName>UIRoot.uasset
    ├── Components/
    ├── Icons/
    └── Notifications/          # 可选
```

子目录名称可以调整。关键要求是包内所有资产都位于项目命名内容根目录下。

## 创建 Widget Blueprint

1. 从 BBQ UGC Tool 打开项目。
2. 在 `Content/<PluginName>/UI` 下创建 **Widget Blueprint**。
3. 将根面板设为全屏布局。
4. 打开 **Class Settings**，在已实现接口中添加 `BBQUIRoot`。
5. 编译并保存控件。

Player 不会接受未实现 `BBQUIRoot` 的选定根类。

## 分离显示图层

从后到前使用独立容器：

1. Player 背景；
2. 运行时播放叠加层；
3. 自定义界面栏和主要视图；
4. 前景创作或预览叠加层；
5. 可选通知中心。

分离图层后，`Set HUD Visibility` 只隐藏界面栏。隐藏 HUD 时，播放和前景内容必须继续挂载。

## 按完整替代界面设计

自定义根界面会替代普通 Player 根界面，因此必须包含用户操作和恢复所需的功能：

- UI 预设选择；
- 安全关闭应用程序；
- 播放控制和当前曲目状态；
- 清晰显示失败请求；
- 界面所提供功能需要的设置。

使用响应式 UMG 布局，不要依赖固定桌面坐标。测试窄屏、宽屏、多种 DPI、较长译文、空列表以及
缺少可选图片的情况。

!!! warning "不要继承内置根界面"
    Player 内置控件属于实现细节。请从 `UUserWidget` 和创作者模板提供的公开桥接协议构建根界面。
