from tools import getSoup


def get_invoice_numbers():
    numbers = []
    try:
        url = 'https://invoice.etax.nat.gov.tw/'
        soup = getSoup(url)
        trs = soup.find(
            'table', class_="etw-table-bgbox etw-tbig").find_all('tr')
        datas = [[td.text.strip() for td in tr.find_all('td')]
                 for tr in trs[1:4]]

        for data in datas:
            # print(data[1].split()[:-1])
            numbers += data[1].split()[:-1]
    except Exception as e:
        print(e)
    return numbers


def search_invoice_bingo(invoice_number, bingo):
    bingo = False
    for i in range(len(numbers)):
        if i == 0 or i == 1:
            if numbers[i][5:] == invoice_number[len(invoice_number)-3:]:
                bingo = True
                break
    message = ''
    if bingo:
        if i == 0:
            message = '恭喜有機會中特別獎1000W'
        elif i == 1:
            message = '恭喜有機會中頭獎200w'
        else:
            message = '恭喜中頭獎,有機會中20W(三個號碼中200)'

        message += f'\n請繼續對獎 ==> {numbers[i]}'
    else:
        message = '下次再努力囉！'
    return message


if __name__ == '__main__':
    numbers = get_invoice_numbers()
    # print(numbers)
    print(search_invoice_bingo('21981893', numbers))
