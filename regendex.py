import os

# Caminho onde estão os modelos (use raw string para evitar erros com barras)
base_dir = r'D:\Website-Templates-master'

# Começa o HTML do catálogo
html = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Catálogo de Modelos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        .modelos {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .modelo {
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
            text-align: center;
        }
        .modelo a {
            text-decoration: none;
            color: #007BFF;
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

# Percorre as subpastas e encontra index.html
for pasta in sorted(os.listdir(base_dir)):
    caminho_completo = os.path.join(base_dir, pasta)
    index_html = os.path.join(caminho_completo, 'index.html')

    if os.path.isdir(caminho_completo) and os.path.isfile(index_html):
        html += f'''
        <div class="modelo">
            <p>{pasta}</p>
            <a href="{pasta}/index.html" target="_blank">Ver modelo</a>
        </div>
        '''

# Fecha o HTML
html += '''
    </div>
</body>
</html>
'''

# Salva o arquivo index.html dentro da pasta de modelos
output_path = os.path.join(base_dir, 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ Catálogo gerado em: {output_path}")
