**[COSADAMA GIT 튜토리얼](https://github.com/Team-COSADAMA/2021-Curriculum/blob/main/GitHub-Guides/gui-githubdesktop.md)을 참고하였음을 밝힙니다.**

# GUI 사용하기 - GitHub Desktop

안녕하세요 여러분 😉 앞서 소개해드렸던 GitHub Desktop 사용법에 대해서 간단히 배워봅니다. 앞서 [깃이 뭔가요?](https://www.notion.so/7f89fd577d53467aa0815043abf581d5) 에서 알려드렸던 것처럼 Desktop 버전은 화면을 보면서 쉽게 git 작업을 할 수 있는 그래픽 사용자 인터페이스(Graphical User Interface, GUI) 입니다. 저희가 배워본 CLI(Command Line Interface) 보다는 사용자가 편리하게, 쉽게 사용할 수 있도록 기능을 알기 쉬운 아이콘 등으로 그래픽으로 나타낸 것입니다. 들어가기에 앞서 말씀드리자면, CLI 버전보다는 기능이 너무 제한 되어 있기 때문에 CLI에서 다룰 수 있는 –amend -f같은 옵션이나, reset, revert, rebase 등과 같은 고급 옵션은 사용할 수 없습니다. 하지만 주요 기능을 보다 쉽게 다뤄볼 수 있다는 점에서 git 초보자들이 믿고 따라 쓸 수 있는, 깔끔한 툴이에요 😊 실제로 간단한 작업에 저도 많이 사용하고 있어요. 그럼 사용법을 간단히 알아볼까요?

## git clone

### Let's get started!

![./contents/gitclone-1.png](https://github.com/Team-COSADAMA/2021-Curriculum/raw/main/GitHub-Guides/contents/gitclone-1.png)  
처음 설치를 마치면 아래와 같은 화면이 나타납니다. 이 화면에서는 “Clone a repository from the internet…" 을 실행하면 팝업 화면이 나타나는데, 본인의 깃헙 계정과 연결하기 위해 sign in을 누르면 됩니다. 그러면 자신의 계정으로 접근 가능한 모든 repository 목록이 나와요!  
초기 설치 이후에 clone을 하고 싶다면 왼쪽 상단의 File → Clone repository 를 누르면 됩니다.  
![./contents/gitclone-2.png](https://github.com/Team-COSADAMA/2021-Curriculum/raw/main/GitHub-Guides/contents/gitclone-2.png)  
원하는 repository를 선택하고, Local Path에 다운로드할 위치를 지정해줍니다. 저는 거의 Documents 내 GitHub 문서에 생성해둡니다. 이후에 Clone을 눌러줄게요. 그럼 끝!  
![./contents/gitclone-3.png](https://github.com/Team-COSADAMA/2021-Curriculum/raw/main/GitHub-Guides/contents/gitclone-3.png)  
Current repository 옆에 있는 조그만 삼각형을 클릭하면 Add 버튼이 나타납니다. 여기서 Clone repository를 클릭해도 clone할 수 있습니다.

**주의사항**
이 때 꼭, 브랜치를 본인이 생성한 브랜치로 변경해주세요. 만약 main branch로 clone을 하게 되면, 다른 사람의 코드를 수정하게 되어 충돌이 발생할 수 있습니다.
브랜치가 없는 경우 `Branch` 탭을 클릭하고 `New branch`를 눌러 새로운 브랜치를 생성해주세요.

## git commit (+add)

![./contents/gitcommit.png](https://github.com/Team-COSADAMA/2021-Curriculum/raw/main/GitHub-Guides/contents/gitcommit.png)  
GitHub Desktop 에서는 git add와 commit을 동시에 할 수 있습니다. 화면 왼쪽 아래에 commit message와 description (선택) 을 작성하면 commit to 버튼이 활성화 됩니다. 그러면 버튼을 눌러주세요. 밑의 캡쳐를 보시면 캡쳐에서는 파일크기가 커서 나오지 않지만, 코드 등을 수정했을 경우 바뀐 부분이 나오게 됩니다.  
![./contents/gitcommit-2.png](https://github.com/Team-COSADAMA/2021-Curriculum/raw/main/GitHub-Guides/contents/gitcommit-2.png)  
Commit을 마쳤습니다! 🤗

## git push

![./contents/gitpush-1.png](https://github.com/Team-COSADAMA/2021-Curriculum/raw/main/GitHub-Guides/contents/gitpush-1.png)  
Commit to main 버튼을 누르면 오른쪽 상단에 Push origin이 생깁니다. 이것을 눌러주면 Push 완료! 😎  
![./contents/gitpush-2.png](https://github.com/Team-COSADAMA/2021-Curriculum/raw/main/GitHub-Guides/contents/gitpush-2.png)  
다음과 같이 현재의 브랜치가 master가 아닌 경우에 (즉, 사설 branch인 경우에는) Push를 마치고 나서 다음과 같이 master로 `Pull request`를 하라는 버튼을 GitHub가 알아서 띄워줍니다.

## pull request

![./contents/gitpull-1.png](pull-request.png)
![./contents/gitpull-2.png](pull-request-2.png)
GitHub Desktop에서는 Pull request를 할 수 있도록 알아서 버튼을 띄워줍니다. 이 버튼을 누르면 GitHub Desktop이 자동으로 브라우저를 열어 Pull request를 할 수 있는 페이지로 이동합니다.

![./contents/gitpull-3.png](pull-request-3.png)
이렇게 Pull request를 할 수 있는 페이지로 이동합니다. 여기서 Pull request를 작성하고 `Create pull request`를 누르면 Pull request가 완료됩니다.

권한이 있는 경우 `Merge` 버튼이 활성화되어 Merge를 할 수 있습니다.
![./contents/gitpull-4.png](merge.png)

## git pull origin main

![./contents/update-from-main.png](update-from-main.png)
main branch에서 변경사항이 있을 경우, GitHub Desktop의 Branch 탭을 클릭하고, `update from main`을 클릭하면 main branch의 변경사항을 가져올 수 있습니다. 이후 Pull origin main을 클릭하면 변경사항을 가져올 수 있습니다.

이메일로 초대되기 전의 친구들(fork)은 다른 사람의 코드가 보이지 않습니다. 크롬에서 github을 들어가 확인하거나, GitHub Desktop에서 만들었던 repository를 삭제하고 다시 clone을 받아야 합니다.
다시 clone하는 것은 필수사항은 아니니 참고만 해주세요.

## git pull

![./contents/gitpull-2.png](https://github.com/Team-COSADAMA/2021-Curriculum/raw/main/GitHub-Guides/contents/gitpull-2.png)  
만약 원격 저장소에서 변경된 사항이 있어서, 현재 checkout한 브랜치가 뒤쳐져 있는 있는 경우, GitHub Desktop이 이를 알아서 상태를 파악하고 Pull을 하라는 버튼을 보여줍니다. 만약 이 버튼이 보이지 않는다면, pull해올 것이 없다는 의미입니다.

[참조 및 이미지](https://engineering-skcc.github.io/github%20pages/github-pages-desktop/)
