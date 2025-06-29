import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Caminho onde estão os modelos
base_dir = r'D:\Website-Templates-master'

# Caminho para salvar imagens
screenshot_width = 1024
screenshot_height = 768

# Configura o Chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--window-size={screenshot_width},{screenshot_height}")
driver = webdriver.Chrome(options=chrome_options)

# Gera miniaturas (thumb.png) de cada index.html
for pasta in sorted(os.listdir(base_dir)):
    caminho_completo = os.path.join(base_dir, pasta)
    index_html = os.path.join(caminho_completo, 'index.html')
    thumb_path = os.path.join(caminho_completo, 'thumb.png')

    if os.path.isdir(caminho_completo) and os.path.isfile(index_html):
        url = f"file:///{index_html.replace(os.sep, '/')}"
        print(f"📸 Capturando: {pasta}")
        driver.get(url)
        sleep(1.5)  # tempo para carregar o site
        driver.save_screenshot(thumb_path)

driver.quit()
print("✅ Screenshots geradas.")

# Agora gera o HTML com essas miniaturas
html = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo de Modelos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #121212;
            color: #f0f0f0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #ffffff;
        }
        .modelos {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .modelo {
            background: #1e1e1e;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
            text-align: center;
            transition: transform 0.2s;
        }
        .modelo:hover {
            transform: scale(1.03);
        }
        .modelo img {
            width: 100%;
            height: 150px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .modelo p {
            margin: 10px 0 5px;
            font-weight: bold;
        }
        .modelo a {
            text-decoration: none;
            color: #00aaff;
            font-weight: bold;
        }
        .modelo a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Catálogo de Modelos de Site</h1>
    <div class="modelos">
'''

for pasta in sorted(os.listdir(base_dir)):
    caminho_completo = os.path.join(base_dir, pasta)
    index_html = os.path.join(caminho_completo, 'index.html')
    thumb_img = os.path.join(caminho_completo, 'thumb.png')

    if os.path.isdir(caminho_completo) and os.path.isfile(index_html):
        img_tag = f'<img src="{pasta}/thumb.png" alt="Preview {pasta}">' if os.path.isfile(thumb_img) else ''
        html += f'''
        <div class="modelo">
            {img_tag}
            <p>{pasta}</p>
            <a href="{pasta}/index.html" target="_blank">Ver modelo</a>
        </div>
        '''

html += '''
    </div>
</body>
</html>
'''

# Salva o index final
output_path = os.path.join(base_dir, 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"📄 HTML do catálogo gerado: {output_path}")
