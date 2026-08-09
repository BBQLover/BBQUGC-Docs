<!-- ©︎ BBQ大好き All Rights Reserved. -->
<!-- source-revision: 1 -->

# 注册包

Player 通过已注册的 Primary Asset 查找自定义根界面。仅创建 Widget Blueprint 不会让它出现在
UI 预设列表中。

## 创建 Definition

1. 在 Content Browser 的 `Content/<PluginName>/UI` 下创建 **BBQ UI Root Definition**。
2. 使用全局唯一且稳定的资产名，例如 `DA_<PluginName>UIRoot`。
3. 将 **Display Name** 设置为预设列表中显示的本地化名称。
4. 将 **Root Widget Class** 设置为根 Widget Blueprint。
5. 保存 Definition。

Definition 资产名会成为其 Primary Asset ID。重命名会改变选择 ID。普通更新时应保持 Definition
名称和 Widget Class Path 不变。

## 加入 PluginEntry

1. 打开 `Content/<PluginName>/PluginEntry`。
2. 找到 **Asset Register List**。
3. 如果没有合适条目，添加一个 `BBQPluginAssetRegister`。
4. 将 UI Root Definition 加入该条目的 **Asset List**。
5. 保存 `PluginEntry` 以及所有包资产。

不要把根类加入 **Class Register List**，也不要修改 Asset Manager 配置。Definition 中已注册的
Soft Reference 是受支持的发现路径。

## 标识规则

- 使用包专属 Definition 名，避免全局 Primary Asset ID 冲突。
- 不要从多个 Definition 注册同一个根 Widget Class；它只会显示一次。
- 将生成的 `PluginEntry` 保留在命名内容根目录中。
- 不要复制其他项目的 `PluginEntry`。
- 每次修改 Definition、Widget 或注册信息后都要重新构建。

## 构建输出

从 BBQ UGC Tool 构建并分发完整的生成包目录。不要只提取或上传某一个载荷文件。测试前确认包中
包含最新元数据和与之匹配的 Cook 后载荷集合。

!!! note "为什么编辑器成功还不够"
    编辑器可直接加载未 Cook 的资产。只有构建包才能证明 Definition、Widget 的 Soft Reference
    和生成的 Entry 已通过 Cook 与运行时注册。
