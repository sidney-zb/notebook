## Linux相关知识点

### Red Hat

Red Hat 是一家总部位于美国的软件公司，同时也是一个提供 Linux 发行版的公司。Red Hat Linux 是一种商业化的 Linux 发行版，而 Red Hat Enterprise Linux（RHEL）是其企业级版本。RHEL 是一种基于开放源代码的操作系统，为企业提供了强大的性能、稳定性和安全性。Red Hat 还提供了开放源代码社区版的 Fedora，以及其他与 Linux 相关的解决方案和服务。

### Debian

Debian 是一种自由和开放源代码的 Linux 发行版，由志愿者社区开发。Debian 以其稳定性、可靠性和广泛的软件包管理系统而闻名。Debian 的软件包管理使用 apt（Advanced Package Tool）工具，它是一个强大的包管理器，能够轻松地管理系统上的软件包、依赖关系和升级。总的来说，Red Hat 和 Debian 都是流行的 Linux 发行版，它们分别以其特定的特性、管理工具和社区而著称。企业通常根据其需求和偏好选择使用 Red Hat Enterprise Linux（或其衍生版本，如 CentOS）或 Debian。

### 软件包管理

* Red Hat/CentOS 使用 ***yum 或 dnf***（在较新的版本中）作为默认的包管理器。例如，使用 yum install 或 dnf install 来安装软件包。
* Debian/Ubuntu 使用 apt（Advanced Package Tool）作为默认的包管理器。例如，使用 apt-get install 或 apt install 来安装软件包。

### 更新软件包列表

`sudo yum update`

`sudo apt update(apt-get update)`

* apt update：apt update 用于更新本地软件包列表，以获取最新的软件包信息和存储库信息，但不会安装新软件包或升级现有软件包。运行 apt update 会从您的软件源（包括操作系统的官方存储库以及第三方存储库）中下载最新的软件包信息，这有助于确保您获得最新的软件包列表，以便在以后执行软件包更新时使用。apt update 不会更改系统上的软件包，它只是更新可用软件包的列表。
* apt upgrade：apt upgrade 用于实际升级系统中已安装的软件包。它会查找并安装新版本的现有软件包，以确保您的系统中的软件保持最新状态。运行 apt upgrade 时，系统会检查已安装的软件包，如果有可用的更新版本，它将下载并安装这些更新版本。apt upgrade 会更改系统上的软件包，因此需要管理员权限。

### update和upgrade的区别

### 切换编译器（查看shell真实配置）

```

ls -al /bin/sh

lrwxrwxrwx 1 root root 4 8月 10 2018 /bin/sh -> dash

```

#### 切换

##### 设置为dash

`sudo ln -fs /bin/bash /bin/sh

`

##### 设置为dash

`sudo ln -fs /bin/dash /bin/sh`

## 常用命令

### 文件管理相关

#### 显示当前文件路径

`pwd`

#### 进入目录

`cd /xxx`

##### 进入下一级目录

`cd ./`

#### 退出目录

`cd ../`

#### 显示当前目录下的文件

`ls -(可选操作a、h等)`

### 文件操作相关

#### 复制文件

#### 粘贴文件

#### 移动文件

#### 删除文件

#### 解压文件

#### 编辑文件

### 管理系统服务

#### 启动服务

`sudo systemctl start service-name`

用于启动指定的服务，将 service-name 替换为实际的服务名称。

#### 停止服务

`sudo systemctl stop service-name`

#### 重启服务

`sudo systemctl restart service-name`

#### 查看服务状态

`sudo systemctl status service-name`

##### 启用服务开机自启

`sudo systemctl enable service-name`

##### 禁用服务开机自启

`sudo systemctl disable service-name`

##### 查看系统内核

`cat /proc/version`

##### 查看是否安装了xxx环境

`dpkg -l | grep xxx`
