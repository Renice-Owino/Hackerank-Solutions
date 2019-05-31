n = int(raw_input().strip())

for a0 in xrange(n):
    grade = int(raw_input().strip())

    if grade>=38 and grade%5>=3:
        while grade%5!=0:
            grade = grade + 1
    print grade