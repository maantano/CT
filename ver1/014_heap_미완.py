# 절대값 힙 구현하기
#  11286번

# 절대값 힙은 다음과 같은 연산을 지원하는 자료구조다.
# 1. 배열에 정수 x(x != 0)을 넣는다.
# 2. 배열에서 절댓값이 가장 적은 값을 출력한 후 그 값을 배열에서 제거한다.
# 절댓값이 가장 작은 값이 여러 개일 경우 그중 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

# 1번째 줄에 연산의 개수 N이 주어진다. 
# 다음 N개의 줄에는 연산과 관련된 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 0이 아니라면 배열에 x라는 값을 추가하고
# 그 값을 배열에서 제거한다. 입력되는 정수는 -2 **31 보다 크고 2**31보다 작다.


# 입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어있는데 절댓값이 가장 작은 값을 출력하라고 할 떄는 0을 출력하면 된다.


