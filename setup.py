import sys
from cx_Freeze import setup, Executable

# Defina os parâmetros do executável
executables = [
    Executable(
        script='main.py',  # Substitua 'main.py' pelo nome do seu arquivo Python principal
        base=None,  # Define a base do executável (None para console ou "Win32GUI" para aplicação sem console)
        icon=None  # Adicione um ícone personalizado para o executável (opcional)
    )
]

# Defina as opções de build
build_options = {
    'packages': [],  # Lista de pacotes Python adicionais a serem incluídos
    'excludes': [],  # Lista de módulos Python a serem excluídos
    'include_files': []  # Lista de arquivos extras a serem incluídos
}

# Configuração do setup
setup(
    name='Pedido de Namoro',  # Nome do executável
    version='1.0',  # Versão do executável
    description='Pedir a boyzinha em namoro',  # Descrição do executável
    options={'build_exe': build_options},
    executables=executables
)
