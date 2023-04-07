import os, sys, PyPDF2

def merge(file_name_1, file_name_2, processed_name):
    pdf_in_1 = open(file_name_1, "rb")
    pdf_in_2 = open(file_name_2, "rb")
    pdf_reader_1 = PyPDF2.PdfReader(pdf_in_1)
    pdf_reader_2 = PyPDF2.PdfReader(pdf_in_2)
    pdf_writer = PyPDF2.PdfWriter()

    for pagenum in range(len(pdf_reader_1.pages)):
        page = pdf_reader_1.pages[pagenum]
        pdf_writer.add_page(page)
    for pagenum in range(len(pdf_reader_2.pages)):
        page = pdf_reader_2.pages[pagenum]
        pdf_writer.add_page(page)

    pdf_out = open(processed_name, "wb")
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in_1.close()
    pdf_in_2.close()

    print("변환 완료!")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        file_name_1 = os.getcwd() +'/' + sys.argv[1]
        if not os.path.isfile(file_name_1):
            print("존재하지 않는 파일입니다.")
            exit()
        if len(sys.argv[2].strip()) == 0:
            print("공백만 입력은 불가능 합니다.")
            exit()
        file_name_2 = os.getcwd() +'/' + sys.argv[2]
        if not os.path.isfile(file_name_2):
            print("존재하지 않는 파일입니다.")
            exit()
        if len(sys.argv[2].strip()) == 0:
            print("공백만 입력은 불가능 합니다.")
            exit()
        processed_name = os.getcwd()+'/' + sys.argv[3]
        if os.path.isfile(processed_name) or os.path.isdir(processed_name):
            print('이미 존재하는 파일명 입니다.')
            exit()
    elif len(sys.argv) != 1:
        print("[파일명1, 파일명2, 결과 파일명] 형태로 인자를 입력해주세요.")
        exit()
    else:
        while True:
            try:
                file_name_1 = input("첫번째 파일명을 적어주세요:  ")
            except EOFError:
                exit()
            file_name = os.getcwd()+'/'+file_name_1
            if not os.path.isfile(file_name):
                print("존재하지 않는 파일입니다. 다시 입력해주세요.")
                continue
            else:
                break
        while True:
            try:
                file_name_2 = input("두번째 파일명을 적어주세요:  ")
            except EOFError:
                exit()
            file_name = os.getcwd()+'/'+file_name_2
            if not os.path.isfile(file_name):
                print("존재하지 않는 파일입니다. 다시 입력해주세요.")
                continue
            else:
                break
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
    
    merge(file_name_1, file_name_2, processed_name)