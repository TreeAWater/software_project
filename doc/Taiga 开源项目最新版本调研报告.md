# **Taiga 开源项目最新版本调研报告**

## **Taiga 项目概述**



**Taiga 是什么？** Taiga 是一个免费开源、功能强大的项目管理平台，专为初创企业和敏捷开发团队设计 [1](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=) 。它

注重简洁和可定制性，支持敏捷开发中的 **Scrum** 和 **Kanban** 方法论 [2](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=1.%20%E5%BC%80%E6%BA%90%E5%85%8D%E8%B4%B9%EF%BC%9A,%EF%BC%8C%E5%AE%9E%E7%8E%B0%E4%BB%A3%E7%A0%81%E6%8F%90%E4%BA%A4%E5%92%8C%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E7%9A%84%E5%AE%9E%E6%97%B6%E5%90%8C%E6%AD%A5%E3%80%82%207.%20%E6%9D%83%E9%99%90%E5%92%8C%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86%EF%BC%9A%E5%85%81%E8%AE%B8%E7%94%A8%E6%88%B7%E6%A0%B9%E6%8D%AE%E8%A7%92%E8%89%B2%E8%AE%BE%E7%BD%AE%E4%B8%8D%E5%90%8C%E7%9A%84%E6%9D%83%E9%99%90%EF%BC%8C%E4%BB%A5%E6%8E%A7%E5%88%B6%E5%AF%B9%E9%A1%B9%E7%9B%AE%E5%92%8C%E4%BB%BB%E5%8A%A1%E7%9A%84%E8%AE%BF%E9%97%AE%E3%80%82%208.%20%E9%80%9A%E7%9F%A5%E7%B3%BB%E7%BB%9F%EF%BC%9A%E9%80%9A%E8%BF%87%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6%E6%88%96%E5%BA%94%E7%94%A8%E5%86%85%E9%80%9A%E7%9F%A5%E8%AE%A9%E7%94%A8%E6%88%B7%E4%BA%86%E8%A7%A3%E9%87%8D%E8%A6%81%E7%9A%84%E6%9B%B4%E6%96%B0%E5%92%8C%E5%8F%98%E6%9B%B4%E3%80%82) 。Taiga 提供了丰富的项目管理功能，

核心功能包括直观的看板、待办事项列表、Wiki 知识库和问题跟踪等 [3](https://segmentfault.com/a/1190000047025465#:~:text=Taiga%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7%E6%8F%90%E4%BE%9B%E4%BA%86%E4%B8%80%E7%B3%BB%E5%88%97%E5%8A%9F%E8%83%BD%EF%BC%8C%E6%97%A8%E5%9C%A8%E7%AE%80%E5%8C%96%E9%A1%B9%E7%9B%AE%E6%B5%81%E7%A8%8B%EF%BC%8C%E6%8F%90%E9%AB%98%E5%9B%A2%E9%98%9F%E5%8D%8F%E4%BD%9C%E6%95%88%E7%8E%87%E3%80%82%E5%85%B6%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD%E5%8C%85%E6%8B%AC%E7%9C%8B%E6%9D%BF%E3%80%81%E5%BE%85%E5%8A%9E%E4%BA%8B%E9%A1%B9%E3%80%81Wiki%E3%80%81%E9%97%AE%E9%A2%98%E8%B7%9F%E8%B8%AA%E7%AD%89%E3%80%82%E7%9C%8B%E6%9D%BF%E5%8A%9F%E8%83%BD%E5%85%81%E8%AE%B8%E5%9B%A2%E9%98%9F%E5%8F%AF%E8%A7%86%E5%8C%96%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B%EF%BC%8C%20%E7%9B%B4%E8%A7%82%E5%9C%B0%E4%BA%86%E8%A7%A3%E4%BB%BB%E5%8A%A1%E8%BF%9B%E5%BA%A6%E3%80%82%E5%BE%85%E5%8A%9E%E4%BA%8B%E9%A1%B9%E5%8A%9F%E8%83%BD%E5%B8%AE%E5%8A%A9%E5%9B%A2%E9%98%9F%E6%88%90%E5%91%98%E6%B8%85%E6%99%B0%E5%9C%B0%E4%BA%86%E8%A7%A3%E8%87%AA%E5%B7%B1%E7%9A%84%E4%BB%BB%E5%8A%A1%E5%92%8C%E4%BC%98%E5%85%88%E7%BA%A7%E3%80%82Wiki%E5%8A%9F%E8%83%BD%E4%B8%BA%E9%A1%B9%E7%9B%AE%E7%9F%A5%E8%AF%86%E7%AE%A1%E7%90%86%E6%8F%90%E4%BE%9B%E4%BA%86%E4%B8%80%E4%B8%AA%E9%9B%86%E4%B8%AD%E7%9A%84%E5%B9%B3%E5%8F%B0%EF%BC%8C%E8%80%8C%E9%97%AE%E9%A2%98%E8%B7%9F%E8%B8%AA%E5%8A%9F%E8%83%BD%E5%88%99%E7%A1%AE%E4%BF%9D%E5%9B%A2%E9%98%9F%E8%83%BD%E5%A4%9F%E5%8F%8A%E6%97%B6%E5%8F%91%E7%8E%B0%E5%B9%B6%20%E8%A7%A3%E5%86%B3%E9%A1%B9%E7%9B%AE%E4%B8%AD%E7%9A%84%E9%97%AE%E9%A2%98%E3%80%82) 。通过这些功能，团队可以轻松规划


冲刺和任务，跟踪项目进度，并实现团队协作与知识共享。例如，Taiga 内置的看板功能让团队以看板方式管理
任务状态，Wiki 模块用于文档协作，问题跟踪模块则用于记录和处理缺陷或工作项 [3](https://segmentfault.com/a/1190000047025465#:~:text=Taiga%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7%E6%8F%90%E4%BE%9B%E4%BA%86%E4%B8%80%E7%B3%BB%E5%88%97%E5%8A%9F%E8%83%BD%EF%BC%8C%E6%97%A8%E5%9C%A8%E7%AE%80%E5%8C%96%E9%A1%B9%E7%9B%AE%E6%B5%81%E7%A8%8B%EF%BC%8C%E6%8F%90%E9%AB%98%E5%9B%A2%E9%98%9F%E5%8D%8F%E4%BD%9C%E6%95%88%E7%8E%87%E3%80%82%E5%85%B6%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD%E5%8C%85%E6%8B%AC%E7%9C%8B%E6%9D%BF%E3%80%81%E5%BE%85%E5%8A%9E%E4%BA%8B%E9%A1%B9%E3%80%81Wiki%E3%80%81%E9%97%AE%E9%A2%98%E8%B7%9F%E8%B8%AA%E7%AD%89%E3%80%82%E7%9C%8B%E6%9D%BF%E5%8A%9F%E8%83%BD%E5%85%81%E8%AE%B8%E5%9B%A2%E9%98%9F%E5%8F%AF%E8%A7%86%E5%8C%96%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B%EF%BC%8C%20%E7%9B%B4%E8%A7%82%E5%9C%B0%E4%BA%86%E8%A7%A3%E4%BB%BB%E5%8A%A1%E8%BF%9B%E5%BA%A6%E3%80%82%E5%BE%85%E5%8A%9E%E4%BA%8B%E9%A1%B9%E5%8A%9F%E8%83%BD%E5%B8%AE%E5%8A%A9%E5%9B%A2%E9%98%9F%E6%88%90%E5%91%98%E6%B8%85%E6%99%B0%E5%9C%B0%E4%BA%86%E8%A7%A3%E8%87%AA%E5%B7%B1%E7%9A%84%E4%BB%BB%E5%8A%A1%E5%92%8C%E4%BC%98%E5%85%88%E7%BA%A7%E3%80%82Wiki%E5%8A%9F%E8%83%BD%E4%B8%BA%E9%A1%B9%E7%9B%AE%E7%9F%A5%E8%AF%86%E7%AE%A1%E7%90%86%E6%8F%90%E4%BE%9B%E4%BA%86%E4%B8%80%E4%B8%AA%E9%9B%86%E4%B8%AD%E7%9A%84%E5%B9%B3%E5%8F%B0%EF%BC%8C%E8%80%8C%E9%97%AE%E9%A2%98%E8%B7%9F%E8%B8%AA%E5%8A%9F%E8%83%BD%E5%88%99%E7%A1%AE%E4%BF%9D%E5%9B%A2%E9%98%9F%E8%83%BD%E5%A4%9F%E5%8F%8A%E6%97%B6%E5%8F%91%E7%8E%B0%E5%B9%B6%20%E8%A7%A3%E5%86%B3%E9%A1%B9%E7%9B%AE%E4%B8%AD%E7%9A%84%E9%97%AE%E9%A2%98%E3%80%82) 。总之，Taiga 作为敏捷







项目管理工具，可帮助团队高效地协同工作、透明地跟踪项目进展，并支持与版本控制系统等外部工具集成

（如 Git 集成实现代码提交与任务状态同步，以及 Webhooks 触发自动流程） [4](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=5.%20%E7%BB%B4%E5%9F%BA%E4%B8%8E%E6%96%87%E6%A1%A3%EF%BC%9A%E5%86%85%E7%BD%AE%E7%BB%B4%E5%9F%BA%E5%8A%9F%E8%83%BD%EF%BC%8C%E6%96%B9%E4%BE%BF%E5%9B%A2%E9%98%9F%E5%85%B1%E4%BA%AB%E7%9F%A5%E8%AF%86%E5%92%8C%E7%BC%96%E5%86%99%E9%A1%B9%E7%9B%AE%E6%96%87%E6%A1%A3%E3%80%82%206.%20%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E9%9B%86%E6%88%90%EF%BC%9A%E6%97%A0%E7%BC%9D%E5%AF%B9%E6%8E%A5%20,%E5%85%81%E8%AE%B8%E4%B8%8E%E5%85%B6%E4%BB%96%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%E3%80%82%2012.%20%E5%88%86%E6%9E%90%E5%92%8C%E6%8A%A5%E5%91%8A%EF%BC%9A%E6%8F%90%E4%BE%9B%E5%AE%8C%E6%95%B4%E7%9A%84%E4%BB%AA%E8%A1%A8%E6%9D%BF%E5%92%8C%E8%BF%9B%E5%BA%A6%E6%8A%A5%E5%91%8A%E5%8A%9F%E8%83%BD%E3%80%82) 。


**Taiga 的核心用途和特点：**


  - **敏捷项目管理：** 支持 Scrum 和 Kanban 两种主要敏捷开发流程，满足不同团队的流程需求 [2](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=1.%20%E5%BC%80%E6%BA%90%E5%85%8D%E8%B4%B9%EF%BC%9A,%EF%BC%8C%E5%AE%9E%E7%8E%B0%E4%BB%A3%E7%A0%81%E6%8F%90%E4%BA%A4%E5%92%8C%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E7%9A%84%E5%AE%9E%E6%97%B6%E5%90%8C%E6%AD%A5%E3%80%82%207.%20%E6%9D%83%E9%99%90%E5%92%8C%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86%EF%BC%9A%E5%85%81%E8%AE%B8%E7%94%A8%E6%88%B7%E6%A0%B9%E6%8D%AE%E8%A7%92%E8%89%B2%E8%AE%BE%E7%BD%AE%E4%B8%8D%E5%90%8C%E7%9A%84%E6%9D%83%E9%99%90%EF%BC%8C%E4%BB%A5%E6%8E%A7%E5%88%B6%E5%AF%B9%E9%A1%B9%E7%9B%AE%E5%92%8C%E4%BB%BB%E5%8A%A1%E7%9A%84%E8%AE%BF%E9%97%AE%E3%80%82%208.%20%E9%80%9A%E7%9F%A5%E7%B3%BB%E7%BB%9F%EF%BC%9A%E9%80%9A%E8%BF%87%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6%E6%88%96%E5%BA%94%E7%94%A8%E5%86%85%E9%80%9A%E7%9F%A5%E8%AE%A9%E7%94%A8%E6%88%B7%E4%BA%86%E8%A7%A3%E9%87%8D%E8%A6%81%E7%9A%84%E6%9B%B4%E6%96%B0%E5%92%8C%E5%8F%98%E6%9B%B4%E3%80%82) 。用户











可以使用待办列表规划产品 backlog，用迭代（冲刺）管理短期任务。
**任务与缺陷跟踪：** 提供任务卡片来跟踪每个工作项的状态、优先级、标签等；内置缺陷/问题跟踪系

统，确保团队及时发现并解决项目问题 [5](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=3.%20%E6%95%8F%E6%8D%B7%E7%AE%A1%E7%90%86%EF%BC%9A%E6%94%AF%E6%8C%81%20,%E6%8F%90%E4%BE%9B%E5%A4%9A%E7%A7%8D%E8%AF%AD%E8%A8%80%EF%BC%8C%E6%BB%A1%E8%B6%B3%E5%85%A8%E7%90%83%E5%8C%96%E5%9B%A2%E9%98%9F%E7%9A%84%E9%9C%80%E6%B1%82%E3%80%82) 。


**知识共享与文档：** 内置 Wiki 和文档模块，方便团队编写项目说明、需求文档和知识库，集中管理项目

相关知识 [6](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=3.%20%E6%95%8F%E6%8D%B7%E7%AE%A1%E7%90%86%EF%BC%9A%E6%94%AF%E6%8C%81%20,%EF%BC%8C%E5%AE%9E%E7%8E%B0%E4%BB%A3%E7%A0%81%E6%8F%90%E4%BA%A4%E5%92%8C%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E7%9A%84%E5%AE%9E%E6%97%B6%E5%90%8C%E6%AD%A5%E3%80%82) 。


**角色权限与通知：** 支持自定义用户角色和权限控制，不同角色可访问不同范围的项目内容；提供邮件及

系统内通知功能，及时提醒相关成员关注项目更新 [7](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=7,%E6%8F%90%E4%BE%9B%E5%A4%9A%E7%A7%8D%E8%AF%AD%E8%A8%80%EF%BC%8C%E6%BB%A1%E8%B6%B3%E5%85%A8%E7%90%83%E5%8C%96%E5%9B%A2%E9%98%9F%E7%9A%84%E9%9C%80%E6%B1%82%E3%80%82) 。




  - **扩展与集成：** 拥有开放的 REST API，可与其他工具集成 [8](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=9.%20%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E4%BD%9C%E6%B5%81%EF%BC%9A%E9%80%9A%E8%BF%87%E8%87%AA%E5%AE%9A%E4%B9%89%E8%A7%84%E5%88%99%E5%92%8C%20,%E5%85%81%E8%AE%B8%E4%B8%8E%E5%85%B6%E4%BB%96%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%E3%80%82%2012.%20%E5%88%86%E6%9E%90%E5%92%8C%E6%8A%A5%E5%91%8A%EF%BC%9A%E6%8F%90%E4%BE%9B%E5%AE%8C%E6%95%B4%E7%9A%84%E4%BB%AA%E8%A1%A8%E6%9D%BF%E5%92%8C%E8%BF%9B%E5%BA%A6%E6%8A%A5%E5%91%8A%E5%8A%9F%E8%83%BD%E3%80%82) ；支持 Git 等版本控制系统无缝集成，提交


代码可自动关联任务状态 [9](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=5.%20%E7%BB%B4%E5%9F%BA%E4%B8%8E%E6%96%87%E6%A1%A3%EF%BC%9A%E5%86%85%E7%BD%AE%E7%BB%B4%E5%9F%BA%E5%8A%9F%E8%83%BD%EF%BC%8C%E6%96%B9%E4%BE%BF%E5%9B%A2%E9%98%9F%E5%85%B1%E4%BA%AB%E7%9F%A5%E8%AF%86%E5%92%8C%E7%BC%96%E5%86%99%E9%A1%B9%E7%9B%AE%E6%96%87%E6%A1%A3%E3%80%82%206.%20%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E9%9B%86%E6%88%90%EF%BC%9A%E6%97%A0%E7%BC%9D%E5%AF%B9%E6%8E%A5%20,%E5%85%81%E8%AE%B8%E4%B8%8E%E5%85%B6%E4%BB%96%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%E3%80%82%2012.%20%E5%88%86%E6%9E%90%E5%92%8C%E6%8A%A5%E5%91%8A%EF%BC%9A%E6%8F%90%E4%BE%9B%E5%AE%8C%E6%95%B4%E7%9A%84%E4%BB%AA%E8%A1%A8%E6%9D%BF%E5%92%8C%E8%BF%9B%E5%BA%A6%E6%8A%A5%E5%91%8A%E5%8A%9F%E8%83%BD%E3%80%82) ；支持 Webhooks，用于触发自动化工作流程 [7](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=7,%E6%8F%90%E4%BE%9B%E5%A4%9A%E7%A7%8D%E8%AF%AD%E8%A8%80%EF%BC%8C%E6%BB%A1%E8%B6%B3%E5%85%A8%E7%90%83%E5%8C%96%E5%9B%A2%E9%98%9F%E7%9A%84%E9%9C%80%E6%B1%82%E3%80%82) 。


以上特点使得 Taiga 成为中小型团队理想的项目管理方案，兼具 **易用的界面** 和 **灵活的定制性** ，能够满足团队在
敏捷开发过程中的协作和管理需求 [1](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=) 。

## **Taiga 最新版本的主要仓库和模块**


最新版本的 Taiga 平台由多个独立的模块组成，每个模块对应一个 GitHub 仓库 [10](https://docs.taiga.io/setup-development.html#:~:text=The%20Taiga%20platform%20consists%20of,three%20main%20components) 。这些模块分工明确，通过

API 调用、消息队列和共享配置等方式协同工作，共同构成完整的 Taiga 平台。下表概述了 Taiga 核心仓库的功
能定位，以及它们之间的依赖关系和交互逻辑：


1


2


3


**表：Taiga 核心 GitHub 仓库及其功能、交互概览（基于最新版本）。**



上表列出了 Taiga 平台的主要组成模块和对应的 GitHub 代码仓库，以及它们的职责和相互关系。其中 taigaback、taiga-front(-dist) 和 taiga-events 是 **Taiga 平台的核心三大组件** [11](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=,RabbitMQ%20as%20the%20message%20broker) ；taiga-protected 和异步任务

(taiga-async) 则属于可选的附加组件，用于增强附件安全和提高性能等 [24](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=Aditionally%2C%20you%20also%20have%20two,other%20optional%20modules) 。taiga-docker 则是官方提供的容

器化部署方案仓库，方便用户将上述组件快速部署在 Docker 环境中。下面将对这些仓库之间的依赖关系和交互

原理作进一步说明。

## **仓库之间的依赖关系与架构原理**


Taiga 采用前后端分离的模块化架构，各组件通过明确的接口进行通信，整体架构如下：











**前后端通信：** Taiga 的 Web 前端（taiga-front 或 taiga-front-dist）通过调用后端 API 来实现大部分功
能。用户在界面上的操作（如创建用户故事、修改任务状态等）会以 REST 请求形式发送到 **taiga-**
**back** ，后端处理业务逻辑和数据库读写，然后返回结果给前端 [11](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=,RabbitMQ%20as%20the%20message%20broker) 。这种松耦合的 API 通信使前后端可


以独立开发和部署。




- **实时更新机制：** 为了在多人协作时提供实时反馈，Taiga 引入了 **taiga-events** WebSocket 服务 [13](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=%3E%20%20%20%2A%20taiga,RabbitMQ%20as%20the%20message%20broker) 。

当后端数据发生变更时（例如某人完成了一项任务）， **taiga-back** 会向 RabbitMQ 发布一条事件消息

[13](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=%3E%20%20%20%2A%20taiga,RabbitMQ%20as%20the%20message%20broker) 。 **taiga-events** 作为订阅者捕获到该消息后，通过 WebSocket 将更新推送给所有连接的前端客户

端，使他们的界面 **实时刷新** 相应的内容 [13](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=%3E%20%20%20%2A%20taiga,RabbitMQ%20as%20the%20message%20broker) 。例如，在任务看板上，一位用户拖动卡片改变了任务状


态，其他用户的看板上几乎瞬时就会反映出该变化。RabbitMQ 在此承担了解耦发布/订阅的角色，而
taiga-events 则是后端和前端之间的 **实时消息桥梁** 。











**异步任务处理：taiga-back** 默认情况下同步执行所有操作，但对于发送邮件、导入导出等耗时任务，
可以启用 Taiga 的异步处理模式（即 **taiga-async** ） [12](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=%2A%20taiga,the%20attachments%20from%20external%20downloads) 。在该模式下，Taiga 后端会将耗时工作投递到

RabbitMQ 队列，由独立的 Celery Worker 进程消费执行 [12](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=%2A%20taiga,the%20attachments%20from%20external%20downloads) 。这个 Celery Worker 可以理解为 taiga
back 代码的另一个运行实例，专门用于执行异步任务（通常通过 Docker Compose 定义为一个独立服
务，如 taiga-async 服务使用 taiga-back 镜像启动 Celery）。这样可以避免阻塞主应用，提高系统吞
吐量。不过值得注意的是， **taiga-async** 并没有独立的代码仓库，其逻辑实现包含在 taiga-back 中，只
是通过配置决定是否以异步模式运行而已 [12](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=%2A%20taiga,the%20attachments%20from%20external%20downloads) 。RabbitMQ 同时被 taiga-events 和 taiga-async 利用，

分别服务于实时通知和异步任务两个机制。


**附件保护机制：** 对于私有项目中的附件文件，Taiga 提供了可选的 **taiga-protected** 模块进行保护

[14](https://github.com/taigaio/taiga-protected#:~:text=Taiga%20Protected%20is%20a%20service,from%20a%20specific%20Nginx%20configuration) 。在没有 taiga-protected 时，附件通常由后端直接提供，或者通过静态服务器开放，这可能导致未

经授权的访问。引入 taiga-protected 后，Taiga 后端会对附件 URL 进行签名，只有携带有效令牌的请
求才能通过 Nginx 获取实际文件 [14](https://github.com/taigaio/taiga-protected#:~:text=Taiga%20Protected%20is%20a%20service,from%20a%20specific%20Nginx%20configuration) 。部署时，Nginx（taiga-gateway）配置了一个内部路径（例如 /

protected ）由 taiga-protected 服务处理 [25](https://github.com/taigaio/taiga-protected#:~:text=specific%20Nginx%20configuration) 。当用户尝试下载某附件时，如果该附件受保护，前端会

请求一个含签名的下载链接；浏览器据此向 Nginx 发起下载，Nginx 将请求转给 taiga-protected 验证
令牌 [14](https://github.com/taigaio/taiga-protected#:~:text=Taiga%20Protected%20is%20a%20service,from%20a%20specific%20Nginx%20configuration) 。验证通过后，Nginx 才从存储卷中读取实际文件（或通过后端提供文件）返回给用户，否则

拒绝访问。令牌通常设置短期限（例如几分钟），过期后需重新请求，以确保附件链接无法长期传播

[26](https://docs.taiga.io/setup-production.html#:~:text=This%20section%20describes%20the%20installation,the%20attachments%20from%20external%20downloads) 。这一机制确保了 **附件资源只能被授权用户访问** ，强化了 Taiga 在安全性方面的能力。


**统一网关与部署：** 在生产部署中，通常使用 Nginx 作为前端网关服务器，它通过反向代理将请求分别导
向不同的 Taiga 服务。Taiga 官方的 Docker 部署( **taiga-docker** )仓库提供了示例 Nginx 配置



taiga.conf [19](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=taiga) 。根据该配置，Nginx 将： / 根路径下的请求交给前端容器（taiga-front-dist）处理





静态页面，【 /api 】前缀的请求转发给 taiga-back 容器的 API，【 /events 】路径升级为
WebSocket 并代理到 taiga-events，【 /media 】和【 /static 】等静态资源路径映射到后端或静态
卷（部分受 taiga-protected 控制） [21](https://www.liangz.org/1143.html#:~:text=,Scheme%20%24scheme%3B) 。这种架构下，Nginx 扮演了 **集中入口** 的角色，客户端只需要访

问 Nginx 的域名和端口即可使用 Taiga 的全部功能，由 Nginx 来协调后端各服务。taiga-docker 则利用


4


Docker Compose 将上述所有组件和依赖服务（数据库 Postgres、消息队列 RabbitMQ、缓存 Redis
等）定义在一起，一次性部署。根据官方文档说明，一个标准的 Taiga 部署包含上述 **taiga-back、**
**taiga-front-dist、taiga-events、taiga-async 和 taiga-protected** 等多个模块，它们既可以部署在
同一台机器上，也可以分布部署 [27](https://docs.taiga.io/setup-production.html#:~:text=%2A%20taiga) 。使用 taiga-docker 则默认将它们部署为相互连接的容器，以简化

搭建流程 [23](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=%60Taiga%60%20%E7%94%A8%E5%88%B0%20%609%60%20%E4%B8%AA%E9%95%9C%E5%83%8F%EF%BC%8C%E9%87%87%E7%94%A8%20%60docker,%E5%AE%89%E8%A3%85%E6%96%B9%E5%BC%8F%EF%BC%8C%E9%9C%80%E8%A6%81%E5%87%86%E5%A4%87%E5%A5%BD%E4%B8%89%E4%B8%AA%E6%96%87%E4%BB%B6) 。


综上，Taiga 的架构体现了典型的 **前后端分离 + 异步消息 + 微服务** 设计思想。各仓库模块通过明确的接口
（HTTP API、WebSocket、消息队列、共享配置等）集成，实现了 **功能解耦** 和 **水平扩展** ：前端界面与后端逻辑

解耦，实时通知与主流程解耦，附件服务独立，部署上也可按需拆分。这使得 Taiga 在保证丰富功能的同时，
仍能保持较好的可维护性和扩展性。

## **官方文档与架构资料**


关于 Taiga 各组件和仓库关系的更多信息，可以参考官方提供的文档和社区资源：











**官方文档：** Taiga 官方文档的安装和开发指南部分对平台架构有基本说明。例如，开发环境设置指南中
指出 _“Taiga 平台由三个主要组件组成：taiga-back（后端API）、taiga-front（前端）和 taiga-events_
_（WebSocket 实时网关）”_ ，并提到 taiga-events 是可选组件 [10](https://docs.taiga.io/setup-development.html#:~:text=The%20Taiga%20platform%20consists%20of,three%20main%20components) 。生产部署文档则进一步列出了标准

Taiga 平台包括 taiga-front-dist 前端发布版、taiga-async 异步任务和 taiga-protected 附件保护等模块

[27](https://docs.taiga.io/setup-production.html#:~:text=%2A%20taiga) 。这些官方文档有助于理解各仓库模块的职责划分和部署拓扑。


**架构示意与讨论：** 在 Taiga 社区论坛，有开发团队成员对 Taiga 的架构进行了总结说明。例如，有帖子

引用了上述官方文档内容，并补充说明了 taiga-async 和 taiga-protected 等可选模块的作用 [24](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=Aditionally%2C%20you%20also%20have%20two,other%20optional%20modules) 。这些

讨论提及了 Taiga 技术栈（Django、AngularJS、RabbitMQ、Celery等）以及各部分协同工作的方
式，对理解仓库之间的交互很有帮助。


**仓库自述文件：** 大部分 Taiga 仓库（如 taiga-back、taiga-front、taiga-events 等）的 README 中也
提供了简要的介绍和指向更详尽文档的链接。例如，taiga-back 和 taiga-front 的 README 提供了文档
网址和社区支持链接 [28](https://github.com/taigaio/taiga-back#:~:text=Documentation) [29](https://github.com/taigaio/taiga-front-dist#:~:text=Documentation) 。taiga-front-dist、taiga-events、taiga-protected 等仓库的 README 冒

头通常有提示，指向官方博客公告（如 Taiga 未来规划）以及相关文档 [18](https://github.com/taigaio/taiga-front-dist#:~:text=Taiga%20Front%20Dist) [30](https://github.com/taigaio/taiga-protected#:~:text=Taiga%20Protected) 。阅读这些说明有助于

快速了解仓库用途，以及获取进一步配置指导（例如 taiga-protected README 提供了插件安装和
Nginx 配置的文档链接 [14](https://github.com/taigaio/taiga-protected#:~:text=Taiga%20Protected%20is%20a%20service,from%20a%20specific%20Nginx%20configuration) ）。


**资料链接：** 如果需要，可参阅 Taiga 官方文档站点的 [安装部署指南](https://docs.taiga.io/setup-production.html) 和 [开发者指南，以及 Taiga](https://docs.taiga.io/setup-development.html)
社区的相关讨论帖获取更深入的架构说明 [27](https://docs.taiga.io/setup-production.html#:~:text=%2A%20taiga) [24](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=Aditionally%2C%20you%20also%20have%20two,other%20optional%20modules) 。上述资源详细阐述了各模块的安装配置和作


用原理，对本次调研内容提供了权威参考。


5


[1](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=) [2](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=1.%20%E5%BC%80%E6%BA%90%E5%85%8D%E8%B4%B9%EF%BC%9A,%EF%BC%8C%E5%AE%9E%E7%8E%B0%E4%BB%A3%E7%A0%81%E6%8F%90%E4%BA%A4%E5%92%8C%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E7%9A%84%E5%AE%9E%E6%97%B6%E5%90%8C%E6%AD%A5%E3%80%82%207.%20%E6%9D%83%E9%99%90%E5%92%8C%E8%A7%92%E8%89%B2%E7%AE%A1%E7%90%86%EF%BC%9A%E5%85%81%E8%AE%B8%E7%94%A8%E6%88%B7%E6%A0%B9%E6%8D%AE%E8%A7%92%E8%89%B2%E8%AE%BE%E7%BD%AE%E4%B8%8D%E5%90%8C%E7%9A%84%E6%9D%83%E9%99%90%EF%BC%8C%E4%BB%A5%E6%8E%A7%E5%88%B6%E5%AF%B9%E9%A1%B9%E7%9B%AE%E5%92%8C%E4%BB%BB%E5%8A%A1%E7%9A%84%E8%AE%BF%E9%97%AE%E3%80%82%208.%20%E9%80%9A%E7%9F%A5%E7%B3%BB%E7%BB%9F%EF%BC%9A%E9%80%9A%E8%BF%87%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6%E6%88%96%E5%BA%94%E7%94%A8%E5%86%85%E9%80%9A%E7%9F%A5%E8%AE%A9%E7%94%A8%E6%88%B7%E4%BA%86%E8%A7%A3%E9%87%8D%E8%A6%81%E7%9A%84%E6%9B%B4%E6%96%B0%E5%92%8C%E5%8F%98%E6%9B%B4%E3%80%82) [4](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=5.%20%E7%BB%B4%E5%9F%BA%E4%B8%8E%E6%96%87%E6%A1%A3%EF%BC%9A%E5%86%85%E7%BD%AE%E7%BB%B4%E5%9F%BA%E5%8A%9F%E8%83%BD%EF%BC%8C%E6%96%B9%E4%BE%BF%E5%9B%A2%E9%98%9F%E5%85%B1%E4%BA%AB%E7%9F%A5%E8%AF%86%E5%92%8C%E7%BC%96%E5%86%99%E9%A1%B9%E7%9B%AE%E6%96%87%E6%A1%A3%E3%80%82%206.%20%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E9%9B%86%E6%88%90%EF%BC%9A%E6%97%A0%E7%BC%9D%E5%AF%B9%E6%8E%A5%20,%E5%85%81%E8%AE%B8%E4%B8%8E%E5%85%B6%E4%BB%96%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%E3%80%82%2012.%20%E5%88%86%E6%9E%90%E5%92%8C%E6%8A%A5%E5%91%8A%EF%BC%9A%E6%8F%90%E4%BE%9B%E5%AE%8C%E6%95%B4%E7%9A%84%E4%BB%AA%E8%A1%A8%E6%9D%BF%E5%92%8C%E8%BF%9B%E5%BA%A6%E6%8A%A5%E5%91%8A%E5%8A%9F%E8%83%BD%E3%80%82) [5](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=3.%20%E6%95%8F%E6%8D%B7%E7%AE%A1%E7%90%86%EF%BC%9A%E6%94%AF%E6%8C%81%20,%E6%8F%90%E4%BE%9B%E5%A4%9A%E7%A7%8D%E8%AF%AD%E8%A8%80%EF%BC%8C%E6%BB%A1%E8%B6%B3%E5%85%A8%E7%90%83%E5%8C%96%E5%9B%A2%E9%98%9F%E7%9A%84%E9%9C%80%E6%B1%82%E3%80%82) [6](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=3.%20%E6%95%8F%E6%8D%B7%E7%AE%A1%E7%90%86%EF%BC%9A%E6%94%AF%E6%8C%81%20,%EF%BC%8C%E5%AE%9E%E7%8E%B0%E4%BB%A3%E7%A0%81%E6%8F%90%E4%BA%A4%E5%92%8C%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E7%9A%84%E5%AE%9E%E6%97%B6%E5%90%8C%E6%AD%A5%E3%80%82) [7](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=7,%E6%8F%90%E4%BE%9B%E5%A4%9A%E7%A7%8D%E8%AF%AD%E8%A8%80%EF%BC%8C%E6%BB%A1%E8%B6%B3%E5%85%A8%E7%90%83%E5%8C%96%E5%9B%A2%E9%98%9F%E7%9A%84%E9%9C%80%E6%B1%82%E3%80%82) [8](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=9.%20%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E4%BD%9C%E6%B5%81%EF%BC%9A%E9%80%9A%E8%BF%87%E8%87%AA%E5%AE%9A%E4%B9%89%E8%A7%84%E5%88%99%E5%92%8C%20,%E5%85%81%E8%AE%B8%E4%B8%8E%E5%85%B6%E4%BB%96%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%E3%80%82%2012.%20%E5%88%86%E6%9E%90%E5%92%8C%E6%8A%A5%E5%91%8A%EF%BC%9A%E6%8F%90%E4%BE%9B%E5%AE%8C%E6%95%B4%E7%9A%84%E4%BB%AA%E8%A1%A8%E6%9D%BF%E5%92%8C%E8%BF%9B%E5%BA%A6%E6%8A%A5%E5%91%8A%E5%8A%9F%E8%83%BD%E3%80%82) [9](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=5.%20%E7%BB%B4%E5%9F%BA%E4%B8%8E%E6%96%87%E6%A1%A3%EF%BC%9A%E5%86%85%E7%BD%AE%E7%BB%B4%E5%9F%BA%E5%8A%9F%E8%83%BD%EF%BC%8C%E6%96%B9%E4%BE%BF%E5%9B%A2%E9%98%9F%E5%85%B1%E4%BA%AB%E7%9F%A5%E8%AF%86%E5%92%8C%E7%BC%96%E5%86%99%E9%A1%B9%E7%9B%AE%E6%96%87%E6%A1%A3%E3%80%82%206.%20%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6%E9%9B%86%E6%88%90%EF%BC%9A%E6%97%A0%E7%BC%9D%E5%AF%B9%E6%8E%A5%20,%E5%85%81%E8%AE%B8%E4%B8%8E%E5%85%B6%E4%BB%96%E7%B3%BB%E7%BB%9F%E9%9B%86%E6%88%90%E3%80%82%2012.%20%E5%88%86%E6%9E%90%E5%92%8C%E6%8A%A5%E5%91%8A%EF%BC%9A%E6%8F%90%E4%BE%9B%E5%AE%8C%E6%95%B4%E7%9A%84%E4%BB%AA%E8%A1%A8%E6%9D%BF%E5%92%8C%E8%BF%9B%E5%BA%A6%E6%8A%A5%E5%91%8A%E5%8A%9F%E8%83%BD%E3%80%82) [19](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=taiga) [23](https://blog.csdn.net/wbsu2004/article/details/141642374#:~:text=%60Taiga%60%20%E7%94%A8%E5%88%B0%20%609%60%20%E4%B8%AA%E9%95%9C%E5%83%8F%EF%BC%8C%E9%87%87%E7%94%A8%20%60docker,%E5%AE%89%E8%A3%85%E6%96%B9%E5%BC%8F%EF%BC%8C%E9%9C%80%E8%A6%81%E5%87%86%E5%A4%87%E5%A5%BD%E4%B8%89%E4%B8%AA%E6%96%87%E4%BB%B6)



开源项目管理工具Taiga-CSDN博客



[https://blog.csdn.net/wbsu2004/article/details/141642374](https://blog.csdn.net/wbsu2004/article/details/141642374)



[3](https://segmentfault.com/a/1190000047025465#:~:text=Taiga%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7%E6%8F%90%E4%BE%9B%E4%BA%86%E4%B8%80%E7%B3%BB%E5%88%97%E5%8A%9F%E8%83%BD%EF%BC%8C%E6%97%A8%E5%9C%A8%E7%AE%80%E5%8C%96%E9%A1%B9%E7%9B%AE%E6%B5%81%E7%A8%8B%EF%BC%8C%E6%8F%90%E9%AB%98%E5%9B%A2%E9%98%9F%E5%8D%8F%E4%BD%9C%E6%95%88%E7%8E%87%E3%80%82%E5%85%B6%E6%A0%B8%E5%BF%83%E5%8A%9F%E8%83%BD%E5%8C%85%E6%8B%AC%E7%9C%8B%E6%9D%BF%E3%80%81%E5%BE%85%E5%8A%9E%E4%BA%8B%E9%A1%B9%E3%80%81Wiki%E3%80%81%E9%97%AE%E9%A2%98%E8%B7%9F%E8%B8%AA%E7%AD%89%E3%80%82%E7%9C%8B%E6%9D%BF%E5%8A%9F%E8%83%BD%E5%85%81%E8%AE%B8%E5%9B%A2%E9%98%9F%E5%8F%AF%E8%A7%86%E5%8C%96%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B%EF%BC%8C%20%E7%9B%B4%E8%A7%82%E5%9C%B0%E4%BA%86%E8%A7%A3%E4%BB%BB%E5%8A%A1%E8%BF%9B%E5%BA%A6%E3%80%82%E5%BE%85%E5%8A%9E%E4%BA%8B%E9%A1%B9%E5%8A%9F%E8%83%BD%E5%B8%AE%E5%8A%A9%E5%9B%A2%E9%98%9F%E6%88%90%E5%91%98%E6%B8%85%E6%99%B0%E5%9C%B0%E4%BA%86%E8%A7%A3%E8%87%AA%E5%B7%B1%E7%9A%84%E4%BB%BB%E5%8A%A1%E5%92%8C%E4%BC%98%E5%85%88%E7%BA%A7%E3%80%82Wiki%E5%8A%9F%E8%83%BD%E4%B8%BA%E9%A1%B9%E7%9B%AE%E7%9F%A5%E8%AF%86%E7%AE%A1%E7%90%86%E6%8F%90%E4%BE%9B%E4%BA%86%E4%B8%80%E4%B8%AA%E9%9B%86%E4%B8%AD%E7%9A%84%E5%B9%B3%E5%8F%B0%EF%BC%8C%E8%80%8C%E9%97%AE%E9%A2%98%E8%B7%9F%E8%B8%AA%E5%8A%9F%E8%83%BD%E5%88%99%E7%A1%AE%E4%BF%9D%E5%9B%A2%E9%98%9F%E8%83%BD%E5%A4%9F%E5%8F%8A%E6%97%B6%E5%8F%91%E7%8E%B0%E5%B9%B6%20%E8%A7%A3%E5%86%B3%E9%A1%B9%E7%9B%AE%E4%B8%AD%E7%9A%84%E9%97%AE%E9%A2%98%E3%80%82)



如何利用Taiga项目管理工具提升团队效率？5个实用技巧分享 - 老杨的PM手记 - SegmentFault 思否



[https://segmentfault.com/a/1190000047025465](https://segmentfault.com/a/1190000047025465)



[10](https://docs.taiga.io/setup-development.html#:~:text=The%20Taiga%20platform%20consists%20of,three%20main%20components)



Taiga: Setup development environment



[https://docs.taiga.io/setup-development.html](https://docs.taiga.io/setup-development.html)



[11](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=,RabbitMQ%20as%20the%20message%20broker) [12](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=%2A%20taiga,the%20attachments%20from%20external%20downloads) [13](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=%3E%20%20%20%2A%20taiga,RabbitMQ%20as%20the%20message%20broker) [15](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=endpoints,in%20the%20backlog%2C%20taskboard%2C%20kanban) [24](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358#:~:text=Aditionally%2C%20you%20also%20have%20two,other%20optional%20modules)



What technologies are being used in Taiga? - Self hosted Taiga - Taiga Community



[https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358](https://community.taiga.io/t/what-technologies-are-being-used-in-taiga/2358)



[14](https://github.com/taigaio/taiga-protected#:~:text=Taiga%20Protected%20is%20a%20service,from%20a%20specific%20Nginx%20configuration) [22](https://github.com/taigaio/taiga-protected#:~:text=The%20server%20has%202%20configuration,options) [25](https://github.com/taigaio/taiga-protected#:~:text=specific%20Nginx%20configuration) [30](https://github.com/taigaio/taiga-protected#:~:text=Taiga%20Protected)



GitHub - taigaio/taiga-protected



[https://github.com/taigaio/taiga-protected](https://github.com/taigaio/taiga-protected)



[16](https://www.howtoforge.com/tutorial/how-to-install-and-configure-taigaio-on-centos-7/#:~:text=1.%20Taiga,time%20changes%20in%20the%20apps)



How to Install Taiga.io Project Management Software on CentOS 7



[https://www.howtoforge.com/tutorial/how-to-install-and-configure-taigaio-on-centos-7/](https://www.howtoforge.com/tutorial/how-to-install-and-configure-taigaio-on-centos-7/)



[17](https://docs.taiga.io/setup-production.html#:~:text=,%28see%20examples%20below) [26](https://docs.taiga.io/setup-production.html#:~:text=This%20section%20describes%20the%20installation,the%20attachments%20from%20external%20downloads) [27](https://docs.taiga.io/setup-production.html#:~:text=%2A%20taiga)



Install Taiga in Production



[https://docs.taiga.io/setup-production.html](https://docs.taiga.io/setup-production.html)



[18](https://github.com/taigaio/taiga-front-dist#:~:text=Taiga%20Front%20Dist) [29](https://github.com/taigaio/taiga-front-dist#:~:text=Documentation)



GitHub - taigaio/taiga-front-dist



[https://github.com/taigaio/taiga-front-dist](https://github.com/taigaio/taiga-front-dist)



[20](https://www.liangz.org/1143.html#:~:text=taiga,%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2%E8%AE%BF%E9%97%AE%E3%80%81%20%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6%E6%9C%8D%E5%8A%A1%E5%92%8C%E5%AA%92%E4%BD%93%E6%96%87%E4%BB%B6%E6%9C%8D%E5%8A%A1%EF%BC%8C%20%E4%BB%A5%E5%8F%8A%20WebSocket%20%E4%BA%8B%E4%BB%B6%E9%80%9A%E4%BF%A1%E3%80%82) [21](https://www.liangz.org/1143.html#:~:text=,Scheme%20%24scheme%3B)



Synology 部署开源项目管理工具 Taiga | 飘零博客



[https://www.liangz.org/1143.html](https://www.liangz.org/1143.html)



[28](https://github.com/taigaio/taiga-back#:~:text=Documentation)



GitHub - taigaio/taiga-back



[https://github.com/taigaio/taiga-back](https://github.com/taigaio/taiga-back)



6


