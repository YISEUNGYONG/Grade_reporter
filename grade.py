# 입력 함수
def input_student_info():
    student_info = {}
    student_info['학번'] = input("학번: ")
    student_info['이름'] = input("이름: ")
    student_info['영어'] = int(input("영어 점수: "))
    student_info['C언어'] = int(input("C-언어 점수: "))
    student_info['파이썬'] = int(input("파이썬 점수: "))
    return student_info

# 총점/평균 계산 함수
def calculate_total_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average

# 학점 계산 함수
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# 등수 계산 함수
def calculate_rank(scores, student_average):
    sorted_scores = sorted(scores, reverse=True)
    rank = sorted_scores.index(student_average) + 1
    return rank

# 출력 함수
def print_student_info(student_info, total, average, grade, rank):
    print("=" * 130)
    print(f"{'학번':<10}\t{'이름':<10}\t{'영어':<10}\t{'C-언어':<10}\t{'파이썬':<10}\t{'총점':<10}\t{'평균':<10}\t{'학점':<10}\t{'등수':<10}")
    print("=" * 130)
    print(f"{student_info['학번']:<10}\t{student_info['이름']:<10}\t{student_info['영어']:<10}\t{student_info['C언어']:<10}\t{student_info['파이썬']:<15}\t{total:<15}\t{average:<10.2f}\t{grade:<10}\t{rank:<10}\n")

# 메인 함수
def main():
    students = []
    while len(students) < 5:
        print(f"\n학생 {len(students) + 1} 정보 입력")
        student_info = input_student_info()
        students.append(student_info)

    print("        ""성적관리 프로그램")
    
    for student in students:
        scores = [student['영어'], student['C언어'], student['파이썬']]
        total, average = calculate_total_average(scores)
        grade = calculate_grade(average)
        rank = calculate_rank([calculate_total_average([s['영어'], s['C언어'], s['파이썬']])[0] for s in students], total)
        print_student_info(student, total, average, grade, rank)

if __name__ == "__main__":
    main()
