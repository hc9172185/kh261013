#은행 관리 프로그램
#입금 입금조회 출금 종료
class Bank:
    def __init__(self):
        self.cash_list = []
        self.balance = 0

    def print_menu(self):
        print("====ATM====")
        print("0. 종료")
        print("1. 계좌 입금")
        print("2. 계좌 조회")
        print("3. 계좌 출금")

    def deposit(self): 
        print("---계좌 입금---")
        c = int(input("입금할 금액: "))
        self.cash_list.append(c)
        self.balance += c
        print(f"현재 계좌에 {c}원 입금되었습니다.")

    def deposit_list(self):
        print(f"현재 잔액은 {self.balance}원")

    def withdraw(self):
        print("---계좌 출금---")
        c = int(input("출금할 금액: "))
        if self.balance >= c:
            self.balance -= c
            self.cash_list.remove(c)
            print(f"현재 계좌에 {c}원 출금되었습니다.")
        else:
            print("잔액이 부족합니다.")

    def run(self):
        while True:
            self.print_menu()
            n = int(input("메뉴 선택: "))
            match n:
                case 0:
                    print("ATM을 종료합니다.")
                    break
                case 1:
                    self.deposit()
                case 2:
                    self.deposit_list()
                case 3:
                    self.withdraw()

bank = Bank()
bank.run()
