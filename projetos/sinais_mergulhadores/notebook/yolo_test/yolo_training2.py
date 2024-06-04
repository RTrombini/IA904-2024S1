import torch
from ultralytics import YOLO

def main():
    # Verificar se a GPU está disponível
    print("Verificando a disponibilidade da GPU...")
    print("Versão do PyTorch:", torch.__version__)
    print("Versão do CUDA disponível:", torch.version.cuda)
    print("CUDA disponível:", torch.cuda.is_available())

    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"Usando GPU: {torch.cuda.get_device_name(0)}")
    else:
        device = torch.device("cpu")
        print("Usando CPU")

    # Listar todas as GPUs disponíveis
    for i in range(torch.cuda.device_count()):
        print(f"Dispositivo {i}: {torch.cuda.get_device_name(i)}")

    # Carregar o modelo YOLOv8
    print("Carregando o modelo YOLOv8...")
    model = YOLO('yolov8n.pt')  # Você pode escolher entre 'yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt', 'yolov8x.pt'

    # Caminho para o arquivo dataset.yaml
    dataset_yaml_path = r'c:\Users\rapha\OneDrive\Documentos\mestrado\projeto_de_visao_computacional\Project\Dataset\dataset.yaml'

    # Treinar o modelo
    print("Iniciando o treinamento do modelo...")
    model.train(data=dataset_yaml_path, epochs=100, imgsz=640, device=device)

    # Avaliar o modelo após o treinamento
    print("Avaliando o modelo treinado...")
    metrics = model.val()

    # Exibir métricas de avaliação
    print("Métricas de Avaliação:")
    print(metrics)

    # Salvar o modelo treinado
    model_path = 'yolov8_trained_model.pt'
    model.save(model_path)
    print(f'Modelo salvo em: {model_path}')

if __name__ == "__main__":
    main()
