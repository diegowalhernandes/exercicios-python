{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Desafio020.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyNahpPdowLcx6LmSqPct/v1",
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
        "<a href=\"https://colab.research.google.com/github/diegowalhernandes/exercicios-python/blob/main/Desafio020.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0_wy93KmIzS_",
        "outputId": "cbc05df4-a98d-438b-d68f-9188cdca8caf"
      },
      "source": [
        "import random\n",
        "print('''===Desafio 20===\n",
        "O mesmo professor do desafio \n",
        "anterior quer sortear a ordem \n",
        "de apresentação de trabalhos dos alunos.\n",
        "Faça um programa que leia o nome\n",
        "dos quatro alunos e mostre a \n",
        "ordem sorteada.''')\n",
        "print('=-'*15)\n",
        "n1 = str(input('Primeiro aluno: '))\n",
        "n2 = str(input('Segundo aluno: '))\n",
        "n3 = str(input('Terceiro aluno: '))\n",
        "n4 = str(input('Quarto aluno: '))\n",
        "lista = [n1, n2, n3, n4]\n",
        "random.shuffle(lista)\n",
        "print('A ordem de apresentação será ')\n",
        "print(lista)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "===Desafio 20===\n",
            "O mesmo professor do desafio \n",
            "anterior quer sortear a ordem \n",
            "de apresentação de trabalhos dos alunos.\n",
            "Faça um programa que leia o nome\n",
            "dos quatro alunos e mostre a \n",
            "ordem sorteada.\n",
            "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n",
            "Primeiro aluno: joao\n",
            "Segundo aluno: pedro\n",
            "Terceiro aluno: aline\n",
            "Quarto aluno: maria\n",
            "A ordem de apresentação será \n",
            "['joao', 'pedro', 'aline', 'maria']\n"
          ]
        }
      ]
    }
  ]
}
