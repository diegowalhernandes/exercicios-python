{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio19.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPQVc2Wm9Ni8yEQORjQQ9n6",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio19.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pfaTajORFTD6",
        "outputId": "b445907c-8a0a-4792-dabb-e3a822994152"
      },
      "source": [
        "import random\n",
        "print('''===Desafio 019===\n",
        "Um professor quer sortear um dos seus \n",
        "quatro alunos para pagar o quadro.\n",
        "Faça um programa que ajude ele,\n",
        "lendo o nome deles e escrevendo o nome\n",
        "do escolhido.''')\n",
        "print('=-'*15)\n",
        "\n",
        "n1 = str(input('Primeiro aluno: '))\n",
        "n2 = str(input('Segundo aluno: '))\n",
        "n3 = str(input('Terceiro aluno: '))\n",
        "n4 = str(input('Quarto aluno: '))\n",
        "lista = [n1, n2, n3, n4]\n",
        "escolhido = random.choice(lista)\n",
        "print(f'O aluno escolhido foi {escolhido}')\n"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "===Desafio 019===\n",
            "Um professor quer sortear um dos seus \n",
            "quatro alunos para pagar o quadro.\n",
            "Faça um programa que ajude ele,\n",
            "lendo o nome deles e escrevendo o nome\n",
            "do escolhido.\n",
            "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n",
            "Primeiro aluno: ana\n",
            "Segundo aluno: pedro\n",
            "Terceiro aluno: maria\n",
            "Quarto aluno: lucas\n",
            "O aluno escolhido foi maria\n"
          ]
        }
      ]
    }
  ]
}
