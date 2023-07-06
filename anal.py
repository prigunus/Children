# Import and use JS function and variable into Python
from js import alltext
import js
import re
from pyscript import Element


upload_btn = Element("upload")
runtest_btn = Element("test")
outputtext = Element("pdftext")
outputtext_result = Element("pdftext_result")
guide = Element("box")
text_item_group = Element("text_group")
select_pdf = Element("selectpdf")


#outputtext = js.document.getElementsByName("pdftext_result")
#pybutton = Element("upload2")



cou = []

def speak1(*args):

    print("넘어온값", type(alltext))
    guide.clear()   
    filename = select_pdf.element.value
    
    if len(filename) == 0:
        guide.element.innerHTML = "<h4>유효한 파일이 선택되지 않았습니다.</h4>"
        #display("유효한 파일이 선택되지 않았습니다.", append=True, target="guide")
    else:

        document = outputtext.element.value
        
        #document = alltext
        print(type(document))
        #document = alltext
        #docs_jun = document.replace(" ", ",")
        #print(len(alltext))
        #for k in alltext:
        #    k_list = k.split(" ")
        #    df = pd.DataFrame(k_list)
        #    print(type(df), df[0])


        #docs = document.replace("회사명 ", "new회사명").replace("성적서번호,", "new성적서번호").replace("대표자 ", "new대표자").replace("주소 ", "new주소").replace("1.시료명", "new시료명").replace("-규격 ","new규격").replace("2.성적서의 용도,", "new성적서의용도").replace("3.접수일자 ","new접수일자").replace("4.검사일자 ","new검사일자").replace("5.검사방법 ","new검사방법").replace("6.검사결과 ","new검사결과").replace("구분","new구분:").replace("제조업체명","new제조업체명").replace("제조국명","new제조국명").replace("3.2","new3.2 ").replace("해당없음","해당없음new").replace(" 검사결과"," new검사결과").replace("합격","합격new").replace("3.2.2.1.1","new3.2.2.1.1").replace("3.2.2.2.1","new3.2.2.2.1").replace("3.2.2.4","new3.2.2.4").replace("3.2.3.1.1","new3.2.3.1.1").replace("3.2.3.2.1","new3.2.3.2.1").replace("3.2.4.1","new3.2.4.1").replace("4.32","new4.32").replace("3.3전기적안전요건","new3.3전기적안전요건").replace("시료내용No","new시료내용No").replace("본문서는전자문서용으로","new본문서는전자문서용으로").replace("(mg/kg)","(mg/kg)new").replace("Page","new").replace("포장에경고문구","new포장에경고문구")
        
        docs = document.replace("회 사 명 ", "new회사명").replace("성적서 번호,", "new성적서번호").replace("대 표 자 ", "new대표자").replace("주 소 ", "new주소").replace("1. 시 료 명", "new시시료명").replace("- 규격 ","new규격").replace("2. 성적서의 용도,", "new성적서의용도")   .replace("3. 접수일자 ","new접수일자").replace("4. 검사일자 ","new검사일자").replace("5. 검사방법 ","new검사방법").replace("6. 검사결과 ","new검사결과").replace(" 구분 ","new구분:").replace("제조업체명","new제조업체명").replace("제조국명","new제조국명").replace("3.2","new3.2 ").replace("해당없음","해당없음new").replace(" 검사결과"," new검사결과").replace("합격","합격new").replace("3.2.2.1.1","new3.2.2.1.1").replace("3.2.2.2.1","new3.2.2.2.1").replace("3.2.2.4","new3.2.2.4").replace("3.2.3.1.1","new3.2.3.1.1").replace("3.2.3.2.1","new3.2.3.2.1").replace("3.2.4.1","new3.2.4.1").replace("4.32","new4.32").replace("3.3전기적안전요건","new3.3전기적안전요건").replace("시료내용No","new시료내용No").replace("본문서는전자문서용으로","new본문서는전자문서용으로").replace("(mg/kg)","(mg/kg)new").replace("Page","new").replace("포장에경고문구","new포장에경고문구").replace("성적서 번호 :","new성적서번호")

        docs2 = re.split(r'new|^^|!!', docs)
    
        testnum = ""
        company = ""
        address = ""
        manufactor = ""
        nation = ""
        model = ""
        testpart = []
        Renewal = []
        #print(len(docs2))

        for doc in docs2:
            #Renewal.append(doc)
            if "시료내용No" in doc: testpart.append(doc)
            if "성적서번호" in doc: testnum = doc
            if "회사명" in doc: company = doc.replace("회사명:","")
            if "제조업체명" in doc: manufactor = doc.replace("제조업체명","")
            if "주소:" in doc: address = doc.replace("주소:","")
            if "제조국명" in doc:nation = doc.replace("제조국명","")
            if "구분:" in doc:
                try:
                    model = doc.replace("구분:","")
                    models = model.split("(")[1]
                    model = models.split(")")[0]
                    model2 = models.split(")")[1]
                except : model2 = model
            if "시시료명" in doc:items = doc.replace("시시료명","")
            else: model2 = "검출되지 않음"
           
            Renewal.append(doc)
    
        print(items)

        if "" in items:
            if "승용" in model2:
                display(f"• 크기·체중의 한계 : ", append=True, target="box")
            else:
                display(f"• 크기·체중의 한계 : (해당되는 제품만 기재하시면 됩니다.)", append=True, target="box")
            #display(f"• 제조업체명 : {manufactor}", append=True, target="box")      
            display(f"• 사용상 주의사항", append=True, target="box")
    
            for renew in Renewal:
                #print(type(renew))
                renew = renew.replace(" ","")
                if ("전자문서용으로" in renew) or ("검사결과합부판정" in renew) or ("of" in renew):
                    pass
                else:
                    pass
            
            (testpart)

          
            Element("box").element.innerHTML = f"<h3>{items}({testnum})에 대한 정보입니다.</h3>"

            print(str(cou))
            #---------------------------------------------------------------
            def announce(ment, op_an):
                item = js.document.createElement(op_an)
                item.classList.add('ment_an')  #<h2 class="ment0"> </h2>
                item.innerText = ment
                return item        

            def stringment0(ment, op0): 
                item = js.document.createElement(op0)
                item.classList.add('ment0')  #<h2 class="ment0"> </h2>
                item.innerText = ment
                return item        

            def stringment1(ment, op1): # 공통적인 information
                item = js.document.createElement(op1)
                item.classList.add('ment1')
                item.innerText = ment
                return item
                #flexItem.append(item)
            
            def stringment2(ment, op2): # 실제 주의사항 information
                item = js.document.createElement(op2)
                item.classList.add('ment2')
                item.innerText = ment
                return item
   
            if len(cou) == 0:
                flexContainer = js.document.createElement('div')
                flexContainer.classList.add('flex-container')

                flexItem = js.document.createElement('div')
                flexItem.classList.add('flex-item')
                flexItem1 = js.document.createElement('div')
                flexItem1.classList.add('flex-item1')


                flexItem.append(announce("1. 제품 낱개에는 아래의 사항이 표시되어야 합니다.","h4"))
                flexItem.append(announce("- ‘제조(수입)자명 또는 그 약호’ ","h4"))
                flexItem.append(announce("- ‘안전표시’","h4"))
                flexItem.append(announce("- ‘지시사항’","h4"))

                item_img = js.document.createElement('img')
                item_img.classList.add('thumnail')
                item_img.setAttribute('src', f"./img/kc.JPG")
                flexItem.append(item_img)

                flexItem.append(stringment0("어린이제품안전특별법에 의한 표시사항", 'h2'))
                flexItem.append(stringment1(f"• 제조자명 또는 수입자명 : {company}",'h4'))
                flexItem.append(stringment1(f"• 주소 및 전화번호 : {address}",'h4'))
                flexItem.append(stringment1(f"• 제조년월 :"+"○○○○년 ○○월",'h4'))
                flexItem.append(stringment1(f"• 제조국 : {nation}",'h4'))
                flexItem.append(stringment1(f"• 사용연령 : {model}",'h4'))
                flexItem.append(stringment1(f"• 제조업체명 : {manufactor}",'h4'))

                flexItem1.append(stringment1(f"• 사용상 주의사항",'h4'))

                etcment = []
                
                for renew_origin in Renewal:
                    renew = renew_origin.replace(" ", "") # 공백 다 없애라....
                    if ("전자문서용으로" in renew) or ("검사결과합부판정" in renew) or ("of" in renew):
                        pass
                    else:
                        print(type(renew), renew)
                        if ("3.2.1.2" in renew):# and ("" in renew):
                            flexItem1.append(stringment2("- “경고! 3세 미만의 어린이는 사용할 수 없음. 작은 부품을 포함하고 있음”", "h4"))
                        if ("3.2.2.2.2" in renew) and ("" in renew):
                            flexItem1.append(stringment2("- 기능성 날카로운 부분이 있음????","h4"))
                        if ("포장에경고문구" in renew) and ("" in renew):
                            flexItem1.append(stringment2("- 기능성 날카로운 끝이 있음????",'h4'))
                        if ("3.2.4.1" in renew) and ("해당없음" in renew):
                            flexItem1.append(stringment2("- 자석을 가지고 있음???","h4"))
                        if ("3.2.5" in renew) and ("" in renew):
                            flexItem1.append(stringment2("-유리를 가지고 있음??", "h4"))
                        if ("3.3.1.1" in renew) and ("" in renew):
                            flexItem1.append(stringment2("-2차전지의 위험하다는 부록 E 권고사항", "h4"))
                        if ("3.3.1.2" in renew) and ("" in renew):
                            flexItem1.append(stringment2("-2차전지의 위험하다는 부록 F 권고사항", "h4"))
                        if ("-모델번호" in renew): #?????
                            flexItem1.append(stringment2("-모델번호-정격전압,정격용량-제조년전지는또한적절한주의문구","h4"))
                        if ("-4.4.2" in renew):
                            flexItem1.append(stringment2("경고!3세미만의 어린이가 사용할 수 없음. 작은부품을 포함함","h4"))
                        if ("-4.5.2" in renew):
                            flexItem1.append(stringment2("이 완구는 질식의 위험이 있는 작은 공을 포함하고 있음. 3세미만의 어린이는 사용할 수 없음","h4"))
                        if ("-4.5.6" in renew):
                            flexItem1.append(stringment2("경고!8세 미만의 어린이는 부풀리지 않은 풍선 또는 터진풍선에 의해 기도가 막혀질식할수있음. 성인의통제를 요함.부풀리지 않은 풍선을 어린이의 손에 닿지 않게 해야함. 터진풍선은 곧바로 치워야함.","h4"))
                        if ("-4.5.7" in renew):
                            flexItem1.append(stringment2("이 완구는 질식의 위험이 있는 구슬을 포함하고 있음. 3세 미만의 어린이는 사용할 수 없음","h4"))
                        if ("4.6.2" in renew):
                            #if 8세미만만
                            flexItem1.append(stringment2("이 완구에는 기능성 날카로운 가장자리가 있음!", "h4"))
                        if ("-4.11.5" in renew):
                            flexItem1.append(stringment2("[설명서]조립방법 및 주의사항을 설명서에 기재할 것","h4"))
                        if ("천둥번개" in renew): #??
                            flexItem1.append(stringment2("경고!천둥번개시 또는 전압선 근처에서는 사용을 금함","h4"))
                        if ("4.17" in renew):
                            flexItem1.append(stringment2("경고! 사고발생시 보호받지 못함 또는 경고! 자외선으로부터 보호받지못함, 경고! 자외선 차단기능이 없으며선 글라스로 사용할 수 없음,야외에서 사용시 햇빛에 의한 안구화상의 위험이 있음.","h4"))
                        if ("-b)5" in renew):#???
                            flexItem1.append(stringment2("경고! 눈이나 얼굴쪽으로 겨누지 말 것","h4"))
                        if ("-4.27" in renew):
                            flexItem1.append(stringment2("경고! 안전모 및 손목보호대등의 보호장구를 착용하여야 함","h4"))
                        if ("4.28" in renew):
                            flexItem1.append(stringment2("경고! 실내에서 사용하지 말것. 눈이나 귀 부근에서 사용하지 말것.","h4"))
                        if ("4.32.2" in renew):
                            flexItem1.append(stringment2("의도된 체중에 대한 경고표시가 있을것, 또한 사용설명서에도 이 내용이 포함될 것, 완구스쿠터의 탑승에 대한 잠재적 위험성에 대해서 보호자 또는 사용자에 대한 주의 표시가 있을 것.","h4"))
                        if ("A.2.11" in renew):
                            flexItem1.append(stringment2("“전동완구는적용가능한경우안전한전지사용에관한지침을포함해야한다. ·전지를삽입하고제거하는방법·재충전할수없는전지는재충전하면안된다.·재충전할수있는전지를충전할때는어른이감독해야한다.·재충전용충전기의충전상태표시등의기능을활용하여과충전사고를방지해야한다.·오래된것과새것또는다른형태의전지들을같이사용하면안된다.·완구로부터다쓴전지를제거해야한다.·전원공급단자를단락시켜서는안된다.”", "h4"))
                flexContainer.append(flexItem)
                flexContainer.append(flexItem1)
            
                js.document.querySelector('.final').append(flexContainer)
            
            else:
                pass
            cou.append('ff')
        
        else:
            guide.element.innerHTML = "<h4>완구만 지원됩니다.</h4>"
            
    #for dan in documents:
        
    #paragraphs = document.split(",")
    #for para in paragraphs:
    #    print(para)
    #i = 1
    #for i , para in enumerate(paragraphs):
    #    print(f'{i} : {para}')
             
    #print(f"Hello {alltext}")
    #print((text))

def speak2(*args):
    print("second select")    
    guide.clear() 

                
                
  

#pybutton.element.onclick = pdfread