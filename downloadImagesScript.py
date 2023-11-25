import requests
from bs4 import BeautifulSoup

frutas = [
    "Base líquida",
    "Batom",
    "Máscara de cílios",
    "Sombra para os olhos",
    "Blush",
    "Corretivo",
    "Pó compacto",
    "Gloss labial",
    "Delineador de olhos",
    "Batom líquido",
    "Perfume",
    "Hidratante facial",
    "Protetor solar",
    "Shampoo",
    "Condicionador",
    "Creme para o corpo",
    "Esfoliante facial",
    "Removedor de maquiagem",
    "Esmalte de unhas",
    "Escova de cabelo",
    "Creme hidratante",
    "Protetor solar",
    "Creme antienvelhecimento",
    "Tônico facial",
    "Sabonete facial",
    "Esfoliante",
    "Máscara facial",
    "Óleo de limpeza",
    "Sérum",
    "Removedor de maquiagem",
    "Creme para os olhos",
    "Gel de limpeza",
    "Loção para o corpo",
    "Bálsamo labial",
    "Água micelar",
    "Creme para acne",
    "Hidratante labial",
    "Loção pós-barba",
    "Loção autobronzeadora",
    "Creme para as mãos",
    "Escova de dentes",
    "Pasta de dente",
    "Enxaguante bucal",
    "Fio dental",
    "Escova interdental",
    "Creme dental para sensibilidade",
    "Enxaguante bucal antisséptico",
    "Enxaguante bucal sem álcool",
    "Enxaguante bucal com flúor",
    "Escova de língua",
    "Creme dental infantil",
    "Enxaguante bucal infantil",
 ]
run = True
print(50*'=')
directory = str("C:\dev\Projetos\python-scripts\dataset")
for fruta in frutas:
    print('')
    print("Baixando "+ fruta )
    search = str(fruta)
    print('')
    num_of_img = int(5)
    print('')
    print('Downloading...')
    print('')
    links_list = []
    img_list = []
    img_index = 0
    page_number = (num_of_img // 20) * 20

    url1 = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&source=lnms&tbm=isch&sa=X&ved=2ahUKEwipwcKTxOfrAhUUDrkGHZ3kB5kQ_AUoAXoECB8QAw&sfr=gws&sei=g8xeX6WWO4KI5OUP1Ne2sAQ'  
    req = requests.get(url1)
    soup = BeautifulSoup(req.text, 'html.parser')

    for img in soup.find_all('img')[1:]: #getting all the 'img' tag from the html file, excelpt the google icon
        if img_index == num_of_img: 
            break
        else:
            links_list.append(img.get('src'))
            img_index += 1

    for links in links_list:
        img_list.append(requests.get(links)) #acessing the images page and storing the link in a list

    for i, img in enumerate(img_list): #converting the images into byte
        with open(f'{directory}/{search}_{i}.png', 'wb') as f: #wb = write byte
            f.write(img.content)

    for pages in range(20, page_number + 20, 20):
        img_list = []
        links_list = []

        if img_index == num_of_img:
            break
        else:
            urln = f'https://www.google.com/search?q={search}&hl=pt-BR&gbv=1&tbm=isch&ei=78xeX5PTGc_Z5OUPrsyA0A0&start={pages}&sa=N' 
            req = requests.get(urln)
            soup = BeautifulSoup(req.text, 'html.parser')

            for img in soup.find_all('img')[1:]:
                if img_index == num_of_img:
                    break
                else:
                    links_list.append(img.get('src'))
                    img_index += 1

            for links in links_list:
                img_list.append(requests.get(links))

            for i, img in enumerate(img_list):
                with open(f'{directory}/{search}_{i + img_index - len(links_list)}.png', 'wb') as f: #wb = write byte
                    f.write(img.content)
        
    print('DONE!')
    print('')
    if img_index < num_of_img:
        print(f"It was only possible to download {img_index} images")
        print('')
    if img_index == 0:
        print("Unfortunately we didn't find any image to download")
        print('')
        
    ##exit_question = str(input('Do you want to quit?[Y/N]'))
    if frutas.index(fruta) == len(frutas):
        break
    else:
        print(50*'=')
        continue
print('')
print(50*'=')
print("Check back often!")