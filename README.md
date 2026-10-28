# Care Label Tool

独立 HTML 水洗标生成器。无需 npm 安装或后端服务，直接用 Edge / Chrome 打开 `水洗标生成器.html`。

## 当前接手基线

- 接手日期：2026-10-02。
- 仓库： https://github.com/shaynzhuang/care-label-tool
- 本地跟踪分支：`claude/pensive-babbage-kle75j`。
- 基线提交：`d7e1dfd4a1b89dd2e3c6ad93444e63df9730f7ee`。
- `main` 为初始版本；上述分支比 main 多 5 次提交，包含排版调整、追踪码规则、Excel 批量生成与洗护文字调整。尚未合并到 main。

## 文件与维护方式

- `水洗标生成器.html`：浏览器运行入口，包含样式、数据和 JavaScript。
- `_build.py`：生成上述 HTML 的 Python 脚本；使用标准库，读取相邻 `data/`。维护生成逻辑时修改此文件，再用 Python 3 执行 `python _build.py`，检查生成差异。
- `tracker-bridge.js`：仅在 tracker 路径启用的选款界面；tracker 部署时需与两份 HTML 一起同步，数据接口由 sample_tracker 提供。
- `data/excel_lists.json`、`data/excel_care.json`：仓库内规则派生数据。注释声明来源为 S27 工作簿，接手时未对照共享正本核验。
- `批复-0921.html`、`批复-0921.pdf`、图片目录：参考资料与历史截图。
- `_patch*.py`、`_shot_b.py` 等：历史修改辅助脚本，部分包含旧机器绝对路径，不作为当前构建入口，也不要批量执行。

HTML 与生成脚本需要保持一致：只改 HTML 可能在下次构建时被覆盖。

## 已有功能（按代码确认）

- 单款编辑、款号识别模板、标签预览、浏览器打印 / 保存 PDF。
- ADV / CC / SH、EdgeHill、ANDY & EVAN 模板与多语言内容。
- Excel 订单导入、批量标签、输入模板下载与 Excel 导出。
- tracker 部署时可从 tracker 只读搜索生产单/样衣并预填款号、品牌、英文成分和参考数量；独立打开 HTML 时仍使用手动 / Excel 方式。
- 品牌洗护预设存储在当前浏览器的 localStorage；不是订单数据库，不会跨浏览器同步。

## 网络与验证边界

Excel 功能依赖 cdnjs 的 SheetJS 0.18.5；部分字体依赖 Google Fonts。直接打开 HTML 不代表所有功能均可离线使用，字体未加载时还需检查排版。

接手时已通过：HTML 内联 JavaScript 语法检查、两个 JSON 文件解析检查。
尚未验证：浏览器交互、真实订单导入与导出、打印毫米尺寸、字体渲染、Python 构建重现性和客户规则正确性。仓库当前没有自动测试或 CI 配置。

涉及客户业务规则或生产标签时，先读取共享工作根 `D:/BaiduSyncdisk/工作文件夹` 的启动说明、共同首页、适用客户约束与流程合同，再核对原始规则和批复。仓库注释及派生 JSON 不能替代共享正本。

## 后续优先事项

1. 用真实样例核验单款、批量导入、Excel 导出及打印结果。
2. 对照当前共享正本核验规则数据与品牌模板。
3. 核验生成脚本与 HTML 一致性，确定后续维护入口。
4. 验收后决定是否将现有功能分支合并到 main。
