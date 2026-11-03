# 把话说清楚：普通人的关键对话

**作者：KK · 原创AI辅助首稿 · draft v0.1 · 内容已获作者验收**

正文和版权文件保留首稿时的原有文字；当前内容验收状态以本页和元数据为准。

一本围绕实际任务展开的中文沟通读物：怎样提出可回答的请求、谈清分工、解释误会、表达异议、开会、发文字消息，以及谈不成后怎样收尾。清楚不等于让别人同意；本书关注的是理解、决定、承诺和行动怎样接得上。

本版包含前言、十二章完整正文、读者练习及来源说明。人物、故事和对话均为原创虚构，不是作者亲历或研究个案。方法建议未经本书专项效果验证，研究与方法来源的使用边界见[来源卡](sources/README.md)。本书不是任何沟通体系的认证教材。

**[完整中文初稿阅读](dist/reader-manuscript.md)** · [分章目录](#阅读) · [提交反馈](https://github.com/kavadream/clear-conversations/issues)

## 阅读

- [前言](manuscript/00-preface.md)
- [第一章 开口以前 先确定这次要谈哪件事](manuscript/01-purpose.md)
- [第二章 提出一个对方能够回答的请求](manuscript/02-request.md)
- [第三章 谈分工时 把交接处也谈进去](manuscript/03-division.md)
- [第四章 解释误会 先找出理解从哪里分开](manuscript/04-misunderstanding.md)
- [第五章 提出异议时 让别人知道你反对哪一步](manuscript/05-disagreement.md)
- [第六章 开会时 把讨论和决定分开](manuscript/06-meetings.md)
- [第七章 发文字消息时 别让对方替你补语气和背景](manuscript/07-messages.md)
- [第八章 家庭里的时间和钱 怎样谈得具体而不冷淡](manuscript/08-home.md)
- [第九章 遇到服务问题 把不满变成能够处理的事项](manuscript/09-service.md)
- [第十章 面对有权决定你处境的人 怎样开口](manuscript/10-power.md)
- [第十一章 谈不成以后 不必无限重复同一场对话](manuscript/11-stop.md)
- [第十二章 话说完以后 让约定接得上行动](manuscript/12-followup.md)
- [合并阅读版](dist/reader-manuscript.md)
- [来源与阅读边界](sources/README.md)
- [版权说明](CONTENT-LICENSE.md)

## 反馈

欢迎指出难懂的句子、情节中的不一致、不适用的条件或来源对应问题。反馈最好注明章名、小标题、原句和修改理由；不同意某项建议也欢迎说明具体处境。请勿提交真实他人的可识别隐私信息。

当前完整中文首稿的内容已获作者验收；这不代表出版终稿、专业同行评审或读者效果验证。英文简介见[README.en.md](README.en.md)，完整的AI辅助英文翻译预览现已提供，尚待英语母语者校正。

## 本地构建

需要Python 3，无第三方依赖：

```sh
python3 scripts/build.py
python3 scripts/check.py
```

构建按`book.json`顺序合并正文、版权与来源说明，生成`dist/reader-manuscript.md`及文件校验清单。检查覆盖编号、章节存在、链接、明显占位符和清单哈希，不替代内容审阅。本版不含PDF或EPUB。

## 英文翻译预览

- [完整英文译稿](translations/en/book.md)
- [英文目录、来源与纠错说明](translations/en/README.md)
- [英文版权说明](translations/en/COPYRIGHT.md)

英文为完整的AI辅助翻译预览，尚待英语母语者校正，未经过人类目标语审阅。作者KK的母语是中文，欢迎英语母语读者通过本仓Issues或pull request提出准确性、措辞与可读性修正。中文内容已获作者验收；原有中文正文、来源和版权范围保持不变。
