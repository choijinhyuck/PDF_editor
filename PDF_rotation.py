import os, sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        file_name = os.getcwd() +'/' + sys.argv[1]
        if not os.path.isfile(file_name):
            print("존재하지 않는 파일입니다.")
            exit()
        if len(sys.argv[2].strip()) == 0:
            print("공백만 입력은 불가능 합니다.")
            exit()
        processed_name = os.getcwd()+'/' + sys.argv[2]
        if os.path.isfile(processed_name) or os.path.isdir(processed_name):
            print('이미 존재하는 파일명 입니다.')
            exit()
        try:
            angle = int(sys.argv[3])
            if angle % 90 != 0:
                print("회전 불가능한 각도를 입력하셨습니다.")
                exit()
        except:
            print('정수만 입력해 주세요.')
    elif len(sys.argv) != 1:
        print("[변환 대상 파일명, 결과 파일명, 90도 간격 양, 음의 정수 값] 형태로 인자를 입력해주세요.")
        exit()
    else:
        while True:
            try:
                file_name = input("파일명을 적어주세요:  ")
            except EOFError:
                exit()
            
            file_name = os.getcwd()+'/'+file_name
            if not os.path.isfile(file_name):
                print("존재하지 않는 파일입니다. 다시 입력해주세요.")
                continue
            else:
                break
        
        while True:
            try:
                angle = int(input("회전 각도를 90도 간격으로 정수로 입력해주세요 (시계=양수,반시계=음수):  "))
                if angle % 90 != 0:
                    print("회전 불가능한 각도를 입력하셨습니다. 다시 입력해주세요.")
                    continue
                else:
                    break
            except EOFError:
                exit()
            except:
                print('정수만 입력해 주세요.')
                continue
        
        while True:
            try:
                processed_name = input("결과 파일의 이름을 설정해주세요.(확장자 제외):  ")
            except EOFError:
                exit()

            if len(processed_name.strip()) == 0:
                print("공백만 입력은 불가능 합니다. 다시 입력해주세요.")
                continue
            else:
                processed_name = os.getcwd()+'/' + processed_name + '.pdf'
                if os.path.isfile(processed_name) or os.path.isdir(processed_name):
                    print('이미 존재하는 파일명 입니다. 다른 이름을 입력해주세요.')
                    continue
                else:
                    break


import PyPDF2

pdf_in = open(file_name, "rb")
pdf_reader = PyPDF2.PdfReader(pdf_in)
pdf_writer = PyPDF2.PdfWriter()

for pagenum in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[pagenum]
    page.rotate(angle)
    pdf_writer.add_page(page)

pdf_out = open(processed_name, "wb")
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()

print("변환 완료!")