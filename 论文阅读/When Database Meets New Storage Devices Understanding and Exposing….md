# When Database Meets New Storage Devices: Understanding and Exposing Performance Mismatches via Configurations

## 阅读

##### 这篇文章属于什么领域或方向？

数据库与nvms

##### 解决了什么问题？为什么这个问题这么重要？

问题：现有的数据库管理系统可能无法发挥出nvms应有的性能，但没有解决

##### 使用了什么方法和模型？为什么这个方法可以解决这个问题？

*实验设计*：控制变量是设备（nvme，SSD，HDD），在同一个DBMS上测试效果

*测试平台*：

* MySQL, PostgreSQL，SQL- ite, MariaDB, MongoDB and Redis
* YCSB and TPC

*测试方法*：

![1706020157885](image/WhenDatabaseMeetsNewStorageDevicesUnderstandingandExposing…/1706020157885.png)

生成工作负载，仅调整与io相关的knobs，通过分析运行结果得到原因。

*测试过程*：

* I/O相关旋钮确定
* 

##### 核心结论是什么？下一步还可以怎么做？

在本文中，我们发现将新的存储设备插入现有的DBMS可能会导致性能不匹配，从而对性能产生严重影响。性能不匹配很少被研究和/或检测到。为了填补这一空白，我们对性能不匹配进行全面研究，以了解其症状、根本原因和触发条件。在这项研究中，我们提出了一种利用配置来检测性能不匹配的方法。我们发现，性能不匹配可以根据其根本原因分为三种类型，我们对根本原因模式进行了深入分析。与基线方法相比，我们的方法更有效率，可以检测到更多的性能不匹配。

## 疑问

##### 如何发现性能不匹配，标准是什么，这个标准是否可否？

##### 性能不匹配产生的影响是什么，这个影响是否重要？

##### 检测方法是否合理，是否考虑全面

##### 分类是否正确
