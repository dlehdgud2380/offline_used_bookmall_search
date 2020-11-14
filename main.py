#알라딘 또는 YES24 오프라인 검색기 테스트 프로그램

import module.aladin as Aladin
import module.yes24 as Yes24

class Search_Process:
    def __init__(self, word, mod):
        self.word = word
        self.mod = mod
        if mod == "0":
            self.search_aladin()
        else:
            self.search_yes24()
    def search_aladin(self):
        search_page = Aladin.Searchpage(self.word)
        search_page.print_searchdata()
        select = int(input("몇번째 검색결과를 선택? : "))
        item_page = Aladin.Itempage(select, search_page.return_data())
        item_page.print_data()
        
    def search_yes24(self):
        search_page = Yes24.Searchpage(self.word)
        search_page.print_data()

if __name__ == "__main__":
    word = input("검색어를 입력하세요: ")
    searchmod = input("알라딘검색 - 0, yes24 - 1 : ")
    print('\n')
    search = Search_Process(word, searchmod)