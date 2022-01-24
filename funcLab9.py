def isPYTHON(a):
    if "PYTHON" in a:
        return True
    else:
        return False

def is_print(a):
    if a == 1:
        print("PYTHON이 존재합니다")
    else:
        print("PYTHON이 존재하지 않습니다")

is_print(isPYTHON("나는 PYTHON을 학습합니다."))
is_print(isPYTHON("나는 python을 학습합니다."))
is_print(isPYTHON("PYTHON1234"))

