# 安裝 Django 套件

- pip install django

# 建立專案

- django-admin startproject 'App Name'

# 開啟專案目錄

# 啟動 Server

- python3 manage.py runserver

# 新增模塊(功能)

- python3 manage.py startapp 'module name'

# git 指令

- 要先安裝 git 程式

# 初始化本地倉庫

- git init

# 產生忽略檔案

- .gitignore (要在專案最外層生成)
- 將不需要紀錄的檔案放進去(可以包括整個目錄等)

# 檔案屬性

- 初始化之後檔案列表會出現幾個字母符號

- U => UntTracked (尚未被儲存)
- A => Added (已經成成功被儲存)
- M => Modified (有變更的檔案)

# 加入控管

- git add 'filename'

- git add . (全部一次控管)

# 確認儲存

- git commit -m 'message'

# 檢視狀態

- git status

# 檢視 commit log

- git log
- git --oneline(可以將所有 log 變成一行一行)

# 綁定遠端倉庫

- 要先登入 github 並 create new project, 之後會生成一個指令

- git remote add origin master

- git remote -v

# 複製專案

- git clone <倉庫的網址> (前提是要是 owner)
