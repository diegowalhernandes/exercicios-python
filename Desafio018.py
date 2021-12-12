{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio018.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPZor4Chh3+5ygNpzObggjU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio018.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WQPSYwlfDBCc",
        "outputId": "9842c2b5-1524-45c0-df8c-f0130d2b9796"
      },
      "source": [
        "import math\n",
        "print('''===Desafio 018===\n",
        "Faça um programa que leia um ângulo\n",
        "qualquer e mostre na tela o valor do seno\n",
        "cosseno e tangente desse ângulo.''')\n",
        "print('=-'*15)\n",
        "angulo = float(input('Digite o ângulo que você deseja: '))\n",
        "seno = math.sin(math.radians(angulo))\n",
        "print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')\n",
        "cosseno = math.cos(math.radians(angulo))\n",
        "print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')\n",
        "tan = math.tan(math.radians(angulo))\n",
        "print(f'O ângulo de {angulo} tem a TANGENTE de {tan:.2f}')"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "===Desafio 018===\n",
            "Faça um programa que leia um ângulo\n",
            "qualquer e mostre na tela o valor do seno\n",
            "cosseno e tangente desse ângulo.\n",
            "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n",
            "Digite o ângulo que você deseja: 30\n",
            "O ângulo de 30.0 tem o SENO de 0.50\n",
            "O ângulo de 30.0 tem o COSSENO de 0.87\n",
            "O ângulo de 30.0 tem a TANGENTE de 0.58\n"
          ]
        }
      ]
    }
  ]
}
