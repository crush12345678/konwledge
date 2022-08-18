**git init**  ：初始化文件 

将目录变成git可以管理的仓库

---

**git clone** ：克隆远程仓库

同时生个.git 文件，对仓库可以管理控制 

###### git clone <克隆>[url(即远程仓库克隆网址)]，那么就会在你的本地仓库中创建一个origin(远程仓库url的别名) /master和跟踪远程仓库的分支 master。

---

**git satus** :查看文件状态

---

**git add .**  : 全部添加到暂存区

---

**git commit -m "提交说明"** : 使用commit将暂存区的文件进行提交到本地的分支，-m 代表本次的提交说明

----

**git config --list**  :查看全部配置

**git config -- global --list** : 查看个人配置

**git confoig --system --list** : 查看系统配置

---

**git reflog** ：查看版本号

---

**git reset --hard HEAD ^/~** ：回到上一个版本，如果想回到上上一个版本只需将HEAD^改成HEAD^^以此类推，那如果要回到100个版本前，肯定不方便，我们可以使用git reset --hard HEAD~100即可。

---

**git diff <文件>**  ：可以查看文件修改前后的对比

---

**mkdir <文件夹>**  ：生成文件夹

---

**touch <文件>**  ：生成文件

---

**mv <文件> <文件夹>**  ：将文件移入文件夹

---

**rm <文件>**  ：删除文件

---

**rm -r <文件夹>**  ：删除文件夹

---

**rm -rf <文件夹>**  ： 直接删除无需提示。例如可删除.git文件或隐藏文件

---

**git branch**  :列出本地仓库所有的分支(分支前面有星号表示当前分支)

---

**git branch -v** :将要显示各个分支分别最后一次提交的对象信息

---

**git branch –merged** :会显示已合并的分支,没合并的分支不会显示

---

**git branch –no-merged** 会显示没合并的分支，合并的分支不会显示

---

**ls**  :显示文件和目录

---

**git checkout <分支>**  ：切换分支 

---

**git branch <分支>** : 创建分支

---

**git checkout -b <分支>**  ：创建并切换分支

---

**git branch -d <分支>**  ：删除分支 

* 删除远程分支：$ git push origin --delete [branch -name]

---

**git merge <分支>** ：合并指定分指到当前分支

---

**git branch -r** ：列出所有远程分支

---

**git branch - M <>**

---

**git push -uf origin <>** 

---

**git fetch** :

    一旦远程仓库主机的版本库有了更新（Git术语叫做commit）,需要将这些更新取回本地，这时就要用到git fetch命令 

* git fetch 命令通常用来查看他人的进程，因为它取回的代码对你本地的开发代码没有影响。

* 默认情况下，git fetch 取回所有分支（branch）的更新。如果只想取回特定分支的更新，可以指定分支名，命令如下：git fetch <远程主机名> <远程分支名>

---

**git pull <远程主机名> <远程分支名> <本地分支名>** ：

---

**pwd** ：查看文件或文档位置

---

**exit** : 退出

---

**clear** : 清屏

---

**git branch -r**:列出所有远程分支

---

**git remote -v** :可以详细查看你的从远程仓库克隆的网址

---

**git remote show remote-name** :

    它会详细显示了有哪些远端分支还没有同步到本地，哪些已同步到本地的远端分支在远端服务器上已被删除，以及运行 git pull 时将自动合并哪些分支。

---

**git log** :

     现在对readme文件做了多次修改，下面我们查看下历史记录，如何查，我们可以使用git log命令

    git log命令显示从近到远的日志，如果嫌上面显示的信息太多，可以使用git log --pretty=oneline（千万注意是oneline，不是online）

---

**git checkout -- file** :可以丢弃工作区的修改

---

**cd** 进入特定的目录

---

**git push origin master** ：

    将本地版本库推送到远程服务器，origin是远程主机，master表示是远程服务器上的master分支，分支名是可以修改的。

---

**cd ~/.ssh** 

​	查看密钥

---






