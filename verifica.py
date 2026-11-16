from pathlib import Path

pasta_images = Path(r"C:\Users\gusta\Downloads\cheat\wzai-advantage\ds_final\train\images")
pasta_labels = Path(r"C:\Users\gusta\Downloads\cheat\wzai-advantage\ds_final\train\labels")

images = {arquivo.stem for arquivo in pasta_images.iterdir() if arquivo.is_file()}
labels = {arquivo.stem for arquivo in pasta_labels.iterdir() if arquivo.is_file()}

# Excluir imagens sem label correspondente
for arquivo in pasta_images.iterdir():
    if arquivo.is_file() and arquivo.stem not in labels:
        arquivo.unlink()
        print(f"Imagem excluída: {arquivo.name}")

# Excluir labels sem imagem correspondente
for arquivo in pasta_labels.iterdir():
    if arquivo.is_file() and arquivo.stem not in images:
        arquivo.unlink()
        print(f"Label excluído: {arquivo.name}")

print("Verificação concluída!")