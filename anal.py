# Import and use JS function and variable into Python
from js import alltext
import pyodide
import js
import pandas as pd
import re

upload_btn = Element("upload")
runtest_btn = Element("test")
outputtext = Element("pdftext")
outputtext_result = Element("pdftext_result")

text_item_group = Element("text_group")

select_pdf = Element("selectpdf")

#pybutton = Element("upload2")

def speak(*args):
    filename = select_pdf.element.value
    document = outputtext.element.value
    #print(document)

    #docs_jun = document.replace(" ", ",")
 

    docs = document.replace("회 사 명 ", "new회사명").replace("성적서 번호,", "new성적서번호").replace("대 표 자 ", "new대표자").replace("주 소 ", "new주소").replace("1. 시 료 명", "new시료명").replace("- 규격 ","new규격").replace("2. 성적서의 용도,", "new성적서의용도")   .replace("3. 접수일자 ","new접수일자").replace("4. 검사일자 ","new검사일자").replace("5. 검사방법 ","new검사방법").replace("6. 검사결과 ","new검사결과").replace(" 구분 ","new구분:").replace("제조업체명","new제조업체명").replace("제조국명","new제조국명").replace("3.2","new3.2 ").replace("해당없음","해당없음new").replace(" 검사결과"," new검사결과").replace("합격","합격new").replace("3.2.2.1.1","new3.2.2.1.1").replace("3.2.2.2.1","new3.2.2.2.1").replace("3.2.2.4","new3.2.2.4").replace("3.2.3.1.1","new3.2.3.1.1").replace("3.2.3.2.1","new3.2.3.2.1").replace("3.2.4.1","new3.2.4.1").replace("3.3전기적안전요건","new3.3전기적안전요건").replace("시료내용No","new시료내용No").replace("본문서는전자문서용으로","new본문서는전자문서용으로").replace("(mg/kg)","(mg/kg)new").replace("Page","new")
    
  
    
    docs2 = re.split(r'new|^^|!!', docs)
    
    testnum = ""
    company = ""
    address = ""
    manufactor = ""
    nation = ""
    model = ""
    testpart = []
    Renewal = []
    print(len(docs2))
    for i, doc in enumerate(docs2):
        Renewal.append(doc)
        if "시료내용No" in doc: testpart.append(doc)
        if "성적서번호" in doc: testnum = doc
        if "회사명" in doc: company = doc.replace("회사명:","")
        if "제조업체명" in doc: manufactor = doc.replace("제조업체명","")
        if "주소:" in doc: address = doc.replace("주소:","")
        if "제조국명" in doc:nation = doc.replace("제조국명","")
        if "구분:" in doc:
            model = doc.replace("구분:","")
            models = model.split("(")[1]
            model = models.split(")")[0]
    
            
        
        
        #if ("본문서는전자문서용으로" in doc):
        #    pass
        #else:
        #print(f'{i})', doc)
    print("ㄹ어나머리", model)
    display(f"• 제조자명 또는 수입자명 : {company}", append=True, target="pdftext_result")    
    display(f"• 주소 및 전화번호 : {address}, (연락처 기재)", append=True, target="pdftext_result")
    display(f"• 제조년월 : ○○○○년 ○○월", append=True, target="pdftext_result")
    display(f"• 제조국 : {nation}", append=True, target="pdftext_result")
    display(f"• 사용연령 : {model}", append=True, target="pdftext_result")
    display(f"• 크기·체중의 한계 : ", append=True, target="pdftext_result")
    display(f"• 제조업체명 : {manufactor}", append=True, target="pdftext_result")      
    display(f"• 사용상 주의사항", append=True, target="pdftext_result")
    display("KC마크는 이 제품이 공통안전기준에 적합하였음을 의미합니다.", append=True, target="pdftext_result")
    

    for renew in Renewal:
        print(renew)     
        if "합격" in renew:
            if "3.2.1.2" in renew:
                display("작은부품이 발견되지 않았으나 ~~~~~", append=True, target="pdftext_result")
    

    print(testpart)



    #for dan in documents:
        
    #paragraphs = document.split(",")
    #for para in paragraphs:
    #    print(para)
    #i = 1
    #for i , para in enumerate(paragraphs):
    #    print(f'{i} : {para}')
             
    #print(f"Hello {alltext}")
    #print((text))

def pdfread(*args):
    print("kcmkcm")


#pybutton.element.onclick = pdfread