# AI_Tech
## Algorithm
- 주차별 문제 내용 README.md에 각 주차 모더레이터가 기록
    - 레퍼런스 : Week2 디렉토리 README.md 참조
    ### 문제풀이 올릴 경우
    - LocalRepo로 Clone 후에, 자신 이름 브랜치 생성
        - 각 주차에 해당하는 문제 파일명 통일 -> ex)`Week2/Yungi_1.py`, `Week2/Yungi_2.py` ...
        - LocalRepo에 문제풀이 코드 commit 및 push 후에, 자신의 RemoteRepo에 올라간 브랜치를, Remote `main` Repo로 PULL REQUEST 요청, Reviewers에 모든 팀원들 등록
        - PR명은 __'[이름] n번 문제 풀이'__ 로 통일
        - PR내용은 자유롭게 어려웠던 점, 공부해볼 점 작성
        - Create pull request로 PR 게시
        - Week 지날수록 쌓인 __남의 코드 수정 금지__
    ### 문제풀이 Review 할 경우
    - 수정하면 더 효율적일 것 같다, 혹은 나와 다르게 구현했다 하는 부분 코드 옆 `+`버튼 눌러서 해당 코드에 대한 수정사항 게시 가능 => 제안사항 적은 후 Start a Review버튼 눌러서 작성완료
    - 모든 제안사항 다 적었을 경우, Review내용에 총평 작성 후, `Approve` 하여 코드 Merge 허가

    ### 코드리뷰가 끝나면
    - PR게시자는 `Confirm squash and merge` 하여, 커밋 로그들이 지저분하지 않도록 Merge