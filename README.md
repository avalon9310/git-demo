### 查詢版本號
- git --version 

### 建立基本資訊
- git config --global user.name avalon
- git config --global user.email asd95027@gmail.com

### 查找config
- git config --list

### 建立倉庫
- git init

### 觀察狀態
- git status(untrack,added,modified


### 加入暫存區
- git add (filename

### 觀察object
- git cat-file -p sha1
    -內容
- git cat-file -t sha1
    -型態

### 查看站存區控管的檔案
- git ls-files 
- git ls-files -s

### 將暫存區檔案加入倉庫
- git commit -m '(message)'
   - am(已確認後的增加跟message)
   --amend

### 檢視commit的紀錄
- git log
- git log --oneline(一行輸出

### 修改上一次的commit紀錄
- git commit --amend

### 手動刪除恢復
- git restore

### 指令刪除
- git rm -f (filename 手動刪除+git add
    -git restore --staged filename

### 將檔案搬離暫存/倉庫區
- git rm --cached filename

### 分支指令
- git branch

### 新增分支
- git branch branch-name

### 切換分支
- git checkout branch-name

### 新增跟切換分支
-git checkout -b test2

### 更改分支名稱
- git branch -m dev test2

### 刪除分支
- git branch -D dev

###合併分支
- git checkout master
    -git merge test

### 衝突處理
- 確認修改狀態


### 切換commit
- git log --oneline  >  git checkout (commit-object

### 恢復commit指令
-git reset
     -mixed
     --soft
     --hard


### 綁定雲端網址
- git remote add origin https://github.com/avalon9310/git-demo

### 推送指令
- git push -u origin master
      -git push

### 雲端版本推送錯誤
- git push -f (強制更新或使用git comm

### 拉取雲端版本
- git pull

### 完整複製專案
- git clone https://github.com/avalon9310/git-demo