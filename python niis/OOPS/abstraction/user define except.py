class VoteError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

print("Enter age:")
age = int(input())

if age >= 18:
    print("Eligible")
else:
    try:
        raise VoteError("Age not allowed")
    except VoteError as e:
        print("Not allowed:", e)

print("End")