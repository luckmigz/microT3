# Alarme com Raspberry Pi 3 B+

Este projeto tem como objetivo criar um alarme utilizando um Raspberry Pi 3 B+ e um sensor de luz LM393. O sistema monitora a presença de luz em um ambiente e emite alertas visuais e auditivos quando a luz está desligada.

## Integrantes

- Larissa Navarro Pizarro - RA: 19.02028-7
- Lucas Miguel de Matos Negri - RA: 19.00386-2
- Matheus Igino Machado - RA: 20.01629-8
- Vinicius Urias da Cruz - RA: 20.00601-2

## Tecnologias Utilizadas

- **Raspberry Pi 3 B+**: Microcomputador que executa o código do sensor e se comunica via HTTP.
- **Python**: Linguagem de programação utilizada para ler o sensor de luz e enviar dados.
- **Flask**: Micro-framework para criar uma API RESTful que fornece dados do sensor.
- **HTML/CSS/JavaScript**: Usados para construir a interface web que exibe o status do sensor em tempo real.

## Componentes Necessários

- Raspberry Pi 3 B+
- Sensor de luz LM393
- Jumpers para conexão
- Resistor (se necessário)
- Acesso à internet (opcional, para instalar dependências)

## Funcionalidades

- **Monitoramento em Tempo Real**: A interface web atualiza a cada segundo para refletir o estado atual do sensor.
- **Alertas Visuais**: Quando a luz está desligada, a tela pisca entre vermelho e branco, e um alerta é exibido.
- **GIF de Estado**: Um GIF é exibido quando a luz está ligada, proporcionando um feedback visual.

## Video

Você pode assistir ao vídeo de demonstração do projeto no seguinte link: [Vídeo de Demonstração](https://drive.google.com/file/d/1bTJrbqwmCdnKykHxfI2-QxYyKMQz6YLu/view?usp=drive_link)


## Diagrama de Blocos 

[diagrama de blocos](https://github.com/luckmigz/microT3/blob/main/diagrama%20de%20blocos.png)
